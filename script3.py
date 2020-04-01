# Enter the 'Recall Number' text box in any text.
from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://www.homedepot.com")
element = driver.find_element_by_css_selector("input[class='SearchBox__input']").send_keys("bolt")
button = driver.find_element_by_css_selector("button[id='headerSearchButton']").click()
driver.close()