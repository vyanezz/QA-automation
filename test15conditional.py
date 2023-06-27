from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



driver =webdriver.Chrome()

driver.get('https://demoqa.com/')
driver.maximize_window()

title = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/header/a/img')))

sectionbtn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]')))


if (title.is_displayed()==True):
    sectionbtn.click()
    time.sleep(5)
else:
    print('not existing the web title..')

time.sleep(3)

driver.close()