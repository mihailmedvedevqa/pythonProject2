from selenium import webdriver
from selenium.webdriver import Keys

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Страница для работы
driver.get("https://the-internet.herokuapp.com/key_presses")
# Локатор поля ввода
KEY_PRESS_INPUT = ("xpath", "//input[@id='target']")
# Ввод текста
driver.find_element(*KEY_PRESS_INPUT).send_keys("Hello World")
# Выделение всего текста
driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.CONTROL + "A")
# Удаление выделенного текста
driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.BACKSPACE)

# Копирование и вставка

# Страница для работы
driver.get("https://clipboardjs.com/")
# Локаторы элементов
COPY_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
PASTE_LOCATOR = ("xpath", "//textarea[@id='bar']")
# Находим элементы на странице с помощью заданных локаторов
COPY = driver.find_element(*COPY_LOCATOR)
PASTE = driver.find_element(*PASTE_LOCATOR)
# Выделим все внутри поля
PASTE.send_keys(Keys.CONTROL + "A")
# Вырежем весь текст
PASTE.send_keys(Keys.CONTROL + "X")
# Вставим весь текст
PASTE.send_keys(Keys.CONTROL + "V")
