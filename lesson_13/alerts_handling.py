from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)
# Устанавливаем ожидание до 15 секунд, проверяя наличие элемента каждую секунду
wait = WebDriverWait(driver, 15, poll_frequency=1)

# Принять alert

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")
# Клик на кнопку, которая вызывает alert
BUTTON_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())
# Переключение на alert
driver.switch_to.alert
alert.accept()  # Принимаем alert

# Отклонить alert

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")
# Клик на кнопку, которая вызывает alert
BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.dismiss()  # Отклоняем alert

# Получение текста из alert

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")
# Клик на кнопку, которая вызывает alert
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
print(alert.text)  # Вывод текста из alert

# Ввод данных в alert

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")
# Клик на кнопку, которая вызывает alert
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
# Ввод данных в alert
alert.send_keys("Hello world")
alert.accept()  # Обязательно либо принять, либо отклонить alert после ввода данных
