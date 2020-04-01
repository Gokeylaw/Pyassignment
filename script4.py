# Table Validation - Retrieve all values from any one column in a table and print it in a console.
from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
element = driver.find_element_by_xpath("//*[@id='product']/tbody/tr[2]/td[1]")
print("Instrctor=", element.text)
element = driver.find_element_by_xpath("//*[@id='product']/tbody/tr[2]/td[2]")
print("course=", element.text)
element = driver.find_element_by_xpath("//*[@id='product']/tbody/tr[2]/td[3]")
print("Price=", element.text)
driver.close()