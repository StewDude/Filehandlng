from os import listdir, mkdir, path, rename
from os.path import isfile, join, isdir
import shutil

if __name__ == "__main__":
    checking_dir = r'\\OMV-3\media\Video\Television'
    file_types = ['AVI', 'MPEG', 'WMV', 'ASF', 'FLV', 'MKV', 'MKA', 'QT', 'MP4', 'M4A',
                  'AAC', 'NUT', 'OGG', 'OGM', 'RAM', 'RM', 'RV', 'RA', 'RMVB', '3GP',
                  'VIVO', 'PVA', 'NUV', 'NSV', 'NSA', 'FLI', 'FLC', 'DVR-MS', 'WTV', 'TRP', 'F4V']

    only_dirs = [d for d in listdir(checking_dir) if isdir(checking_dir)]

    if only_dirs != []:
        for d in only_dirs:
            present_dir = checking_dir + "\\" + d
            print(present_dir)
            only_files = [f for f in listdir(present_dir) if isfile(join(present_dir, f))]
            count = 0
            for f in only_files:
                for e in file_types:
                    extension = '.' + e.casefold()
                    print(f'Comparing {extension}')
                    f.casefold()
                    if f.find(extension) != -1:
                        count += 1
                        print(f'{f} has extension {e} in it!')
                        break
                if(count == 0):
                    print(f'{checking_dir} has no discoverable video files')