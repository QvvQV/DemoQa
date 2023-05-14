from pages.base_page import BasePage
from components.components import WebElement

class Login(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'

        super().__init__(driver, self.base_url)

        self.Username = WebElement(driver, '#user-name')
        self.Password = WebElement(driver, '#password')
        self.btn_login = WebElement(driver, '#login-button')
