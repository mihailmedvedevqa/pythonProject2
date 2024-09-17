from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/courses")

SIGN_IN_BUTTON = driver.find_elements("xpath", "//button[contains(@class, 'btn-outline-light'")
START_FOR_FREE_BUTTON = driver.find_elements("xpath", "//button[contains(@class, 'btn-primary'")
