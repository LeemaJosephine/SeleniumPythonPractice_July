import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)  # wait for 5 seconds

# Locate the dropdown
country = Select(driver.find_element(By.ID,"country"))

# Select by Visible text
#country.select_by_visible_text("        Canada      ")

# Select by value
country.select_by_value("france")

time.sleep(2)

# Select by index
country.select_by_index(6)
time.sleep(5)



