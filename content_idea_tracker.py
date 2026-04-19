import csv
import os
from datetime import datetime

print("\n💡 CONTENT IDEA TRACKER")
print("-" * 40)
print("\nCapture it now. Organize it once. Build it later.\n")

today = datetime.now().strftime("%Y-%m-%d")
filename = "content_ideas.csv"

idea_type = input("Idea type (youtube / kdp / jde / ai product): ").strip().lower()
title = input("Idea title/name: ").strip()
topic = input("Topic or niche: ").strip()
platform = input("Platform (YouTube / KDP / LinkedIn / Fiverr / Other): ").strip()
status = input("Status (idea / researching / building / published): ").strip().lower()
notes = input("Notes: ").strip()

file_exists = os.path.isfile(filename)

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Date",
            "Idea Type",
            "Title",
            "Topic",
            "Platform",
            "Status",
            "Notes"
        ])

    writer.writerow([
        today,
        idea_type,
        title,
        topic,
        platform,
        status,
        notes
    ])

print("\n✅ Idea saved!")
print(f"File updated: {filename}")