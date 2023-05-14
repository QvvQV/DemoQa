from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.address = WebElement(driver, '#currentAddress')
        self.submit_click = WebElement(driver, '#submit')
        self.output = WebElement(driver, '#output > div')
        self.output_name = WebElement(driver, '#name')
        self.output_current = WebElement(driver, '#currentAddress')


   # def proverka_text(self):

     #   if (self.full_name == 'Cheburashka'):
       #     return False
       # return True
