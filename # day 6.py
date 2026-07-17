# day 6 

import pandas as pd
import numpy as np


marks_df = pd.read_csv("student_marks.csv")
info_df = pd.read_csv("student_info.csv")

print("Raw Data:\n", marks_df)


print("\nMissing values per column:\n", marks_df.isnull().sum())


marks_df["Marks"] = marks_df.groupby("Subject")["Marks"].transform(
    lambda x: x.fillna(x.mean())
)

marks_df["Marks"] = marks_df["Marks"].round(2)

print("\nCleaned Data:\n", marks_df)


subject_avg = marks_df.groupby("Subject")["Marks"].mean().round(2)
print("\nSubject-wise Average Marks:\n", subject_avg)


student_avg = marks_df.groupby("Name")["Marks"].mean().round(2)
print("\nStudent-wise Average Marks:\n", student_avg)

merged_df = pd.merge(marks_df, info_df[["StudentID", "Class"]], on="StudentID", how="left")
print("\nMerged Data:\n", merged_df)


summary = merged_df.groupby(["Class", "Subject"])["Marks"].mean().round(2).reset_index()
summary.rename(columns={"Marks": "Average Marks"}, inplace=True)

print("\n===== SUMMARY REPORT =====")
print(sum)