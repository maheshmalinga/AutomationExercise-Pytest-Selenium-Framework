from selenium.webdriver import Chrome
from time import sleep
driver = Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://automationexercise.com/")
try:
    element = driver.find_element("xpath",'//a[@href="/category_products/1"]')
    print(element.is_displayed())
finally:
    driver.find_element("xpath","//*[@href='#Women']").click()
    element = driver.find_element("xpath", '//a[@href="/category_products/1"]')
    print(element.is_displayed())


sleep(3)
driver.quit()