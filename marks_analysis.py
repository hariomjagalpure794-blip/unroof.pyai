"""
Student Marks Analysis Project
Day 6 - Pandas: Data Wrangling

Concepts used: DataFrame, read_csv(), fillna(), groupby(), merge()
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. READ DATA
# ---------------------------------------------------------
marks_df = pd.read_csv("student_marks.csv")
info_df = pd.read_csv("student_info.csv")

print("Raw marks data:")
print(marks_df)
print()

# ---------------------------------------------------------
# 2. CLEAN MISSING / INVALID DATA
# ---------------------------------------------------------
# Marks must be between 0 and 100. Anything outside that range
# (e.g. -5, 102) is invalid data entry -> treat as missing (NaN).
marks_df["Marks"] = pd.to_numeric(marks_df["Marks"], errors="coerce")
marks_df.loc[(marks_df["Marks"] < 0) | (marks_df["Marks"] > 100), "Marks"] = np.nan

# Fill missing marks with that SUBJECT's average (a fairer fill than
# an overall average, since subjects can differ in difficulty).
subject_means = marks_df.groupby("Subject")["Marks"].transform("mean")
marks_df["Marks"] = marks_df["Marks"].fillna(subject_means).round(1)

print("Cleaned marks data:")
print(marks_df)
print()

# ---------------------------------------------------------
# 3. MERGE with student info (Name, Class)
# ---------------------------------------------------------
merged_df = pd.merge(marks_df, info_df[["StudentID", "Class"]], on="StudentID", how="left")

# ---------------------------------------------------------
# 4. SUBJECT-WISE AVERAGE MARKS
# ---------------------------------------------------------
subject_avg = marks_df.groupby("Subject")["Marks"].mean().round(2)
print("Subject-wise average marks:")
print(subject_avg)
print()

# Class-wise, subject-wise average (extra insight using merged data)
class_subject_avg = merged_df.groupby(["Class", "Subject"])["Marks"].mean().round(2)

# ---------------------------------------------------------
# 5. STUDENT-WISE TOTAL & AVERAGE
# ---------------------------------------------------------
student_summary = (
    merged_df.groupby(["StudentID", "Name", "Class"])["Marks"]
    .agg(Total="sum", Average=lambda x: round(x.mean(), 2))
    .reset_index()
    .sort_values("Average", ascending=False)
)

# ---------------------------------------------------------
# 6. TOPPER PER SUBJECT
# ---------------------------------------------------------
toppers = merged_df.loc[merged_df.groupby("Subject")["Marks"].idxmax()][
    ["Subject", "Name", "Marks"]
].reset_index(drop=True)

# ---------------------------------------------------------
# 7. WRITE SUMMARY REPORT
# ---------------------------------------------------------
with open("summary_report.txt", "w") as f:
    f.write("STUDENT MARKS ANALYSIS - SUMMARY REPORT\n")
    f.write("=" * 45 + "\n\n")

    f.write("1. Subject-wise Average Marks\n")
    f.write("-" * 30 + "\n")
    f.write(subject_avg.to_string() + "\n\n")

    f.write("2. Class & Subject-wise Average Marks\n")
    f.write("-" * 30 + "\n")
    f.write(class_subject_avg.to_string() + "\n\n")

    f.write("3. Student-wise Total & Average (ranked)\n")
    f.write("-" * 30 + "\n")
    f.write(student_summary.to_string(index=False) + "\n\n")

    f.write("4. Topper in Each Subject\n")
    f.write("-" * 30 + "\n")
    f.write(toppers.to_string(index=False) + "\n\n")

    overall_class_avg = merged_df.groupby("Class")["Marks"].mean().round(2)
    f.write("5. Overall Class Average\n")
    f.write("-" * 30 + "\n")
    f.write(overall_class_avg.to_string() + "\n")

print("Summary report written to summary_report.txt")

# Save cleaned data too, useful for the next day's visualization step
merged_df.to_csv("cleaned_merged_marks.csv", index=False)
