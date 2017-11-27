# -*- coding: utf-8 -*-

import os
if os.name == "nt":
    import win32api, win32con

DirList = [ r"\\SYNOLOGY-DS-414\Video\Films", #r"\\SYNOLOGY-DS-414\Video\Television",
            r"\\DS3615xs_1\Video\Films", #r"\\DS3615xs_1\Video\Television",
            r"\\DS3615xs_2\Video\Films", #r"\\DS3615xs_2\Video\Television",
            r"\\QNAP-TS-219\Video\Films", #r"\\QNAP-TS-219\Video\Television",
            r"\\FREENAS\Video\Films"] #r"\\FREENAS\Video\Television" ]

ExtList = [ "AVI", "MPEG", "WMV", "ASF", "FLV", "MKV", "MKA", "mov", "MP4", "M4A", "AAC",
             "NUT", "Ogg", "OGM", "RAM", "RM", "RV", "RA", "RMVB", "3gp", "VIVO", "PVA",
             "NUV", "NSV", "NSA", "FLI", "FLC", "DVR-MS", "WTV", "MPG", "VOB", "bdmv" ]

def file_is_hidden(p):
    if os.name == "nt":
        if p.startswith(".") == False:
            attribute = win32api.GetFileAttributes(p)
            attribute &= (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
            return attribute
        else:
            return False
    else:
        return p.startswith(".") #linux-osx


for Dir in DirList:
#    print( Dir )
    for dirName, subdirList, fileList in os.walk(Dir):
        for subdir in subdirList:
            subdir = subdir.lower()
            if not subdir.endswith(".actors") and \
               not subdir.endswith("featurettes") and \
               not subdir.endswith("extras") and \
               not subdir.endswith("deleted") and \
               not subdir.endswith("sample") and \
               not subdir.endswith("extras-grym"):
                for fname in fileList:
                    dirName = dirName.lower()
                    fname = fname.lower()
                    old_path = dirName + os.sep + subdir + os.sep + fname
                    vid_found = False
#                   print("\t" + old_path)
#                   print("\tFound directory: %s" % dirName)
                    for extension in ExtList:
                        if (vid_found == False) and fname.endswith(extension.lower()):
                            vid_found = True
                            break

                    if vid_found == True:
                        break
                    else:
                        print( dirName + os.sep + subdir + " looks suspect" )
            else:
                print( dirName + os.sep + subdir + os.sep )