import os
import shutil

# defining the file path
path = r"C:/testing/"

# checks the files in the path
file_name = os.listdir(path)

# give the folder names
folder_names = ['excel files' , 'image files' , 'text files']

# checking if the folders given above are already present , if not create it
for loop in range(0, len(folder_names)):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])

# loop
for file in file_name:

    # checking the file type by their extensions
    if ".xlsx" in file and not os.path.exists(path + "excel files/" + file):
        shutil.move(path + file, path + "excel files/" + file)

    # doing the same for other file types
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)

    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)

    else:
        print("There are files that are not moved")

