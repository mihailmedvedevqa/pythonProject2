import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Browser options
chrome_options = webdriver.ChromeOptions()
# Driver initialization
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)
UPLOAD_FILE = driver.find_element("xpath", "//input[@type='file']")
UPLOAD_FILE.send_keys(f"{os.getcwd()}\\downloads\\test-upload.txt")
time.sleep(3)