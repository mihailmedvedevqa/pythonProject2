import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Выбор элементов

# Локатор для dropdown
DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
# Страница для работы
driver.get("https://the-internet.herokuapp.com/dropdown")
# Объект dropdown
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))

# Выбор элемента по содержимому text
DROPDOWN.select_by_visible_text("Option 1")
# Выбор элемента по index
DROPDOWN.select_by_index(1)
# Выбор элемента по value
DROPDOWN.select_by_value("1")
# Получение всех элементов dropdown
print(DROPDOWN.options)

# Перебор элементов

# Локатор для dropdown
DROPDOWN_LOCATOR = ("xpath", "//select[@id='oldSelectMenu']")
# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Объект dropdown
DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
# Все элементы dropdown
all_options = DROPDOWN.options
# Перебор элементов по text
for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_visible_text(option.text)
# Перебор элементов по index
for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_index(all_options.index(option))
# Перебор элементов по value
for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))

# Современный Dropdown, способ 1

# Локатор dropdown
SELECT_TITLE = ("xpath", "//input[@id='react-select-3-input']")
# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Вводим текст в dropdown
driver.find_element(*SELECT_TITLE).send_keys("Mrs.")
time.sleep(5)
# Подтверждаем выбор
driver.find_element(*SELECT_TITLE).send_keys(Keys.ENTER)

# Современный Dropdown, способ 2
# Вариант 1
# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Открываем dropdown
driver.find_element("xpath", "//div[@id='withOptGroup']").click()
# Кликаем на элемент внутри
driver.find_element("xpath", "//div[@id='withOptGroup']//div[text()='A root option']").click()

# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Открываем dropdown
driver.find_element("xpath", "//div[@id='withOptGroup']").click()


# Вариант 2
# Поиск элемента внутри dropdown по text
def choose_dropdown_element_by_text(text):
    elements = driver.find_elements("xpath", "//div[@id='withOptGroup']//div[contains(@id, 'react-select')]")
    for element in elements:
        if text in element.text:
            return element  # Возвращаем нужный элемент из dropdown по text


# Кликаем на выбранный элемент
choose_dropdown_element_by_text("Another root option").click()
