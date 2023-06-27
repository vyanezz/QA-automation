from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



driver =webdriver.Chrome()

driver.get('http://the-internet.herokuapp.com/?ref=hackernoon.com')

driver.maximize_window()

time.sleep(4)

links = driver.find_elements(By.TAG_NAME,"a")

print('el numero de links son: ', len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT('A/B Testing')).click()

time.sleep(4)

driver.close()