# Fetch the top right corner from the store number value
from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://www.homedepot.com")
title = driver.title
# Check whether launched website has title 'The Home Depot' and Maximize window
if title == 'The Home Depot':
    driver.maximize_window()
print(driver.find_element_by_css_selector("div[class='MyStore__store']").text)
driver.close()









# element = driver.find_element_by_class_name('myStore')
# if element == 'myStore':
# element.get_attribute("value")
# element1 = driver.find_element_by_id('email')
# element1.send_keys("9843140361")
# element1 = driver.find_element_by_id('pass')
# element1.send_keys('gokesamu12@')
# element = driver.find_element_by_id("u_0_b").click()
# print(element1)
# print(title)
# print(driver.current_url)