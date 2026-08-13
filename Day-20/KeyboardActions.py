import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# # # Type and select the value
name = driver.find_element(By.ID,"name")
name.send_keys("Testuser")

# Select the text - CTRL + A
ActionChains(driver) \
    .click(name) \
    .key_down(Keys.CONTROL) \
    .send_keys("a") \
    .key_up(Keys.CONTROL) \
    .perform()

# Copy

ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .send_keys("c") \
    .key_up(Keys.CONTROL) \
    .perform()

# Paste
email= driver.find_element(By.ID,"email")

ActionChains(driver) \
    .click(email) \
    .key_down(Keys.CONTROL) \
    .send_keys("v") \
    .key_up(Keys.CONTROL) \
    .perform()

# name.send_keys(Keys.CONTROL, "a")
# name.send_keys(Keys.CONTROL,"c")
#
# # # Paste
# email= driver.find_element(By.ID,"email")
# email.send_keys(Keys.CONTROL, "v")



time.sleep(5)
