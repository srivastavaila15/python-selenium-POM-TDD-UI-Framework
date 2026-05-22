from Base import BasePage
from locators.loginLocators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()

    def login_to_application(self, username, password):
        """Standard login flow using inherited BasePage methods"""
        self.type(self.locators.USERNAME_FIELD, username)
        self.type(self.locators.PASSWORD_FIELD, password)
        self.click(self.locators.LOGIN_BUTTON)

    def invalid_login_to_application(self, username, invalid_password):
        """Standard login flow using inherited BasePage methods"""
        self.type(self.locators.USERNAME_FIELD, username)
        self.type(self.locators.PASSWORD_FIELD, invalid_password)
        self.click(self.locators.LOGIN_BUTTON)

    def empty_field_login_to_application(self):
        self.click(self.locators.LOGIN_BUTTON)

    def logout_application(self):
        self.click(self.locators.SETTING_BUTTON)
        self.click(self.locators.LOGOUT_LINK)

    def navigate_to_registration(self):
        self.click(self.locators.REGISTRATION_LINK)

    def is_login_box_present(self):
        """Checks if the login box container is visible to the user."""
        return self.is_element_displayed(self.locators.LOGIN_BOX)