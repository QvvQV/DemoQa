import time

from pages.modal_dialogs import modal_dialogs
from pages.demoqa import DemoQa


def test_page_dialogs(browser):
    modal_dialog_page = modal_dialogs(browser)

    modal_dialog_page.visit()
    assert modal_dialog_page.btns_first_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialog_page = modal_dialogs(browser)
    demo_qa_page = DemoQa(browser)

    modal_dialog_page.visit()
    browser.refresh()

    modal_dialog_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()
    assert demo_qa_page.equel_url()
    assert demo_qa_page.get_title() == demo_qa_page.pageData['title']
    browser.set_window_size(1000, 1000)
    time.sleep(1)

