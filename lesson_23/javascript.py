from selenium import webdriver
from selenium.webdriver import ActionChains
from scrolls import Scrolls

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Создаем сервис для Chrome
service = webdriver.ChromeService()
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)
# Создаем объект ActionChains для выполнения действий с элементами на странице
actions = ActionChains(driver)
# Инициализируем класс Scrolls с драйвером и действиями
scrolls = Scrolls(driver, actions)

# Открываем целевую страницу
driver.get("https://seiyria.com/bootstrap-slider/")
# Локатор элемента
EXAMPLE2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
# Находим элемент на странице с помощью заданного локатора
EXAMPLE2 = driver.find_element(*EXAMPLE2_LOCATOR)
# Прокручиваем страницу к элементу
scrolls.scroll_to_element(EXAMPLE2)

