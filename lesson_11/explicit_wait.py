from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")
WILL_ENABLE_BUTTON = ("xpath", "//button[@id='enableAfter']")
wait.until(EC.element_to_be_clickable(WILL_ENABLE_BUTTON)).click()
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)).click()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
driver.find_element(*REMOVE_BUTTON).click()
wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
TEXT_FIELD = ("xpath", "//input[@type='text']")
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
ADD_ELEMENT_BUTTON = ("xpath", "//button[@id='sbm']")
wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))
driver.find_element(*ADD_ELEMENT_BUTTON).click()

driver.get("https://demoqa.com/dynamic-properties")
ADD_ELEMENT = ("xpath", "//button[@onclick='addElement()']")
DELETE_BUTTON = ("xpath", "//button[@onclick='deleteElement()']")
wait.until(EC.element_to_be_clickable(ADD_ELEMENT))
driver.find_element(*ADD_ELEMENT).click()
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

driver.get("https://demoqa.com/dynamic-properties")
ADD_ELEMENT = ("xpath", "//button[@onclick='addElement()']")
DELETE_BUTTON = ("xpath", "//button[@onclick='deleteElement()']")
wait.until(EC.element_to_be_clickable(ADD_ELEMENT))
driver.find_element(*ADD_ELEMENT).click()
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))
driver.find_element(*DELETE_BUTTON).click()
wait.until(EC.invisibility_of_element_located(DELETE_BUTTON))

driver.get("http://the-internet.herokuapp.com/dynamic_controls")
SWAP_BUTTON = ("xpath", "//button[@onclick='swapCheckbox()']")
driver.find_element(*SWAP_BUTTON).click()
wait.until(EC.text_to_be_present_in_element(SWAP_BUTTON, "Add"))






