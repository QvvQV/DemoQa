from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.by import By

class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement (driver, '#addNewRecordButton')
        self.regist_form = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal-header')
        self.btn_dialog_submit = WebElement(driver, '#submit')

        #заполнение полей
        self.first_name = WebElement(driver,'#firstName')
        self.btn_delete = WebElement(driver,'#delete-record-4 > svg > path')

        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.departament = WebElement(driver, '#department')

        self.new_pole = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.btn_karandash = WebElement(driver, '#edit-record-4 > svg')
        self.pole_s_dannimi = WebElement(driver,'div.modal-header')

        self.stroki_na_str = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.five_row = WebElement(driver, 'select > option:nth-child(1)')

        self.btn_next = WebElement(driver,'div.-next > button')
        self.btn_previous = WebElement(driver,'div.-previous > button')

        self.page2 = WebElement(driver, 'input[type=number]')
        self.page_all = WebElement(driver,'span.-pageInfo > span')

        self.zapis = WebElement(driver, 'div.rt-noData')

        self.DELETE = {
            'title': 'Delete'
        }
        self.btn_delete_1 = WebElement(driver, '//*[@id="delete-record-1"]/svg/path')

        self.table_fname = WebElement(driver, 'div.rt-resizable-header-content')
        self.table_lname = WebElement(driver, 'div.rt-resizable-header-content')
        self.table_age = WebElement(driver, 'div.rt-resizable-header-content')




   # def is_Button_Disabled(self):
       # element = self.element.findElement(By.xpath, 'locator')
       # return element.is_enabled()
