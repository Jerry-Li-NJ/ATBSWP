#! /usr/bin/python3

# chapter11_ISD.py -- Go to flicker and download the friday related images.

import requests, bs4, os

def getImageUrls(url, css_seclector):
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)
	imageElems = soup.select(css_seclector)

	list = []	
	for singleImage in imageElems:
		imageUrl = singleImage.get('src')
		imageUrl = imageUrl.split('?')[0]
		list.append(imageUrl)
	
	return list


def downloadAndSave(urlList, localPath):
	os.makedirs(localPath, exist_ok=True)
	for url in urlList:
		draftFileName = os.path.basename(url)
		Filename = draftFileName.split('?')[0]

		localFile = open(os.path.join(localPath, Filename), 'wb')

		print('Downloading image from %s' % url)
		res = requests.get(url)

		print('Writing image to local.')
		for chunk in res.iter_content(100000):
			localFile.write(chunk)
		localFile.close()

url = 'https://blog.flickr.net/category/flickrfriday'

folderName = os.path.basename(url)

# Download the whole html
# Get the url of all images
listOfUrls = getImageUrls(url, '.post-thumbnail > img')

# Download all images and save them to local path
downloadAndSave(listOfUrls, folderName + '_v2')
	
# Get the filename
# Create file
# Download file from Internet
# Save file to local



