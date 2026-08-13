import os.path
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/p/download-files_25.html")
driver.maximize_window()
driver.implicitly_wait(5)

# Uploading

# Get abosulte file path
file_path = os.path.abspath("sample.txt")


upload = driver.find_element(By.ID,"singleFileInput")
upload.send_keys(file_path)

driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()

# Download file

driver.find_element(By.ID,"inputText").send_keys("This is a sample file")
driver.find_element(By.ID,"generateTxt").click()
driver.find_element(By.ID, "txtDownloadLink").click()

file_path = r"C:\Users\leema\Downloads\info.txt"
assert os.path.exists(file_path)

time.sleep(10)