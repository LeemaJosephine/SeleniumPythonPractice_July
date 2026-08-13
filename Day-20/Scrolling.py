import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

element = driver.find_element(By.XPATH,"//a[text()='Download Files']")

driver.execute_script("arguments[0].scrollIntoView(true);",element)
element.click()

time.sleep(5)