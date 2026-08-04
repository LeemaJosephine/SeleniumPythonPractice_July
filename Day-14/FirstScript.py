import time

from selenium import webdriver

# Step 1: Launching the browser
# Chrome
#driver = webdriver.Chrome()
# Edge
driver = webdriver.Edge()
# Step 2: Loading the url
driver.get("https://www.amazon.in/")
# Step 3: Maximize the window
driver.maximize_window()

time.sleep(10)  # This will pause the execution