import csv
import os
from datetime import datetime

print("\n📬 OUTREACH LOGGER")
print("-" * 40)
print("\nNo zero days. Stay visible.\n")

today = datetime.now().strftime("%Y-%m-%d")
filename = "outreach_log.csv"

name = input("Contact name: ").strip()
company = input("Company: ").strip()
contact_type = input("Type (coworker / client / recruiter / hiring manager): ").strip()
platform = input("Platform (LinkedIn / email / text / other): ").strip()
message_sent = input("Message sent? (yes/no): ").strip().lower()
notes = input("Notes: ").strip()

file_exists = os.path.isfile(filename)

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Date",
            "Contact Name",
            "Company",
            "Type",
            "Platform",
            "Message Sent",
            "Notes"
        ])

    writer.writerow([
        today,
        name,
        company,
        contact_type,
        platform,
        message_sent,
        notes
    ])

print("\n✅ Outreach entry saved!")
print(f"File updated: {filename}")