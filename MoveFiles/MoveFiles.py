# -*- coding: utf-8 -*-

import os
import shutil
if os.name == "nt":
    import win32api, win32con

DirList = [ r"\\SYNOLOGY-DS-414\Video\Films", r"\\SYNOLOGY-DS-414\Video\Television",
            r"\\DS3615xs_1\Video\Films", r"\\DS3615xs_1\Video\Television",
            r"\\DS3615xs_2\Video\Films", r"\\DS3615xs_2\Video\Television",
            r"\\QNAP-TS-219\Video\Films", r"\\QNAP-TS-219\Video\Television",
            r"\\FREENAS\Video\Films", r"\\FREENAS\Video\Television" ]

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the directory.
    for file in os.scandir(directory):
        if not file_is_hidden(file) and \
            not file.is_dir() and \
            not file.name.endswith(".jpg") and \
            not file.name.endswith(".nfo"):
                file_paths.append(file)  # Add it to the list.

    return file_paths  # Self-explanatory.


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


def output_file_text(file, fname):
    stat_info = os.stat(fname.path)
    spacing = " " * (132 - len(fname.name))

    output_str = fname.name
    if( stat_info.st_size > 0):
        output_str += spacing + format(stat_info.st_size, ",d") + " Bytes\n"
        file.write(output_str)
    else:
        file.write(output_str + "\n")

    output_str = fname.name
    if(stat_info.st_size > 0):
        output_str += spacing + format(stat_info.st_size, ",d") + " Bytes"
        print(output_str)
    else:
        print(output_str)

    return( stat_info )


def output_text(file, text):
    file.write(text + "\n")
    print(text)


try:
    separator = "\n\n\n"
    root_dir = DirList[8]
    root_dir = root_dir.rstrip(" ")
    files = get_filepaths(root_dir)
    files.sort(key=lambda x: x.name)
    for file in files:
        old_path = root_dir + os.sep + file.name
        old_path = old_path.rstrip(" ")
#        print(old_path)
        new_dir = root_dir + os.sep + file.name[:-4]
        new_dir = new_dir.rstrip(" ")
#        print(new_dir)
        try:
            os.makedirs(new_dir, exist_ok=True)
            new_path = new_dir + os.sep + file.name
            input_text = input( "Move " + old_path + " to " + new_path + "?: " )
            if input_text.startswith("y"):
#               os.rename(old_path, )
                shutil.move(old_path, new_path)

        except OSError as exc:  # Guard against race condition
            raise


except Exception:

    print(Exception.__name__)
    print(const.pi)
    print(const.e)


