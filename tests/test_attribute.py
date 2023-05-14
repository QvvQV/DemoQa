from pages.text_box import TextBox

def test_attribute(browser):
    text_box_pages = TextBox(browser)

    text_box_pages.visit()
    assert text_box_pages.full_name.get_dom_attribute('placeholder') == 'Full Name'