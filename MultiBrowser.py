from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="E:\Drivers\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

print(driver.title)
driver.close()
