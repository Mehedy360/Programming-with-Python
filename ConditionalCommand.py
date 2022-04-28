from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver.exe")

driver.get('http://newtours.demoaut.com/')

user_ele = driver.find_element_by_name("userName")

print(user_ele.is_displayed())  #returns true if it is available if not returns false

print(user_ele.is_enabled())  #returns true/false

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name("login").click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")

print("status of round trip radio button ", roundtrip_radio.is_selected())  #print status of radio button

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")

print("status of oneway radio button", onetrip_radio.is_selected())



