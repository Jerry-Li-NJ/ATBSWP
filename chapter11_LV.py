#! /usr/bin/python3

# download all links inside given URL, and print all broken links.

import sys, os, requests, bs4, time

def writeToLocal(r, fileName):
	with open(fileName, 'wb') as fd:
		for chunk in r.iter_content(chunk_size=100000):
			fd.write(chunk)



# Get the given URL from command line argument
if len(sys.argv) == 2:
	url = sys.argv[1]
elif len(sys.argv) == 1:
	print('Please add 1 argument!' + '\n\tUsage: chapter11_LV.py www.baidu.com')
else:
	print('Only 1 argument is permitted!' + '\n\tUsage: chapter11_LV.py www.baidu.com')

# Create a folder to save all downloaded pages
os.makedirs('link_verification', exist_ok=True)

# Download the page
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.5', 
		'Cache-Control': 'max-age=0', 
		'Connection': 'keep-alive', 
		'Host': 'www.baidu.com', 
		'Upgrade-Insecure-Requests': '1', 
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

r = requests.get(url, headers=headers)
#writeToLocal(r, os.path.join('link_verification', os.path.basename(url))) # Debugging

r.raise_for_status()

# Get all links inside and parse them, download or throw out broken message
## Get all URLs
soup = bs4.BeautifulSoup(r.text, 'lxml')
subLinkObjs = soup.select('a')

## Download content for all URLs
for link in subLinkObjs:
	subUrl = link.get('href')
	if 'http' not in subUrl:
		continue
	print('Preparing to download %s' % subUrl)
	try:
		subRes = requests.get(subUrl, headers=headers)
	#except TooManyRedirects:
	except requests.exceptions.TooManyRedirects:	#Exceeded 30 redirects
		#print('Ops! Too many redirects, so ignore this URL.')
		#print('Exception is ' + str(x))
		print('URL ignored.\n')		
		continue
	except requests.exceptions.ConnectionError:
		time.sleep(3)
		print('Anti-webscripting detected, retey again!')
		subRes = requests.get(subUrl, headers=headers)

	statusCode = subRes.status_code
	print('Response status code: %s' % statusCode)
	if statusCode == 404:
		print('This link is broken!\n')
	else:
		print('Downloading %s ...' % subUrl)
		if subUrl.endswith('/'):
			finalName = subUrl.split('/')[-2]	# Handle the URLs ends with /
		else:
			finalName = os.path.basename(subUrl)
		writeToLocal(subRes, os.path.join('link_verification', finalName))
		print('Downloading %s ... done!!!\n' % subUrl)

