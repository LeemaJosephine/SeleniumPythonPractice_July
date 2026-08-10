import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(5)

# CSS - Using ID - #
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").send_keys("Mobile")

time.sleep(5)

# Class name - .
driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute").send_keys("Laptop")

time.sleep(5)

# Attribute value
driver.find_element(By.CSS_SELECTOR, "input[name='field-keywords']").send_keys("Appliances")
time.sleep(5)