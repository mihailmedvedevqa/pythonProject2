import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver.get("https://hyperskill.org/courses")
# time.sleep(3)
# driver.find_elements("class name", "nav-link")[3].click()
# time.sleep(3)

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(3)

driver.find_elements("class name", "wikipedia-icon")
driver.find_elements("id", "Wikipedia1_wikipedia-search-input")
driver.find_elements("class name", "wikipedia-search-button")
driver.find_elements("tag name", "button")
