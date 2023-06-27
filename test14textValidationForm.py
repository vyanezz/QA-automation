from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



driver =webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()


user = 'tomsmith'
passw = 'flasetry'
passwTrue = 'SuperSecretPassword!'

inputUser = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
inputUser.send_keys(user)

inputpass = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
inputpass.send_keys(passw)
time.sleep(3)


send = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/button')))
send.click()

time.sleep(3)
alertInvalid = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="flash"]')))
alertInvalidText = alertInvalid.text


if "Your password is invalid!" in alertInvalidText:

    inputpass.send_keys(passwTrue)
    send.click()
else:
    print('cannot login')






time.sleep(4)

driver.close()