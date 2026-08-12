import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

point_me=driver.find_element(By.CLASS_NAME, "dropbtn")

actions = ActionChains(driver)

# Hover and click
actions.move_to_element(point_me).click().perform()

copy_text = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
actions.double_click(copy_text).perform()

# Right click
actions.context_click(copy_text).perform()

# Drag and drop

src = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

# actions.drag_and_drop(src, target).perform()

# Click hold and release
actions.click_and_hold(src).move_to_element(target).release().perform()

time.sleep(5)