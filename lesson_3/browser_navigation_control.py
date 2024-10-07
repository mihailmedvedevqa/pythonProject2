from selenium import webdriver

# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service)

# Переходим на страницу Google
driver.get("https://www.google.com/")
# Переходим на страницу Bing
driver.get("https://www.bing.com/")
# Возвращаемся на предыдущую страницу Google
driver.back()
# Перемещаемся вперед на страницу Bing
driver.forward()
# Обновляем текущую страницу Bing
driver.refresh()




