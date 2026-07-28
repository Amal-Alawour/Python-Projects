import os
import shutil


def organize_files(folder_path):

    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Excel-Files": [".xlsx", ".xls", ".csv"],
        "Videos": [".mp4", ".avi"],
    }

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):

            file_extension = os.path.splitext(file_name)[1].lower()

            moved = False

            for folder, extensions in file_categories.items():

                if file_extension in extensions:

                    destination_folder = os.path.join(
                        folder_path,
                        folder
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

                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(
                    folder_path,
                    "Other-Files"
                )

                os.makedirs(
                    other_folder,
                    exist_ok=True
                )

                shutil.move(
                    file_path,
                    os.path.join(
                        other_folder,
                        file_name
                    )
                )


folder = input("Enter folder path: ")

organize_files(folder)

print("Files organized successfully!")
