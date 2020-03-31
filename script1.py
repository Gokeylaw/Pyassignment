# Launch a chrome browser, Maximize it and validate the page title.
from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://www.homedepot.com")
driver.maximize_window()
title = driver.title
print(driver.current_url)
# validate the page title
assert title in "The Home Depot"
print(title)
driver.close()