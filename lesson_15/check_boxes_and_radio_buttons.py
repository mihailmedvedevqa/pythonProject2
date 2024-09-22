from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Способ 1
driver.get("http://the-internet.herokuapp.com/checkboxes")
# Объявляем локаторы
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
driver.get("http://the-internet.herokuapp.com/checkboxes")
CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")
# Ставим флажок
driver.find_element(*CHECKBOX_1).click()
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чек-бокс не выбран"
# Убираем флажок
driver.find_element(*CHECKBOX_2).click()
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чек-бокс до сих пор выбран"

# Нюанс 1
driver.get("https://demoqa.com/checkbox")
# Сам чек-бокс для проверки статуса
HOME_CHECKBOX = ("xpath", "//input[@id='tree-node-home']")
# Элемент для клика, чтобы выставить флажок
HOME_BUTTON = ("xpath", "//span[text()='Home']")
print(driver.find_element(*HOME_CHECKBOX).is_selected())
# Кликаем на элемент, который выставляет чек-бокс
driver.find_element(*HOME_BUTTON).click()
# Выведем статус чек-бокса, так как он меняется при клике на элемент, отвечающий за выставление флажка
print(driver.find_element(*HOME_CHECKBOX).is_selected())

# Нюанс 2
driver.get("https://demoqa.com/selectable")
# Записываем локатор первого чек-бокса
FIRST_CHECKBOX = ("xpath", "//li[contains(text(), 'Cras')]")
# Кликаем на него
driver.find_element(*FIRST_CHECKBOX).click()
# Проверяем, что после клика, к нему добавился класс active
assert "active" in driver.find_element(*FIRST_CHECKBOX).get_attribute("class"), "Чек-бокс не выбран"

# Радио-кнопки
driver.get("https://demoqa.com/radio-button")
YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")  # Для статуса
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")  # Для взаимодействия
driver.find_element(*YES_RADIO_LABEL).click()
assert driver.find_element(*YES_RADIO_BUTTON).is_selected() is True, "Радио-кнопка не выбрана"
