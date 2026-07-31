import os
import shutil


def organize_files(folder_path):

    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return

    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Excel-Files": [".xlsx", ".xls", ".csv"],
        "Videos": [".mp4", ".avi"]
    }

    moved_files = 0

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        file_extension = os.path.splitext(file_name)[1].lower()

        destination = "Other-Files"

        for folder, extensions in file_categories.items():

            if file_extension in extensions:
                destination = folder
                break

        destination_folder = os.path.join(
            folder_path,
            destination
        )

        os.makedirs(
            destination_folder,
            exist_ok=True
        )

        shutil.move(
            file_path,
            os.path.join(
                destination_folder,
                file_name
            )
        )

        moved_files += 1

    print(f"{moved_files} files organized successfully!")


folder = input("Enter folder path: ")

organize_files(folder)
