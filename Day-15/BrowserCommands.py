import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com") # Navigational command

# driver.maximize_window()
# driver.minimize_window()
driver.fullscreen_window()

title = driver.title
print("The title of the web page is: ", title)

url = driver.current_url
print("The url of the web page is: ", url)

source = driver.page_source
print("The source of the web page is: ", source)

time.sleep(10)

driver.close()
