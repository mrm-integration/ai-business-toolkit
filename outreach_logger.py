import csv
import os
from datetime import datetime

print("\n📬 OUTREACH LOGGER")
print("-" * 40)
print("\nNo zero days. Stay visible.\n")

filename = "outreach_log.csv"
file_exists = os.path.isfile(filename)

while True:
    today = datetime.now().strftime("%Y-%m-%d")

    name = input("\nContact name: ").strip()
    company = input("Company: ").strip()
    contact_type = input("Type (coworker / client / recruiter): ").strip()
    platform = input("Platform: ").strip()
    message_sent = input("Message sent? (yes/no): ").strip().lower()
    notes = input("Notes: ").strip()

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date", "Contact Name", "Company",
                "Type", "Platform", "Message Sent", "Notes"
            ])
            file_exists = True

        writer.writerow([
            today, name, company,
            contact_type, platform, message_sent, notes
        ])

    print("\n✅ Entry saved!")

    again = input("\nAdd another? (y/n): ").strip().lower()
    if again != "y":
        break

print("\nDone logging outreach.")