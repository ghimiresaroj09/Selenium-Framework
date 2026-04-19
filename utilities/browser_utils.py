"""
Browser utility for the Selenium Framework
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

logger = get_logger(__name__)

class BrowserUtils:
    """Utility class for browser operations"""
    
    def __init__(self, driver):
        """
        Initialize BrowserUtils
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
    
    def get_page_title(self):
        """
        Get the current page title
        
        Returns:
            str: Page title
        """
        try:
            title = self.driver.title
            logger.info(f"Page title: {title}")
            return title
        except Exception as e:
            logger.error(f"Failed to get page title: {e}")
            return None
    
    def get_current_url(self):
        """
        Get the current page URL
        
        Returns:
            str: Current URL
        """
        try:
            url = self.driver.current_url
            logger.info(f"Current URL: {url}")
            return url
        except Exception as e:
            logger.error(f"Failed to get current URL: {e}")
            return None
    
    def navigate_to(self, url):
        """
        Navigate to a URL
        
        Args:
            url: URL to navigate to
        """
        try:
            self.driver.get(url)
            logger.info(f"Navigated to: {url}")
        except Exception as e:
            logger.error(f"Failed to navigate to {url}: {e}")
    
    def go_back(self):
        """Go back to previous page"""
        try:
            self.driver.back()
            logger.info("Went back to previous page")
        except Exception as e:
            logger.error(f"Failed to go back: {e}")
    
    def go_forward(self):
        """Go forward to next page"""
        try:
            self.driver.forward()
            logger.info("Went forward to next page")
        except Exception as e:
            logger.error(f"Failed to go forward: {e}")
    
    def refresh_page(self):
        """Refresh the current page"""
        try:
            self.driver.refresh()
            logger.info("Page refreshed")
        except Exception as e:
            logger.error(f"Failed to refresh page: {e}")
    
    def scroll_to_top(self):
        """Scroll to top of the page"""
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            logger.info("Scrolled to top")
        except Exception as e:
            logger.error(f"Failed to scroll to top: {e}")
    
    def scroll_to_bottom(self):
        """Scroll to bottom of the page"""
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            logger.info("Scrolled to bottom")
        except Exception as e:
            logger.error(f"Failed to scroll to bottom: {e}")
    
    def scroll_to_element(self, element):
        """
        Scroll to a specific element
        
        Args:
            element: WebElement to scroll to
        """
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
                element
            )
            logger.info("Scrolled to element")
        except Exception as e:
            logger.error(f"Failed to scroll to element: {e}")
    
    def get_page_source(self):
        """
        Get the current page source
        
        Returns:
            str: Page source HTML
        """
        try:
            source = self.driver.page_source
            logger.info("Retrieved page source")
            return source
        except Exception as e:
            logger.error(f"Failed to get page source: {e}")
            return None
    
    def execute_script(self, script, *args):
        """
        Execute JavaScript
        
        Args:
            script: JavaScript code to execute
            *args: Arguments to pass to the script
        
        Returns:
            Any: Result of script execution
        """
        try:
            result = self.driver.execute_script(script, *args)
            logger.info("Script executed successfully")
            return result
        except Exception as e:
            logger.error(f"Failed to execute script: {e}")
            return None
    
    def maximize_window(self):
        """Maximize the browser window"""
        try:
            self.driver.maximize_window()
            logger.info("Window maximized")
        except Exception as e:
            logger.error(f"Failed to maximize window: {e}")
    
    def set_window_size(self, width, height):
        """
        Set the browser window size
        
        Args:
            width: Window width
            height: Window height
        """
        try:
            self.driver.set_window_size(width, height)
            logger.info(f"Window size set to {width}x{height}")
        except Exception as e:
            logger.error(f"Failed to set window size: {e}")
