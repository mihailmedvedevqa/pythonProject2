import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
driver_user_1 = webdriver.Chrome(options=chrome_options)


LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

driver_user_1.get("https://hyperskill.org/login")
driver_user_1.find_element(*LOGIN_FIELD).send_keys("alekseik@ya.ru")
driver_user_1.find_element(*PASSWORD_FIELD).send_keys("Qwerty132!")
driver_user_1.find_element(*SUBMIT_BUTTON).click()
time.sleep(3)

driver_user_2 = webdriver.Chrome(options=chrome_options)
driver_user_2.get("https://hyperskill.org/login")
time.sleep(3)
