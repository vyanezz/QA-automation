import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class baseTest(unittest.TestCase):

    def setUp(self):
      self.driver=webdriver.Chrome()

    def test1(self):
        driver = self.driver
        driver.get('')
        driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()