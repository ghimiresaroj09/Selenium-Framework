"""
WebDriver Manager for the Selenium Framework
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
from config import BrowserConfig, Browser
from utilities.logger import get_logger

logger = get_logger(__name__)

class DriverManager:
    """Manager for WebDriver instances"""
    
    _driver = None
    
    @staticmethod
    def create_driver(browser_name=BrowserConfig.DEFAULT_BROWSER):
        """
        Create a WebDriver instance
        
        Args:
            browser_name: Name of the browser (chrome, firefox, edge)
        
        Returns:
            WebDriver: WebDriver instance
        """
        try:
            if browser_name.lower() == Browser.CHROME.value:
                driver = DriverManager._create_chrome_driver()
            elif browser_name.lower() == Browser.FIREFOX.value:
                driver = DriverManager._create_firefox_driver()
            elif browser_name.lower() == Browser.EDGE.value:
                driver = DriverManager._create_edge_driver()
            else:
                logger.warning(f"Unknown browser: {browser_name}, using Chrome")
                driver = DriverManager._create_chrome_driver()
            
            # Set implicit wait
            driver.implicitly_wait(BrowserConfig.IMPLICIT_WAIT)
            
            # Set page load timeout
            driver.set_page_load_timeout(BrowserConfig.PAGE_LOAD_TIMEOUT)
            
            # Maximize window
            if BrowserConfig.MAXIMIZE_WINDOW:
                driver.maximize_window()
            
            logger.info(f"WebDriver created successfully for {browser_name}")
            DriverManager._driver = driver
            return driver
        except Exception as e:
            logger.error(f"Failed to create WebDriver: {e}")
            raise
    
    @staticmethod
    def _create_chrome_driver():
        """Create Chrome WebDriver"""
        try:
            chrome_options = ChromeOptions()
            
            # Disable password manager
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            chrome_options.add_experimental_option("prefs", prefs)
            
            # Disable automation notification
            chrome_options.add_experimental_option(
                "excludeSwitches", ["enable-automation"]
            )
            chrome_options.add_experimental_option("useAutomationExtension", False)
            
            # Add additional options
            for option in BrowserConfig.CHROME_OPTIONS:
                chrome_options.add_argument(option)
            
            # Headless mode
            if BrowserConfig.HEADLESS:
                chrome_options.add_argument("--headless")
            
            # Create driver
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options
            )
            logger.info("Chrome WebDriver created")
            return driver
        except Exception as e:
            logger.error(f"Failed to create Chrome WebDriver: {e}")
            raise
    
    @staticmethod
    def _create_firefox_driver():
        """Create Firefox WebDriver"""
        try:
            firefox_options = FirefoxOptions()
            
            # Add additional options
            for option in BrowserConfig.FIREFOX_OPTIONS:
                firefox_options.add_argument(option)
            
            # Headless mode
            if BrowserConfig.HEADLESS:
                firefox_options.add_argument("--headless")
            
            # Create driver
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=firefox_options
            )
            logger.info("Firefox WebDriver created")
            return driver
        except Exception as e:
            logger.error(f"Failed to create Firefox WebDriver: {e}")
            raise
    
    @staticmethod
    def _create_edge_driver():
        """Create Edge WebDriver"""
        try:
            edge_options = EdgeOptions()
            
            # Add additional options
            for option in BrowserConfig.EDGE_OPTIONS:
                edge_options.add_argument(option)
            
            # Headless mode
            if BrowserConfig.HEADLESS:
                edge_options.add_argument("--headless")
            
            # Create driver
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=edge_options
            )
            logger.info("Edge WebDriver created")
            return driver
        except Exception as e:
            logger.error(f"Failed to create Edge WebDriver: {e}")
            raise
    
    @staticmethod
    def quit_driver():
        """Close and quit the WebDriver"""
        try:
            if DriverManager._driver:
                DriverManager._driver.quit()
                DriverManager._driver = None
                logger.info("WebDriver quit successfully")
        except Exception as e:
            logger.error(f"Failed to quit WebDriver: {e}")
    
    @staticmethod
    def get_driver():
        """Get the current WebDriver instance"""
        return DriverManager._driver
