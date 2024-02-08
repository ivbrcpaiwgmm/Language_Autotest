import time
from selenium.webdriver.common.by import By


def test_add_to_basket_btn_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)
    assert browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket'), "Кнопки 'Добавить в корзину' на странице нет!"
    # time.sleep(10)
