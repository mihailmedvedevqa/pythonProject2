from selenium import webdriver

# Создаем объект FirefoxOptions для настройки браузера
options = webdriver.FirefoxOptions()
# Создаем сервис для Firefox
service = webdriver.FirefoxService()
# Инициализируем веб-драйвер для Firefox с заданными сервисом и опциями
driver = webdriver.Firefox(service=service, options=options)

# Переходим на страницу Google
driver.get("https://www.google.com/")
print(driver.title)  # Печатаем заголовок страницы
# Закрываем драйвер после выполнения
driver.quit()

