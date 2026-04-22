"""
Pytest configuration and fixtures for Selenium Framework
"""

import pytest
from utilities.driver_manager import DriverManager
from utilities.logger import get_logger
from dotenv import load_dotenv
import sys
import os

# Load environment variables from .env file
load_dotenv()

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logger = get_logger(__name__)


# -------------------------
# CLI OPTIONS
# -------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome, firefox, edge"
    )

    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Run tests in headless mode (true/false)"
    )


# -------------------------
# CONFIG FIXTURE (CLEAN)
# -------------------------
@pytest.fixture(scope="session")
def test_config(request):
    return {
        "browser": request.config.getoption("--browser").lower(),
        "headless": request.config.getoption("--headless").lower() in ("true", "1", "yes")
    }


# -------------------------
# DRIVER FIXTURE
# -------------------------
@pytest.fixture()
def driver(test_config):

    driver = DriverManager.create_driver(
        browser_name=test_config["browser"],
        headless=test_config["headless"]
    )

    logger.info(f"Driver started: {test_config['browser']} | headless={test_config['headless']}")

    yield driver

    DriverManager.quit_driver()
    logger.info("Driver closed")


# -------------------------
# PYTEST HOOKS
# -------------------------
def pytest_configure(config):
    logger.info("Pytest configuration initialized")


def pytest_sessionstart(session):
    logger.info("Test session started")


def pytest_sessionfinish(session, exitstatus):
    logger.info("Test session finished")


# -------------------------
# FAILURE HOOK (IMPORTANT)
# -------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Only act on test execution phase
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            try:
                screenshot_path = f"screenshots/{item.name}.png"
                driver.save_screenshot(screenshot_path)
                logger.error(f"Screenshot saved: {screenshot_path}")
            except Exception as e:
                logger.error(f"Failed to capture screenshot: {e}")
