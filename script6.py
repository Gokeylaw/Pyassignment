# Validate if login is successful by checking if we have landed in the home page.
from datetime import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
# Landed_page_title = driver.title
# current_page_title = driver.current_url.title
# print(driver.current_url)
# Check whether launched website is in homepage
# if Landed_page_title == current_page_title:
#     driver.maximize_window()
#     print("You have landed at homepage")
# Facebook – log in or sign up
# driver.close()
driver.get("https://www.linkedin.com/login")
# print(driver.title)
driver.find_element_by_xpath("//*[@id='username']").send_keys("gokeylaw125@gmail.com")
driver.find_element_by_xpath("//*[@id='password']").send_keys("gokesamu12")
driver.find_element_by_css_selector("button[type='submit']").click()
# time.sleep(1)
# print(driver.title)
assert driver.title in 'LinkedIn'
print("Landed in homepage ")