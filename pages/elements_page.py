from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.get_text = WebElement('Please select an item from left to start practice.')

    def equel_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    def podval_check_text(self):
        if self.get_text == 'Please select an item from left to start practice.':
            return False
        return True
