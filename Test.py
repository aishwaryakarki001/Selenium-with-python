from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = r"C:\Program Files (x86)\chromedriver.exe"

service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")

time.sleep(1000)
#driver.quit()
