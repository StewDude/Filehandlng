
import os

root = r'\\OMV-3\media\Video\Films'
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
print (dirlist)