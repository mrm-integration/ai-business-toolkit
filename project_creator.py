import os
from datetime import datetime

print("\n📁 PROJECT CREATOR")
print("-" * 40)
print("\nNo zero days. Build something.\n")

project_type = input("Project type (youtube / kdp / jde): ").strip().lower()
project_name = input("Project name: ").strip()

date_str = datetime.now().strftime("%Y-%m-%d")
safe_name = project_name.replace(" ", "_")
folder_name = f"{date_str}_{safe_name}"

base_path = r"C:\AI_BUSINESS"

project_paths = {
    "youtube": ["script", "audio", "images", "video", "thumbnails", "notes"],
    "kdp": ["draft", "interior", "cover", "keywords", "notes", "final"],
    "jde": ["requirements", "demo", "screenshots", "notes", "proposal", "final"]
}

if project_type not in project_paths:
    print("\n❌ Invalid project type. Use youtube, kdp, or jde.")
else:
    main_folder = os.path.join(base_path, project_type, folder_name)
    os.makedirs(main_folder, exist_ok=True)

    for subfolder in project_paths[project_type]:
        os.makedirs(os.path.join(main_folder, subfolder), exist_ok=True)

    notes_file = os.path.join(main_folder, "notes", "project_notes.txt")
    with open(notes_file, "w") as file:
        file.write(f"Project Type: {project_type}\n")
        file.write(f"Project Name: {project_name}\n")
        file.write(f"Date Created: {date_str}\n")

    print("\n✅ Project created successfully!")
    print(f"Location: {main_folder}")
    print("Subfolders created:")

    for subfolder in project_paths[project_type]:
        print(f" - {subfolder}")