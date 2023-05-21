import time

from pages.alert_page import Alert


def test_alert(browser):
    d_a = Alert(browser)
    d_a.visit()

    assert not d_a.alert()
    d_a.btn_alert.click()
    time.sleep(2)
    assert d_a.alert()

def test_alert_text(browser):
    d_t = Alert(browser)
    d_t.visit()

    assert not d_t.alert()
    d_t.btn_alert.click()
    time.sleep(2)
    assert d_t.alert().text == 'You clicked a button'
    d_t.alert().accept()
    assert not d_t.alert()

def test_confirm(browser):
    d_conf = Alert(browser)

    d_conf.visit()
    d_conf.btn_confirm.click()
    time.sleep(2)
    d_conf.alert().dismiss()
    assert d_conf.result.get_text() == 'You selected Cancel'

def test_promt(browser):
    d_prom = Alert(browser)

    d_prom.visit()
    d_prom.btn_promt.click()
    time.sleep(2)
    d_prom.alert().send_keys('Vadim')
    d_prom.alert().accept()
    assert d_prom.promt_res.get_text() == 'You entered Vadim'
    time.sleep(2)
