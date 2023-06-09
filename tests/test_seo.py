import pytest

from pages.demoqa import DemoQa
from pages.alert_page import Alert
from pages.accordion import Accordion
from pages.browser_page import Browser #BrowserTab

@pytest.mark.parametrize('pages', [Accordion, Alert, DemoQa, Browser])
def test_seo(browser, pages):
    page = pages(browser)
    #demo_qa_page = DemoQa(browser)

    page.visit()
    assert page.get_title() == page.pageData['title']