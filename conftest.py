import os
from datetime import datetime

import pytest_html
from selenium import webdriver
import pytest

# Update: 'items' is now 'cells' in the latest versions
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.pop()

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{getattr(report, 'description', '')}</td>")
    cells.pop()
# This hook allows us to modify the HTML report table
# @pytest.hookimpl(optionalhook=True)
# def pytest_html_results_table_header(items):
#     items.insert(2, "<th>Description</th>")
#     items.pop()


# @pytest.hookimpl(optionalhook=True)
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, f"<td>{getattr(report, 'description', '')}</td>")
#     cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Create screenshot directory
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%H%M%S')}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(file_path)

            # Embed screenshot into the HTML report
            if file_path:
                html = '<div><img src="screenshots/%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

@pytest.fixture(scope="function")
def driver(request):
    """Setup and teardown for the WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    # This line allows the 'request' to pass the driver back to the hook below
    request.node.driver = driver

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture a screenshot if a test fails.
    """
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # We only look at the 'call' phase (the actual test execution)
    if rep.when == "call" and rep.failed:
        try:
            # Retrieve the driver from the test item
            driver = item.funcargs['driver']

            # Create a folder for screenshots if it doesn't exist
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # Generate a unique filename using test name and timestamp
            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"\n[FAILURE] Screenshot saved to: {file_path}")

        except Exception as e:
            print(f"\n[ERROR] Failed to capture screenshot: {e}")