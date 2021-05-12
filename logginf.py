from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time




def logar_click(logar, pas):
    campo_log = driver.find_element_by_xpath('//input[contains(@id, "index_email")]')
    time.sleep(1)
    campo_log.click()
    campo_log.send_keys(logar)
    time.sleep(2)
    campo_password = driver.find_element_by_xpath('//input[contains(@id, "index_pass")]')
    time.sleep(1)
    campo_password.click()
    campo_password.send_keys(pas)
    time.sleep(1)
    campo_password.send_keys(Keys.ENTER)




driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://vk.com/')
# Insert your Phone or Email
log = ['Your log'] 
# Insert your password
password = ['Your password']  
logar_click(log, password)