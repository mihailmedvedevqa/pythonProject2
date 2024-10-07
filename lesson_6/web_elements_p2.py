from selenium import webdriver

# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service)

# driver.get("https://hyperskill.org/courses")
# time.sleep(3)
# driver.find_elements("class name", "nav-link")[3].click()
# time.sleep(3)

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(3)

driver.find_elements("class name", "wikipedia-icon")
driver.find_elements("id", "Wikipedia1_wikipedia-search-input")
driver.find_elements("class name", "wikipedia-search-button")
driver.find_elements("tag name", "button")
