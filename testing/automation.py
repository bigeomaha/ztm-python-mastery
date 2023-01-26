from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='chromedriver')
chrome_browser = webdriver.Chrome(service=service)
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')


user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('Testing my knowledge of selenium. How cool!')
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()
time.sleep(2)
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'Testing my knowledge of selenium. How cool!' in output_message.text

## Handle buggy Close functionality
try:
    chrome_browser.close()
    chrome_browser.close()
except:
    exit()
