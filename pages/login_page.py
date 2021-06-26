from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        pass
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Login Page url is not correct"

    def should_be_login_form(self):
        # проверка наличия формы входа в личный кабинет
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"