from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver.exe")

driver.maximize_window()

driver.get('https://www.expedia.com/')
driver.implicitly_wait(5)

driver.find_elements_by_class_name("uitk-tab-text")
driver.find_element(By.ID,"uitk-tab-text").click() #Flights button

time.sleep(2)  #from python
driver.find_element(By.ID,"location-field-leg1-origin-dialog-trigger").send_keys("NYC") #  origin

driver.find_element(By.ID,"location-field-leg1-origin-dialog-trigger").send_keys("SFO") #  destination
driver.find_element(BY.ID,"flight-departing-hp-flight").clear()
driver.find_element(BY.ID,"flight-departing-hp-flight").send_keys("12/10/2022")
driver.find_element(BY.ID,"flight-departing-hp-flight").clear()
driver.find_element(BY.ID,"flight-returning-hp-flight").send_keys('15/10/2022')
#  driver.find_element(BY.XPATH,"//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button").click()

#Explicit waits
wait = WebDriverWait(driver,10)

element=wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//*[@id="app-layer-base"]/div/main/div/div/div/section/div/div[2]")))

element.click()

time.sleep(3)

driver.quit()





