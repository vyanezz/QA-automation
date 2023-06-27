from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



driver =webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/dropdown")

driver.maximize_window()


options = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dropdown"]')))
selectOpt=Select(options)

selectOpt.select_by_index(1)

time.sleep(5)

selectOpt.select_by_visible_text('Option 2')

time.sleep(5)

driver.close()