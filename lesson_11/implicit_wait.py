from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(executable_path=ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом
driver = webdriver.Chrome(service=service)
# Устанавливаем неявное ожидание в 10 секунд
driver.implicitly_wait(10)

# Переходим на страницу с динамическими свойствами
driver.get("https://demoqa.com/dynamic-properties")
# Определяем кнопку, которая должна стать видимой
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
# Находим кнопку и нажимаем на неё
driver.find_element(*VISIBLE_AFTER_BUTTON).click()


