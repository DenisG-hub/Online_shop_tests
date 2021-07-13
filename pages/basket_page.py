from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def message_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY), "No empty basket message"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_BUTTON), \
           "Products is in basket"
