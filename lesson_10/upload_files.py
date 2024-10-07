import os
from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Переходим на страницу для загрузки файлов
driver.get("https://the-internet.herokuapp.com/upload")
# Находим элемент для загрузки файла
UPLOAD_FILE = driver.find_element("xpath", "//input[@type='file']")
# Отправляем путь к файлу, который хотим загрузить
UPLOAD_FILE.send_keys(f"{os.getcwd()}\\downloads\\test-upload.txt")
