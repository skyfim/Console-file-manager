import os
import shutil


def create_new_folder():
    folder_name = input("Enter folder name: ")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


def delete_folder():
    folder_to_remove = input("Enter folder name: ")
    os.rmdir(folder_to_remove)


def copy_obj():
    folder_to_copy = input("Enter folder name: ")
    new_folder_name = input("Enter new folder name: ")
    shutil.copytree(folder_to_copy, new_folder_name)


if __name__ == "__main__":
    print("This is main_funcs.py")