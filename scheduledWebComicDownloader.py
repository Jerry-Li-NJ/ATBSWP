#! /usr/bin/python3

# scheduledWebComicDownloader.py -- Check updates for several websites of comics, and then copy it to desktop after downloading the new updates.

import requests, os, shutil, threading
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}

# Define a function for web comic downloading
def commonComicDownloader(folder, url, imageSelector, previousSelector, processFlag, imageSelectorChanged="#comic > img"):
	savePath = os.path.join(os.getcwd(), 'scheduledWebComicDownloader', folder)
	os.makedirs(savePath, exist_ok=True)	# Create a directory to store the images
	firstURL = url
	toBeCopied = []
	while True:
		# Get the image URL
		print(processFlag + '########################')
		print(processFlag + 'Scrapping the page of ' + firstURL + '...')
		r = requests.get(firstURL, headers=headers)
		r.raise_for_status()
		soup = BeautifulSoup(r.text, 'html.parser')
		ele = soup.select(imageSelector)
		if ele == []:
			ele = soup.select(imageSelectorChanged)
		urlOfComic = ele[0]['src']
		print(processFlag + 'Comic image URL got: ' + urlOfComic)
		
		# Check whether this comic exists
		baseName = os.path.basename(urlOfComic)
		pathAndFileName = os.path.join(savePath, baseName)
		if os.path.isfile(pathAndFileName):
			print(processFlag + "File-" + baseName + " already exists, stop now.")
			break
		else:
			# Download the image
			imageRaw = requests.get(urlOfComic, headers=headers)
			imageRaw.raise_for_status()
			print(processFlag + 'Downloading the image...')
			with open(pathAndFileName, 'wb') as fd:
				for chunk in imageRaw.iter_content(chunk_size=128):
					fd.write(chunk)
			
			toBeCopied.append(pathAndFileName)

			print(processFlag + 'Downloading done, image saved to ' + pathAndFileName)
			
			# Get the URL of previous comic
			previousEle = soup.select(previousSelector)
			if len(previousEle) == 0:
				print(processFlag + 'Downloading is done!!!')
			else:
				urlOfPreviousComic = previousEle[0]['href']
				print(processFlag + 'Previous URL detected: ' + urlOfPreviousComic + '\n')
				firstURL = urlOfPreviousComic

	# Copy new comics to the desktop
	if toBeCopied == []:
		return None
	else:
		print(processFlag + 'Start copying...')
		for file in toBeCopied:
			newPath = os.path.join('/', 'root', 'Desktop', os.path.basename(file))
			shutil.copy(file, newPath)
			print(processFlag + '\t' + os.path.basename(file) + ' copied to the Desktop.')
		


# Run the three functions in multiple threads

kwArguments = [
		{'folder':'buttersafe', 'url':'https://www.buttersafe.com', 'imageSelector':"#comic > img", 'previousSelector':"[rel=prev]", 'processFlag':'1st thread '}, 
		{'folder':'happletea', 'url':'http://www.happletea.com', 'imageSelector':"#comic > a > img", 'previousSelector':".navi.comic-nav-previous.navi-prev", 'processFlag':'2nd thread '}, 
		{'folder':'nonadventures', 'url':'http://nonadventures.com', 'imageSelector':"#comic > img", 'previousSelector':".nav > a:nth-of-type(2)", 'processFlag':'3rd thread '}]

ts = []

for i in range(len(kwArguments)):	# Start the three threads
	t =  threading.Thread(target=commonComicDownloader, kwargs=kwArguments[i])
	ts.append(t)
	t.start()

for thread in ts:		# Waiting for the threads to terminate
	thread.join()

print('All done!!!')


