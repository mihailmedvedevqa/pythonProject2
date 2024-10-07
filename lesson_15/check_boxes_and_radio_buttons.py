from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Статусы чек-боксов

# Способ 1

# Страница для работы
driver.get("http://the-internet.herokuapp.com/checkboxes")
# Локаторы элементов
CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")
# Выполняем клик по первому чек-боксу
driver.find_element(*CHECKBOX_1).click()
# Убеждаемся что первый чек-бокс действительно выставлен
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None
# Выполняем клик по второму чек-боксу
driver.find_element(*CHECKBOX_2).click()
# Убеждаемся что второй чек-бокс действительно не выставлен
assert driver.find_element(*CHECKBOX_2).get_attribute("checked") is None

# Способ 2

# Страница для работы
driver.get("http://the-internet.herokuapp.com/checkboxes")
# Локаторы элементов
CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")
# Ставим флажок
driver.find_element(*CHECKBOX_1).click()
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чек-бокс не выбран"
# Убираем флажок
driver.find_element(*CHECKBOX_2).click()
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чек-бокс до сих пор выбран"

# Нюансы работы с чек-боксами

# Нюанс 1

# Страница для работы
driver.get("https://demoqa.com/checkbox")
# Локаторы элементов
HOME_CHECKBOX = ("xpath", "//input[@id='tree-node-home']")  # Сам чек-бокс для проверки статуса
HOME_BUTTON = ("xpath", "//span[text()='Home']")  # Элемент для клика, чтобы выставить флажок
print(driver.find_element(*HOME_CHECKBOX).is_selected())
# Кликаем на элемент, который выставляет чек-бокс
driver.find_element(*HOME_BUTTON).click()
# Выведем статус чек-бокса, так как он меняется при клике на элемент, отвечающий за выставление флажка
print(driver.find_element(*HOME_CHECKBOX).is_selected())

# Нюанс 2

# Страница для работы
driver.get("https://demoqa.com/selectable")
# Локатор чек-бокса
FIRST_CHECKBOX = ("xpath", "//li[contains(text(), 'Cras')]")
# Кликаем на него
driver.find_element(*FIRST_CHECKBOX).click()
# Проверяем, что после клика, к нему добавился класс active
assert "active" in driver.find_element(*FIRST_CHECKBOX).get_attribute("class"), "Чек-бокс не выбран"

# Радио-кнопки

# Страница для работы
driver.get("https://demoqa.com/radio-button")
# Локаторы элементов
YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")  # Для проверки статуса радио-кнопки
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")  # Для взаимодействия с меткой радио-кнопки
# Клик по метке для выбора радио-кнопки "Yes"
driver.find_element(*YES_RADIO_LABEL).click()
# Проверяем, что радио-кнопка "Yes" выбрана
assert driver.find_element(*YES_RADIO_BUTTON).is_selected() is True, "Радио-кнопка не выбрана"
