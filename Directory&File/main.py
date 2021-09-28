from os import listdir, mkdir, path, rename
from os.path import isfile, join, isdir
import shutil

mypath = r'\\OMV-1\downloads\complete\Great Films 4 Mp4 1080p'
terminating = " 1080p Surround"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

if onlyfiles != []:
    for f in onlyfiles:
        pos = f.find(terminating)
        print(f, "  ", pos)
        dir_name = f[0:pos]
        print(dir_name)
        target_dir = path.join(mypath, dir_name)
        print(f'Checking whether {target_dir} exists...')
        if not path.exists(target_dir):
            full_path_src = mypath + '\\' + f
            print(full_path_src)
            full_path_dst = target_dir + '\\'
            print(f"It doesn't. Creating {target_dir}")
            mkdir(target_dir)
            print(f'Copying {full_path_src} to {full_path_dst}')
            shutil.move(full_path_src, full_path_dst)
else:
    print(f'No files found in directory "{mypath}".')
