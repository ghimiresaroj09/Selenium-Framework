"""
Action utilities for the Selenium Framework
"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from utilities.logger import get_logger

logger = get_logger(__name__)

class ActionUtils:
    """Utility class for action operations"""
    
    def __init__(self, driver):
        """
        Initialize ActionUtils
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.actions = ActionChains(driver)
    
    def click_element(self, element):
        """
        Click on an element
        
        Args:
            element: WebElement to click
        """
        try:
            self.actions.click(element).perform()
            logger.info("Element clicked successfully")
        except Exception as e:
            logger.error(f"Failed to click element: {e}")
    
    def double_click_element(self, element):
        """
        Double click on an element
        
        Args:
            element: WebElement to double click
        """
        try:
            self.actions.double_click(element).perform()
            logger.info("Element double-clicked successfully")
        except Exception as e:
            logger.error(f"Failed to double-click element: {e}")
    
    def right_click_element(self, element):
        """
        Right click on an element
        
        Args:
            element: WebElement to right click
        """
        try:
            self.actions.context_click(element).perform()
            logger.info("Element right-clicked successfully")
        except Exception as e:
            logger.error(f"Failed to right-click element: {e}")
    
    def send_keys(self, element, keys):
        """
        Send keys to an element
        
        Args:
            element: WebElement to send keys to
            keys: String of keys to send
        """
        try:
            element.send_keys(keys)
            logger.info(f"Keys sent to element: {keys}")
        except Exception as e:
            logger.error(f"Failed to send keys: {e}")
    
    def clear_and_send_keys(self, element, keys):
        """
        Clear element and send keys
        
        Args:
            element: WebElement to clear and send keys to
            keys: String of keys to send
        """
        try:
            element.clear()
            element.send_keys(keys)
            logger.info(f"Element cleared and keys sent: {keys}")
        except Exception as e:
            logger.error(f"Failed to clear and send keys: {e}")
    
    def hover_over_element(self, element):
        """
        Hover over an element
        
        Args:
            element: WebElement to hover over
        """
        try:
            self.actions.move_to_element(element).perform()
            logger.info("Hovered over element successfully")
        except Exception as e:
            logger.error(f"Failed to hover over element: {e}")
    
    def drag_and_drop(self, source, target):
        """
        Drag and drop an element
        
        Args:
            source: Source WebElement
            target: Target WebElement
        """
        try:
            self.actions.drag_and_drop(source, target).perform()
            logger.info("Drag and drop performed successfully")
        except Exception as e:
            logger.error(f"Failed to drag and drop: {e}")
    
    def select_by_value(self, element, value):
        """
        Select an option by value
        
        Args:
            element: Select WebElement
            value: Value to select
        """
        try:
            select = Select(element)
            select.select_by_value(value)
            logger.info(f"Selected value: {value}")
        except Exception as e:
            logger.error(f"Failed to select value: {e}")
    
    def select_by_text(self, element, text):
        """
        Select an option by text
        
        Args:
            element: Select WebElement
            text: Text to select
        """
        try:
            select = Select(element)
            select.select_by_visible_text(text)
            logger.info(f"Selected text: {text}")
        except Exception as e:
            logger.error(f"Failed to select text: {e}")
    
    def select_by_index(self, element, index):
        """
        Select an option by index
        
        Args:
            element: Select WebElement
            index: Index to select
        """
        try:
            select = Select(element)
            select.select_by_index(index)
            logger.info(f"Selected index: {index}")
        except Exception as e:
            logger.error(f"Failed to select index: {e}")
    
    def press_key(self, element, key):
        """
        Press a specific key
        
        Args:
            element: WebElement to send key to
            key: Key constant from selenium.webdriver.common.keys.Keys
        """
        try:
            element.send_keys(key)
            logger.info(f"Key pressed: {key}")
        except Exception as e:
            logger.error(f"Failed to press key: {e}")
