from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)
actions = ActionChains(driver)


# Двойной клик
DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")

driver.get("https://demoqa.com/buttons")
DB_BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)
actions.double_click(DB_BUTTON).perform()

# Клик правой кнопкой мыши
RC_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")
RC_BUTTON = driver.find_element(*RC_BUTTON_LOCATOR)
actions.context_click(RC_BUTTON).perform()

# Наведение на элемент
STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

driver.get("https://demoqa.com/menu")
STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)

actions.move_to_element(STEP_1)
actions.move_to_element(STEP_2)
actions.click(STEP_3)
actions.perform()

# Пауза в цепочке действий
STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

driver.get("https://demoqa.com/menu")
STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)

actions.move_to_element(STEP_1)
actions.pause(2)
actions.move_to_element(STEP_2)
actions.pause(2)
actions.click(STEP_3)
actions.perform()

# Scroll к элементу
SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")

driver.get("https://clipboardjs.com/")
SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)
actions.scroll_to_element(SOME_ELEMENT)
actions.perform()



