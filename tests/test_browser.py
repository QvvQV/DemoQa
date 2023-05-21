import time

from pages.browser_page import Browser

def test_browser(browser):
    d_brow = Browser(browser)

    d_brow.visit()
    assert len(browser.window_handles) == 1 #открытие новой вкладки
    d_brow.btn_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0]) #переход от одной вкладке к другой
    time.sleep(2)