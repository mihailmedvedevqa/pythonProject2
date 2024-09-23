from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Вариант 1
# Локатор dropdown
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Вводим текст в поле ввода
driver.find_element(*MULTISELECT).send_keys("Gre")
# Проверяем, что введённый текст соответствует ожидаемому значению
assert driver.find_element(*MULTISELECT).get_attribute("value") == "Gre", "Текст не введен"
# Подтверждаем выбор, используя клавишу TAB
driver.find_element(*MULTISELECT).send_keys(Keys.TAB)

# Вариант 2
# Локатор dropdown
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Вводим текст в поле ввода
driver.find_element(*MULTISELECT).send_keys("Bla")
# Проверяем, что введённый текст соответствует ожидаемому значению
assert driver.find_element(*MULTISELECT).get_attribute("value") == "Bla", "Текст не введен"
# Подтверждаем выбор, используя клавишу ENTER
driver.find_element(*MULTISELECT).send_keys(Keys.ENTER)

