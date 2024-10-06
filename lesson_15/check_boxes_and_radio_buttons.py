from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Статусы чек-боксов

# Способ 1

# Локаторы элементов
CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")
# Страница для работы
driver.get("http://the-internet.herokuapp.com/checkboxes")
# Выполняем клик по первому чек-боксу
driver.find_element(*CHECKBOX_1).click()
# Убеждаемся что первый чек-бокс действительно выставлен
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None
# Выполняем клик по второму чек-боксу
driver.find_element(*CHECKBOX_2).click()
# Убеждаемся что второй чек-бокс действительно не выставлен
assert driver.find_element(*CHECKBOX_2).get_attribute("checked") is None

# Способ 2

# Локаторы элементов
CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")
# Страница для работы
driver.get("http://the-internet.herokuapp.com/checkboxes")
# Ставим флажок
driver.find_element(*CHECKBOX_1).click()
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чек-бокс не выбран"
# Убираем флажок
driver.find_element(*CHECKBOX_2).click()
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чек-бокс до сих пор выбран"

# Нюансы работы с чек-боксами

# Нюанс 1

# Локаторы элементов
HOME_CHECKBOX = ("xpath", "//input[@id='tree-node-home']")  # Сам чек-бокс для проверки статуса
HOME_BUTTON = ("xpath", "//span[text()='Home']")  # Элемент для клика, чтобы выставить флажок
# Страница для работы
driver.get("https://demoqa.com/checkbox")
print(driver.find_element(*HOME_CHECKBOX).is_selected())
# Кликаем на элемент, который выставляет чек-бокс
driver.find_element(*HOME_BUTTON).click()
# Выведем статус чек-бокса, так как он меняется при клике на элемент, отвечающий за выставление флажка
print(driver.find_element(*HOME_CHECKBOX).is_selected())

# Нюанс 2

# Локатор чек-бокса
FIRST_CHECKBOX = ("xpath", "//li[contains(text(), 'Cras')]")
# Страница для работы
driver.get("https://demoqa.com/selectable")
# Кликаем на него
driver.find_element(*FIRST_CHECKBOX).click()
# Проверяем, что после клика, к нему добавился класс active
assert "active" in driver.find_element(*FIRST_CHECKBOX).get_attribute("class"), "Чек-бокс не выбран"

# Радио-кнопки

# Локаторы элементов
YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")  # Для проверки статуса радио-кнопки
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")  # Для взаимодействия с меткой радио-кнопки
# Страница для работы
driver.get("https://demoqa.com/radio-button")
# Клик по метке для выбора радио-кнопки "Yes"
driver.find_element(*YES_RADIO_LABEL).click()
# Проверка, что радио-кнопка "Yes" выбрана
assert driver.find_element(*YES_RADIO_BUTTON).is_selected() is True, "Радио-кнопка не выбрана"
