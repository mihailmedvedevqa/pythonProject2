import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Browser options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless") # Headless mode
# chrome_options.add_argument("--incognito") # Incognito mode
# chrome_options.add_argument("--ignore-certificate-errors") # Ignore certificate errors
# chrome_options.add_argument("--window-size=700,700") # Browser window size
# chrome_options.add_argument("--disable-cache") # Disable cache

# chrome_options.page_load_strategy = "normal"
# chrome_options.page_load_strategy = "eager"
# chrome_options.page_load_strategy = "none"

# Driver initialization
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.set_window_size(700, 700)

start_time = time.time()
driver.get("https://whatismyipaddress.com/")
end_time = time.time()
result = end_time - start_time
print(result)
