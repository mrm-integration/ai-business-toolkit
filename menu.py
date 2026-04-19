import os

def run_script(script_name):
    if os.path.exists(script_name):
        os.system(f'python "{script_name}"')
    else:
        print(f"\n❌ Could not find {script_name}\n")

while True:
    print("\n🧠 PYTHON BUSINESS TOOLKIT")
    print("-" * 40)
    print("1 - Daily Command Center")
    print("2 - Project Creator")
    print("3 - Outreach Logger")
    print("4 - Content Idea Tracker")
    print("5 - Weekly Review")
    print("6 - Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        run_script("daily_command_center.py")
    elif choice == "2":
        run_script("project_creator.py")
    elif choice == "3":
        run_script("outreach_logger.py")
    elif choice == "4":
        run_script("content_idea_tracker.py")
    elif choice == "5":
        run_script("weekly_review.py")
    elif choice == "6":
        print("\nGood work. Keep building.\n")
        break
    else:
        print("\nInvalid choice. Try again.\n")