from selenium import webdriver

# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service)

# Переходим на главную страницу Википедии
driver.get("https://www.wikipedia.org/")
# Получаем текущий URL страницы
PAGE_URL = driver.current_url
print(f"Page URL: {PAGE_URL}")
# Проверяем, что URL соответствует ожидаемому
assert PAGE_URL == "https://www.wikipedia.org/", "Ошибка URL, открыта не та страница"
# Получаем заголовок страницы
PAGE_TITLE = driver.title
print(f"Page Title: {PAGE_TITLE}")
# Проверяем, что заголовок соответствует ожидаемому
assert PAGE_TITLE == "Wikipedia", "Неправильный заголовок страницы"
# Получаем исходный код страницы
PAGE_SOURCE = driver.page_source
print(PAGE_SOURCE)

