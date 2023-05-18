import time

from pages.webtables import Webtables

def test_web_dop(browser):
    webtables_page = Webtables(browser)

    webtables_page.visit()
    webtables_page.five_row.click()
    time.sleep(2)

    assert not webtables_page.btn_next.click()
    assert webtables_page.btn_next.get_dom_attribute('disabled')
    assert not webtables_page.btn_previous.click()
    assert webtables_page.btn_previous.get_dom_attribute('disabled')

    #добавление первой записи
    for i in range (3):
        webtables_page.btn_add.click()
        time.sleep(1)


        # заполнение формы
        webtables_page.first_name.send_keys('Tester')
        webtables_page.last_name.send_keys('Tosterov')
        webtables_page.email.send_keys('ad@look.ru')
        webtables_page.age.send_keys('31')
        webtables_page.salary.send_keys('75000')
        webtables_page.departament.send_keys('tester')
        webtables_page.btn_dialog_submit.click()
        time.sleep(2)

    assert not webtables_page.btn_next.get_dom_attribute('disabled')
    assert webtables_page.page_all.get_text() == '2'

    webtables_page.btn_next.click()
    assert webtables_page.page2.get_dom_attribute('value') == '2'
    time.sleep(2)
    webtables_page.btn_previous.click()
    time.sleep(2)
    assert webtables_page.page2.get_dom_attribute('value') == '1'
