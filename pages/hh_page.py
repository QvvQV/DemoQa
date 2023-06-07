from pages.base_page import BasePage
from components.components import WebElement

class HeadHunter(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://spb.hh.ru/account/login?backurl=%2F&hhtmFrom=main'
        super().__init__(driver,self.base_url)

        #Регистрция
        self.na_parol = WebElement(driver, 'div.account-login-actions > button.bloko-link.bloko-link_pseudo')
        self.email = WebElement(driver,'form > div.bloko-form-item > fieldset > input')
        self.parol = WebElement(driver, 'div:nth-child(9) > fieldset > input')
        self.button = WebElement(driver, '#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div > div > div > div:nth-child(1) > div.account-login-tile-content-wrapper > div > form > div.bloko-form-row > div > button.bloko-button.bloko-button_kind-primary')

#Страница после регистрации
        self.heart = WebElement(driver, 'div.supernova-icon-dynamic > a > span')
        self.profil = WebElement(driver, '#HH-React-Root > div > div.supernova-navi-search-wrapper.supernova-navi-search-wrapper_expanded > div.supernova-navi-wrapper > div > div > div > div:nth-child(11) > div > div.supernova-dropdown-anchor > div > button > span')
        self.text_elements = WebElement(driver, 'body > div.bloko-drop.bloko-drop_menu.bloko-drop_theme-light.bloko-drop_layer-overlay.bloko-drop_flexible.bloko-drop_bottom.bloko-drop_clickable.bloko-drop_done-enter > div > div > div.supernova-dropdown > div:nth-child(1) > a > span')

        #Вакансия
        self.jun_qa = WebElement(driver, '#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_m-8.bloko-column_l-11 > div:nth-child(2) > div > div:nth-child(3) > div > div.vacancy-serp-item-body > div > div:nth-child(1) > h3 > span > a')
        self.otcklick = WebElement(driver,'#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div > div > div > div:nth-child(1) > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div > div.noprint > div:nth-child(3) > div > div > a')

        #заполнение тест вопросов
        self.text_str = WebElement(driver, '#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-16 > h3 > a')
        self.but_ot = WebElement(driver,'#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_m-8.bloko-column_l-11 > div:nth-child(2) > div > div:nth-child(3) > div > div.serp-item-controls > a')
        self.who_test = WebElement(driver, '#RESPONSE_MODAL_FORM_ID > div:nth-child(10) > div.bloko-form-item-baseline > textarea')
        self.target = WebElement(driver, '#RESPONSE_MODAL_FORM_ID > div:nth-child(11) > div.bloko-form-item-baseline > textarea')
        self.pismo = WebElement(driver, '#RESPONSE_MODAL_FORM_ID > div.vacancy-response-popup-body > div.bloko-form-row > div.vacancy-response-popup-letter > button')
        self.pis = WebElement(driver, 'div.bloko-form-row > textarea')
        self.but_niz = WebElement(driver, '#RESPONSE_MODAL_FORM_ID > div.vacancy-response-popup-body > div.bloko-gap.bloko-gap_top > button')




