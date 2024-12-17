from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)  #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/
print(driver.page_source)#give page source code

# driver.quit()