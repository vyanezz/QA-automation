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
from Funciones.page_login import paginaLogin


class baseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # ruta de localizacion del driver chrome

    def test_login(self):
        driver = self.driver
        f = paginaLogin(driver)  # llamada a la clase importada pasando driver
        f.loginMaster("https://www.saucedemo.com/","standard_user","secret_sauce",4) #llamada al metodo que llama a su vez a otros metodos de otra clase

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
