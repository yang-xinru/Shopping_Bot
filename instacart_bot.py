from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os  

import schedule
import time

def slot_check():
	try:
		browser=webdriver.Chrome('/Users/blablabla/chromedriver') #Path to the chrome driver
		browser.get('https://www.instacart.com/')
		time.sleep(2)
		login_button=browser.find_element_by_link_text('Log in')
		login_button.click()
		time.sleep(5)
		login=browser.find_element_by_id('nextgen-authenticate.all.log_in_email')
		login.send_keys('xxxx@gmail.com') #your account email here
		time.sleep(2)
		password=browser.find_element_by_id('nextgen-authenticate.all.log_in_password')
		password.send_keys('blablabla') #your password here
		time.sleep(5)
		password=browser.find_element_by_id('nextgen-authenticate.all.log_in_password')
		password.send_keys(Keys.RETURN)
		time.sleep(5)
		checkout_url='https://www.instacart.com/store/checkout_v3'
		browser.get(checkout_url)
		time.sleep(15)
		try:
			slot_check = browser.find_element_by_xpath("//*[@id='react-views-container']/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/h1")
			slot_text=slot_check.text
			if slot_text!="No delivery times available":
				res='Slot Found!!!'
			else:
				res='No Slot....'
		except NoSuchElementException as e:
			res='Slot Found!!!'
	except NoSuchElementException as e:
		res=str(e)
	if res=='Slot Found!!!':
		os.environ['res']='Instacart (H-Mart) '+str(res)
		os.system("echo $res|mail -s '{}' blabla@gmail.com".format(res)) #specify who to receive the notification email in here


schedule.every(3).minutes.do(slot_check)


while True:
    schedule.run_pending()

