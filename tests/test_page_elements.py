from pages.elements_page import ElementsPage

def test_icon_exist(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()