from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome
driver = webdriver.Chrome(executable_path='E:\Drivers\chromedriver.exe')

driver.get('http://demo.automationtesting.in/Windows.html')  # opens the url of the page

# get the title of the page
print(driver.title)  # return the title of the page
print(driver.current_url) #return the current url
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button ").click()

time.sleep(5)

driver.close() #Currently focused browser
driver.quit() #Close all the browser
