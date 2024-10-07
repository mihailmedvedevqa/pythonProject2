import os
from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
# Указываем путь для загрузки файлов
prefs = {
    "download.default_directory": f"{os.getcwd()}\\downloads"  # Задаем директорию для загрузок
}
options.add_experimental_option("prefs", prefs)  # Применяем настройки
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Переходим на страницу для загрузки файлов
driver.get("https://the-internet.herokuapp.com/download")
# Находим элемент для загрузки файла (третья ссылка в списке)
DOWNLOAD_FILE = driver.find_elements("xpath", "//a")[3]
# Кликаем на ссылку для загрузки файла
DOWNLOAD_FILE.click()

