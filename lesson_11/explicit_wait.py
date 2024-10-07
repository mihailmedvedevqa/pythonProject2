from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(executable_path=ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом
driver = webdriver.Chrome(service=service)
# Устанавливаем ожидание до 15 секунд, проверяя наличие элемента каждую секунду
wait = WebDriverWait(driver, 15, poll_frequency=1)

# Переходим на страницу с динамическими свойствами
driver.get("https://demoqa.com/dynamic-properties")
WILL_ENABLE_BUTTON = ("xpath", "//button[@id='enableAfter']")
# Ждем, пока кнопка станет доступной для клика, и нажимаем на неё
wait.until(EC.element_to_be_clickable(WILL_ENABLE_BUTTON)).click()
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
# Ждем, пока кнопка станет видимой, и нажимаем на неё
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)).click()

# Переходим на страницу для работы с динамическими контролем
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
# Нажимаем кнопку "Remove"
driver.find_element(*REMOVE_BUTTON).click()
# Ждем, пока элемент исчезнет
wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
# Ждем, пока кнопка "Enable" станет доступной для клика, и нажимаем на неё
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
TEXT_FIELD = ("xpath", "//input[@type='text']")
# Ждем, пока текстовое поле станет доступным, и вводим текст
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")
# Проверяем, что текст был введен
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))

# Переходим на страницу для добавления элементов
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
ADD_ELEMENT_BUTTON = ("xpath", "//button[@id='sbm']")
# Ждем, пока кнопка станет доступной для клика
wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))
# Нажимаем на кнопку для добавления элемента
driver.find_element(*ADD_ELEMENT_BUTTON).click()

# Возвращаемся на страницу с динамическими свойствами для работы с элементами
driver.get("https://demoqa.com/dynamic-properties")
ADD_ELEMENT = ("xpath", "//button[@onclick='addElement()']")
DELETE_BUTTON = ("xpath", "//button[@onclick='deleteElement()']")
# Ждем, пока кнопка добавления станет доступной
wait.until(EC.element_to_be_clickable(ADD_ELEMENT))
driver.find_element(*ADD_ELEMENT).click()
# Ждем, пока кнопка удаления станет видимой
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

# Повторяем операцию добавления и удаления элемента
driver.get("https://demoqa.com/dynamic-properties")
wait.until(EC.element_to_be_clickable(ADD_ELEMENT))
driver.find_element(*ADD_ELEMENT).click()
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))
driver.find_element(*DELETE_BUTTON).click()
# Ждем, пока кнопка удаления исчезнет
wait.until(EC.invisibility_of_element_located(DELETE_BUTTON))

# Переходим на страницу с динамическим контролем для работы с чек-боксом
driver.get("http://the-internet.herokuapp.com/dynamic_controls")
SWAP_BUTTON = ("xpath", "//button[@onclick='swapCheckbox()']")
# Нажимаем на кнопку для переключения состояния чекбокса
driver.find_element(*SWAP_BUTTON).click()
# Ждем, пока текст на кнопке изменится на "Add"
wait.until(EC.text_to_be_present_in_element(SWAP_BUTTON, "Add"))






