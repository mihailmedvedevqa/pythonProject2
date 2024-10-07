from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service)

# Переходим на страницу
driver.get("https://hyperskill.org/courses")
# Ожидаем, пока кнопка "Войти" станет кликабельной
SIGN_IN_BUTTON = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(("xpath", "//button[contains(@class, 'btn-outline-light')]"))
)
SIGN_IN_BUTTON.click()  # Кликаем на кнопку
# Ожидаем, пока кнопка "Начать бесплатно" станет кликабельной
START_FOR_FREE_BUTTON = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(("xpath", "//button[contains(@class, 'btn-primary')]"))
)
START_FOR_FREE_BUTTON.click()  # Кликаем на кнопку
