from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Login Page url is not correct"

    def should_be_login_form(self):
        # проверка наличия формы входа в личный кабинет
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        password_input.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONF_PASS)
        password_confirm.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        btn.click()
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
