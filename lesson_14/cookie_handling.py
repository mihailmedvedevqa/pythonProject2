import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get("https://www.freeconferencecall.com/login")
# print(driver.get_cookie("country_code"))
# print(driver.get_cookies())
# driver.add_cookie({
#     "name": "test_name",
#     "value": "test_value"
# })
# print(driver.get_cookie("test_name"))

# cookie_before = driver.get_cookie("split")
# print(cookie_before)
# driver.delete_cookie("split")
# driver.add_cookie({
#      "name": "split",
#      "value": "test_split"
# })
# cookie_after = driver.get_cookie("split")
# print(cookie_after)

# cookies_before = driver.get_cookies()
# print(cookies_before)
# driver.delete_all_cookies()
# driver.add_cookie({
#      "name": "test_name",
#      "value": "test_value"
# })
# cookies_after = driver.get_cookies()
# print(cookies_after)

# LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

# driver.get("https://www.freeconferencecall.com/login")
# driver.find_element(*LOGIN_FIELD).send_keys("login")
# driver.find_element(*PASSWORD_FIELD).send_keys("password")
# driver.find_element(*SUBMIT_BUTTON).click()
# pickle.dump(driver.get_cookies(), open(os.getcwd() + "\\cookies\\cookies.pkl", "wb"))

driver.get("https://www.freeconferencecall.com/login")
driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd() + "\\cookies\\cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.get("https://www.freeconferencecall.com/profile")
