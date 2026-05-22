from selenium.webdriver.common.by import By

class LoginLocators:
    #USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    USERNAME_FIELD = (By.ID, "user-name")
    #PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    SETTING_BUTTON = (By.XPATH, "//div[@class='bm-burger-button']")
    LOGIN_BOX = (By.XPATH, "//div[@id='login_button_container']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot login info?")
    REGISTRATION_LINK = (By.LINK_TEXT, "Register")