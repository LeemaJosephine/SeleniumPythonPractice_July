import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.implicitly_wait(5)

# Using id or name
#driver.switch_to.frame("singleframe")

# using index
#driver.switch_to.frame(0)

# using webelement
element = driver.find_element(By.XPATH, "//iframe[@name='SingleFrame']")
driver.switch_to.frame(element)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Testuser")
time.sleep(5)

#Switch back to default content
driver.switch_to.default_content()

# Nested Frames

driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()

# switch to parent frame
parent_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(parent_frame)
parent_text = driver.find_element(By.TAG_NAME, "h5").text
print(parent_text)

# switch to child frame
child_frame = driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(child_frame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Testuser")

# switch back to parent frame
driver.switch_to.parent_frame()
parent_text = driver.find_element(By.TAG_NAME, "h5").text
print(parent_text)

# switch to default content
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//a[text()='Single Iframe ']").click()
time.sleep(5)

