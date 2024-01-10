"""
Sort the files in the 'data' folder based on the following associations:
mp3, wav, flac: Music
avi, mp4, gif: Videos
bmp, png, jpg: Images
txt, pptx, csv, xls, odp, pages: Documents
other: Miscellaneous
"""
from pathlib import Path

EXTENSIONS_MAPPING = {".mp3": "Music",
                      ".wav": "Music",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".gif": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".csv": "Documents",
                      ".xls": "Documents",
                      ".odp": "Documents",
                      ".pages": "Documents"}

BASE_DIR = Path('/Users/thibh/sorter_files/data')

# Get all files in the base directory
files = [f for f in BASE_DIR.iterdir() if f.is_file()]
for file in files:  # Loop through each file
    # Get the target folder based on the dictionary
    target_folder = EXTENSIONS_MAPPING.get(file.suffix, "Miscellaneous")
    # Concatenate the base directory with the target folder
    target_folder_absolute = BASE_DIR / target_folder
    # Create the target folder if it does not already exist
    target_folder_absolute.mkdir(exist_ok=True)
    # Concatenate the target folder with the file name
    target_file = target_folder_absolute / file.name
    # Move the file
    file.rename(target_file)
