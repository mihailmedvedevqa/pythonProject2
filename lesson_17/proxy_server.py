from selenium import webdriver

# Указываем адрес прокси-сервера
PROXY = "37.19.220.129:8443"
# Указываем адрес прокси-сервера с авторизацией
AUTH_PROXY = "username:password@37.19.220.129:8443"
# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Добавляем прокси через опции
options.add_argument(f"--proxy-server={PROXY}")
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Проверяем IP-адрес
driver.get("https://whatismyipaddress.com/")


