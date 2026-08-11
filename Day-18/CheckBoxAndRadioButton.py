import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# Radio Button
# male = driver.find_element(By.ID,"male")
# male.click()
#
# if male.is_selected():
#     print("Male selected")

radio_options = driver.find_elements(By.NAME,"gender")
gender = "Female"

for option in radio_options:
    if option.get_attribute("id") == gender:
        option.click()

    if option.is_selected():
        print(gender , " selected")

# CheckBox
day = driver.find_element(By.ID,"tuesday")
day.click()

if day.is_selected():
    print("Tuesday selected")