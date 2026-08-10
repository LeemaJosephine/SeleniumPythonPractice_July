import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
driver.maximize_window()
driver.implicitly_wait(5)  # wait for 5 seconds

driver.find_element(By.ID, "btn1").click()
driver.find_element(By.ID, "txt1").send_keys("Test") # this will be handles by implicit wait

driver.find_element(By.ID, "btn2").click()

# Explicit wait

wait = WebDriverWait(driver, 10)
# textbox = wait.until(EC.visibility_of_element_located((By.ID, "txt2")))
# textbox.send_keys("User")

time.sleep(5)

# Fluent Wait
wait = WebDriverWait(
    driver,
10,
    poll_frequency=2,
    ignored_exceptions=[
        NoSuchElementException,
    ]
)
textbox = wait.until(EC.visibility_of_element_located((By.ID, "txt2")))
textbox.send_keys("User")