# -*- coding: utf-8 -*-

import os
if os.name == "nt":
    import win32api, win32con

DirList = [ #r"\\SYNOLOGY-DS-414\Video\Films", r"\\SYNOLOGY-DS-414\Video\Television",
            #r"\\DS3615xs_1\Video\Films", r"\\DS3615xs_1\Video\Television",
            #r"\\DS3615xs_2\Video\Films", r"\\DS3615xs_2\Video\Television",
            r"\\QNAP-TS-219\Video\Films", r"\\QNAP-TS-219\Video\Television",
            r"\\FREENAS\Video\Films", r"\\FREENAS\Video\Television" ]

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    dir_paths = []

    # Walk the directory.
    for file in os.scandir(directory):
        if file.is_dir():
            dir_paths.append(file)
        else:
            file_paths.append(file)  # Add it to the list.

    return dir_paths, file_paths  # Self-explanatory.

def os_walk(directory):
    paths = []

    path = os.walk(directory.name)



def file_is_hidden(p):
    if os.name == "nt":
        if p.startswith(".") == False:
#            attribute = win32api.GetFileAttributes(p)
#            attribute &= (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
#            return attribute
#        else:
            return False
    else:
        return p.startswith(".") #linux-osx

for dir in DirList:
    for dirName, subdirList, fileList in os.walk(dir):
        print('Found directory: %s' % dirName)
        for subdir in subdirList:
            for fname in fileList:
                old_path = dirName + os.sep + subdir + os.sep + fname
                if not file_is_hidden(old_path):
                    print(fname)
                    old_name = fname
                    new_name = fname.replace("..", ".")
                    print(new_name)
                    if new_name != old_name:
                        text = input("Double dots found in " + old_path  + " replace? : ")
                        if text.startswith("y"):
                            path = dirName + os.sep
                            print(path)
                            os.rename(path + old_name, path + new_name)