from datetime import datetime

print("\n📊 WEEKLY REVIEW")
print("-" * 40)
print("\nNo zero days. Progress compounds.\n")

today = datetime.now().strftime("%Y-%m-%d")

print("Answer honestly — this is for YOU.\n")

worked_on = input("What did you work on this week? ")
completed = input("What did you COMPLETE? ")
progress = input("What made progress but isn’t finished? ")
struggles = input("What did you struggle with or avoid? ")
wins = input("Biggest win this week: ")
next_focus = input("Main focus for next week: ")

filename = f"weekly_review_{today}.txt"

with open(filename, "w") as file:
    file.write("WEEKLY REVIEW\n")
    file.write(f"Date: {today}\n\n")
    file.write(f"Worked On: {worked_on}\n\n")
    file.write(f"Completed: {completed}\n\n")
    file.write(f"In Progress: {progress}\n\n")
    file.write(f"Struggles: {struggles}\n\n")
    file.write(f"Biggest Win: {wins}\n\n")
    file.write(f"Next Week Focus: {next_focus}\n")

print("\n✅ Weekly review saved!")
print(f"File created: {filename}")