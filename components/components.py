from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class WebElement:

    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def get_text(self):
        str(self.find_element().text)

    def exist(self):
        try:
            self.find_element() #locator='#app>header>a'
        except NoSuchElementException:
            return False
        return True

