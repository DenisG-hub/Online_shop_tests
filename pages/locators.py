from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD2CART = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:first-child")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_TITLE = (By.CSS_SELECTOR, ".page-header h1")
    PROCEED_BUTTON = (By.CSS_SELECTOR, ".btn-primary")


class LoginPageLocators():
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONF_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")
