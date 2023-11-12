import os
import shutil

from_dir = "C:/Users/Asus/Downloads"
to_dir = 'C:/Adithya/document_files'

# List of allowed extensions
allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']

list_of_files = os.listdir(from_dir)

for files in list_of_files:
    file_name, file_extension = os.path.splitext(files)

    # Check if the extension is blank (empty string)
    if file_extension == "":
        continue

    # Check if the extension is one of the allowed extensions
    if file_extension in allowed_extensions:
        # Your code for processing files with allowed extensions
        # You can copy or move the file to the target directory here
        shutil.move(os.path.join(from_dir, files), os.path.join(to_dir, files))
