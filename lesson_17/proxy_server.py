from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Указываем адрес прокси-сервера
PROXY = "37.19.220.129:8443"
# Указываем адрес прокси-сервера с авторизацией
AUTH_PROXY = "username:password@37.19.220.129:8443"
# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Добавляем прокси через опции
options.add_argument(f"--proxy-server={PROXY}")
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)


# Проверяем IP-адрес
driver.get("https://whatismyipaddress.com/")


