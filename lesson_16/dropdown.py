from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Стандартный dropdown

# Страница для работы
driver.get("https://the-internet.herokuapp.com/dropdown")
# Локатор выпадающего списка
DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
# Создаем объект выпадающего списка, поместив внутрь веб-элемент dropdown
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
# Выбор элемента по содержимому text
DROPDOWN.select_by_visible_text("Option 1")
# Выбор элемента по index
DROPDOWN.select_by_index(1)
# Выбор элемента по value
DROPDOWN.select_by_value("1")
print(DROPDOWN.options)  # Вернет все элементы

# Перебор элементов

# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Локатор выпадающего списка
DROPDOWN_LOCATOR = ("xpath", "//select[@id='oldSelectMenu']")
# Создаем объект выпадающего списка, поместив внутрь веб-элемент dropdown
DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
# Запишем все элементы выпадающего списка
all_options = DROPDOWN.options
# Перебор элементов по text
for option in all_options:
    DROPDOWN.select_by_visible_text(option.text)
# Перебор элементов по index
for option in all_options:
    DROPDOWN.select_by_index(all_options.index(option))
# Перебор элементов по value
for option in all_options:
    DROPDOWN.select_by_value(option.get_attribute("value"))

# Современный Dropdown

# Способ 1

# Локатор выпадающего списка
SELECT_TITLE = ("xpath", "//input[@id='react-select-3-input']")
# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Вводим текст в dropdown
driver.find_element(*SELECT_TITLE).send_keys("Mrs.")
# Подтверждаем выбор
driver.find_element(*SELECT_TITLE).send_keys(Keys.ENTER)

# Способ 2

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

# Поиск элемента внутри выпадающего списка по text
def choose_dropdown_element_by_text(text):
    elements = driver.find_elements("xpath", "//div[@id='withOptGroup']//div[contains(@id, 'react-select')]")
    for element in elements:
        if text in element.text:
            return element  # Возвращаем нужный элемент из выпадающего списка по text


choose_dropdown_element_by_text("Another root option").click()  # Кликаем на выбранный элемент
