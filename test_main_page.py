import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(page.browser, page.browser.current_url)
    basket_page.message_empty_basket()
    basket_page.should_not_be_products_in_basket()

@pytest.mark.login_state
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
         pass
         # реализация теста

    def test_guest_should_see_login_link(self, browser):
         pass
         # реализация теста