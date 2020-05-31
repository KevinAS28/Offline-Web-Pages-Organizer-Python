import os
import getpass
import shutil

download_directory_full_path = f"/home/{getpass.getuser()}/Downloads"
target_offline_web = os.path.join(download_directory_full_path, "offline_pages")

list_downloaded_files = os.listdir(download_directory_full_path)
for file in list_downloaded_files:
    if file.endswith(".html"):
        file_name = file[:-5]
