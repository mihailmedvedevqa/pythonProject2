import time
from selenium import webdriver

# Указываем адрес прокси-сервера
PROXY = "37.19.220.129:8443"
# Указываем адрес прокси-сервера с авторизацией
AUTH_PROXY = "username:password@37.19.220.129:8443"
chrome_options = webdriver.ChromeOptions()
# Добавляем прокси через опции
chrome_options.add_argument(f"--proxy-server={PROXY}")
driver = webdriver.Chrome(options=chrome_options)
# Проверяем IP-адрес
driver.get("https://2ip.ru")
time.sleep(5)

