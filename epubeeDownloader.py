#! /usr/bin/python3

# epubeeDownloader.py -- Used to download ebooks for free from 1:30 to 6:30

import time, sys
from selenium import webdriver

#Wait until around 3:00.

time.sleep(32400)	# Now is almost 18:00, wait another 9 hours, it should be 3:00

# Sign in

browser = webdriver.Firefox()
browser.get('http://cn.epubee.com/files.aspx')

emailElem = browser.find_element_by_xpath('//*[@id="retrieve_id"]')
emailElem.send_keys('rpm23@yopmail.com')

signInElem = browser.find_element_by_xpath('//*[@id="retrieve_btn"]')
signInElem.click()

time.sleep(30)

# Download
#//*[@id="gvBooks_gvBooks_child_0_hpdownload_0"]
bookElem = browser.find_element_by_xpath('//*[@id="gvBooks_gvBooks_child_0_hpdownload_0"]')
bookElem.click()

time.sleep(30)
bookElem = browser.find_element_by_xpath('//*[@id="gvBooks_gvBooks_child_1_hpdownload_0"]')
bookElem.click()

time.sleep(30)
bookElem = browser.find_element_by_xpath('//*[@id="gvBooks_gvBooks_child_2_hpdownload_0"]')
bookElem.click()
 
#browser.quit()
