import time

import pytest

from pages.modal_page import Modal

#@pytest.mark.skipif(True, reason='просто пропуск')
def test_check_modal(browser, request):
    check_mod = Modal(browser)

    if not check_mod.request(): # функция request закинута в base_page
        pytest.skip(reason=f'Страница {check_mod.base_url} недоступна')
    check_mod.visit()

    assert not check_mod.alert()
    check_mod.btn_small.click()
    time.sleep(2)
    assert check_mod.title_sm.get_text() == 'Small Modal'
    time.sleep(2)
    check_mod.btn_small_close.click()


    assert not check_mod.alert()
    check_mod.btn_large.click()
    time.sleep(2)
    assert check_mod.title_lr.get_text() == 'Large Modal'
    check_mod.btn_large_close.click()
    time.sleep(2)
    assert not check_mod.alert()
