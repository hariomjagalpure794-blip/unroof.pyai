#day 5

import re
import logging

logging.basicConfig(
    filename="text_extractor.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- Regex patterns ---
EMAIL_PATTERN = r"[\w.+-]+@[\w-]+\.[\w.-]+"
PHONE_PATTERN = r"(?:\+91[-\s]?)?[6-9]\d{9}"          # Indian 10-digit numbers, optional +91
DATE_PATTERN = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b"    # matches DD-MM-YYYY or DD/MM/YY etc.


def extract_emails(text):
    
    pass


def extract_phones(text):
    
    pass


def extract_dates(text):

    pass


def clean_phone(phone):
    """Strip out spaces/dashes/+91 so all numbers look the same, e.g. '+91-98765 43210' -> '9876543210'"""
    return re.sub(r"[^\d]", "", phone)[-10:]


def display_results(emails, phones, dates):
    print("\n" + "=" * 40)
    print("📊 EXTRACTED INFORMATION")
    print("=" * 40)

    print(f"\n📧 Emails found ({len(emails)}):")
    # TODO: loop and print each email, or "None found" if empty

    print(f"\n📱 Phone numbers found ({len(phones)}):")
    # TODO: loop and print each CLEANED phone number, or "None found" if empty

    print(f"\n📅 Dates found ({len(dates)}):")
    # TODO: loop and print each date, or "None found" if empty

    print("=" * 40)


def main():
    print("--- Text Information Extractor ---")
    print("Paste your text below. Type 'END' on a new line when done:\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    text = "\n".join(lines)

    if not text.strip():
        print("⚠️  No text provided.")
        logging.warning("Empty input provided.")
        return

    emails = extract_emails(text)
    phones = extract_phones(text)
    dates = extract_dates(text)

    display_results(emails, phones, dates)
    logging.info(f"Extraction complete: {len(emails)} emails, {len(phones)} phones, {len(dates)} dates")


if __name__ == "__main__":
    main()