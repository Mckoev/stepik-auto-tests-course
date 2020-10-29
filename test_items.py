import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_a_button_to_add_a_product_to_the_cart(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector(".btn-primary") != 0