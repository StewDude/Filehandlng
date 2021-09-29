
import re
import os
import shutil

no_year = 'No Year Found'

def rename_folder(folder):
	final_name = None
	folder_strip = folder.rstrip()
	correct = re.search(r' \((19|20)\d{2}\)', folder_strip)
	spc_dot = re.search(r'( |\.)(19|20)\d{2}', folder_strip)

	if (correct !=  None) and (correct.span()):
		pass
	elif (spc_dot != None) and (spc_dot.span()):
		year = spc_dot.group()
		folder_name = folder_strip[0:spc_dot.start()]
		final_name = folder_name + ' (' + year[1:5] + ')'
	else:
		final_name = no_year

	return(final_name)

dir_src = r"\\OMV-3\media\Video\Films"

if __name__ == "__main__":
	for root, dirs, files in os.walk(dir_src):
		for folder in dirs:
			name = rename_folder(folder)
			if name == None:
				print(f'{folder} is correct')
			elif name == no_year:
				print(f'{folder}: {name}')
			else:
				print(f'{folder} becomes >>>> {name}')