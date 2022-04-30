from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver.exe")


driver.get("http://newtours.demoaut.com/")  #opening URL takes some time

driver.implicitly_wait(10)  #seconds

assert "Welcome: Mercury Tours" in driver.title

# wait some time her
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()