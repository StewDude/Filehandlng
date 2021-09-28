

# -*- coding: utf-8 -*-

import os
if os.name == "nt":
    import win32api, win32con

DirList = [ r"\\SYNOLOGY-DS-414\Video\Films", r"\\SYNOLOGY-DS-414\Video\Television",
#            r"\\DS3615xs_1\Video\Films", r"\\DS3615xs_1\Video\Television",
#            r"\\DS3615xs_2\Video\Films", r"\\DS3615xs_2\Video\Television",
            r"\\QNAP-TS-219\Video\Films", r"\\QNAP-TS-219\Video\Television",
            r"\\FREENAS\Video\Films", r"\\FREENAS\Video\Television" ]

#DirList = [r"\\FREENAS\mnt\zfs_pool\Video\Films\James.Bond.007.The.Complete.Series 1962-2015.BluRay.1080p.x265.10bit.MNHD-FRDS"]

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
    with open(r"C:\Temp\DirList.txt", "w", encoding="utf-8") as out_file:
        total_size = 0
        for Dir in DirList:
            list = []
            dir_size = 0
            output_text(out_file, "Directory of " + Dir + "\n")

            dir_list, file_list = get_filepaths(Dir)
            dir_list.sort(key = lambda x: x.name)
            for dir_name in dir_list:
                if not file_is_hidden(dir_name):
                    output_file_text(out_file, dir_name)

            file_list.sort(key = lambda x: x.name)
            for filename in file_list:
                if not file_is_hidden(filename) and \
                not filename.name.endswith(".jpg") and \
                not filename.name.endswith(".txt") and \
                not filename.name.endswith(".url") and \
                not filename.name.endswith(".png") and \
                not filename.name.endswith(".nfo"):
                    statinfo = output_file_text(out_file, filename)
                    dir_size += statinfo.st_size

            total_size += dir_size
            out_text = "\nDirectory size is: " + format(dir_size, ",d") + " Bytes" + separator
            output_text(out_file, out_text)

        out_text = "\nTotal size is: " + format(total_size, ",d") + " Bytes" + "\n"
        output_text(out_file, out_text)
        out_file.close()

except Exception:
    print(Exception.__name__)
