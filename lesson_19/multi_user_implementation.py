import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Запускаем экземпляр Chrome для первого пользователя
driver_user_1 = webdriver.Chrome(options=options, service=service)

# Локаторы элементов
LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
# Открываем страницу логина
driver_user_1.get("https://hyperskill.org/login")
# Вводим логин из переменной окружения
driver_user_1.find_element(*LOGIN_FIELD).send_keys(os.environ["LOGIN_L19"])
# Вводим пароль из переменной окружения
driver_user_1.find_element(*PASSWORD_FIELD).send_keys(os.environ["PASSWORD_L19"])
# Нажимаем кнопку входа
driver_user_1.find_element(*SUBMIT_BUTTON).click()

# Запускаем второй экземпляр Chrome для другого пользователя
driver_user_2 = webdriver.Chrome(options=options, service=service)
# Открываем страницу логина для второго пользователя
driver_user_2.get("https://hyperskill.org/login")

