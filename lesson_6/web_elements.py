from selenium import webdriver

# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service)

# Переходим на страницу
driver.get("https://hyperskill.org/courses")
# Нажимаем на четвертую ссылку в навигации
nav_link = driver.find_elements("class name", "nav-link")[3]
nav_link.click()

# Переходим на другую страницу
driver.get("https://testautomationpractice.blogspot.com/")
# Ищем элементы на странице
wikipedia_icon = driver.find_elements("class name", "wikipedia-icon")
search_input = driver.find_elements("id", "Wikipedia1_wikipedia-search-input")
buttons = driver.find_elements("tag name", "button")
