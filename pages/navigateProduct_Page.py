from Base import BasePage
from selenium.webdriver.common.by import By
from locators.loginLocators import LoginLocators
from locators.navigateProductLocator import NavigateProductLocator

class NavigateProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()
        self.locators = NavigateProductLocator()

    def search_product(self, ProductName):
        raw_xpath = NavigateProductLocator.PRODUCT_NAME_XPATH
        dynamic_xpath = raw_xpath.format(ProductName)
        dynamic_locator = (By.XPATH, dynamic_xpath)
        self.driver.find_element(By.XPATH, dynamic_locator).click()


    def verify_product_id(self, product_id):
        pass

    def add_to_cart(self, quantity):
        pass

    def proceed_to_checkout(self):
        pass


