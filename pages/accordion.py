from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.text_element = WebElement(driver, '#section1Content > p')
        self.btn_sidebar = WebElement(driver,'#section1Heading')

        self.btn_sidebar2 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.btn_sidebar3 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.btn_sidebar4 = WebElement(driver, '#section3Content > p')

