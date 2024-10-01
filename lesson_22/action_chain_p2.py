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

# Клик с удержанием
OUTLINE_BUTTON_LOCATOR = ("xpath", "//button[text()='Click Me']")

driver.get("https://demoqa.com/buttons")
BUTTON = driver.find_element(*OUTLINE_BUTTON_LOCATOR)
actions.click_and_hold(BUTTON)
actions.perform()

# Перетаскивание / drag and drop
# Вариант 1
SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")

driver.get("https://demoqa.com/droppable")
SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)
wait.until(EC.element_to_be_clickable(SOURCE))
actions.drag_and_drop(SOURCE, TARGET)
actions.perform()

# Вариант 1
SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")

driver.get("https://demoqa.com/sortable")


def drag_and_drop(source_element, target_element):
    source_element = driver.find_element(*source_element)  # Находим source-элемент
    target_element = driver.find_element(*target_element)  # Находим target-элемент
    wait.until(EC.element_to_be_clickable(source_element))  # Ждем кликабельности source-элемента
    actions.drag_and_drop(source_element, target_element)
    actions.perform()


drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR)  # Использование функции

# Отпускаем кнопку мыши
driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")

source = driver.find_element("xpath", "//div[@class='grid__item'][7]")  # Что перетаскиваем
target = driver.find_element("xpath", "//div[@class='drop-area__item'][2]")  # Куда перетаскиваем

actions.click_and_hold(source)
actions.pause(2)
actions.move_to_element(target)
actions.release()
actions.perform()
