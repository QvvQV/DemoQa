import time

from pages.saucedemo import Login
from pages.saucedemo_korzina import Korzina


def test_korzina(browser):
    saucedemo_page = Login(browser)
    saucedemo_korzina = Korzina(browser)

    saucedemo_page.visit()
    saucedemo_page.Username.send_keys('standard_user')
    saucedemo_page.Password.send_keys('secret_sauce')
    saucedemo_page.btn_login.click()

    saucedemo_korzina.visit()
    saucedemo_korzina.btn_add_bag.click()
    saucedemo_korzina.btn_add_Tshirt.click()
    saucedemo_korzina.btn_korzina.click()
    assert saucedemo_korzina.bag.exist()
    assert saucedemo_korzina.Tshirt.exist()
    saucedemo_korzina.btn_delete_bag.click()
    saucedemo_korzina.btn_delete_Tsirt.click()
    assert not saucedemo_korzina.bag.exist()
    assert not saucedemo_korzina.Tshirt.exist()

def test_sohr_tovara(browser):
    saucedemo_page = Login(browser)
    saucedemo_korzina = Korzina(browser)

    saucedemo_page.visit()
    saucedemo_page.Username.send_keys('standard_user')
    saucedemo_page.Password.send_keys('secret_sauce')
    saucedemo_page.btn_login.click()

    saucedemo_korzina.btn_add_Tshirt.click()
    saucedemo_korzina.btn_add_bag.click()
    saucedemo_korzina.menu.click()
    time.sleep(2)
    saucedemo_korzina.logout.click()

    saucedemo_page.Username.send_keys('standard_user')
    saucedemo_page.Password.send_keys('secret_sauce')
    saucedemo_page.btn_login.click()
    time.sleep(2)

    saucedemo_korzina.btn_korzina.click()
    time.sleep(2)
    assert saucedemo_korzina.bag.exist()
    assert saucedemo_korzina.Tshirt.exist()