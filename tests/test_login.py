import pytest
from selenium.webdriver.common.by import By

from pages.login_Page import LoginPage
from utilities.configReader import config # Import the config data


def test_valid_login(driver):
    login_page = LoginPage(driver)

    # Use config data instead of hardcoded strings
    driver.get(config["base_url"])
    login_page.login_to_application(config["username"], config["password"])

    #assert "overview" in driver.current_url
    assert "Test Test" in driver.find_element(By.XPATH, "//p[contains(.,'Test Test')]").text

def test_failing_example(driver):
    driver.get(config["base_url"])
    # This will fail and trigger the screenshot
    assert "Wrong Title" in driver.title
    #assert "ParaBank | Welcome | Online Banking" in driver.title