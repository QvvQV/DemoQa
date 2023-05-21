import pytest

from pages.demoqa import DemoQa
from pages.alert_page import Alert
from pages.accordion import Accordion
from pages.browser_page import Browser #BrowserTab

@pytest.mark.parametrize('pages', [Accordion, Alert, DemoQa, Browser])
def test_seo_meta(browser, pages):
    page = pages(browser)

    page.visit()
    assert page.metaView.get_dom_attribute('name') == 'viewport'
    assert page.metaView.get_dom_attribute('content') == 'width=device-width,initial-scale=1'