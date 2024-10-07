from selenium import webdriver

# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service)
# Устанавливаем неявное ожидание в 10 секунд
driver.implicitly_wait(10)

# Переходим на страницу
driver.get("https://demoqa.com/dynamic-properties")
# Определяем кнопку, которая должна стать видимой
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
# Находим кнопку и нажимаем на неё
driver.find_element(*VISIBLE_AFTER_BUTTON).click()


