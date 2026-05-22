from selenium.webdriver.common.by import By

class NavigateProductLocator:
    PRODUCT_NAME_XPATH = (By.XPATH,"//div[@class='inventory_item_name' and contains(., '{}')]")