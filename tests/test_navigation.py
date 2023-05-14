import time

from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)


    demo_qa_page.visit()
    demo_qa_page.btn_elements.click
    elements_page.refresh()
    time.sleep(1)
    browser.back()
    browser.forward()
    time.sleep(1)
    elements_page.equel_url()
