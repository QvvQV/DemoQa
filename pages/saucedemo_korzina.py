from pages.base_page import BasePage
from components.components import WebElement

class Korzina(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/inventory.html'

        super().__init__(driver, self.base_url)
        self.btn_add_bag = WebElement(driver, '#add-to-cart-sauce-labs-backpack')
        self.btn_add_Tshirt = WebElement(driver, '#add-to-cart-sauce-labs-bolt-t-shirt')
        self.btn_korzina = WebElement(driver, '#shopping_cart_container > a')
        self.bag = WebElement(driver, '#item_4_title_link > div')
        self.Tshirt = WebElement(driver, '#item_1_title_link > div')
        self.btn_delete_bag = WebElement(driver,'#remove-sauce-labs-backpack')
        self.btn_delete_Tsirt = WebElement(driver, '#remove-sauce-labs-bolt-t-shirt')
        self.menu = WebElement(driver, '#react-burger-menu-btn')
        self.logout = WebElement(driver, '#logout_sidebar_link')

