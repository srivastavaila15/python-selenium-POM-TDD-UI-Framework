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

    def navigate_to_registration(self):
        self.click(self.locators.REGISTRATION_LINK)