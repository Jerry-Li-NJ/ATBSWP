#! /usr/bin/python3
# chapter11_CLE.py - Get destination email and context from command line, then sent this email via my own account.

import sys, time
from selenium import webdriver

# My own email address and password
myOwnAddress= {'email': 'xxx@qq.com', 'passwd': 'xxx'}	# Replace value of email with your own QQ email, passwd with your password.

def getDesEamilAndContext():	# Get command line arguments
	if len(sys.argv) != 3:
		print('Argument incorrect.')
		print('Please make sure 2 arguments are added.')
	else:
		dest_email = sys.argv[1]
		email_context = sys.argv[2]
	return [dest_email, email_context]

def loginMyOwnEmailBox(email, password):	# Login email box and rerurn browser/driver
	browser = webdriver.Firefox()
	browser.get('https://mail.qq.com/cgi-bin/loginpage')

	qqElement = browser.find_element_by_id('qqLoginTab')	# Make sure login mathod is QQ, not WeChat.
	qqElement.click()

	browser.implicitly_wait(30)

	browser.switch_to_frame('login_frame')	# Frame of login email box

	emailElement = browser.find_element_by_xpath('//*[@id="u"]')
	passwdElement = browser.find_element_by_xpath('//*[@id="p"]')
	submitElement = browser.find_element_by_xpath('//*[@id="login_button"]')

	emailElement.clear()
	emailElement.send_keys(email)
	passwdElement.send_keys(password)
	submitElement.click()
	
	return browser

def inputDesAndCon(browser, demail, context):	# Input everything of an email
	browser.switch_to_default_content()	# Default frame that contain the element of writing email
	browser.implicitly_wait(30)
	sentElement = browser.find_element_by_xpath('//*[@id="composebtn"]')	# Find the element of writing email.
	sentElement.click()

	browser.implicitly_wait(30)

	browser.switch_to_frame('mainFrame')	# Main frame of the email that contains destination email and summary
	desEmailElement = browser.find_element_by_xpath('/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input')

	desEmailElement.send_keys(demail)

	summaryElement = browser.find_element_by_xpath('//*[@id="subject"]')	# Fill out summary.
	summaryElement.send_keys('summary')

	time.sleep(20)	# Wait the loading of body of email

	bodyIframe = browser.find_element_by_class_name('qmEditorIfrmEditArea')
	browser.switch_to_frame(bodyIframe)	# Switch to iframe of body.

	contextElement = browser.find_element_by_xpath('/html/body')	# Fill out body.
	contextElement.send_keys(context)

def sendOutEmail(browser):	# Click sent out button
	browser.switch_to_default_content()	# Before switch to another frame, it's necessary to switch to default frame first.
	browser.switch_to_frame('mainFrame')
	sendElement = browser.find_element_by_xpath('/html/body/form[2]/div[1]/div/a[1]')	# Click submit button.
	sendElement.click()
	time.sleep(20)
	browser.quit()

# Get the des-email, context
listOfDE = getDesEamilAndContext()

# Login my own email box
xBrowser = loginMyOwnEmailBox(myOwnAddress['email'], myOwnAddress['passwd'])

# Input des-email and context
inputDesAndCon(xBrowser, listOfDE[0], listOfDE[1])

# Send out this email
sendOutEmail(xBrowser)


