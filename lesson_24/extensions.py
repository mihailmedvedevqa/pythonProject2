from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
options.add_extension('extensions\\adblock.crx')  # Устанавливаем расширение
# Инициализируем веб-драйвер для Chrome с заданными опциями
driver = webdriver.Chrome(options=options)

# Открываем тестовую страницу
driver.get("https://test.adminforge.de/adblock.html")
