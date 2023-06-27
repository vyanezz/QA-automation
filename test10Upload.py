from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



driver =webdriver.Chrome()

driver.get("https://testpages.herokuapp.com/file_upload_j.html")

driver.maximize_window()

try:
    fileinput = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fileinput"]')))
    fileinput.send_keys('//Users//laurayanez//PycharmProjects//cursoQA//images//image1.png')
    type = driver.find_element(By.XPATH, '/html/body/form/div/input[1]').click()
    time.sleep(2)
    upload = driver.find_element(By.XPATH, '/html/body/form/input[2]') .click()

    time.sleep(5)

except TimeoutException as ex:
    print(ex.msg)

    #http://the-internet.herokuapp.com/?ref=hackernoon.com



time.sleep(5)

driver.close()