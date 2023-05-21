from pages.base_page import BasePage
from components.components import WebElement


class Modal(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_small = WebElement(driver,'#showSmallModal')
        self.btn_small_close = WebElement(driver, '#closeSmallModal')
        self.btn_large = WebElement(driver,'#showLargeModal')
        self.btn_large_close = WebElement(driver, '#closeLargeModal')
        self.title_sm = WebElement(driver, '#example-modal-sizes-title-sm')
        self.title_lr = WebElement(driver, '#example-modal-sizes-title-lg')

