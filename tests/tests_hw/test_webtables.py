import time

from pages.webtables import Webtables


def test_form(browser):
    webtables_page = Webtables(browser)

    webtables_page.visit()
    webtables_page.btn_add.click()
    time.sleep(1)
    assert webtables_page.regist_form.exist()
    assert not webtables_page.btn_dialog_submit.click()
    time.sleep(2)

#заполнение формы
    webtables_page.first_name.send_keys('Tester')
    webtables_page.last_name.send_keys('Tosterov')
    webtables_page.email.send_keys('ad@look.ru')
    webtables_page.age.send_keys('31')
    webtables_page.salary.send_keys('75000')
    webtables_page.departament.send_keys('tester')
    webtables_page.btn_dialog_submit.click()
    assert not webtables_page.regist_form.exist()
    time.sleep(2)
    assert webtables_page.new_pole.exist()

#работа с оформленной записью
    webtables_page.btn_karandash.click()
    assert webtables_page.pole_s_dannimi.exist()
    webtables_page.first_name.clear()
    webtables_page.first_name.send_keys('Toster')
    webtables_page.btn_dialog_submit.click()
    time.sleep(2)
    assert webtables_page.new_pole.get_text() == 'Toster'
    webtables_page.btn_delete.click()
    time.sleep(2)

    #проверка на пустое поле
    assert webtables_page.new_pole.get_text() == ' '

