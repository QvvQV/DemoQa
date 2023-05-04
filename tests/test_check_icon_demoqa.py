#from selenium import webdriver
from pages.demoqa import DemoQa

def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equel_url()
    assert demo_qa_page.icon.exist()


#browser.get('https://demoqa.com/')

# поиск элемента
#icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
#if icon is None:
#    print('Элемент не найден')
#else:
  #  print('Элемент найден')