import time

from pages.text_box import TextBox

def test_text_box(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.full_name.send_keys('Cheburashka')
    text_box_page.address.send_keys('krokodil')
    text_box_page.submit_click.click()
    time.sleep(2)
    assert text_box_page.output_name.get_text() == 'Name:Cheburashka'
    assert text_box_page.output_current.get_text() == 'Current Address:krokodil'

