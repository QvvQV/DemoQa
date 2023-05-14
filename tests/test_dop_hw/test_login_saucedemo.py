import time

from pages.saucedemo import Login
from components.components import WebElement

def test_logon(browser):
    saucedemo_page = Login(browser)

    saucedemo_page.visit()
    saucedemo_page.Username.send_keys('standard_user')
    saucedemo_page.Password.send_keys('secret_sauce')
    saucedemo_page.btn_login.click()
    time.sleep(2)
    assert saucedemo_page.get_url() == 'https://www.saucedemo.com/inventory.html'