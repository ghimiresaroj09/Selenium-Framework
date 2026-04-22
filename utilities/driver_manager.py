"""
WebDriver Manager for Selenium Framework
Thread-safe, CI/CD-ready implementation using Selenium Manager (Selenium 4.15.2)
"""

import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from config import BrowserConfig, Browser
from utilities.logger import get_logger

logger = get_logger(__name__)

_thread_local = threading.local()


class DriverManager:
    """
    Thread-safe WebDriver manager using Selenium Manager (no driver binaries required).
    Designed for pytest-xdist + CI/CD pipelines.
    """

    # ----------------------------------------------------------------------
    # Public API
    # ----------------------------------------------------------------------

    @staticmethod
    def create_driver(browser_name: str = BrowserConfig.DEFAULT_BROWSER, headless: bool = None) -> webdriver.Remote:
        browser = browser_name.strip().lower()

        creators = {
            Browser.CHROME.value: DriverManager._create_chrome_driver,
            Browser.FIREFOX.value: DriverManager._create_firefox_driver,
            Browser.EDGE.value: DriverManager._create_edge_driver,
        }

        creator = creators.get(browser)

        if not creator:
            logger.warning(
                "Unsupported browser '%s'. Falling back to Chrome.",
                browser_name
            )
            creator = DriverManager._create_chrome_driver
            browser = Browser.CHROME.value

        driver = creator(headless=headless)
        DriverManager._configure_driver(driver)

        _thread_local.driver = driver

        logger.info(
            "WebDriver created | browser=%s | headless=%s | thread=%s",
            browser,
            headless if headless is not None else BrowserConfig.HEADLESS,
            threading.current_thread().name
        )

        return driver

    @staticmethod
    def get_driver() -> webdriver.Remote:
        return getattr(_thread_local, "driver", None)

    @staticmethod
    def quit_driver() -> None:
        driver = getattr(_thread_local, "driver", None)

        if not driver:
            return

        try:
            driver.quit()
            logger.info(
                "WebDriver quit | thread=%s",
                threading.current_thread().name
            )
        except Exception as exc:
            logger.error("Error quitting driver: %s", exc)
        finally:
            _thread_local.driver = None

    # ----------------------------------------------------------------------
    # Configuration
    # ----------------------------------------------------------------------

    @staticmethod
    def _configure_driver(driver: webdriver.Remote) -> None:
        driver.implicitly_wait(BrowserConfig.IMPLICIT_WAIT)
        driver.set_page_load_timeout(BrowserConfig.PAGE_LOAD_TIMEOUT)

        if BrowserConfig.MAXIMIZE_WINDOW:
            driver.maximize_window()

    # ----------------------------------------------------------------------
    # Chrome
    # ----------------------------------------------------------------------

    @staticmethod
    def _create_chrome_driver(headless: bool = None) -> webdriver.Chrome:
        options = ChromeOptions()

        # Disable password manager
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        })

        # Automation flags
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")

        if headless is None:
            headless = BrowserConfig.HEADLESS
        
        if headless:
            options.add_argument("--headless=new")

        for arg in BrowserConfig.CHROME_OPTIONS:
            options.add_argument(arg)

        driver = webdriver.Chrome(options=options)  # Selenium Manager handles driver

        DriverManager._apply_stealth(driver)

        return driver

    # ----------------------------------------------------------------------
    # Firefox
    # ----------------------------------------------------------------------

    @staticmethod
    def _create_firefox_driver(headless: bool = None) -> webdriver.Firefox:
        options = FirefoxOptions()

        if headless is None:
            headless = BrowserConfig.HEADLESS
        
        if headless:
            options.add_argument("--headless")

        for arg in BrowserConfig.FIREFOX_OPTIONS:
            options.add_argument(arg)

        return webdriver.Firefox(options=options)  # Selenium Manager handles driver

    # ----------------------------------------------------------------------
    # Edge
    # ----------------------------------------------------------------------

    @staticmethod
    def _create_edge_driver(headless: bool = None) -> webdriver.Edge:
        options = EdgeOptions()

        if headless is None:
            headless = BrowserConfig.HEADLESS
        
        if headless:
            options.add_argument("--headless=new")

        # Stability flags
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Automation detection reduction (best-effort)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # Disable password manager
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        })

        for arg in BrowserConfig.EDGE_OPTIONS:
            options.add_argument(arg)

        driver = webdriver.Edge(options=options)  # Selenium Manager handles driver

        DriverManager._apply_stealth(driver)

        return driver

    # ----------------------------------------------------------------------
    # Stealth helper (Chromium only)
    # ----------------------------------------------------------------------

    @staticmethod
    def _apply_stealth(driver: webdriver.Remote) -> None:
        """
        Best-effort removal of automation flags.
        Only applies to Chromium-based browsers.
        """
        try:
            driver.execute_cdp_cmd(
                "Page.addScriptToEvaluateOnNewDocument",
                {
                    "source": """
                        Object.defineProperty(navigator, 'webdriver', {
                            get: () => undefined
                        });
                    """
                }
            )
        except Exception:
            # Firefox does not support CDP
            pass