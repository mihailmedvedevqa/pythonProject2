import time
from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Запускаем браузер в фоновом режиме
options.add_argument("--incognito")  # Используем режим инкогнито
options.add_argument("--ignore-certificate-errors")  # Игнорируем ошибки сертификатов
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
options.add_argument("--disable-cache")  # Отключаем кэширование
# Устанавливаем стратегию загрузки страницы
options.page_load_strategy = "normal"  # Ждем полной загрузки страницы
options.page_load_strategy = "eager"  # Ждем, пока DOM будет загружен и доступен для взаимодействия
options.page_load_strategy = "none"  # Не ждем загрузки страницы

# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Измеряем время загрузки страницы
start_time = time.time()  # Записываем время начала
driver.get("https://whatismyipaddress.com/")  # Переходим на сайт для проверки IP
end_time = time.time()  # Записываем время окончания
# Рассчитываем время загрузки
result = end_time - start_time
# Выводим результат
print(f"Время загрузки страницы: {result} секунд")
