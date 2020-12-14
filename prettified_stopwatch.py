#! /usr/bin/python3

# stopwatch.py - A simple stopwatch program.

import time, pyperclip

def spaceRjust(num, length):	# Define a function to return a rjust format for provided numbers and length
	string = str(num).rjust(length, ' ')
	return string

# Display the program's instructions.
print('Press ENTER to begin, Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()			# press Enter to begin
print('Started.')
startTime = time.time()	# get the first lap's start time
lastTime = startTime
lapNum = 1
records = []		# Create a empty list to store messages that will be printted to the screen

# Start tracking the lap time.
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		#message = 'Lap #' + str(lapNum).rjust(2, ' ') + ': ' + str(totalTime).rjust(6, ' ') + ' (' + str(lapTime).rjust(6, ' ') + ')'
		message = 'Lap #' + spaceRjust(lapNum, 2) + ': ' + spaceRjust(totalTime, 6) + ' (' + spaceRjust(lapTime, 6) + ')'
		print(message, end='')
		records.append(message)	# Append the printed messages to the list
		lapNum += 1
		lastTime = time.time()	# reset the last lap time
except KeyboardInterrupt:
	# Handle the Ctrl-C exception to keep its error message from displaying.
	print('\n\nPrint Done')

# Copy the text output to the clipboard.
'''	# Just replace below codes with join()
text = ''
for i in range(len(records)):		# Merge all the solo strings into a large string
	if i == 0:
		text = text + records[i]
	else:
		text = text + '\n' + records[i]
'''

text = '\n'.join(records)		# Merge all the solo strings into a large string

pyperclip.copy(text)
pyperclip.paste()			# Copy the big string to the clipboard

print('\nText output copied to clipboard done\n')
