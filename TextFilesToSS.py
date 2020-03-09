#! /usr/bin/python3

import sys, openpyxl, os

# Get filenames from command line.
if len(sys.argv) < 2:
	print('''
		Please make sure one filename passed at least!!!
		''')
else:
	result = True
	for i in range(1, len(sys.argv)):
		result = os.path.exists(sys.argv[i]) and result
	if result != True:
		print('''
		Please make sure all the files really exists!!!
		''')
	else:
		#print('Pass')
		

# Read data from text file, write data to the spreadsheet in a for loop.
		wb = openpyxl.Workbook()
		sheet = wb.active
		
		for i in range(1, len(sys.argv)):
			textFile = open(sys.argv[i])
			texts = textFile.readlines()
			textFile.close()
			#print(texts)
			for j in range(1, len(texts)+1):
				#print('j: ' + str(j))
				sheet.cell(row=j, column=i, value=texts[j-1].strip())

# Save the generated spreadsheet file.
		print('''
	New spreadsheet generated...SSForxxxx.xlsx
			''')
		wb.save('SSForxxxx.xlsx')


