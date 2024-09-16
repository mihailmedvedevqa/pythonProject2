import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/")
LOGIN_BUTTON = driver.find_element("xpath", "//a[@id='login-desktop']")
LOGIN_BUTTON.click()

EMAIL_FIELD = driver.find_element("xpath", "//input[@id='login_email']")
EMAIL_FIELD.clear()
assert EMAIL_FIELD.get_attribute("value") == ""
EMAIL_FIELD.send_keys("text@mail.com")
EMAIL_FIELD_VALUE = EMAIL_FIELD.get_attribute("value")
assert "text@mail.com" in EMAIL_FIELD_VALUE
print(EMAIL_FIELD.get_attribute("value"))

PASSWORD_FIELD = driver.find_element("xpath", "//input[@id='password']")
PASSWORD_FIELD.clear()
assert PASSWORD_FIELD.get_attribute("value") == ""
PASSWORD_FIELD.send_keys("0123456789")
PASSWORD_FIELD_VALUE = PASSWORD_FIELD.get_attribute("value")
assert "0123456789" in PASSWORD_FIELD_VALUE
print(PASSWORD_FIELD.get_attribute("value"))
