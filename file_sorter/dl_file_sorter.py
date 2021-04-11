import os
import shutil


# FILES WILL BE SORTED BY FORMAT/EXTENSIONS

def sort_files():
    download_path = r'C:\Users\Kyriakos\Downloads'  # user = computer name
    list_of_files = os.listdir(download_path)  # 2. returns a list with all the items in download forlder

    os.chdir(download_path)  # 1. cd Downloads

    # 4. a list with all the folders where the files will be sorted
    main_folders = ("Execs", "PDFs", "Programs", "Zips", "Texts", "Folders", "Images", "Other")
    for folder in main_folders:
        if not os.path.exists(folder):
            os.makedirs(f'{download_path}\{folder}')

    # 3. folders' directories where the files will be sorted
    exec_folder = fr'{download_path}\Execs'
    pdf_folder = fr'{download_path}\PDFs'
    zip_folder = fr'{download_path}\Zips'
    text_folder = fr'{download_path}\Texts'
    folders = fr"{download_path}\Folders"
    images_folder = fr"{download_path}\Images"
    others = fr'{download_path}\Other'

    # 4. a list with all the folders where the files will be sorted

    # 5. list of item extensions
    execs_extension_list = [".exe", ".jar", ".msi", ".ini"]
    zips_extension_list = [".zip", ".rar", ".iso"]
    text_extension_list = [".txt", ".docx", ".doc", ".xlsx", ".xls", ".csv", ".json"]
    image_extension_list = [".jpg", ".png", ".jpeg"]

    for item in list_of_files:  # itterates though all the files in the download folder
        extension = os.path.splitext(item)[1]  # Get the extension of every non folder item
        if os.path.isfile(item):  # checks if item is a file
            if extension in execs_extension_list:
                shutil.move(item, exec_folder)
            elif extension == ".pdf":
                shutil.move(item, pdf_folder)
            elif extension in zips_extension_list:
                shutil.move(item, zip_folder)
            elif extension in text_extension_list:
                shutil.move(item, text_folder)
            elif extension in image_extension_list:
                shutil.move(item, images_folder)
            else:
                shutil.move(item, others)

        if os.path.isdir(item):  # checks if item is folder and if it is not one of the main folders, it sent to the
            # specified folder
            if item not in main_folders:
                shutil.move(item, folders)



sort_files()

# *IMPORTANT USE WINDOWS TASK SCHEDULER TO RUN IN BACKGROUND EVERY SPECIFIED TIME
