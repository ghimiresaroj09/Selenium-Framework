"""
Custom Assertion Helpers for Tests
"""
from utilities.logger import get_logger

logger = get_logger(__name__)

class AssertionHelpers:
    """Custom assertion helper methods for common test scenarios"""
    
    @staticmethod
    def assert_element_visible(element, message="Element should be visible"):
        """Assert element is visible"""
        assert element is not None and element.is_displayed(), message
        logger.info(message)
    
    @staticmethod
    def assert_element_clickable(element, message="Element should be clickable"):
        """Assert element is clickable"""
        assert element is not None and element.is_enabled(), message
        logger.info(message)
    
    @staticmethod
    def assert_text_contains(actual, expected, message=None):
        """Assert text contains expected value"""
        default_msg = f"Expected text to contain '{expected}', but got '{actual}'"
        message = message or default_msg
        assert expected.lower() in actual.lower(), message
        logger.info(f"Text assertion passed: {message}")
    
    @staticmethod
    def assert_url_contains(actual_url, expected_url, message=None):
        """Assert URL contains expected value"""
        default_msg = f"Expected URL to contain '{expected_url}', but got '{actual_url}'"
        message = message or default_msg
        assert expected_url.lower() in actual_url.lower(), message
        logger.info(f"URL assertion passed: {message}")
    
    @staticmethod
    def assert_attribute_equals(element, attribute, expected_value, message=None):
        """Assert element attribute equals expected value"""
        actual_value = element.get_attribute(attribute)
        default_msg = f"Expected attribute '{attribute}' to be '{expected_value}', but got '{actual_value}'"
        message = message or default_msg
        assert actual_value == expected_value, message
        logger.info(f"Attribute assertion passed: {message}")
    
    @staticmethod
    def assert_list_not_empty(items, message="List should not be empty"):
        """Assert list is not empty"""
        assert len(items) > 0, message
        logger.info(f"{message} - Found {len(items)} items")
    
    @staticmethod
    def assert_list_length(items, expected_length, message=None):
        """Assert list has expected length"""
        default_msg = f"Expected list length {expected_length}, but got {len(items)}"
        message = message or default_msg
        assert len(items) == expected_length, message
        logger.info(f"Length assertion passed: {message}")
    
    @staticmethod
    def assert_true(condition, message="Assertion failed"):
        """Assert condition is true"""
        assert condition, message
        logger.info(f"True assertion passed: {message}")
    
    @staticmethod
    def assert_false(condition, message="Assertion failed"):
        """Assert condition is false"""
        assert not condition, message
        logger.info(f"False assertion passed: {message}")
