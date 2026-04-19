"""
Wait utilities for the Selenium Framework
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utilities.logger import get_logger

logger = get_logger(__name__)

class WaitUtils:
    """Utility class for wait operations"""
    
    def __init__(self, driver, timeout=10):
        """
        Initialize WaitUtils
        
        Args:
            driver: WebDriver instance
            timeout: Wait timeout in seconds
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout
    
    def wait_for_element_visible(self, locator, timeout=None):
        """
        Wait for element to be visible
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            timeout: Custom timeout (uses default if None)
        
        Returns:
            WebElement or None
        """
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Element {locator} is visible")
            return element
        except TimeoutException:
            logger.warning(f"Element {locator} not visible after {timeout} seconds")
            return None
    
    def wait_for_element_present(self, locator, timeout=None):
        """
        Wait for element to be present in DOM
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            timeout: Custom timeout (uses default if None)
        
        Returns:
            WebElement or None
        """
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            logger.info(f"Element {locator} is present")
            return element
        except TimeoutException:
            logger.warning(f"Element {locator} not present after {timeout} seconds")
            return None
    
    def wait_for_element_clickable(self, locator, timeout=None):
        """
        Wait for element to be clickable
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            timeout: Custom timeout (uses default if None)
        
        Returns:
            WebElement or None
        """
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            logger.info(f"Element {locator} is clickable")
            return element
        except TimeoutException:
            logger.warning(f"Element {locator} not clickable after {timeout} seconds")
            return None
    
    def wait_for_element_invisible(self, locator, timeout=None):
        """
        Wait for element to be invisible
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            timeout: Custom timeout (uses default if None)
        
        Returns:
            Boolean
        """
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            logger.info(f"Element {locator} is invisible")
            return True
        except TimeoutException:
            logger.warning(f"Element {locator} still visible after {timeout} seconds")
            return False
    
    def wait_for_url_contains(self, partial_url, timeout=None):
        """
        Wait for URL to contain specific text
        
        Args:
            partial_url: String that should appear in URL
            timeout: Custom timeout (uses default if None)
        
        Returns:
            Boolean
        """
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(partial_url)
            )
            logger.info(f"URL contains '{partial_url}'")
            return True
        except TimeoutException:
            logger.warning(f"URL does not contain '{partial_url}' after {timeout} seconds")
            return False
    
    def wait_for_title_contains(self, title, timeout=None):
        """
        Wait for page title to contain specific text
        
        Args:
            title: String that should appear in title
            timeout: Custom timeout (uses default if None)
        
        Returns:
            Boolean
        """
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.title_contains(title)
            )
            logger.info(f"Title contains '{title}'")
            return True
        except TimeoutException:
            logger.warning(f"Title does not contain '{title}' after {timeout} seconds")
            return False
