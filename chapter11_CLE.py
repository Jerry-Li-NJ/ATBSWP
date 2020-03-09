#! /usr/bin/python3
# chapter11_CLE.py - Get destination email and context from command line, then sent this email via my own account.

import sys, time
from selenium import webdriver

# My own email address and password
myOwnAddress= {'email': 'xxx@qq.com', 'passwd': 'xxx'}	# Replace value of email with your own QQ email, passwd with your password.

# Get the des-email, context
if len(sys.argv) != 3:
	print('Argument incorrect.')
	print('Please make sure 2 arguments are added.')
else:
	dest_email = sys.argv[1]
	email_context = sys.argv[2]
	#print(sys.argv)

# Login my own email box
browser = webdriver.Firefox()
browser.get('https://mail.qq.com/cgi-bin/loginpage')

qqElement = browser.find_element_by_id('qqLoginTab')	# Make sure login mathod is QQ, not WeChat.
qqElement.click()

browser.implicitly_wait(30)

browser.switch_to_frame('login_frame')

emailElement = browser.find_element_by_xpath('//*[@id="u"]')
passwdElement = browser.find_element_by_xpath('//*[@id="p"]')
submitElement = browser.find_element_by_xpath('//*[@id="login_button"]')

emailElement.clear()
emailElement.send_keys(myOwnAddress['email'])
passwdElement.send_keys(myOwnAddress['passwd'])
#passwdElement.submit()		# Submit not work, click() work, weird.
submitElement.click()

# Input des-email and context
browser.switch_to_default_content()
browser.implicitly_wait(30)
sentElement = browser.find_element_by_xpath('//*[@id="composebtn"]')	# Find the element of writing email.
sentElement.click()

browser.implicitly_wait(30)

browser.switch_to_frame('mainFrame')
desEmailElement = browser.find_element_by_xpath('/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input')

#desEmailElement.click()
desEmailElement.send_keys(dest_email)

summaryElement = browser.find_element_by_xpath('//*[@id="subject"]')	# Fill out summary.
summaryElement.send_keys('summary')

#browser.implicitly_wait(30)	# Do not make sense at all, it only check the whole page, not part of the page.
time.sleep(20)

bodyIframe = browser.find_element_by_class_name('qmEditorIfrmEditArea')
#print(str(bodyIframe))
#print('Type of return:' + str(type(bodyIframe)))
browser.switch_to_frame(bodyIframe)	# Switch to iframe of body.

contextElement = browser.find_element_by_xpath('/html/body')	# Fill out body.
#contextElement.click()
contextElement.send_keys(email_context)

# Send out this email
browser.switch_to_default_content()	# Before switch to another frame, it's necessary to switch to default frame first.
browser.switch_to_frame('mainFrame')
sendElement = browser.find_element_by_xpath('/html/body/form[2]/div[1]/div/a[1]')	# Click submit button.
sendElement.click()

