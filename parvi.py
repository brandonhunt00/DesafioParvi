from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://rpachallenge.com/")

time.sleep(5)

start_button = driver.find_element(By.XPATH, "//button[contains(text(),'Start')]")
start_button.click()

time.sleep(3)

inputs = driver.find_elements(By.CLASS_NAME, "tableCell")
for i, input_field in enumerate(inputs):
    input_field.send_keys(str(i + 1))

submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
submit_button.click()

time.sleep(3)

driver.quit()
