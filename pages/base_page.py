"""
Base Page class for all page objects
"""
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import BrowserConfig, TestConfig
from utilities.logger import get_logger
from utilities.wait_utils import WaitUtils
from utilities.action_utils import ActionUtils
from utilities.browser_utils import BrowserUtils

logger = get_logger(__name__)

class BasePage:
    """Base page class with common functionality"""
    
    def __init__(self, driver):
        """
        Initialize BasePage
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, BrowserConfig.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)
        self.wait_utils = WaitUtils(driver, BrowserConfig.EXPLICIT_WAIT)
        self.action_utils = ActionUtils(driver)
        self.browser_utils = BrowserUtils(driver)

        self.message_locator= (By.XPATH,"//div[@role = 'alert']")
        self.tender_locator = (By.XPATH,"//a[@href = '/tender']")
        self.project_locator = (By.XPATH,"//a[@href = '/projects']")
        self.budget_locator = (By.XPATH,"//a[@href = '/budget']")
        self.procurement_locator = (By.XPATH,"//a[@href = '#0']")
        self.purchase_request_locator = (By.XPATH,"//a[@href = '/procurement/pr']")
        self.request_for_quote_locator = (By.XPATH,"//a[@href = '/procurement/rfq']")
        self.purchase_order_locator = (By.XPATH,"//a[@href = '/procurement/po']")
        self.invoice_locator = (By.XPATH,"//a[@href = '/procurement/invoice']")
        self.delivery_tracker_locator = (By.XPATH,"//a[@href = '/procurement/delivery-tracker']")
        self.items_management_locator = (By.XPATH,"//a[@href = '/items-management']")
        self.inventory_management_locator = (By.XPATH,"//a[@href = '/inventory-management']")
        self.configuration_locator = (By.XPATH,"//a[@href = '/configuration']")
        self.supplier_management_locator = (By.XPATH,"//a[@href = '/supplier-management']")
        self.settings_locator = (By.XPATH,"//a[@href = '/settings']")
        self.logout_locator = (By.XPATH,"//div[@data-slot='tooltip-trigger' and .//span[normalize-space()='Logout']]")
        self.profile_locator = (By.XPATH,"//button[@type='button' and contains(@class,'cursor-pointer')]")
        self.dashboard_locator = (By.XPATH,"//h3[text() = 'Dashboard']")
        self.search_box_locator = (By.XPATH,"//input[@type='text']")
        self.pagination_right_locator = (By.XPATH,"//*[local-name()='svg' and contains(@class,'lucide lucide-chevron-right')]")
        self.back_breadcrumb_locator = (By.XPATH,"//*[local-name()='svg' and contains(@class,'lucide-circle-chevron-left')]")
        self.view_details_locator = (By.XPATH,"//*[local-name()='svg' and contains(@class,'lucide-eye')]")
        self.action_locator = (By.XPATH,"//*[local-name()='svg' and contains(@class,'lucide-circle-arrow-right')]")

    
    def open_page(self, url=TestConfig.BASE_URL):
        """
        Open a page
        
        Args:
            url: URL to open (default: BASE_URL from config)
        """
        try:
            self.driver.get(url)
            logger.info(f"Page opened: {url}")
        except Exception as e:
            logger.error(f"Failed to open page: {e}")
    
    def find_element(self, locator):
        """
        Find a single element
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
        
        Returns:
            WebElement or None
        """
        try:
            element = self.driver.find_element(*locator)
            logger.info(f"Element found: {locator}")
            return element
        except Exception as e:
            logger.warning(f"Element not found: {locator}")
            return None
    
    def find_elements(self, locator):
        """
        Find multiple elements
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
        
        Returns:
            List of WebElements
        """
        try:
            elements = self.driver.find_elements(*locator)
            logger.info(f"Found {len(elements)} elements for: {locator}")
            return elements
        except Exception as e:
            logger.warning(f"Elements not found: {locator}")
            return []
    
    def is_element_visible(self, locator):
        """
        Check if element is visible
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
        
        Returns:
            Boolean
        """
        element = self.wait_utils.wait_for_element_visible(locator)
        return element is not None
    
    def is_element_present(self, locator):
        """
        Check if element is present in DOM
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
        
        Returns:
            Boolean
        """
        element = self.wait_utils.wait_for_element_present(locator)
        return element is not None
    
    def is_field_ready(self, locator):
        """
        Check if element is displayed and enabled
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
        
        Returns:
            Boolean
        """
        try:
            element = self.wait_utils.wait_for_element_visible(locator)
            return element is not None and element.is_displayed() and element.is_enabled()
        except Exception as e:
            logger.warning(f"Field {locator} not ready: {e}")
            return False
    
    def click_element(self, locator):
        """
        Click on element using locator
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
        """
        try:
            element = self.wait_utils.wait_for_element_clickable(locator)
            if element:
                self.action_utils.click_element(element)
            else:
                logger.error(f"Failed to click element {locator}: element not clickable")
        except Exception as e:
            logger.error(f"Failed to click element {locator}: {e}")

    def enter_text(self, locator, text):
        """
        Enter text into element
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            text: Text to enter
        """
        try:
            element = self.wait_utils.wait_for_element_visible(locator)
            if element:
                self.action_utils.clear_and_send_keys(element, text)
            else:
                logger.error(f"Failed to enter text in element {locator}: element not visible")
        except Exception as e:
            logger.error(f"Failed to enter text in element {locator}: {e}")

    def get_element_text(self, locator):
        """
        Get text from element
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
        
        Returns:
            str: Element text
        """
        try:
            element = self.wait_utils.wait_for_element_visible(locator)
            return element.text if element else ""
        except Exception as e:
            logger.error(f"Failed to get text from element {locator}: {e}")
            return ""
    
    def hover_over_element(self, locator):
        """
        Hover over element
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
        """
        try:
            element = self.wait_utils.wait_for_element_visible(locator)
            if element:
                self.action_utils.hover_over_element(element)
            else:
                logger.error(f"Failed to hover over element {locator}: element not visible")
        except Exception as e:
            logger.error(f"Failed to hover over element {locator}: {e}")

    def get_element_attribute(self, locator, attribute):
        """
        Get attribute value from element
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            attribute: Attribute name to retrieve
        
        Returns:
            str: Attribute value
        """
        try:
            element = self.wait_utils.wait_for_element_visible(locator)
            return element.get_attribute(attribute) if element else ""
        except Exception as e:
            logger.error(f"Failed to get attribute from element {locator}: {e}")
            return ""
        
    def wait_for_page_load(self, timeout=10):
        """
        Wait for page to fully load
        
        Args:
            timeout: Maximum wait time in seconds
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            logger.info("Page loaded successfully")
        except Exception as e:
            logger.warning(f"Page did not load within {timeout} seconds: {e}")

    def select_dropdown(self, locator, by="text", value=None):
        """
        Select option from standard HTML dropdown
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            by: Selection method ('text', 'value', 'index')
            value: Value to select
        """
        try:
            element = self.wait_utils.wait_for_element_visible(locator)
            if element:
                select = Select(element)
                if by == "text":
                    select.select_by_visible_text(value)
                    logger.info(f"Selected by text: {value}")
                elif by == "value":
                    select.select_by_value(value)
                    logger.info(f"Selected by value: {value}")
                elif by == "index":
                    select.select_by_index(int(value))
                    logger.info(f"Selected by index: {value}")
                else:
                    raise ValueError("Invalid selection method. Use 'text', 'value', or 'index'.")
            else:
                logger.error(f"Failed to select from dropdown {locator}: element not visible")
        except Exception as e:
            logger.error(f"Failed to select from dropdown {locator}: {e}")


    def select_radix_hidden_select(self, label_text, visible_text):
        """
        Select from Radix UI dropdown by visible text.
        Works with various DOM structures.
        """
        # Try multiple strategies to find the button
        button_xpaths = [
            # Strategy 1: Direct parent (most common)
            f"//label[contains(normalize-space(.), '{label_text}')]/parent::div//button[@role='combobox']",
            
            # Strategy 2: Ancestor with space-y class (your case)
            f"//label[contains(normalize-space(.), '{label_text}')]/ancestor::div[contains(@class,'space-y')]//button[@role='combobox']",
            
            # Strategy 3: Any ancestor div
            f"//label[contains(normalize-space(.), '{label_text}')]/ancestor::div[1]//button[@role='combobox']",
            
            # Strategy 4: Following sibling
            f"//label[contains(normalize-space(.), '{label_text}')]/following-sibling::button[@role='combobox']",
        ]
        
        button = None
        for xpath in button_xpaths:
            try:
                button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                break
            except:
                continue
        
        if not button:
            raise Exception(f"Could not find combobox button for label '{label_text}'")
        
        # Scroll button into view to avoid overlay issues
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(0.2)
        
        # Click using JavaScript to bypass overlay elements
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(0.3)
        
        # Click the option by visible text (case-insensitive)
        option = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            f"//div[@role='listbox']//*[translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='{visible_text.lower()}']"
        )))
        
        self.driver.execute_script("arguments[0].click();", option)
        time.sleep(0.2)


    def select_search_dropdown(self, locator, value, timeout=10):
        """
        Select from react-select dropdown by typing and selecting
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            value: Value to search for and select
            timeout: Maximum wait time
        """
        try:
            input_el = self.wait.until(EC.element_to_be_clickable(locator))
            input_el.click()
            input_el.clear()
            input_el.send_keys(value)
            logger.info(f"Typed in search dropdown: {value}")

            # Extract react-select index
            input_id = input_el.get_attribute("id")
            select_index = input_id.replace("-input", "")
            listbox_id = f"{select_index}-listbox"

            # Wait until listbox exists
            self.wait.until(
                EC.presence_of_element_located((By.ID, listbox_id))
            )

            # Wait until at least one option is rendered
            self.wait.until(
                lambda d: d.find_elements(
                    By.XPATH, f"//div[@id='{listbox_id}']//div[@role='option']"
                )
            )

            # Select first matched option
            input_el.send_keys(Keys.ARROW_DOWN)
            input_el.send_keys(Keys.ENTER)
            logger.info(f"Selected option from search dropdown")
        except Exception as e:
            logger.error(f"Failed to select from search dropdown: {e}")

    def select_date(self, date_button_locator, date_str, timeout=10):
        """
        Select a date in Radix UI datepicker dynamically.

        Args:
            date_button_locator: Locator tuple for the datepicker button (e.g., (By.ID, 'tenderDeadline'))
            date_str: Date string from Excel, e.g., "March 25, 2026"
            timeout: Maximum wait time for elements
        """
        try:
            target_date = datetime.strptime(date_str, "%B %d, %Y")
            target_day = target_date.day
            target_year = target_date.year

            # 1. Open the datepicker
            date_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(date_button_locator)
            )
            date_button.click()
            time.sleep(0.5)

            # 2. Navigate month/year
            while True:
                header = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(@data-state,'open')]//div[@aria-live='polite' and contains(@class,'text-sm')]")
                    )
                )
                current_month_year = header.text.strip()
                try:
                    current_date = datetime.strptime(current_month_year, "%B %Y")
                except ValueError:
                    parts = current_month_year.split()
                    current_date = datetime.strptime(f"{parts[0]} {parts[-1]}", "%B %Y")

                if current_date.year == target_year and current_date.month == target_date.month:
                    break

                if current_date < target_date:
                    next_btn = self.driver.find_element(
                        By.XPATH, "//div[contains(@data-state,'open')]//*[local-name()='svg' and contains(@class,'lucide-chevron-right')]/ancestor::button"
                    )
                    WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(next_btn)).click()
                else:
                    prev_btn = self.driver.find_element(
                        By.XPATH, "//div[contains(@data-state,'open')]//*[local-name()='svg' and contains(@class,'lucide-chevron-left')]/ancestor::button"
                    )
                    WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(prev_btn)).click()

                time.sleep(0.3)

            # 3. Click the day
            day_xpath = (
                f"//div[contains(@data-state,'open')]//button[@role='gridcell']"
                f"[normalize-space(.)='{target_day}' or @aria-label and contains(@aria-label, '{target_day}')]"
            )
            day_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, day_xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", day_element)
            try:
                if day_element.tag_name.lower() == "button":
                    day_element.click()
                else:
                    button_parent = day_element.find_element(By.XPATH, "./ancestor::button")
                    button_parent.click()
            except:
                button_parent = day_element.find_element(By.XPATH, "./ancestor::button")
                self.driver.execute_script("arguments[0].click();", button_parent)

            time.sleep(0.3)
            logger.info(f"Date selected: {date_str}")
        except Exception as e:
            logger.error(f"Failed to select date: {e}")

    def wait_for_message_contains(self, message_locator, text, timeout=10):
        """
        Wait for element message to contain specific text
        
        Args:
            message_locator: Locator tuple for message element
            text: Text to wait for
            timeout: Maximum wait time
        
        Returns:
            bool: True if text is found
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(message_locator, text)
            )
            logger.info(f"Message contains: {text}")
            return True
        except Exception as e:
            actual = self.get_element_text(message_locator)
            logger.error(f"Expected message containing '{text}' but got '{actual}'")
            return False


    def upload_file(self, locator, file_path):
        """
        Upload file using file input element
        
        Args:
            locator: Tuple (By.XPATH, "/path") or similar
            file_path: Absolute path to file to upload
        """
        try:
            file_input = self.wait.until(EC.presence_of_element_located(locator))
            file_input.send_keys(file_path)
            logger.info(f"File uploaded successfully: {file_path}")
        except Exception as e:
            logger.error(f"Failed to upload file: {e}")