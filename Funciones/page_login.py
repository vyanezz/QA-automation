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



class paginaLogin():

    def __init__(self, driver):
        self.driver=driver

    def loginMaster(self,url,user,passw,t):
        driver = self.driver
        f = driverFunciones(driver)  # llamada a la clase importada pasando driver
        f.inicio(url, t)  # llamada al metodo incio pasandole los dos valores
        f.userPassXpath('//*[@id="user-name"]', user, t)  # llamada a funcion que manda los valores por xpath
        f.userPassXpath('//*[@id="password"]', passw, t)
        f.clickXpath('//*[@id="login-button"]', t)



