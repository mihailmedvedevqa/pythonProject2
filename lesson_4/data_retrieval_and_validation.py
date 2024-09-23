import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

PAGE_URL = driver.current_url
print(f"Page URL: {PAGE_URL}")
assert PAGE_URL == "https://www.wikipedia.org/", "URL error, wrong page opened"

PAGE_TITLE = driver.title
print(f"Page Title: {PAGE_TITLE}")
assert PAGE_TITLE == "Wikipedia", "Incorrect page title"

PAGE_SOURCE = driver.page_source
print(PAGE_SOURCE)

time.sleep(3)
