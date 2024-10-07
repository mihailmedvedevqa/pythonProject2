from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from scrolls import Scrolls

# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера

# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)
# Создаем объект ActionChains для выполнения действий с элементами на странице
action = ActionChains(driver)
# Инициализируем класс Scrolls с драйвером и действиями
scrolls = Scrolls(driver, action)

# Локатор элемента
EXAMPLE2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
# Открываем целевую страницу
driver.get("https://seiyria.com/bootstrap-slider/")
# Находим элемент на странице с помощью заданного локатора
EXAMPLE2 = driver.find_element(*EXAMPLE2_LOCATOR)
# Прокручиваем страницу к элементу
scrolls.scroll_to_element(EXAMPLE2)

