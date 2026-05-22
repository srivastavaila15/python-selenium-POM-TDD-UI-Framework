import pytest
from selenium.webdriver.common.by import By

from pages import login_Page
from pages.login_Page import LoginPage
from utilities.configReader import config # Import the config data


def test_valid_login(driver):
    login_page = LoginPage(driver)

    # Use config data instead of hardcoded strings
    driver.get(config["base_url"])
    login_page.login_to_application(config["username"], config["password"])

    #assert "overview" in driver.current_url
    assert "Swag Labs" in driver.find_element(By.XPATH, "//div[@class='app_logo' and contains(.,'Swag Labs')]").text

def test_logout_flow(driver):
    login_page = LoginPage(driver)

    # Use config data instead of hardcoded strings
    driver.get(config["base_url"])
    login_page.login_to_application(config["username"], config["password"])
    assert "Swag Labs" in driver.find_element(By.XPATH, "//div[@class='app_logo' and contains(.,'Swag Labs')]").text
    login_page.logout_application()
    assert login_page.is_login_box_present() == True

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.logout_application()
    assert login_page.is_login_box_present() == True

def test_invalid_login(driver):
    login_page = LoginPage(driver)

    # Use config data instead of hardcoded strings
    driver.get(config["base_url"])
    login_page.invalid_login_to_application(config["username"], config["invalid_password"])

    #assert "overview" in driver.current_url
    assert "Epic sadface: Username and password do not match any user in this service" in driver.find_element(By.XPATH, "//h3[contains(.,'Epic sadface: Username and password do not match any user in this service')]").text

def empty_field_login(driver):
    login_page = LoginPage(driver)
    driver.get(config["base_url"])
    login_page.empty_field_login_to_application()
    assert "Epic sadface: Username is required" in driver.find_element(By.XPATH, "//h3[contains(.,'Epic sadface: Username is required')]")

def test_failing_example(driver):
    driver.get(config["base_url"])
    # This will fail and trigger the screenshot
    assert not "Wrong Title" in driver.title
