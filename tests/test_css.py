from pages.text_box import TextBox

def test_style(browser):
    t_b = TextBox(browser)

    t_b.visit()
    assert t_b.submit_click.check_css('color', 'rgba(255, 255, 255, 1)')

    assert t_b.submit_click.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert t_b.submit_click.check_css('borderColor', 'rgb(0, 123, 255)')