"""
Screenshot utility for the Selenium Framework
"""
import os
from datetime import datetime
from config import TestConfig
from utilities.logger import get_logger

logger = get_logger(__name__)

class ScreenshotUtils:
    """Utility class for screenshot operations"""
    
    @staticmethod
    def take_screenshot(driver, filename=None):
        """
        Take a screenshot and save it
        
        Args:
            driver: WebDriver instance
            filename: Custom filename (without extension)
        
        Returns:
            str: Path to saved screenshot
        """
        try:
            # Create screenshots directory if it doesn't exist
            if not os.path.exists(TestConfig.SCREENSHOTS_PATH):
                os.makedirs(TestConfig.SCREENSHOTS_PATH)
            
            # Generate filename if not provided
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}"
            
            # Add extension
            if not filename.endswith(".png"):
                filename = f"{filename}.png"
            
            filepath = os.path.join(TestConfig.SCREENSHOTS_PATH, filename)
            driver.save_screenshot(filepath)
            logger.info(f"Screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return None
    
    @staticmethod
    def take_screenshot_on_failure(driver, test_name):
        """
        Take a screenshot on test failure
        
        Args:
            driver: WebDriver instance
            test_name: Name of the test that failed
        
        Returns:
            str: Path to saved screenshot
        """
        filename = f"failure_{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        return ScreenshotUtils.take_screenshot(driver, filename)
    
    @staticmethod
    def get_element_screenshot(driver, element, filename=None):
        """
        Take a screenshot of a specific element
        
        Args:
            driver: WebDriver instance
            element: WebElement to screenshot
            filename: Custom filename (without extension)
        
        Returns:
            str: Path to saved screenshot
        """
        try:
            # Create screenshots directory if it doesn't exist
            if not os.path.exists(TestConfig.SCREENSHOTS_PATH):
                os.makedirs(TestConfig.SCREENSHOTS_PATH)
            
            # Generate filename if not provided
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"element_screenshot_{timestamp}"
            
            # Add extension
            if not filename.endswith(".png"):
                filename = f"{filename}.png"
            
            filepath = os.path.join(TestConfig.SCREENSHOTS_PATH, filename)
            element.screenshot(filepath)
            logger.info(f"Element screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Failed to take element screenshot: {e}")
            return None
