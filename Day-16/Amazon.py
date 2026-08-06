import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(5)

# Link Text
driver.find_element(By.LINK_TEXT, "Prime Video").click()

driver.back()
# Partial Link Text
driver.find_element(By.PARTIAL_LINK_TEXT, "Today's").click()

# Attribute based XPATH
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Mobile phones")

driver.back()

#Text based xpath
text = driver.find_element(By.XPATH, "//span[text()='Min. 50% off | Unique home finds  | Amazon Brands & more']").text
print(text)

# Contains
text = driver.find_element(By.XPATH, "//span[contains(text(),'Min. 50% off | Unique home finds')]").text
print(text)

# Collection based xpath
driver.find_element(By.XPATH, "(//input[contains(@class,'nav-input nav-progressive')])[1]").send_keys("Tabs")


time.sleep(10)
