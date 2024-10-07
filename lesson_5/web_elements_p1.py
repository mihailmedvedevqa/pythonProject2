from selenium import webdriver

# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service)

# Переходим на страницу
driver.get("https://www.freeconferencecall.com/login")
# Кликаем на элемент
driver.find_element("id", "loginformsubmit").click()


# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"
