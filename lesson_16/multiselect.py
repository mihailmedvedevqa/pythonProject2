from selenium import webdriver
from selenium.webdriver import Keys

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Вариант 1

# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Локатор выпадающего списка
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
# Вводим текст в поле ввода
driver.find_element(*MULTISELECT).send_keys("Gre")
# Проверяем, что введённый текст соответствует ожидаемому значению
assert driver.find_element(*MULTISELECT).get_attribute("value") == "Gre", "Текст не введен"
# Подтверждаем выбор, используя клавишу TAB
driver.find_element(*MULTISELECT).send_keys(Keys.TAB)

# Вариант 2

# Страница для работы
driver.get("https://demoqa.com/select-menu")
# Локатор выпадающего списка
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
# Вводим текст в поле ввода
driver.find_element(*MULTISELECT).send_keys("Bla")
# Проверяем, что введённый текст соответствует ожидаемому значению
assert driver.find_element(*MULTISELECT).get_attribute("value") == "Bla", "Текст не введен"
# Подтверждаем выбор, используя клавишу ENTER
driver.find_element(*MULTISELECT).send_keys(Keys.ENTER)

