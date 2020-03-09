#! /usr/bin/python3

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
	#elem = browser.find_element_by_class_name('card-img-top cover-thumb')
	elem = browser.find_element_by_css_selector("[class='card-img-top cover-thumb']")
	print('Found <%s> element with that class name!' % (elem.tag_name))
except:
	print('Was not able to find an element with that name.')
