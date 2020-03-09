#! /usr/bin/python3

# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
print(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

'''
#! /usr/bin/python3
# lucky.py - Open several Google search results.

import requests, sys, webbrowser, bs4, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
#logging.debug('Start of program')

print('Googling...') # display text while downloading the Google page
#logging.debug('Request URL: http://google.com/search?q=' + ' '.join(sys.argv[1:]))
print('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status
#logging.debug(res.text)


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
#logging.debug('Length of linkElems: ' + str(len(linkElems)))

# Open a browser tab for each result.
linkElems = soup.select('.jfp3ef a')
#logging.debug('Length of linkElems: ' + str(len(linkElems)))
assert len(linkElems) > 1, 'No element detected!'

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	#webbrowser.open('http://google.com' + linkElems[i].get('href'))
	#logging.debug(str(i) + 'URL will open: ' + linkElems[i].get('href'))
	webbrowser.open(linkElems[i].get('href'))

#logging.debug('End of program')


'''



