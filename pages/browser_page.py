from pages.base_page import BasePage
from components.components import WebElement

class Browser(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)


        self.pageData = {
            'title': 'DEMOQA'
        }
        self.btn_tab = WebElement(driver, '#tabButton')