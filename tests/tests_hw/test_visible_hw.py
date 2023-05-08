from pages.accordion import Accordion
import time


def test_visible(browser):
    accordion_pages = Accordion(browser)
    accordion_pages.visit()
    assert accordion_pages.text_element.visible()
    accordion_pages.btn_sidebar.click()
    time.sleep(2)
    assert not accordion_pages.text_element.visible()

def test_visible_accordion_default(browser):
    accordion_pages = Accordion(browser)
    accordion_pages.visit()
    assert not accordion_pages.btn_sidebar2.visible()
    time.sleep(2)
    assert not accordion_pages.btn_sidebar3.visible()
    time.sleep(1)
    assert not accordion_pages.btn_sidebar4.visible()
