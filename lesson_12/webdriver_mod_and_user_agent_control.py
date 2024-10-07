from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Отключаем песочницу, что может помочь при запуске в некоторых окружениях
options.add_argument("--no-sandbox")
# Отключаем использование общего пространства памяти, чтобы избежать ошибок в контейнерах
options.add_argument("--disable-dev-shm-usage")
# Скрываем информацию о том, что браузер управляется автоматизацией
options.add_argument("--disable-blink-features=AutomationControlled")
# Устанавливаем пользовательский агент для обхода блокировок
options.add_argument("--user-agent=Selenium")
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)
# Устанавливаем ожидание до 15 секунд, проверяя наличие элемента каждую секунду
wait = WebDriverWait(driver, 15, poll_frequency=1)

# Открываем тестовую страницу
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
# Сохраняем изображение экрана в файл
driver.save_screenshot("screenshot.png")


