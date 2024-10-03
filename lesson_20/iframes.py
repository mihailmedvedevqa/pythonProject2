from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Вариант 1

# Локаторы элементов
FROM_NAME_FIELD_LOCATOR = ("xpath", "//input[@name='RESULT_TextField-1']")
COPY_TEXT_LOCATOR = ("xpath", "//button[text()='Copy Text']")
IFRAME_LOCATOR = ("xpath", "//iframe")
# Открываем целевую страницу
driver.get("https://testautomationpractice.blogspot.com")
# Переключение на iframe
iframe = driver.find_element(*IFRAME_LOCATOR)  # Находим iframe
driver.switch_to.frame(iframe)  # Переключаемся на iframe
# Вводим текст в поле
driver.find_element(*FROM_NAME_FIELD_LOCATOR).send_keys("Test")
# Возвращаемся к основному контенту страницы
driver.switch_to.default_content()
# Нажимаем кнопку
driver.find_element(*COPY_TEXT_LOCATOR).click()

# Вариант 2

# Открываем целевую страницу
driver.get("https://demoqa.com/nestedframes")
# Переключаемся на первый фрейм по его имени
driver.switch_to.frame("frame1")
# Получаем текст из тела первого фрейма и выводим его на экран
print(driver.find_element("xpath", "//body").text)
# Переключаемся на вложенный фрейм по индексу (0 - первый вложенный фрейм)
driver.switch_to.frame(0)
# Получаем текст из тела вложенного фрейма и выводим его на экран
print(driver.find_element("xpath", "//body").text)
# Возвращаемся к родительскому фрейму
driver.switch_to.parent_frame()
# Получаем текст из тела родительского фрейма и выводим его на экран
print(driver.find_element("xpath", "//body").text)
# Возвращаемся к основному контенту страницы
driver.switch_to.default_content()
