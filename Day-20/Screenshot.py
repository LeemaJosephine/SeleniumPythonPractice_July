import datetime
import os.path
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/p/download-files_25.html")
driver.maximize_window()
driver.implicitly_wait(5)

# Capturing Screenshot
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
driver.save_screenshot(f"screenshot/image_{timestamp}.png")

element = driver.find_element(By.XPATH,"//h1[@class='title']")
element.screenshot(f"screenshot/logo_{timestamp}.png")