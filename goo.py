from lib2to3.pgen2 import driver
from selenium import webdriver 

path = 'driver/chromedriver.exe'
browser = webdriver.Chrome(path)
browser.implicitly_wait(10)
browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")
browser.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.close()
browser.quit()