import time

from pages.droppable import Drop
from selenium.webdriver import ActionChains #перенос элементов

def test_drop (browser):
    droppable = Drop(browser)
    action_chains = ActionChains(browser)

    droppable.visit()
    assert droppable.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        droppable.drag.find_element(), #element
        droppable.drop.find_element() #target
    ).perform()

    time.sleep(1)
    assert droppable.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')

    action_chains.drag_and_drop_by_offset(
       droppable.drag.find_element(), #element
        -130, 0 #target
    ).perform()

    time.sleep(1)
    assert droppable.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
