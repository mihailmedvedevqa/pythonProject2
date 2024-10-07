from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Переходим на страницу
driver.get("https://www.freeconferencecall.com/")
# Находим кнопку и нажимаем на нее
LOGIN_BUTTON = driver.find_element("xpath", "//a[@id='login-desktop']")
LOGIN_BUTTON.click()
# Находим поле для ввода email
EMAIL_FIELD = driver.find_element("xpath", "//input[@id='login_email']")
EMAIL_FIELD.clear()  # Очищаем поле для ввода email
# Убеждаемся, что поле пустое
assert EMAIL_FIELD.get_attribute("value") == ""
# Вводим email
EMAIL_FIELD.send_keys("text@mail.com")
# Проверяем, что введенный email соответствует ожидаемому значению
EMAIL_FIELD_VALUE = EMAIL_FIELD.get_attribute("value")
assert "text@mail.com" in EMAIL_FIELD_VALUE
print(EMAIL_FIELD.get_attribute("value"))  # Выводим введенный email
# Находим поле для ввода пароля
PASSWORD_FIELD = driver.find_element("xpath", "//input[@id='password']")
PASSWORD_FIELD.clear()  # Очищаем поле для ввода пароля
# Убеждаемся, что поле пустое
assert PASSWORD_FIELD.get_attribute("value") == ""
# Вводим пароль
PASSWORD_FIELD.send_keys("0123456789")
# Проверяем, что введенный пароль соответствует ожидаемому значению
PASSWORD_FIELD_VALUE = PASSWORD_FIELD.get_attribute("value")
assert "0123456789" in PASSWORD_FIELD_VALUE
print(PASSWORD_FIELD.get_attribute("value"))  # Выводим введенный пароль

