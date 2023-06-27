from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By


driver =webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

driver.maximize_window()


nom = driver.find_element(By.XPATH, '//*[@id="userName" and @type="text"]') #Xpath booleano and
nom.send_keys("Víctor")






driver.find_element(By.XPATH, '//*[@id="userEmail"]').send_keys("mailvictor@gmail.com")

driver.find_element(By.XPATH, '//*[@id="currentAddress"]').send_keys("Madrird")

driver.find_element(By.XPATH, '//*[@id="permanentAddress"]').send_keys("Madrird 2")

driver.execute_script("window.scrollTo(0,500)")

time.sleep(1)



driver.find_element(By.XPATH, '//*[@id="submit"]').click()



time.sleep(2)


driver.close()