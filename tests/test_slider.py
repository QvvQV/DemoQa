from pages.slider_page import Slider
from selenium.webdriver.common.keys import Keys

def test_slider(browser):
    slid = Slider(browser)

    slid.visit()
    assert slid.number.get_dom_attribute('value') == '25'

    while not slid.number.get_dom_attribute('value') == '50':
        slid.bar.send_keys(Keys.ARROW_RIGHT)

    assert slid.number.get_dom_attribute('value') == '50'