from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
# Устанавливаем ожидание до 10 секунд для элементов на странице
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Клик с удержанием

# Открываем целевую страницу
driver.get("https://demoqa.com/buttons")
# Локатор элемента
OUTLINE_BUTTON_LOCATOR = ("xpath", "//button[text()='Click Me']")
# Находим элемент на странице с помощью заданного локатора
BUTTON = driver.find_element(*OUTLINE_BUTTON_LOCATOR)
# Удерживаем кнопку мыши на элементе
actions.click_and_hold(BUTTON)
actions.perform()

# Перетаскивание / drag and drop

# Открываем целевую страницу
driver.get("https://demoqa.com/droppable")
# Вариант 1
SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")  # Локатор для элемента, который будем перетаскивать
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")  # Локатор для элемента, куда будем перетаскивать
# Находим элементы
SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)
# Ожидаем, пока элемент не станет кликабельным
wait.until(EC.element_to_be_clickable(SOURCE))
# Перетаскиваем SOURCE в TARGET
actions.drag_and_drop(SOURCE, TARGET)
actions.perform()

# Вариант 2

# Открываем целевую страницу
driver.get("https://demoqa.com/sortable")
# Локатор для элемента, который будем перетаскивать
SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
# Локатор для элемента, куда будем перетаскивать
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")


# Функция для перетаскивания элемента
def drag_and_drop(source_element, target_element):
    source_element = driver.find_element(*source_element)  # Находим source-элемент
    target_element = driver.find_element(*target_element)  # Находим target-элемент
    wait.until(EC.element_to_be_clickable(source_element))  # Ждем кликабельности source элемента
    actions.drag_and_drop(source_element, target_element)
    actions.perform()


drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR)  # Использование функции

# Отпускаем кнопку мыши

# Открываем целевую страницу
driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")
# Локатор для элемента, который будем перетаскивать
SOURCE_LOCATOR = ("xpath", "//div[@class='grid__item'][7]")
# Локатор для элемента, куда будем перетаскивать
TARGET_LOCATOR = ("xpath", "//div[@class='drop-area__item'][2]")
# Находим элементы
SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)
actions.click_and_hold(SOURCE)  # Удерживаем кнопку мыши на source элементе
actions.pause(2)  # Делаем паузу в 2 секунды
actions.move_to_element(TARGET)  # Перемещаем курсор к target элементу
actions.release()  # Отпускаем кнопку мыши
actions.perform()  # Выполняем все действия
