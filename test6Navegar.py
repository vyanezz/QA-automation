from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By


driver =webdriver.Chrome()

t = 3

driver.get("https://demoqa.com/text-box")

time.sleep(t)

driver.get("https://www.selenium.dev/")

time.sleep(t)

driver.get("https://www.selenium.dev/selenium-ide/")

time.sleep(t)

driver.execute_script("window.history.go(-1)")

time.sleep(t)

driver.execute_script("window.history.go(-1)")

time.sleep(t)

driver.execute_script("window.history.go(-2)")

time.sleep(2)

driver.close()