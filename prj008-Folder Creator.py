from pathlib import Path

path = "/Users/thibh/test_folder"

d = {"Movies": ["The Lord of the Rings",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
     "Employees": ["Paul",
                   "Pierre",
                   "Marie"],
     "Exercises": ["variables",
                   "files",
                   "loops"]}

for main_folder, sub_folders in d.items():
    for sub_folder in sub_folders:
        folder_path = Path(path) / main_folder / sub_folder
        folder_path.mkdir(exist_ok=True, parents=True)
