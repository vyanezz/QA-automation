from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By


driver =webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

driver.maximize_window()


nom = driver.find_element(By.XPATH, '//*[@id="userName" and @type="text"]') #Xpath booleano and
nom.send_keys("Víctor")

nom.send_keys(Keys.TAB + "mailvictor@gmail.com" + Keys.TAB + "Madrid" + Keys.TAB + "Madrid 2" + Keys.TAB + Keys.ENTER)



driver.execute_script("window.scrollTo(0,500)")

time.sleep(2)





driver.close()