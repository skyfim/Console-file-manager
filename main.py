from modules import main_funcs as mf


task = input("""Select an action:
                    --create folder
                    --delete file/folder
                    --copy file/folder
                    --view the contents of the working directory""")

if task == "create":
    mf.create_new_folder()
