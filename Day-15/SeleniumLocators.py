import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()
driver.implicitly_wait(5)  # it will wait for 5 seconds for the element to load

# Class name locator  and text
ele = driver.find_element(By.CLASS_NAME, "text-center")
print(ele.is_displayed())
print(ele.text)

# ID Locator
driver.find_element(By.ID, "email-id").send_keys("testuser@gmail.com")

#Name locator and sendkeys
driver.find_element(By.NAME, "password-name").send_keys("admin123")

# click command
remember = driver.find_element(By.ID,"remember")
remember.click()
print(remember.is_selected())

# Submit command
submit = driver.find_element(By.NAME,"submit-name")
print(submit.is_enabled())
submit.submit()

time.sleep(5)
