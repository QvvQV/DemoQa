from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equel_url()
    #assert demo_qa_page.podval_check_text()
    demo_qa_page.btn_elements.click()
    elements_page.visit()
    elements_page.equel_url
   # assert elements_page.podval_check_text()


def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'

