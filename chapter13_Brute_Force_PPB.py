#! /usr/bin/python3

# chapter13_Brute_Force_PPB.py -- Try decrypt the PDF with every possible Englist Word.
# dictionary.txt is need for this script

import sys, os, PyPDF2

# Get the PDF file name from CMD.
if len(sys.argv) != 2:			# First, make sure 1 argument passed
	print('\n\tPlease make sure one and only one argument passed.\n')
elif not os.path.isfile(sys.argv[1]):	# Second, make sure the passed file exists
	print('\n\tPlease make sure the file exists.\n')
elif not sys.argv[1].endswith('.pdf'):	# Third, make sure the passed file is a PDF
	print('\n\tPlease make sure the file is a PDF.\n')
else:

# Save all the words from text file to a list.
	with open('dictionary.txt') as wordFile:
		longString = wordFile.read()
		wordList = longString.split('\n')	# Store the capital words to a list

# Loop over the list, try to decrypt the PDF file.
	PFR = PyPDF2.PdfFileReader(sys.argv[1])		# Generate the corresponding PdfFileReader object for the PDF
	for word in wordList:
		print('\n\t%s is on trying...\n' %(word))
		if PFR.decrypt(word) == 1:		# Try to decrypt with uppercase word
			thePassword = word
			break
		elif PFR.decrypt(word.lower()) == 1:
			thePassword = word.lower()	# Try to decrypt with lowercase word
			break
		else:
			continue

	print('\n\n\n\n\n\n\t###')
	print('\tPassword got: %s.' %(thePassword))	# Print the password for the PDF
	print('\t###')		
			
