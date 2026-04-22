import os
from datetime import datetime
from config import TestConfig
from utilities.logger import get_logger

logger = get_logger(__name__)

class ScreenshotUtils:
    """Utility class for screenshot operations"""

    @staticmethod
    def _ensure_directory():
        """Ensure screenshot directory exists"""
        os.makedirs(TestConfig.SCREENSHOTS_PATH, exist_ok=True)

    @staticmethod
    def _build_filename(prefix="screenshot", name=None):
        """Generate standardized filename"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if name:
            return f"{prefix}_{name}_{timestamp}.png"
        return f"{prefix}_{timestamp}.png"

    @staticmethod
    def take_screenshot(driver, filename=None):
        try:
            ScreenshotUtils._ensure_directory()

            filename = filename or ScreenshotUtils._build_filename()

            filepath = os.path.join(TestConfig.SCREENSHOTS_PATH, filename)

            driver.save_screenshot(filepath)
            logger.info(f"Screenshot saved: {filepath}")

            return filepath

        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return None

    @staticmethod
    def take_screenshot_on_failure(driver, test_name):
        filename = ScreenshotUtils._build_filename(
            prefix="failure",
            name=test_name
        )
        return ScreenshotUtils.take_screenshot(driver, filename)

    @staticmethod
    def get_element_screenshot(driver, element, filename=None):
        try:
            ScreenshotUtils._ensure_directory()

            filename = filename or ScreenshotUtils._build_filename(
                prefix="element"
            )

            filepath = os.path.join(TestConfig.SCREENSHOTS_PATH, filename)

            element.screenshot(filepath)
            logger.info(f"Element screenshot saved: {filepath}")

            return filepath

        except Exception as e:
            logger.error(f"Failed to take element screenshot: {e}")
            return None