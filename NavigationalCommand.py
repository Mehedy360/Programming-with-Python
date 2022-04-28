from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver.exe")

driver.get("https://gtmetrix.com/") #open the link of gtmetrix website

print(driver.title) #FR

driver.get("https://www.webpagetest.org/") #Open the link of the webpagetest website

time.sleep(5)
print(driver.title) #print the title of https://www.webpagetest.org/ website

driver.back()

time.sleep(5)
print(driver.title) # print the title of https://www.webpagetest.org/ website

driver.forward()  #Come backs to the gtmetrix

time.sleep(5)
print(driver.title) #print the title of gt metrix


