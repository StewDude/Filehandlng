
# -*- coding: utf-8 -*-

import os
if os.name == "nt":
    import win32api, win32con

import subprocess as sp

cmd_name = r'"C:\Program Files\MediaInfoCLI\mediainfo"'
path = r'"\\QNAP-TS-219\Video\Films'
filename = r'\A German Youth (2015)\A German Youth (2015).mp4"'

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

    for dirName, subdirList, fileList in os.walk(directory):
        print("Found directory: {}".format(dirName))
        for fname in fileList:
            if fname.name.replace("..", "."):
                print('\t%s' % fname)


def file_is_hidden(p):
    if os.name == "nt":
        if p.name.startswith(".") == False:
            attribute = win32api.GetFileAttributes(p.path)
            attribute &= (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
            return attribute
        else:
            return True
    else:
        return p.name.startswith(".") #linux-osx

try:
    dir_list, file_list = get_filepaths(path)
    p = sp.run( cmd_name + " " + path + filename, shell=True, capture_output=True, text=True)
    print( p.stdout )

except Exception:
    print(Exception.__name__)

