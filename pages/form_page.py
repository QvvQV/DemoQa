from pages.base_page import BasePage
from components.components import WebElement

class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.user_email = WebElement(driver, "#userEmail")
        self.gender_radio_1 = WebElement(driver, "#gender-radio-1")
        self.user_number = WebElement(driver, "#userNumber")
        self.btn_submit = WebElement(driver, "#submit")
        self.modal_dialog = WebElement(driver, "body > div.fade.modal.show > div")
        self.close_modal = WebElement(driver, "#closeLargeModal")
        self.hobbies = WebElement(driver, '#hobbies-checkbox-2')
        self.address = WebElement(driver, '#currentAddress')
        self.btn_close_modal= WebElement(driver, '#submit')
        self.validate = WebElement(driver, '#userForm')
        #self.strelka = WebElement(driver, '#state > div > div.css-1wy0on6 > div > svg > path')
       # self.state = WebElement(driver, '//*[@id="state"]/div/div[1]/div[1]')
        #self.statecity = WebElement (driver, '#stateCity-wrapper > div:nth-child(2)')
        #self.state = WebElement(driver, "//*[contains(@text, 'NCR')]")

        self.state = WebElement(driver, '//option[contains(text(),"NCR"]')
        self.strelka = WebElement(driver, '//*[@id="state"]/div/div[2]/div')

        #self.state = WebElement(driver, '//*[contains(@class, 'point_info') and contains(string(), 'Краснодар')]')

