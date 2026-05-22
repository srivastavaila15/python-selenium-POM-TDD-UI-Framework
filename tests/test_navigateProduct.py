import pytest

from Base import BasePage
import json
import os
from locators import navigateProductLocator
from locators.loginLocators import LoginLocators
from locators.navigateProductLocator import NavigateProductLocator
from utilities.excelReader import get_excel_data
from pages.navigateProduct_Page import NavigateProductPage


def load_env_config():
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "..", "utilities", "config.json")
    with open(config_path, "r") as file:
        return json.load(file)


class test_navigateProduct:

    # 2. Demonstrating Excel expertise by driving the purchase datasets
    @pytest.mark.parametrize("TestCase ID, ProductName, ProductID, Quantity", get_excel_data("PurchaseSheet"))
    def test_purchase_workflow(self, setup, scenario_id, product_name, product_id, qty, expected):
        driver = setup
        config = load_env_config()

        # Navigate to the URL fetched via JSON config
        driver.get(config["base_url"])

        product_page = NavigateProductPage(driver)

        # Execute workflow using data fetched via Excel
        product_page.search_product(product_name)
        product_page.verify_product_id(product_id)
        product_page.add_to_cart(qty)
        product_page.proceed_to_checkout()

        # TDD Verification / Assertion
        #assert product_page.get_transaction_status() == expected



