from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)
# Устанавливаем ожидание до 10 секунд для элементов на странице
wait = WebDriverWait(driver, 10, poll_frequency=1)
# Создаем объект ActionChains для выполнения действий с элементами на странице
action = ActionChains(driver)

# Клик с удержанием

# Локатор элемента
OUTLINE_BUTTON_LOCATOR = ("xpath", "//button[text()='Click Me']")
# Открываем целевую страницу
driver.get("https://demoqa.com/buttons")
# Находим элемент на странице с помощью заданного локатора
BUTTON = driver.find_element(*OUTLINE_BUTTON_LOCATOR)
# Удерживаем кнопку мыши на элементе
action.click_and_hold(BUTTON)
action.perform()

# Перетаскивание / drag and drop

# Вариант 1
SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")  # Локатор для элемента, который будем перетаскивать
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")  # Локатор для элемента, куда будем перетаскивать
# Открываем целевую страницу
driver.get("https://demoqa.com/droppable")
# Находим элементы
SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)
# Ожидаем, пока элемент не станет кликабельным
wait.until(EC.element_to_be_clickable(SOURCE))
# Перетаскиваем SOURCE в TARGET
action.drag_and_drop(SOURCE, TARGET)
action.perform()

# Вариант 2

# Локатор для элемента, который будем перетаскивать
SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
# Локатор для элемента, куда будем перетаскивать
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")
# Открываем целевую страницу
driver.get("https://demoqa.com/sortable")


# Функция для перетаскивания элемента
def drag_and_drop(source_element, target_element):
    source_element = driver.find_element(*source_element)  # Находим source-элемент
    target_element = driver.find_element(*target_element)  # Находим target-элемент
    wait.until(EC.element_to_be_clickable(source_element))  # Ждем кликабельности source элемента
    action.drag_and_drop(source_element, target_element)
    action.perform()


drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR)  # Использование функции

# Отпускаем кнопку мыши

# Локатор для элемента, который будем перетаскивать
SOURCE_LOCATOR = ("xpath", "//div[@class='grid__item'][7]")
# Локатор для элемента, куда будем перетаскивать
TARGET_LOCATOR = ("xpath", "//div[@class='drop-area__item'][2]")
# Открываем целевую страницу
driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")
# Находим элементы
SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)
action.click_and_hold(SOURCE)  # Удерживаем кнопку мыши на source элементе
action.pause(2)  # Делаем паузу в 2 секунды
action.move_to_element(TARGET)  # Перемещаем курсор к target элементу
action.release()  # Отпускаем кнопку мыши
action.perform()  # Выполняем все действия
