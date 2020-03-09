#! /usr/bin/python3

# insertGaps.py -- Insert gaps into numbered files with new added files.

import fillingInTheGaps, os

def insertGaps(folder):
	# Detect the gaps.
	gapsDetectedNew = fillingInTheGaps.fillingInTheGaps(folder)

	# Generate the gap files name.
	for i in range(len(gapsDetectedNew)):	# Replaced the items with string format. 
		gapsDetectedNew[i] = fillingInTheGaps.transferWithValidNumber(gapsDetectedNew[i], 'toString')

	gapFileNames = []
	for stuff in gapsDetectedNew:		# Generate and save the full name to a list.
		name = 'spam' + stuff + '.txt'
		gapFileNames.append(name)

	# Create the gap files.
	for file in gapFileNames:
		print(os.path.join(folder, file) + ' will be created.')
		x = open(os.path.join(folder, file), 'w')
		x.close()


insertGaps('test_2')		

