from selenium import webdriver

url = "http://www.google.com"

driver = webdriver.Chrome()

driver.get(url)

driver.close()