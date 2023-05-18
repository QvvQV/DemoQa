from pages.hero_page import Hero_app
from pages.add_remove_element import Add_element
import time

def test_btn_add(browser):
    h_p = Hero_app(browser)
    a_remove_e = Add_element(browser)

    h_p.visit()
    assert h_p.add.get_text() == 'Add/Remove Elements'
    h_p.add.click()

    assert a_remove_e.add_element.get_text() == 'Add Element'
    assert a_remove_e.add_element.get_dom_attribute('onclick') =='addElement()'

    for i in range(4):
        a_remove_e.add_element.click()
        time.sleep(1)

    assert a_remove_e.delete.check_count_elements(4)

#проверка для всех элементов
    for element in a_remove_e.delete.find_elements():
        assert element.text == 'Delete'

    #проверка только для первого элемента
    assert a_remove_e.delete.get_text() == 'Delete'

    #While кликнуть на каждую кнопку Delete
    while a_remove_e.delete.exist():
        a_remove_e.delete.click()

    assert not a_remove_e.delete.exist()




