from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD2CART)
        link.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Adding message is not found"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not present"

        product_name = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME)[0].text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "No product name in the message"


    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Basket total price is not present"

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        busket_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text

        assert product_price in busket_message, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
