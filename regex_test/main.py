# -*- coding: utf-8 -*-

import re
import os
if os.name == "nt":
    import win32api, win32con

DirList = [ r"\\SYNOLOGY-DS-414\Video\Films",   r"\\SYNOLOGY-DS-414\Video\Television",
            r"\\DS3615xs_1\Video\Films",        r"\\DS3615xs_1\Video\Television",
            r"\\DS3615xs_2\Video\Films",        r"\\DS3615xs_2\Video\Television",
            r"\\QNAP-TS-219\Video\Films",       r"\\QNAP-TS-219\Video\Television",
            r"\\FREENAS\Video\Films",           r"\\FREENAS\Video\Television" ]

RegEx = [   #r"(?i)[!-._\\\/]@eadir[!-._\\\/]*$",
            #r"(?i)[!-._\\\/]featurette[!-._\\\/]*$",
            #r"(?i)[!-._\\\/]featurettes[!-._\\\/]*$",
            #r"(?i)[!-._\\\/]deleted[!-._\\\/]*$",
            #r"(?i)[!-._\\\/]deleted scenes[!-._\\\/]*s",
            #r"(?i)[!-._\\\/]Extras[!-._\\\/]*$",
            #r"(?i)[!-._\\\/]sample[!-._\\\/]*$",
            #r"(?i)[!-._\\\/]samples[!-._\\\/]*$"
            r"(?i)[!-._\/\\]extras|featurette|@eadir|deleted|sample|sample.|xtras|making of[!.-_\/\\]*$"
        ]


counter = 0
regex = re.compile(RegEx[0])
for dir in DirList:
    for root, dirs, files in os.walk(dir):
        for name in dirs:
            dir = os.path.join(root, name)
#            for regex in RegEx:
            if re.search(regex, dir):
                print(dir)
                counter = counter + 1

print("There were " + str(counter) + " items found.")

