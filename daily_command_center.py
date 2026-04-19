from datetime import datetime

# Get today's date
today = datetime.now().strftime("%Y-%m-%d")

print("\n🔥 DAILY COMMAND CENTER")
print(f"Date: {today}")
print("-" * 40)

# Get user input
main_focus = input("What is your MAIN focus today? ")
secondary_focus = input("Secondary focus: ")
outreach_target = input("How many outreach messages? ")
build_target = input("What are you building today? ")

print("\n📌 TODAY'S PLAN")
print("-" * 40)
print(f"Main Focus: {main_focus}")
print(f"Secondary Focus: {secondary_focus}")
print(f"Outreach Target: {outreach_target}")
print(f"Build Target: {build_target}")

# Save to file
filename = f"plan_{today}.txt"

with open(filename, "w") as file:
    file.write("DAILY PLAN\n")
    file.write(f"Date: {today}\n\n")
    file.write(f"Main Focus: {main_focus}\n")
    file.write(f"Secondary Focus: {secondary_focus}\n")
    file.write(f"Outreach Target: {outreach_target}\n")
    file.write(f"Build Target: {build_target}\n")

print("\n✅ Plan saved!")
print(f"File created: {filename}")