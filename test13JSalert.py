from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



driver =webdriver.Chrome()

driver.get('http://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

alertbutton= WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/ul/li[1]/button'))).click()
time.sleep(3)

try:

    alert = driver.switch_to.alert
    time.sleep(3)
    alert.accept()

except TimeoutException as ex:
    print(ex.msg)

time.sleep(3)

driver.close()