from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome('../chromedriver.exe')

driver.get("https://web.whatsapp.com")

"""

st = "hello"
driver.find_element(By.XPATH, '//div[@aria-label="Write a comment..."]').send_keys(st)
driver.find_element(By.XPATH, '//div[@aria-label="Write a comment..."]').send_keys(Keys.RETURN) 
    
"""
