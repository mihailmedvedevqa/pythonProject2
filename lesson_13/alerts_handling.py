from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/alerts")
BUTTON_1 = driver.find_element("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.accept()

BUTTON_3 = driver.find_element("xpath", "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.dismiss()

BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
print(alert.text)

# BUTTON_4 = ("xpath", "//button[@id='promtButton']")
# wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
# alert = wait.until(EC.alert_is_present())
# driver.switch_to.alert
# alert.send_keys("Hello world")
# alert.accept()
