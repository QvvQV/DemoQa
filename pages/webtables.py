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

        self.new_pole = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.btn_karandash = WebElement(driver, '#edit-record-4 > svg')
        self.pole_s_dannimi = WebElement(driver,'body > div.fade.modal.show > div > div > div.modal-header')

        self.stroki_na_str = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.five_row = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')

        #self.btn_next = WebElement(driver, '//input[@type=''button'' and @name=''sendBtn'' and @disabled]')
        self.btn_next = WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        #self.btn_previous = WebElement(driver,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[1]/button')
        self.btn_previous = WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')




   # def is_Button_Disabled(self):
       # element = self.element.findElement(By.xpath, 'locator')
       # return element.is_enabled()
