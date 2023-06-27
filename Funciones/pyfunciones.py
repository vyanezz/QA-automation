import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



class driverFunciones():
    def __init__(self, driver):
        self.driver=driver

    def inicio(self,url,t):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Se ha abierto la URL-> {} ".format(url))
        time.sleep(t)
        return t

    def userPassXpath(self, xpath, texto, t):
        wait = WebDriverWait(self.driver, t)
        val = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        val.clear()
        val.send_keys(texto)
        print("Escribiendo en el campo-> {} el texto-> {} ".format(xpath,texto))
        time.sleep(t)
        return wait

    def idText(self, id,texto,t):
        wait = WebDriverWait(self.driver, t)
        val = wait.until(EC.visibility_of_element_located((By.ID, id)))
        val.clear()
        val.send_keys(texto)
        print("Escribiendo en el campo-> {} el texto-> {} ".format(id,texto))

        time.sleep(t)
        return wait

    def validateXpath(self, xpath, texto,t):
        wait = WebDriverWait(self.driver, t)
        try:
            val = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo-> {} el texto-> {} ".format(xpath, texto))
            time.sleep(t)
            return t
        except TimeoutException as ex:
            print("No se encontra el elemento -> ", xpath, ex.msg)

    def clickXpath(self, xpath,t):
        wait = WebDriverWait(self.driver, t)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
            print("Se da click sobre -> {} ".format(xpath))
            time.sleep(t)
            return t
        except TimeoutException as ex:
            print("No se encontra el elemento -> ", xpath, ex.msg)