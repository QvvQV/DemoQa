from pages.demoqa import DemoQa


def test_seo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.get_title() == demo_qa_page.pageData['title']