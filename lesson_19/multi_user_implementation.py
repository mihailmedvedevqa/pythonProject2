import os
from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver_user_1 = webdriver.Chrome(service=service, options=options)

# Открываем страницу логина
driver_user_1.get("https://hyperskill.org/login")
# Локаторы элементов
LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
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

