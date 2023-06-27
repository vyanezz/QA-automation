from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



driver =webdriver.Chrome()

driver.get("https://pixabay.com/es/")

driver.maximize_window()

try:
    searchbutton = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div[3]/div[2]/a/span')))
    go = driver.execute_script("arguments[0].scrollIntoView();", searchbutton)

    time.sleep(5)

except TimeoutException as ex:
    print(ex.msg)






time.sleep(5)

driver.close()