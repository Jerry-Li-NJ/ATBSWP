#! /usr/bin/python3

# chapter11_ISD.py -- Go to flicker and download the friday related images.

import requests, bs4, os

url = 'https://blog.flickr.net/category/flickrfriday'

#print(os.path.basename(url))
os.makedirs(os.path.basename(url), exist_ok=True)
folderName = os.path.basename(url)

# Download the whole html

res = requests.get(url)
res.raise_for_status()

# Get the url of all images

soup = bs4.BeautifulSoup(res.text)
imageElems = soup.select('.post-thumbnail > img')
#print(len(imageElems ))

# Download all images and save them to local path
for singleImage in imageElems:
	imageUrl = singleImage.get('src')
	imageUrl = imageUrl.split('?')[0]	
	print(imageUrl)
	
	# Get the filename
	draftFileName = os.path.basename(imageUrl)
	Filename = draftFileName.split('?')[0]
	#print(Filename)

	# Create file
	#print(folderName)
	#print(os.path.join(folderName, Filename))
	localFile = open(os.path.join(folderName, Filename), 'wb')

	# Download file from Internet
	print('Downloading image from %s' % imageUrl)
	res = requests.get(imageUrl)

	# Save file to local
	print('Writing image to local.')
	for chunk in res.iter_content(100000):
		localFile.write(chunk)
	localFile.close()
	
# Load More Posts? No, I don't want to make this program to much complex
