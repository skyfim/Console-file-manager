from modules import main_funcs as mf


while True:
    task = input("""Select an action:
                    --create folder
                    --delete file/folder
                    --copy file/folder
                    --view the contents of the working directory
                    --exit
                    write there - """)
    if task == "create":
        mf.create_new_folder()
    elif task == "delete":
        mf.delete_folder()
    elif task == "copy":
        mf.copy_obj()
    elif task == "view":
        mf.view_files_in_current_dir()
    elif task == "exit":
        break
