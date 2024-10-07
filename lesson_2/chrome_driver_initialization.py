from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Переходим на страницу Google
driver.get("https://www.google.com/")
print(driver.title)  # Печатаем заголовок страницы
