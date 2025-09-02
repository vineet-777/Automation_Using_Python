"""
File Organizer Script
---------------------
Organizes files in a specified folder into subfolders based on their file extensions.

Created on: Sep 2, 2025
Author: Vineet Gawali
"""

import os
import shutil
import sys

def organize_folder(path: str):
    """
    Sorts files in the given folder into subfolders named after their file extensions.
    """
    if not os.path.exists(path):
        print("❌ The path doesn't exist:", path)
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        # Skip directories
        if os.path.isfile(file_path):
            # Get file extension or use 'OTHERS' for files without one
            ext = file.split(".")[-1].upper() if "." in file else "OTHERS"

            # Create the subfolder if it doesn't exist
            folder = os.path.join(path, ext)
            os.makedirs(folder, exist_ok=True)

            # Move the file into the appropriate folder
            shutil.move(file_path, os.path.join(folder, file))
            print(f"✅ {file} → {ext}/")

if __name__ == "__main__":
    # Check for command-line argument, else ask for input
    if len(sys.argv) == 2:
        folder_path = sys.argv[1]
    else:
        folder_path = input("📂 Enter the full path to the folder you want to organize: ").strip()

    organize_folder(folder_path)
