#! /usr/bin/python3

# chapter13_PP_step_2.py -- Find all encrypted PDFs in the given folder, and then create a decrypted copy.

import sys, os, pprint, PyPDF2

# Get folder path and password via command line.
if  len(sys.argv) != 3:
	print('\n\tPlease make sure only 2 arguments passed, the folder and the password.\n')
elif not os.path.exists(sys.argv[1]):
	print('\n\tPlease make sure the given path:#%s# really exists.\n' %(sys.argv[1]))
else:
	givenPath = sys.argv[1]
	givenPassword = sys.argv[2]

# Get all the encrypted PDFs in a dictionary.
	storeDict = {}
	for root, dirs, files in os.walk(givenPath):	# Walk the folder and subfolders of the given path
		for singleFile in files:
			if singleFile.endswith('encrypted.pdf'):	# Make sure all the selected files are encrypted
				storeDict[singleFile] = root
	print('\n\n\n\tThe dictionary that stored all the encrypted files:\n')
	pprint.pprint(storeDict)
	print('\n')
 
# Decrypt the PDFs and generate a copy. 
	for fileName, filePath in storeDict.items():	# Loop over the Dict
		fullPath = os.path.join(filePath, fileName)
		PFW = PyPDF2.PdfFileWriter()		# Create PdfFileWriter obj to copy pages
		PFR = PyPDF2.PdfFileReader(fullPath)
		decryptFlag = PFR.decrypt(givenPassword)	# Decryption
		if decryptFlag != 1:
			print('\n\tPassword incorrect, break to next one.\n')
			continue
		else:
			for i in range(PFR.numPages):	# Copy every page to another PdfFileWriter obj
				pageObj = PFR.getPage(i)
				PFW.addPage(pageObj)

		originalNameList = fileName.split('_')
		newFileName = originalNameList[0] + '.' + originalNameList[1].split('.')[1]	# Generate new name
		newFullPath = os.path.join(filePath, newFileName)
		#print('\n\tNew file name: %s\n' %(newFileName))
		saveFile = open(newFullPath, 'wb')
		PFW.write(saveFile)
		print('\n\t%s .generated\n' %(newFileName))
		saveFile.close()

