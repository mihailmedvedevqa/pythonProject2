from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Устанавливаем сервис для Chrome с помощью менеджера драйвера
service = Service(executable_path=ChromeDriverManager().install())
# Создаем объект Options для настройки параметров браузера
chrome_options = Options()
# Запускаем экземпляр Chrome для первого пользователя
driver = webdriver.Chrome(options=chrome_options, service=service)

# Вариант 1
# Локаторы
FROM_NAME_FIELD_LOCATOR = ("xpath", "//input[@name='RESULT_TextField-1']")
COPY_TEXT_LOCATOR = ("xpath", "//button[text()='Copy Text']")
IFRAME_LOCATOR = ("xpath", "//iframe")


# Страница для работы
driver.get("https://testautomationpractice.blogspot.com")
# Переключение на iframe
iframe = driver.find_element(*IFRAME_LOCATOR)
driver.switch_to.frame(iframe)
# Вводим текст в поле
driver.find_element(*FROM_NAME_FIELD_LOCATOR).send_keys("Test")
# Возвращаемся к основному контенту страницы
driver.switch_to.default_content()
# Нажимаем кнопку
driver.find_element(*COPY_TEXT_LOCATOR).click()

# Вариант 2
# Страница для работы
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
