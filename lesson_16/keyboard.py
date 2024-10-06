from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys


# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)


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

# Локаторы элементов
COPY_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
PASTE_LOCATOR = ("xpath", "//textarea[@id='bar']")
# Страница для работы
driver.get("https://clipboardjs.com/")
# Находим элементы на странице с помощью заданных локаторов
COPY = driver.find_element(*COPY_LOCATOR)
PASTE = driver.find_element(*PASTE_LOCATOR)
# Выделим все внутри поля
PASTE.send_keys(Keys.CONTROL + "A")
# Вырежем весь текст
PASTE.send_keys(Keys.CONTROL + "X")
# Вставим весь текст
PASTE.send_keys(Keys.CONTROL + "V")
