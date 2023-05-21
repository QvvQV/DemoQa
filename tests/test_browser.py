import time

from pages.browser_page import Browser
from pages.link_page import Link
from pages.demoqa import DemoQa

def test_browser(browser):
    d_brow = Browser(browser)

    d_brow.visit()
    assert len(browser.window_handles) == 1 #открытие новой вкладки
    d_brow.btn_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0]) #переход от одной вкладке к другой
    time.sleep(2)

def test_home(browser):
    d_home = Link(browser)
    d_demo = DemoQa(browser)

    d_home.visit()
    assert len(browser.window_handles) == 1
    assert d_home.btn_home.get_text() == 'Home'
    d_home.btn_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    time.sleep(2)
    browser.switch_to.window(browser.icon.click())
    assert len(browser.window_handles) == 3

    #assert d_demo.equel_url()
    time.sleep(2)

