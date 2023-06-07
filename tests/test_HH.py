import time

from pages.hh_page import HeadHunter

def test_HH(browser):

    wak = HeadHunter(browser) #Вакансия

    wak.visit()

    #Регистрация
    wak.na_parol.click()
    wak.parol.send_keys('c26a13e3r4')
    wak.email.send_keys('vadimgol@gmail.com')
    wak.button.click_force()
    time.sleep(2)

    # Проверка профиля и переход в избранное
    wak.profil.click()
    time.sleep(2)
    assert wak.text_elements.get_text() == 'вадим головин'
    wak.heart.click()

    time.sleep(1)
    wak.but_ot.click()

    #Проверка попадания в опросник
    time.sleep(1)
    assert wak.text_str.get_text() == 'QA Engineer (frontend)'

    #ответы на опросник
    wak.who_test.send_keys('qa - найти слабые места и устранить их. Следит за всем процессом разработки продуктов' + '\n' + 'qc - контроль качества согласно требованиям. Проверка на тестах')
    wak.target.send_keys('Проверка, все ли указанные требования выполнены' + '\n' +
                         'Создание уверенности в уровне качества объекта тестирования' + '\n' +
                         'Предотвращение дефектов' + '\n' +
                         'Обнаружение отказов и дефектов' + '\n' +
                         'Предоставление заинтересованным лицам достаточной информации, позволяющей им принять обоснованные решения (особенно в отношении уровня качества объекта тестирования)'
                         + '\n' + 'Снижение уровня риска ненадлежащего качества программного обеспечения (например, пропущенные сбои в работе)')
    wak.pismo.click()
    time.sleep(1)
    wak.pis.send_keys('Добрый день!' + '\n' +
                      'Путь до опросника и сам опросник заполнены роботом с промежуточными проверками ряда элементов на страницах' +
                      '\n' + 'Тесты писались на языке Phyton при помощи кроссплатформенной интегрированной среды разработки Pycharm' +
                      '\n' + 'с использованием инструмента для автоматизации действий веб-браузера Selenium.' + '\n' +
                      'Это сделано, чтобы привлечь ваше внимание. Ведь мною только закончены курсы в ИТМО.' + '\n' +
                      'Прилагаю ссылки кода на GitHub: https://github.com/QvvQV/DemoQa/blob/main/pages/hh_page.py, https://github.com/QvvQV/DemoQa/blob/main/tests/test_HH.py' + '\n'
                      'Надеюсь на положительный ответ, заранее спасибо')
    time.sleep(1)

    #проверка цвета кнопки и отпрака опросника
    assert wak.but_niz.check_css('backgroundColor', 'rgba(23, 133, 229, 1)')
    wak.but_niz.click()

def test_up(browser):
    wak = HeadHunter(browser)  # Вакансия

    wak.visit()

    # Регистрация
    wak.na_parol.click()
    wak.parol.send_keys('c26a130e3r4')
    wak.email.send_keys('vadimgol@gmail.com')
    wak.button.click_force()
    time.sleep(2)

    wak.my_resume.click()
    time.sleep(1)
    wak.up.click()
