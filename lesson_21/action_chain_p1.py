from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)
# Создаем объект ActionChains для выполнения действий с элементами на странице
action = ActionChains(driver)


# Двойной клик

# Локатор элемента
DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
# Открываем целевую страницу
driver.get("https://demoqa.com/buttons")
# Находим элемент на странице с помощью заданного локатора
DB_BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)
# Двойной клик по элементу
action.double_click(DB_BUTTON)
action.perform()

# Клик правой кнопкой мыши

# Локатор элемента
RC_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")
# Открываем целевую страницу
driver.get("https://demoqa.com/buttons")
# Находим элемент на странице с помощью заданного локатора
RC_BUTTON = driver.find_element(*RC_BUTTON_LOCATOR)
# Клик правой кнопкой мыши по элементу
action.context_click(RC_BUTTON)
action.perform()

# Наведение на элемент

# Локаторы элементов
STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")
# Открываем целевую страницу
driver.get("https://demoqa.com/menu")
# Находим элементы на странице с помощью заданных локаторов
STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)
action.move_to_element(STEP_1)  # Наводим курсор на первый элемент
action.move_to_element(STEP_2)  # Затем на второй элемент
action.click(STEP_3)  # Наконец, кликаем на третий элемент
action.perform()  # Выполняем все накопленные действия

# Пауза в цепочке действий
action.move_to_element(STEP_1)  # Наводим курсор на первый элемент
action.pause(2)  # Делаем паузу в 2 секунды для ожидания появления подменю
action.move_to_element(STEP_2)  # Затем на второй элемент
action.pause(2)  # Делаем паузу в 2 секунды для ожидания появления подменю
action.click(STEP_3)  # Наконец, кликаем на третий элемент
action.perform()  # Выполняем все накопленные действия

# Scroll к элементу

# Локатор элемента
SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
# Открываем целевую страницу
driver.get("https://clipboardjs.com/")
# Находим элемент на странице с помощью заданного локатора
SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)
# Прокручиваем страницу к элементу
action.scroll_to_element(SOME_ELEMENT)
action.perform()



