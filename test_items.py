import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_presence(browser):
    browser.get(link)
    add_to_card_btn = browser.find_element_by_css_selector("button.btn-add-to-basket")
    time.sleep(5)
    assert add_to_card_btn is not None
