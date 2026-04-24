# Selenium Automation Framework

A robust, scalable test automation framework built with Selenium WebDriver and Python for the LDVERP procurement management system. Designed for efficient, maintainable automated testing with best practices for modern QA.

## Features

✅ **Page Object Model (POM)** - Clean separation of test logic and page interactions  
✅ **Environment-based Configuration** - Multiple environments (DEV, STAGING, PROD) with secure credential management  
✅ **Allure & HTML Reporting** - Beautiful Allure reports with screenshots and detailed test reports  
✅ **Screenshot Utilities** - Automatic screenshots on failures and custom captures  
✅ **Comprehensive Logging** - Structured logging with rotation and multiple log levels  
✅ **Multiple Browser Support** - Chrome, Firefox, Edge with configurable options  
✅ **Headless Mode** - Run tests in headless mode for CI/CD pipelines  
✅ **Thread-safe Driver Management** - CI/CD ready with Selenium Manager (no driver binaries needed)  
✅ **Wait Strategies** - Implicit, explicit, and fluent wait utilities  
✅ **Performance Monitoring** - Built-in performance tracking utilities  
✅ **Assertion Helpers** - Custom assertion utilities for cleaner test code  
✅ **Parallel & Retry Support** - pytest-xdist for parallel execution and automatic test retries  

## Project Structure

```
Selenium Framework/
├── config/                 # Configuration files
│   ├── __init__.py
│   ├── config.py          # Environment, browser, and test configuration
│   └── credentials.py     # Credentials from environment variables
├── pages/                 # Page Object Model classes
│   ├── base_page.py       # Base page with common methods and locators
│   └── login_page.py      # Login page object
├── tests/                 # Test files
│   └── test_login.py      # Login tests with Allure reporting
├── utilities/             # Helper utilities
│   ├── action_utils.py    # Common actions (click, type, etc.)
│   ├── assertion_helpers.py # Custom assertions
│   ├── browser_utils.py   # Browser utilities
│   ├── driver_manager.py  # Thread-safe WebDriver management
│   ├── excel_utils.py     # Excel file operations
│   ├── logger.py          # Logging configuration with rotation
│   ├── performance_utils.py # Performance monitoring
│   ├── screenshot_utils.py # Screenshot functionality
│   └── wait_utils.py      # Wait strategies
├── test_data/             # Test data files (Excel, JSON, etc.)
├── screenshots/           # Screenshots (generated on failures)
├── logs/                  # Test execution logs
├── reports/               # Generated HTML and Allure reports
├── assets/                # Report styling (CSS)
├── conftest.py           # Pytest configuration and fixtures
├── pytest.ini            # Pytest settings and markers
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd "Selenium Framework"
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
```bash
# Copy the template
copy .env.example .env

# Edit .env with your credentials
# EMAIL=your-email@example.com
# PASSWORD=your-password
```

## Running Tests

### Run All Tests
```bash
pytest -s -v
```

### Run Specific Test File
```bash
pytest tests/test_login.py -s -v
```

### Run with Specific Markers
```bash
# Smoke tests only
pytest -m smoke -s -v

# Regression tests
pytest -m regression -s -v

# Login-related tests
pytest -m login -s -v
```

### Run with HTML Report
```bash
pytest --html=report.html
```

### Run with Allure Report
```bash
pytest --allure-features --allure-stories
allure generate --clean -o allure-report
allure open allure-report
```

### Run in Headless Mode
```bash
pytest --headless true -s -v
```

### Run with Specific Browser
```bash
# Chrome (default)
pytest --browser=chrome -s -v

# Firefox
pytest --browser=firefox -s -v

# Edge
pytest --browser=edge -s -v
```

### Run with Parallel Execution
```bash
pytest -n auto  # Auto-detect number of CPU cores
pytest -n 4     # Use 4 workers
```

### Run with Retries
Edit `config/config.py`:
```python
TestConfig.RETRY_COUNT = 2  # Retry failed tests 2 times
```

### Run with Timeout
```bash
pytest --timeout=300  # 5 minutes timeout
```

## Configuration

### Main Configuration (`config/config.py`)

The framework supports multiple environments with centralized configuration:

```python
from config.config import Environment, BrowserConfig, TestConfig

# Environments
Environment.DEV  # https://dev.example.com
Environment.STAGING  # https://staging.ldverp.com/ (default)
Environment.PROD  # https://prod.example.com

# Browser Configuration (READ-ONLY)
BrowserConfig.IMPLICIT_WAIT = 5
BrowserConfig.EXPLICIT_WAIT = 10
BrowserConfig.PAGE_LOAD_TIMEOUT = 20
BrowserConfig.DEFAULT_BROWSER = "chrome"
BrowserConfig.MAXIMIZE_WINDOW = True

# Test Configuration
TestConfig.BASE_URL  # Base URL (from Environment.STAGING)
TestConfig.SCREENSHOT_ON_FAILURE = True
TestConfig.RETRY_COUNT = 0  # Number of retries
TestConfig.PARALLEL_EXECUTION = False  # Enable parallel tests
TestConfig.LOG_LEVEL = "INFO"
TestConfig.SLOW_TEST_THRESHOLD = 30  # seconds
```

### Credentials (`config/credentials.py`)

Access credentials from environment variables:

```python
from config.credentials import Credentials

email = Credentials.EMAIL
password = Credentials.PASSWORD
```

**Set environment variables in your `.env` file:**
```
EMAIL=your-email@example.com
PASSWORD=your-password
```

## Usage Examples

### Basic Test with Allure Reporting

```python
import pytest
import allure
from pages.login_page import LoginPage
from utilities.assertion_helpers import AssertionHelpers
from config.credentials import Credentials

@allure.feature("Login Tests")
@allure.title("Verify successful login with valid credentials")
@allure.story("Successful Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(driver):
    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.open_page()

    with allure.step("Login using valid credentials"):
        login_page.login(Credentials.EMAIL, Credentials.PASSWORD)

    with allure.step("Verify Dashboard is displayed"):
        actual_text = login_page.get_element_text(login_page.dashboard_locator)
        AssertionHelpers.assert_text_contains(actual_text, "Dashboard")
```

### Add Test Markers

```python
@pytest.mark.smoke
@pytest.mark.login
def test_login_smoke(driver):
    # Test implementation
    pass

@pytest.mark.regression
def test_login_regression(driver):
    # Test implementation
    pass

@pytest.mark.skip(reason="Under development")
def test_future_feature(driver):
    # Test implementation
    pass
```

### With Screenshots

```python
from utilities.screenshot_utils import ScreenshotUtils

def test_with_screenshot(driver):
    # Take manual screenshot
    ScreenshotUtils.take_screenshot(driver, "login_success")
    
    # Screenshots are auto-captured on failure (from conftest.py hook)
```

### Custom Assertions

```python
from utilities.assertion_helpers import AssertionHelpers

def test_assertions_example(driver):
    AssertionHelpers.assert_element_visible(driver, locator)
    AssertionHelpers.assert_element_text_equals(driver, locator, "Expected Text")
    AssertionHelpers.assert_text_contains(text, "substring")
```

### Performance Monitoring

```python
from utilities.performance_utils import PerformanceUtils

def test_with_performance(driver):
    start_time = PerformanceUtils.get_current_time()
    # Perform actions
    elapsed_time = PerformanceUtils.get_elapsed_time(start_time)
    assert elapsed_time < 5, f"Test took {elapsed_time}s, expected < 5s"
```

## File Descriptions

| File | Purpose |
|------|---------|
| `conftest.py` | Pytest configuration, fixtures (driver, config), CLI options (--browser, --headless), and failure hooks |
| `pytest.ini` | Pytest settings, test paths, markers (smoke, regression, sanity, login, slow), and logging config |
| `config/config.py` | Environment URLs, browser configuration, timeouts, and test settings |
| `config/credentials.py` | Credentials loaded from environment variables (.env) |
| `pages/base_page.py` | Base class for all page objects with common methods, locators, and utilities |
| `pages/login_page.py` | Login page object specific to the application |
| `utilities/driver_manager.py` | Thread-safe WebDriver initialization and management (Selenium Manager) |
| `utilities/logger.py` | Logging setup with rotation and multiple log levels |
| `utilities/screenshot_utils.py` | Screenshot capture on failures and manual screenshots |
| `utilities/wait_utils.py` | Wait strategies (implicit, explicit, fluent) |
| `utilities/action_utils.py` | Common browser actions (click, type, hover, etc.) |
| `utilities/assertion_helpers.py` | Custom assertion methods for cleaner test code |
| `utilities/excel_utils.py` | Excel file reading for test data |
| `utilities/performance_utils.py` | Performance tracking and timing utilities |
| `utilities/browser_utils.py` | Browser-level utilities (navigate, refresh, switch windows, etc.) |

## Best Practices

### 1. Use Page Object Model
Keep test logic separate from page interactions.

```python
# ❌ Bad
def test_login(driver):
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login").click()

# ✅ Good
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("test@example.com", "password123")
```

### 2. Secure Credentials
Always use environment variables, never hardcode credentials.

```python
# ❌ Bad
login_page.login("test@example.com", "password123")

# ✅ Good
login_page.login(Credentials.EMAIL, Credentials.PASSWORD)
```

### 3. Use Explicit Waits
Use explicit waits instead of sleep() or implicit waits.

```python
# ❌ Bad
import time
time.sleep(5)

# ✅ Good
from utilities.wait_utils import WaitUtils
wait_utils = WaitUtils(driver, 10)
wait_utils.wait_for_element_visible(locator)
```

### 4. Use Meaningful Assertions
```python
# ❌ Bad
assert "Dashboard" in driver.page_source

# ✅ Good
from utilities.assertion_helpers import AssertionHelpers
AssertionHelpers.assert_text_contains(
    login_page.get_element_text(login_page.dashboard_locator),
    "Dashboard"
)
```

### 5. Add Allure Reporting
Use Allure decorators to organize tests and enhance reports.

```python
# ✅ Good
@allure.feature("Authentication")
@allure.story("User Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(driver):
    with allure.step("Open login page"):
        login_page.open_page()
    
    with allure.step("Enter credentials"):
        login_page.login(Credentials.EMAIL, Credentials.PASSWORD)
    
    with allure.step("Verify success"):
        assert login_page.is_logged_in()
```

### 6. Use Test Markers
Organize tests with pytest markers for selective execution.

```python
# ✅ Good
@pytest.mark.smoke
@pytest.mark.login
def test_login(driver):
    # Test implementation
    pass

# Run only smoke tests:
# pytest -m smoke
```

### 7. Screenshot on Failures
Screenshots are automatically captured on test failures via conftest.py hook.

```python
# Manual screenshot when needed
ScreenshotUtils.take_screenshot(driver, "state_before_action")
```

### 8. Use Custom Logging
Log important steps for debugging.

```python
from utilities.logger import get_logger

logger = get_logger(__name__)
logger.info("Starting login test")
logger.debug(f"Using email: {Credentials.EMAIL}")
```

## CI/CD Integration

### Run in GitHub Actions
```yaml
name: Selenium Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run tests
        env:
          EMAIL: ${{ secrets.EMAIL }}
          PASSWORD: ${{ secrets.PASSWORD }}
        run: |
          pytest --headless true --html=report.html
      
      - name: Generate Allure Report
        if: always()
        run: |
          allure generate --clean -o allure-report
      
      - name: Upload reports
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-reports
          path: |
            report.html
            allure-report/
```

### Run in Jenkins
```bash
#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set environment variables
export EMAIL=$LDVERP_EMAIL
export PASSWORD=$LDVERP_PASSWORD

# Run tests
pytest -s -v --headless true --html=report.html

# Generate Allure report
allure generate --clean -o allure-report
```

### Run in Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "--headless", "true", "-s", "-v", "--html=report.html"]
```

## Troubleshooting

### Tests Won't Run
- Ensure virtual environment is activated: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
- Install dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)
- Verify `.env` file exists with credentials

### Import Errors
- Verify `conftest.py` is in root directory
- Check `sys.path.insert()` in conftest.py
- Run: `python -c "import config; import utilities"` to test imports
- Clear `__pycache__` folders: `find . -type d -name __pycache__ -exec rm -r {} +`

### WebDriver/Browser Issues
- Selenium Manager auto-downloads correct drivers (Selenium 4.15.2+)
- Clear `drivers/` folder if issues persist: `rm -rf drivers/`
- Check browser compatibility: `selenium --version` and `chrome --version`
- Run in headless mode for CI/CD: `pytest --headless true`

### Screenshot Issues
- Ensure `screenshots/` folder exists or will be auto-created
- Check file permissions in project directory
- Verify disk space available
- Check image format support (PNG is default)

### Logging Issues
- Check `logs/` folder exists or will be auto-created
- Verify log level in `config/config.py`: `TestConfig.LOG_LEVEL`
- Check file permissions for log file writing
- View logs: `tail -f logs/selenium_tests.log` (Unix/Mac)

### Headless Mode Issues
```bash
# If headless tests fail but GUI mode works:
pytest --headless false -s -v  # Debug in GUI mode

# Common headless issues:
# - Missing window size configuration
# - JavaScript timing issues
# - Some UI elements not rendering
```

### Element Location Issues
```python
# Common selector problems:
# ❌ Element not found with XPath
# ✅ Use explicit waits
from utilities.wait_utils import WaitUtils
wait_utils = WaitUtils(driver, 10)
wait_utils.wait_for_element_visible(locator)

# Inspect element in browser DevTools to verify selector
```

### Parallel Execution Issues
- Reduce `pytest-xdist` workers if tests conflict: `pytest -n 2`
- Use thread-local driver storage (already configured)
- Ensure tests are independent and don't share state
- Set `TestConfig.PARALLEL_EXECUTION = False` in config if issues persist

### Allure Report Issues
```bash
# If Allure report won't generate:
allure --version  # Check if installed

# Reinstall Allure:
pip install --upgrade allure-pytest

# Clear Allure cache:
rm -rf .allure/

# Generate report with specific path:
allure generate --clean -o allure-report/
allure open allure-report/
```

### Performance/Timeout Issues
- Increase timeout: `pytest --timeout=300`
- Check `TestConfig.SLOW_TEST_THRESHOLD` in config
- Use `pytest-timeout` plugin for individual test timeouts
- Profile performance: `utilities/performance_utils.py`

### Credential/Environment Variable Issues
- Create `.env` file from `.env.example`
- Verify `EMAIL` and `PASSWORD` are set: `echo $EMAIL`
- Check `.gitignore` includes `.env`
- On CI/CD, set environment variables in secrets manager

## Contributing

1. Create a new branch: `git checkout -b feature/new-tests`
2. Add tests following the existing structure:
   - Create page objects in `pages/`
   - Create test files in `tests/`
   - Use existing utilities from `utilities/`
3. Follow naming conventions:
   - Test files: `test_*.py`
   - Test functions: `test_*`
   - Page objects: `*_page.py`
4. Add Allure decorators to all tests
5. Add pytest markers for test categorization
6. Run tests locally before committing: `pytest -s -v`
7. Commit changes: `git commit -am 'Add new tests for feature X'`
8. Push to branch: `git push origin feature/new-tests`
9. Create a Pull Request

## Testing Standards

- **Test Coverage**: Aim for critical user flows and edge cases
- **Performance**: Tests should complete within `TestConfig.SLOW_TEST_THRESHOLD` (30s)
- **Stability**: Use explicit waits and avoid hard-coded delays
- **Clarity**: Use meaningful test names and assertions
- **Documentation**: Add Allure steps and descriptions
- **Isolation**: Tests should be independent and repeatable
- **Data**: Use `Credentials` class for sensitive data, test data in `test_data/`

## Resources

- [Selenium Python Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Documentation](https://docs.qameta.io/allure/)
- [LDVERP Application](https://staging.ldverp.com/)

## Dependencies

Core Testing & Automation:
- **selenium** (4.15.2) - WebDriver automation
- **pytest** (7.4.3) - Test framework
- **webdriver-manager** (4.0.1) - Automatic driver management (Selenium Manager)
- **python-dotenv** (1.0.0) - Environment variable management

Reporting & Logging:
- **pytest-html** (4.1.1) - HTML test reports
- **allure-pytest** (2.13.2) - Allure report integration
- **allure-python-commons** (2.13.2) - Allure common library

Test Execution:
- **pytest-xdist** (3.5.0) - Parallel test execution
- **pytest-retry** (1.6.1) - Automatic test retries
- **pytest-timeout** (2.1.0) - Test execution timeout
- **pytest-metadata** (3.1.1) - Test metadata

Data & Excel:
- **openpyxl** (3.1.2) - Excel file operations

Utilities:
- **requests** (2.33.1) - HTTP library
- **selenium** dependencies (various) - WebDriver-related libraries

See `requirements.txt` for complete list with all versions.


**Last Updated:** April 2026  
**Framework Version:** 1.1.0  
**Target Application:** LDVERP Procurement Management System
