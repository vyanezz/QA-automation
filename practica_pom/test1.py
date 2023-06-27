import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.pyfunciones import driverFunciones


class baseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # ruta de localizacion del driver chrome

    def test1_xpath(self):
        driver = self.driver
        f = driverFunciones(driver)  # llamada a la clase importada pasando driver
        f.inicio("https://www.saucedemo.com/", 6)  # llamada al metodo incio pasandole los dos valores
        f.userPassXpath('//*[@id="user-name"]', "standard_user", 6)#llamada a funcion que manda los valores por xpath
        f.userPassXpath('//*[@id="password"]', "secret_sauce", 2)

    def test2_id(self):
        driver = self.driver
        f = driverFunciones(driver)  # llamada a la clase importada pasando driver
        f.inicio("https://www.saucedemo.com/", 6)  # llamada al metodo incio pasandole los dos valores
        f.idText('user-name', "standard_user", 6)#llamada a funcion que manda los valores por id
        f.idText('password', "secret_sauce", 2)

    def test3_error(self):
        driver = self.driver
        f = driverFunciones(driver)  # llamada a la clase importada pasando driver
        f.inicio("https://www.saucedemo.com/", 6)  # llamada al metodo incio pasandole los dos valores
        f.validateXpath('//*[@id="user-nameERROR"]', "standard_user", 6)#llamada a funcion forzando error
        f.validateXpath('//*[@id="password"]', "secret_sauce", 2)

    def test4_login(self):
        driver = self.driver
        f = driverFunciones(driver)  # llamada a la clase importada pasando driver
        f.inicio("https://www.saucedemo.com/", 6)  # llamada al metodo incio pasandole los dos valores
        f.userPassXpath('//*[@id="user-name"]', "standard_user", 6)#llamada a funcion que manda los valores por xpath
        f.userPassXpath('//*[@id="password"]', "secret_sauce", 2)
        f.clickXpath('//*[@id="login-button"]',6)




    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
