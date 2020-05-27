#! /usr/bin/python3

# chapter13_PP_step_1.py -- Go through every PDF in given folder, and encrypt them with given password.

import sys, os, pprint, PyPDF2

def get_file_and_path(folder):	# Get a dictionary that have paths the key and filename as the value
	FPDir = {}
	for root, dirs, files in os.walk(folder):
		print("Root is %s ### Dirs is %s ### Files is %s" %(root, dirs, files))
		for file in files:
			if file.endswith('pdf'):
				FPDir[file] = root
	return FPDir

# Get the folder name and the password.
if len(sys.argv) != 3:	# Check the number of argument
	print('\n\tPlease make sure you input 2 and only 2 arguments!')
elif not os.path.exists(sys.argv[1]):	# Check whether the path exist
	print('\n\tPlease make sure the path exists!')
else:
	#print('\n\tTest')

# Loop and get all the PDF paths.
	originalDict = get_file_and_path(sys.argv[1])
	pprint.pprint(originalDict)

# Loop over the list, then encrypt it, then save the new PDFs.
	for fileName, filePath in originalDict.items():	# Loop over the Dict
		ReadFile = open(os.path.join(filePath,fileName), 'rb')
		PFW = PyPDF2.PdfFileWriter()
		PFR = PyPDF2.PdfFileReader(ReadFile)
		
		for pageNum in range(PFR.numPages):	# Loop to add all pages in PFR to PFW
			page = PFR.getPage(pageNum)
			PFW.addPage(page)
		
		PFW.encrypt(sys.argv[2])		# Encrypt the PFW	
		nonPdfName = fileName.split('.')[0]
		WriteFile = open(os.path.join(filePath,nonPdfName + '_encrypted.pdf'), 'wb')
		PFW.write(WriteFile)			# Save encrypted PDF file to HD.
		print('\n' + os.path.join(filePath,fileName) + ' encrypted.')
		ReadFile.close()
		WriteFile.close()

# Loop and get all encrypted PDF paths.
	EPDFAddedDict = get_file_and_path(sys.argv[1])
	pprint.pprint(EPDFAddedDict)
	
	willDelKeys = []
	for fileName, filePath in EPDFAddedDict.items():
		if not fileName.endswith('_encrypted.pdf'):
			willDelKeys.append(fileName)
	
	for i in willDelKeys:
		del EPDFAddedDict[i]
	print('Encrypted PDF files:')
	pprint.pprint(EPDFAddedDict)

# Check all the files with reading and decryption.
	for fileName, filePath in EPDFAddedDict.items():	# Assert, decrypt
		EPath = os.path.join(filePath,fileName)
		EPFR = PyPDF2.PdfFileReader(EPath)
		decryptFlag = EPFR.decrypt(sys.argv[2])		# Decrypt the encrypted PDF
		if decryptFlag !=1:
			print(EPath + ' decrypt fail, please try again later!')
		else:
			print('\n' + EPath + ' decryption done.')
			textValue = EPFR.getPage(0).extractText()	# Read the file
			print('\n' + EPath + ' read check done.')
# Delete all original files.
	for fileName, filePath in originalDict.items():	# Loop over the Dict
		willDeletefile = os.path.join(filePath,fileName)
		os.remove(willDeletefile)
		print('\n' + willDeletefile + ' deleted.')
