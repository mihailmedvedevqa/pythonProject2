class Scrolls:

    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions

    def scroll_by(self, x, y):  # Scroll по x и y
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):  # Scroll в самый низ страницы
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):  # Scroll на самый верх страницы
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, element):  # Scroll к элементу с раскрытием контента под ним
        self.actions.scroll_to_element(element).perform()
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 700,
        });
        """)
