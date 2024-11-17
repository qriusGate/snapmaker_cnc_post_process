"""This file is meant to automatically detect what variant of FreeCAD you are running (snap, appimage, etc), and place the post_processors in the correct folder.
This program assumes you have run FreeCAD at least once before, to ensure that the files and folders have been set up already"""

import os #for the path
import sys #for the args, which are not implemented yet
import shutil
import getpass

user = getpass.getuser()

base_path = "/home/" + user
snap_path = base_path + "/snap/freecad/common/"
deb_path = base_path + "/.local/share/FreeCAD/Macro/"

a350 = "snapmaker_a350_post.py"
a250 = "snapmaker_a250_post.py"
artisan = "snapmaker_artisan_post.py"
post_processor = "./"
macro_path = ""

def detect_path():
# The snap path is given priority, since this is the Ubuntu standard
    if os.path.exists(snap_path):
        macro_path = snap_path
    elif os.path.exists(deb_path):
        macro_path = deb_path
    else:
        print("It appears your macros folder is not setup. Please run FreeCAD to set these up automatically")
        return 0
    return macro_path

print(base_path)
if os.path.exists(base_path):
    print("YAY")
macro_path = detect_path()
if macro_path != 0:
    choice = input("What unit do you want to have the post-processor for (select one) : A250/A350/Artisan/other \n")
    if choice.lower() == "a250":
        post_processor = a250
    elif choice.lower() == "a350":
        post_processor = a350
    else:
        post_processor = artisan

shutil.copy2("./"+post_processor, macro_path+post_processor)