#! /usr/bin/python3

#selectiveCopy.py -- Walk through a folder tree and search for files with certain extension, then copy these files to a new folder.

import os, shutil

def selectiveCopy(folder, new_folder):
# Walk through the folder tree.
	for folderName, subfolderName, files in os.walk(folder):
		print('Current folder: ' + folderName + '####')

		# Copy the xx.pdf files to a new folder.
		for file in files: # Loop the files.
			if not file.endswith('.pdf'):
				continue
			print(os.path.join(folderName, file) + ' copied to ' + new_folder + '.')
			shutil.copy(os.path.join(folderName, file), new_folder)


selectiveCopy('folder_a', 'new')
