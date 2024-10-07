import os
import pickle
from selenium import webdriver

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Переходим на страницу входа
driver.get("https://www.freeconferencecall.com/login")
# Получаем и выводим cookie, чтобы проверить, установлены ли они
print(driver.get_cookie("country_code"))  # Выводим cookie "country_code"
print(driver.get_cookies())  # Выводим все cookies
# Добавляем тестовую cookie
driver.add_cookie({
    "name": "test_name",
    "value": "test_value"
})
print(driver.get_cookie("test_name"))  # Проверяем, была ли cookie добавлена

# Переходим на страницу входа
driver.get("https://www.freeconferencecall.com/login")
# Работа с cookie "split"
cookie_before = driver.get_cookie("split")  # Получаем cookie "split"
print(cookie_before)  # Выводим значение cookie до удаления
driver.delete_cookie("split")  # Удаляем cookie "split"
# Добавляем новую cookie "split"
driver.add_cookie({
     "name": "split",
     "value": "test_split"
})
cookie_after = driver.get_cookie("split")  # Получаем обновленную cookie
print(cookie_after)  # Выводим значение cookie после добавления

# Переходим на страницу входа
driver.get("https://www.freeconferencecall.com/login")
# Получаем все cookies перед удалением
cookies_before = driver.get_cookies()
print(cookies_before)  # Выводим cookies
driver.delete_all_cookies()  # Удаляем все cookies
# Снова добавляем тестовую cookie
driver.add_cookie({
     "name": "test_name",
     "value": "test_value"
})
cookies_after = driver.get_cookies()  # Получаем cookies после добавления
print(cookies_after)  # Выводим cookies

# Локаторы для полей ввода и кнопки на странице
LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")
# Переходим на страницу входа
driver.get("https://www.freeconferencecall.com/login")
# Вводим логин и пароль
driver.find_element(*LOGIN_FIELD).send_keys("test_login")
driver.find_element(*PASSWORD_FIELD).send_keys("test_password")
driver.find_element(*SUBMIT_BUTTON).click()
# Сохраняем cookies в файл для последующего использования
pickle.dump(driver.get_cookies(), open(os.getcwd() + "\\cookies\\cookies.pkl", "wb"))

# Переходим на страницу входа
driver.get("https://www.freeconferencecall.com/login")
driver.delete_all_cookies()  # Удаляем все cookies
# Загружаем cookies из файла
cookies = pickle.load(open(os.getcwd() + "\\cookies\\cookies.pkl", "rb"))
# Добавляем cookies в браузер
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()  # Обновляем страницу, чтобы применить cookies
driver.get("https://www.freeconferencecall.com/profile")  # Переходим на страницу профиля
