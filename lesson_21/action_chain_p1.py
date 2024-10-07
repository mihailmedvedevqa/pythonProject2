from selenium import webdriver
from selenium.webdriver import ActionChains

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)
# Создаем объект ActionChains для выполнения действий с элементами на странице
actions = ActionChains(driver)

# Двойной клик

# Открываем целевую страницу
driver.get("https://demoqa.com/buttons")
# Локатор элемента
DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
# Находим элемент на странице с помощью заданного локатора
DB_BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)
# Двойной клик по элементу
actions.double_click(DB_BUTTON)
actions.perform()

# Клик правой кнопкой мыши

# Открываем целевую страницу
driver.get("https://demoqa.com/buttons")
# Локатор элемента
RC_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")
# Находим элемент на странице с помощью заданного локатора
RC_BUTTON = driver.find_element(*RC_BUTTON_LOCATOR)
# Клик правой кнопкой мыши по элементу
actions.context_click(RC_BUTTON)
actions.perform()

# Наведение на элемент

# Открываем целевую страницу
driver.get("https://demoqa.com/menu")
# Локаторы элементов
STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")
# Находим элементы на странице с помощью заданных локаторов
STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)
actions.move_to_element(STEP_1)  # Наводим курсор на первый элемент
actions.move_to_element(STEP_2)  # Затем на второй элемент
actions.click(STEP_3)  # Наконец, кликаем на третий элемент
actions.perform()  # Выполняем все накопленные действия

# Пауза в цепочке действий
actions.move_to_element(STEP_1)  # Наводим курсор на первый элемент
actions.pause(2)  # Делаем паузу в 2 секунды для ожидания появления подменю
actions.move_to_element(STEP_2)  # Затем на второй элемент
actions.pause(2)  # Делаем паузу в 2 секунды для ожидания появления подменю
actions.click(STEP_3)  # Наконец, кликаем на третий элемент
actions.perform()  # Выполняем все накопленные действия

# Scroll к элементу

# Открываем целевую страницу
driver.get("https://clipboardjs.com/")
# Локатор элемента
SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
# Находим элемент на странице с помощью заданного локатора
SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)
# Прокручиваем страницу к элементу
actions.scroll_to_element(SOME_ELEMENT)
actions.perform()
