import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)


# Переключение между вкладками
# Базовая страница
driver.get("https://whatismyipaddress.com/")
# Открытие нескольких вкладок
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(2)
# Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows))  # Выведем на экран кол-во открытых вкладок
# Получение дескриптора текущего окна для дальнейшей проверки
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print("Индекс: ", windows.index(current_tab))  # Получаем индекс вкладки в списке для информативности
# Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
time.sleep(2)
# Проверка, что вкладка переключилась
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"


# Переключение между окнами
# Базовая страница
driver.get("https://whatismyipaddress.com/")
# Получение дескриптора текущего окна
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)
# Открытие и переключение на новое окно
driver.switch_to.new_window("window")
# Получение дескриптора нового окна
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)
# Проверка, что окно переключилось
assert new_window != old_window, "Окно не переключилось"
time.sleep(2)
# Открытие страницы в новом окне
driver.get("https://vk.com")
# Переключение на старое окно
driver.switch_to.window(old_window)
# Проверка, что переключились на старое окно
assert old_window == driver.current_window_handle, "Окно не переключилось"
# Открытие страницы в старом окне
driver.get("https://ya.ru")
# Переключение на новое окно
driver.switch_to.window(new_window)
# Закрытие нового окна
driver.close()

