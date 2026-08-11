import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID,"alertBtn").click()

# Switch to alert
# Simple alert
alert = driver.switch_to.alert
#To get the text of the alert
text = alert.text
print(text)
#To click ok
alert.accept()

#Confirmation Alert
driver.find_element(By.ID,"confirmBtn").click()
alert = driver.switch_to.alert
# No/Cancel
alert.dismiss()

#Prompt alert
driver.find_element(By.ID,"promptBtn").click()
#TYpe and ok
alert = driver.switch_to.alert
# To type
alert.send_keys("Test User")
alert.accept()

time.sleep(10)

