import os

def create_new_folder():
    folder_name = input("Enter a folder name: ")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


