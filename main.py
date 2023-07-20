from modules import main_funcs as mf
run = True

task = input("""Select an action:
                    --create folder
                    --delete file/folder
                    --copy file/folder
                    --view the contents of the working directory
                    write there - """)

for i in range(2):
    if task == "create":
        mf.create_new_folder()
    elif task == "delete":
        mf.delete_folder()
    elif task == "copy":
        mf.copy_obj()
    elif task == "exit":
        break
