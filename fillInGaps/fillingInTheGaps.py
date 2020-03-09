#! /usr/bin/python3

# fillingInTheGaps.py -- Locate any gaps in the numbering and rename all the later fils to close the gap.

import os, re

def transferWithValidNumber(aStringOrNumber, x='toValid'):
	# Transfer 001 to 1(integer) or transfer 1 to 001(string).
	if x == 'toValid':
		return int(aStringOrNumber)
	elif x == 'toString':
		if aStringOrNumber > 9:
			prefix = '0'
		else:
			prefix = '00'
		return prefix + str(aStringOrNumber)

def findGaps(originalList):
	# Detect the gaps in a list.
	# Return the gaps and the max number as an dictionary.
	originalList.sort()
	returnDictionary = {'gaps': []}	# Define a dictionary to save gaps and the max number.
	for i in range(len(originalList)):
		if i == 0:
			continue
		elif originalList[i] != originalList[i-1] + 1:
			returnDictionary['gaps'].append(originalList[i-1] + 1)
			returnDictionary['max'] = originalList[i]
		returnDictionary['max'] = originalList[i]
	return returnDictionary

	
def fillingInTheGaps(folder):
	# Create an regex.
	nameRegex = re.compile(r'''
		(spam)	# The spam
		(\d{3}) # 3 digits
		(\.txt)	# the file format
		''', re.VERBOSE)
	
	# Loop through all the files in folder to get the gap and max numbering.
	matchedFileNumbering = []
	notMatchedFiles = []
	for file in os.listdir(folder): # Loop to get a list of matched string.
		mo = nameRegex.search(file)
		if mo != None:
			matchedFileNumbering.append(mo.group(2))
		else:
			notMatchedFiles.append(file)
	# Print the gap.
	for i in range(len(matchedFileNumbering)):		# Transfer the list of sting to a list of integer.
		matchedFileNumbering[i] = transferWithValidNumber(matchedFileNumbering[i])
	gapsDetected = findGaps(matchedFileNumbering)['gaps']
	for x in gapsDetected:	# Find and print the gaps.
		gapMessage = 'The gap between the files is ' + str(x) + '.'
		print(gapMessage)

	# Rename files
	for i in range(len(notMatchedFiles)):
		newNumber = findGaps(matchedFileNumbering)['max'] + i + 1
		newName = 'spam' + transferWithValidNumber(newNumber, 'toString') + '.txt'	# Generate the new name.
		print(os.path.join(folder, notMatchedFiles[i]) + ' will be replaced with ' + os.path.join(folder, newName))
		os.rename(os.path.join(folder, notMatchedFiles[i]), os.path.join(folder, newName))
	# Return an interger list of the gap.
	return gapsDetected

#print(fillingInTheGaps('test_2'))





