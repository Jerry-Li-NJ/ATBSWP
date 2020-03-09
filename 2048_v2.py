#! /usr/bin/python3

# 2048.py -- To play game 2048 automatically.

import random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def launchGameBoard(url):	# Launch the gaming web
	browser = webdriver.Firefox()
	browser.set_page_load_timeout(20)	# Shorten the page loading time
	try:
		browser.get(url)
	except:
		print('!!!Time out after 20 s during loading page!!!')
		browser.execute_script('window.stop()')
	return browser


def gameIsOver(browser):	# Check whether game is over
	status = browser.find_element_by_css_selector('.game-message').is_displayed()
	return status	# True or false


def getAllTileElements(browser):	# Get all elements of the tiles
	tiles = browser.find_elements_by_css_selector(".tile-container > div[class*='position']")
	print('Length of detected elements: ' + str(len(tiles)))	# Print the count of detected tile elements
	return tiles


def parseTilesToBoard(tiles):	# Parse the elements to a dictionary with position&value pairs
	gameBoard = {}
	for tile in tiles:
		tileClass = tile.get_attribute('class')
		print(tileClass)					# This is the real info we need to parse
		# Figure out position and corresponding value
		preValue, prePosition = tileClass.split(' tile-position-')	# Split the first time
		realValue = int(preValue.split('-')[1])				# Split the second time
		prePosition = prePosition[:3]	# Split off the lasting string	# Split the third time
		realPosition = (int(prePosition.split('-')[0]), int(prePosition.split('-')[1]))	# Position is a typle	# Split the forth time
		print('realValue: ' + str(realValue))
		print('realPosition: ' + str(realPosition))
		
		# Store the position and value to a dictionary
		gameBoard[realPosition] = realValue
	print('This is the dashboard: ' + str(gameBoard))
	return gameBoard


def parseBoardToValueList(gameBoard):
	valueList = []
	for v in gameBoard.values():
		valueList.append(v)
	print('List of values: ' + str(valueList))
	return valueList


def figureOutDuplicatedValuesOnly(valueList):
	valueCount = {}
	valueList.sort(reverse=True)
	duplicatedValues = []
	for i in range(len(valueList)):
		item = valueList[i]
		if item not in valueCount.keys():
			valueCount[item] = 1
		else:
			valueCount[item] = valueCount[item] + 1
			if item not in duplicatedValues:	
				duplicatedValues.append(item)
	valueList = duplicatedValues	# Update the value list
	print('List of values final: ' + str(valueList))
	return valueList


def determineFinalKey(valueList, gameBoard):
	moveKeystrokes = [Keys.ARROW_DOWN, Keys.ARROW_UP, Keys.ARROW_LEFT, Keys.ARROW_RIGHT]
	finalKey = ''
	if valueList == []:
		finalKey = moveKeystrokes[random.randint(0, 3)]
	else:
		# Loop through the duplicated values
		for value in valueList:
			# Check whether they are close
			# Extract all the positions for a same tile
			positionList = []
			for position in gameBoard.keys():
				if gameBoard[position] == value:
					positionList.append(position)
			print('Positions for tile %s: %s' %(str(value), str(positionList)))		
			# Loop through the position pairs
			length = len(positionList)
			for i in range(length):
				if finalKey != '':	# Once final key generated, stop loop
					break
				for j in range(i+1, length):
					if finalKey != '':	# Once final key generated, stop loop
						break
					if abs(positionList[i][0] - positionList[j][0]) == 1 and positionList[i][1] == positionList[j][1]:
						finalKey = moveKeystrokes[random.randint(2, 3)]
						print('Left and right.')
					elif abs(positionList[i][1] - positionList[j][1]) == 1 and positionList[i][0] == positionList[j][0]:
						finalKey = moveKeystrokes[random.randint(0, 1)]
						print('Up and down.')
					else:
						continue
			
		if finalKey == '':
			finalKey = moveKeystrokes[random.randint(0, 3)]
			print('Random.')
	return finalKey


def sendKeys(browser, finalKey):
	wholeHtml = browser.find_element_by_xpath('/html')
	wholeHtml.send_keys(finalKey)
	return browser


def getFinalScore(browser):
	score = browser.find_element_by_css_selector('.score-container')
	realScoreValue = score.text
	print('Score is ' + realScoreValue)

gameUrl = 'https://gabrielecirulli.github.io/2048/'

# Get all tiles in the browser
# Launch the game portal
xBrowser = launchGameBoard(gameUrl)

a = 0

while not gameIsOver(xBrowser):	# True
	a = a + 1
	print('##########################################################')
	print('#################### Time ' + str(a) + '#############################')
	print('##########################################################')

	time.sleep(3)
	xBrowser.implicitly_wait(20)
	
	xTiles = getAllTileElements(xBrowser)

	# Get all elements positions and values
	# Store all tiles in a data structure, like this {(1,2): 2, (2,2): 4}
	xGameBoard = parseTilesToBoard(xTiles)

	# Parse the tiles, then decide next step
	# Figure out whether there are same tiles

	# Copy all values to a list to figure out the same tiles
	xValueList = parseBoardToValueList(xGameBoard)

	# Get all values that are more than one, and list them in order
	# Update the valueList to save only duplicated values, and save the value and the corresponding count to dictionary

	# This will return a list of values that are only multiple
	# This will return a dictionary that store the values and the count
	xxValueList = figureOutDuplicatedValuesOnly(xValueList)
	xFinalKey= determineFinalKey(xxValueList, xGameBoard)

	# Send keystrokes
	xBrowser = sendKeys(xBrowser, xFinalKey)

# Get the final score
getFinalScore(xBrowser)


