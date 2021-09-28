import subprocess
import os

new_dir = r'\\OMV-1\media\Video\Television'
dir = os.chdir( new_dir )
output = subprocess.check_output( "dir")
print(output)