import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"(//button[contains(text(),'click')])[1]").click()

# Get the current window handle
driver_address = driver.current_window_handle
print("Parent window: " ,driver_address)

# To get all the windows of the browser
handles = driver.window_handles
print("Window handles: " ,handles)

# Switch to another window

driver.switch_to.window(handles[1])

driver_address = driver.current_window_handle
print("Current window: " ,driver_address)

title = driver.title
print("Title: " ,title)

driver.quit()


###################################################################################

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(5)
# Alternative practice

parent_window = driver.current_window_handle

driver.find_element(By.XPATH,"(//button[contains(text(),'click')])[1]").click()

for handle in driver.window_handles:
    if handle != parent_window:
        driver.switch_to.window(handle)
        break

print(driver.title)

driver.switch_to.window(parent_window)
print(driver.title)