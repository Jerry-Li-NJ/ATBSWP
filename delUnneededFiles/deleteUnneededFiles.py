#! /usr/bin/python3
# deleteUnneededFiles.py -- Walk through a folder tree and delete the large files.

import os, sys

def delLargeFiles(folder):
# Walk through the folder tree.
	for foldername, subfolders, files in os.walk(folder):
		print('Now going through ' + foldername + '...')

		# Search for large files that is more than 100MB.
		for file in files:
			filePath = os.path.join(foldername, file)
			if os.path.getsize(filePath) > 100*1024*1024:

				# Delete the files and print it to the screen.
				print(os.path.abspath(filePath) + ' deleted.')
				os.unlink(filePath)
		print('\n')

delLargeFiles(sys.argv[1])
