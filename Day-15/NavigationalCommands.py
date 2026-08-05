import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/") # Navigational command

driver.back()

time.sleep(5)

driver.forward()

time.sleep(5)

driver.refresh()

time.sleep(5)