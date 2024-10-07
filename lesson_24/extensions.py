from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
options.add_extension('extensions\\adblock.crx')  # Устанавливаем расширение
# Инициализируем веб-драйвер для Chrome с заданными опциями
driver = webdriver.Chrome(options=options)

# Открываем тестовую страницу
driver.get("https://test.adminforge.de/adblock.html")
