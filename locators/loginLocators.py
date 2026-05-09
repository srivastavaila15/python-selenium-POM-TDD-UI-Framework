from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot login info?")
    REGISTRATION_LINK = (By.LINK_TEXT, "Register")