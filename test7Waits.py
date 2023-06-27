from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver =webdriver.Chrome()

driver.get("https://www.elmundo.es/")

driver.maximize_window()

#driver.implicitly_wait(10) Espera a la pagina completa


cookies = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="didomi-notice-agree-button"]'))).click()

time.sleep(5)

driver.close()