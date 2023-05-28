import time

from pages.progress_page import Progress
from selenium.webdriver.common.keys import Keys

def test_slider(browser):
    prog = Progress(browser)

    prog.visit()
    time.sleep(2)
    prog.btn.click()

    while True:
        if prog.progress.get_dom_attribute('aria-valuenow') == '51':
            prog.btn.click()
        break

    time.sleep(2)
