"""
Configuration settings for the Selenium Framework
"""
import os
from enum import Enum


class Environment(Enum):
    """Environment URLs"""
    DEV = "https://dev.example.com"
    STAGING = "https://staging.ldverp.com/"
    PROD = "https://prod.example.com"


class Browser(Enum):
    """Supported browsers"""
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"


class BrowserConfig:
    """Browser configuration settings (READ ONLY)"""

    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 20

    DEFAULT_BROWSER = Browser.CHROME.value
    MAXIMIZE_WINDOW = True
    HEADLESS = False

    CHROME_OPTIONS = [
        "--no-default-browser-check",
        "--no-first-run",
        "--disable-default-apps",
        "--disable-popup-blocking",
        "--disable-notifications",
        "--disable-blink-features=AutomationControlled",
    ]

    FIREFOX_OPTIONS = [
        "--disable-popup-blocking",
        "--disable-notifications",
    ]

    EDGE_OPTIONS = [
        "--disable-blink-features=AutomationControlled",
    ]


class TestConfig:
    """Test configuration settings"""

    BASE_URL = Environment.STAGING.value

    TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "test_data")
    SCREENSHOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "screenshots")
    LOGS_PATH = os.path.join(os.path.dirname(__file__), "..", "logs")
    REPORTS_PATH = os.path.join(os.path.dirname(__file__), "..", "reports")

    REPORT_FORMAT = "html"

    SCREENSHOT_ON_FAILURE = True
    RETRY_COUNT = 0

    PARALLEL_EXECUTION = False

    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    SLOW_TEST_THRESHOLD = 30