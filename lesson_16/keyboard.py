import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Локатор поля ввода
KEY_PRESS_INPUT = ("xpath", "//input[@id='target']")
# Страница для работы
driver.get("https://the-internet.herokuapp.com/key_presses")
# Ввод текста
driver.find_element(*KEY_PRESS_INPUT).send_keys("Hello World")
# Выделение всего текста
driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.CONTROL + "A")
# Удаление выделенного текста
driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.BACKSPACE)


# Копирование и вставка

# Локаторы
COPY_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
PASTE_LOCATOR = ("xpath", "//textarea[@id='bar']")
# Страница для работы
driver.get("https://clipboardjs.com/")
COPY = driver.find_element(*COPY_LOCATOR)
PASTE = driver.find_element(*PASTE_LOCATOR)
# Выделим все внутри поля
PASTE.send_keys(Keys.CONTROL + "A")
time.sleep(2)
# Вырежем весь текст
PASTE.send_keys(Keys.CONTROL + "X")
time.sleep(2)
# Вставим весь текст
PASTE.send_keys(Keys.CONTROL + "V")
