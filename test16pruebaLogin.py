import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class login(unittest.TestCase):

    def setUp(self):
      self.driver=webdriver.Chrome()

    def test_login1(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        user=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys('victor')
        passw=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('123')
        logbtn=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        error=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))).text
        if(error=="Epic sadface: Username and password do not match any user in this service"):
            print("Prueba1, los datos no son correctos")
        time.sleep(2)

    def test_login2(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        user=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        passw=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('123')
        logbtn=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        error=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))).text
        if(error=="Epic sadface: Username is required"):
            print("Prueba2, falta user")
        time.sleep(2)

    def test_login3(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys('vvv')
        passw = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        logbtn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))).text
        if (error == "Epic sadface: Password is required"):
            print("Prueba3, falta passw")
        time.sleep(2)
    def test_login4(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        passw = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        logbtn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))).text
        if (error == "Epic sadface: Username is required"):
            print("Prueba4, faltan los 2 campos")
        time.sleep(2)

    def test_login5(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys('standard_user')
        passw = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('secret_sauce')
        logbtn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div')))
        if enter.is_displayed():
            print("Prueba5, login --> " + enter.text + str(enter))
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()