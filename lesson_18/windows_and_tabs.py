from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Создаем объект Options для настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера
# Устанавливаем ChromeDriver через менеджер и создаем сервис
service = Service(ChromeDriverManager().install())
# Инициализируем веб-драйвер для Chrome с заданными сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Переключение между вкладками

# Вариант 1

# Локатор элемента
FOR_BUSINESS_BUTTON = ("xpath", "//a[text()=' For Business ']")
# Базовая страница
driver.get("https://hyperskill.org/login")
# Записали дескриптор текущей вкладки в переменную для будущего сравнения
main_tab = driver.current_window_handle
# Клик по кнопке, которая открывает новую вкладку
driver.find_element(*FOR_BUSINESS_BUTTON).click()
# Получаем список дескрипторов используя параметр window_handles
list_of_tabs = driver.window_handles
# Переключились по индексу на новую вкладку
driver.switch_to.window(list_of_tabs[1])
# Записали дескриптор новой вкладки в переменную
second_tab = driver.current_window_handle
# Убедились, что дескриптор сменился и отличается от изначального
assert second_tab != main_tab, "Ошибка переключения между вкладками"
# Пробуем кликнуть на элемент, который находиться на новой вкладке
START_FOR_FREE_BUTTON = ("xpath", "(//a[contains(@class, 'button-secondary')])[1]")
driver.find_element(*START_FOR_FREE_BUTTON).click()

# Вариант 2

# Базовая страница
driver.get("https://whatismyipaddress.com/")
# Открытие нескольких вкладок
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
# Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows))  # Выведем на экран кол-во открытых вкладок
# Записали дескриптор текущей вкладки в переменную для будущего сравнения
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print("Индекс: ", windows.index(current_tab))  # Получаем индекс вкладки в списке для информативности
# Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
# Проверка, что вкладка переключилась
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"

# Переключение между окнами

# Базовая страница
driver.get("https://whatismyipaddress.com/")
# Записали дескриптор текущего окна в переменную для будущего сравнения
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)
# Открытие и переключение на новое окно
driver.switch_to.new_window("window")
# Получение дескриптора нового окна
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)
# Проверка, что окно переключилось
assert new_window != old_window, "Окно не переключилось"
# Открытие страницы в новом окне
driver.get("https://google.com")
# Переключение на старое окно
driver.switch_to.window(old_window)
# Проверка, что переключились на старое окно
assert old_window == driver.current_window_handle, "Окно не переключилось"
# Открытие страницы в старом окне
driver.get("https://bing.com")
# Переключение на новое окно
driver.switch_to.window(new_window)
# Закрытие нового окна
driver.close()

