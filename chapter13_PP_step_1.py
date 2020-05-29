#! /usr/bin/python3

# chapter13_PP_step_1.py -- Go through every PDF in given folder, and encrypt them with given password.
# Usage:   ./chapter13_PP_step_1.py [path] [password]

import sys, os, pprint, PyPDF2

def get_file_and_path(folder):	# Get a dictionary that have paths the key and filename as the value
	FPDir = {}
	print('\n\t########################################################')
	print('\t############     Start walk the folder %s  #############' %(folder))
	print('\t########################################################\n\n')

	for root, dirs, files in os.walk(folder):
		print("Root: %s\tDirs: %s\tFiles: %s" %(root, dirs, files))
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

# Loop and get all the PDF paths.
	originalDict = get_file_and_path(sys.argv[1]) # Get all the PDF files in the given folder 
	#pprint.pprint(originalDict)

# Loop over the list, then encrypt it, then save the new PDFs.
	print('\n\t########################################################')
	print('\t############     Start file encryption  #############')
	print('\t########################################################\n\n')
	for fileName, filePath in originalDict.items():	# Loop over the Dict
		originalFileName = os.path.join(filePath,fileName)
		ReadFile = open(originalFileName, 'rb')
		PFW = PyPDF2.PdfFileWriter()
		PFR = PyPDF2.PdfFileReader(ReadFile)	# Load the PDF file
		
		for pageNum in range(PFR.numPages):	# Loop to copy all pages in PFR to PFW
			page = PFR.getPage(pageNum)
			PFW.addPage(page)
		
		PFW.encrypt(sys.argv[2])		# Encrypt the PFW	
		nonPdfName = fileName.split('.')[0]
		WriteFile = open(os.path.join(filePath,nonPdfName + '_encrypted.pdf'), 'wb')	# Generate the encrypted PDF name
		PFW.write(WriteFile)			# Save encrypted PDF file to HD.
		print('\n' + originalFileName + ' encrypted and encrypted file generated.')
		ReadFile.close()
		WriteFile.close()

# Loop and get all encrypted PDF paths.
	EPDFAddedDict = get_file_and_path(sys.argv[1])	# Get all the PDF files in the given folder again
	#pprint.pprint(EPDFAddedDict)
	
	#willDelKeys = []
	#for fileName, filePath in EPDFAddedDict.items():
		#if not fileName.endswith('_encrypted.pdf'):
			#willDelKeys.append(fileName)
	
	for i in originalDict.keys():
		del EPDFAddedDict[i]			# Delete the original filenames in the dictionary
	#print('Encrypted PDF files:')
	#pprint.pprint(EPDFAddedDict)

# Check all the files with reading and decryption.
	print('\n\t########################################################')
	print('\t############        Encrypted file checking  #############')
	print('\t########################################################\n\n')
	for fileName, filePath in EPDFAddedDict.items():	# Assert, decrypt
		EPath = os.path.join(filePath,fileName)
		EPFR = PyPDF2.PdfFileReader(EPath)
		decryptFlag = EPFR.decrypt(sys.argv[2])		# Decrypt the encrypted PDF
		if decryptFlag !=1:
			print(EPath + ' decrypt fail, please try again later!')
		else:
			print('\n' + EPath + ' decryption done.')
			textValue = EPFR.getPage(0).extractText()	# Read the file
			print('\n' + EPath + ' readable check done.')
# Delete all original files.
	print('\n\t########################################################')
	print('\t############        Deleting the original files  #############')
	print('\t########################################################\n\n')
	for fileName, filePath in originalDict.items():	# Loop over the Dict
		willDeletefile = os.path.join(filePath,fileName)
		os.remove(willDeletefile)
		print('\n' + willDeletefile + ' deleted.')
