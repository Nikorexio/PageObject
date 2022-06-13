from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not login window"

    def should_be_login_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except (NoSuchElementException):
            assert False, "There is no login form"
        assert True

    def should_be_register_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        except (NoSuchElementException):
            assert False, "There is no registration form"
        assert True
