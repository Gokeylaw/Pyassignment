import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
#pause the test for few seconds using Time
driver.implicitly_wait(5)
# wait until 5 seconds if object is not displayed
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div[1]/div[2]/a[2]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div[2]/div[2]/a[2]").click()
time.sleep(1)
count =len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
driver.back()
time.sleep(1)
driver.close()