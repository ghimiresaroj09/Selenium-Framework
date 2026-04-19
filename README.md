# Selenium Automation Framework

A robust, scalable test automation framework built with Selenium WebDriver and Python. Designed for efficient, maintainable automated testing with best practices for modern QA.

## Features

✅ **Page Object Model (POM)** - Clean separation of test logic and page interactions  
✅ **Environment-based Configuration** - Secure credential management with `.env` files  
✅ **Screenshot Utilities** - Automatic screenshots on failures and custom captures  
✅ **Logging & Reporting** - Comprehensive logs and HTML test reports  
✅ **Multiple Browser Support** - Chrome, Firefox, Edge with configurable options  
✅ **Headless Mode** - Run tests in headless mode for CI/CD pipelines  
✅ **Excel Data-driven Testing** - Load test data from Excel files  
✅ **Wait Strategies** - Implicit, explicit, and fluent wait utilities  
✅ **Performance Monitoring** - Built-in performance tracking utilities  
✅ **Assertion Helpers** - Custom assertion utilities for cleaner test code  

## Project Structure

```
Selenium Framework/
├── config/                 # Configuration files
│   ├── __init__.py
│   ├── config.py          # Main configuration
│   └── credentials.py     # Credentials from environment variables
├── pages/                 # Page Object Model classes
│   ├── base_page.py       # Base page with common methods
│   └── login_page.py      # Login page object
├── tests/                 # Test files
│   └── test_login.py      # Login tests
├── utilities/             # Helper utilities
│   ├── action_utils.py    # Common actions (click, type, etc.)
│   ├── assertion_helpers.py # Custom assertions
│   ├── browser_utils.py   # Browser utilities
│   ├── driver_manager.py  # WebDriver management
│   ├── excel_utils.py     # Excel file operations
│   ├── logger.py          # Logging configuration
│   ├── performance_utils.py # Performance monitoring
│   ├── screenshot_utils.py # Screenshot functionality
│   └── wait_utils.py      # Wait strategies
├── test_data/             # Test data files (Excel, JSON, etc.)
├── screenshots/           # Screenshots (generated on failures)
├── logs/                  # Test execution logs
├── reports/               # Generated HTML reports
├── .env                   # Environment variables (DO NOT COMMIT)
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore patterns
├── conftest.py           # Pytest configuration and fixtures
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

### Run with HTML Report
```bash
pytest --html=report.html
```

### Run in Headless Mode
```bash
pytest --headless -s -v
```

### Run with Specific Browser
```bash
pytest --browser=firefox -s -v
# Options: chrome (default), firefox, edge
```

## Configuration

### Main Configuration (`config/config.py`)

Define your test URLs, timeouts, and paths:

```python
class TestConfig:
    BASE_URL = "https://your-app.com"
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    SCREENSHOTS_PATH = "screenshots"
```

### Credentials (`config/credentials.py`)

Access credentials from environment variables:

```python
from config.credentials import Credentials

email = Credentials.EMAIL
password = Credentials.PASSWORD
```

## Usage Examples

### Basic Test
```python
from pages.login_page import LoginPage
from config.credentials import Credentials

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login(Credentials.EMAIL, Credentials.PASSWORD)
    assert "Dashboard" in login_page.get_element_text(login_page.dashboard_locator)
```

### With Screenshots
```python
from utilities.screenshot_utils import ScreenshotUtils

# Take manual screenshot
ScreenshotUtils.take_screenshot(driver, "login_success")

# Take screenshot on failure (automatic via fixture)
# Screenshots are auto-captured when tests fail
```

### Data-driven Testing
```python
from utilities.excel_utils import read_excel_data

test_data = read_excel_data("test_data/Login_data.xlsx")

@pytest.mark.parametrize("login_data", test_data)
def test_login_multiple(driver, login_data):
    login_page = LoginPage(driver)
    login_page.login(login_data["Email"], login_data["Password"])
    assert login_page.is_logged_in()
```

### Custom Assertions
```python
from utilities.assertion_helpers import AssertionHelpers

AssertionHelpers.assert_element_visible(driver, locator)
AssertionHelpers.assert_element_text_equals(driver, locator, "Expected Text")
```

## File Descriptions

| File | Purpose |
|------|---------|
| `conftest.py` | Pytest configuration, fixtures, and CLI options |
| `config/config.py` | Global test configuration |
| `config/credentials.py` | Credentials from environment variables |
| `pages/base_page.py` | Base class for all page objects |
| `utilities/driver_manager.py` | WebDriver initialization and management |
| `utilities/logger.py` | Logging setup for tests |
| `utilities/screenshot_utils.py` | Screenshot capture functionality |
| `utilities/wait_utils.py` | Wait strategies (implicit, explicit, fluent) |
| `utilities/action_utils.py` | Common browser actions |
| `utilities/assertion_helpers.py` | Custom assertion methods |
| `utilities/excel_utils.py` | Excel file reading for test data |
| `utilities/performance_utils.py` | Performance tracking utilities |

## Best Practices

### 1. Use Page Object Model
Keep test logic separate from page interactions.

```python
# ❌ Bad
driver.find_element(By.ID, "email").send_keys("test@example.com")

# ✅ Good
login_page.enter_email("test@example.com")
```

### 2. Secure Credentials
Always use environment variables, never hardcode credentials.

```python
# ❌ Bad
driver.login("test@example.com", "password123")

# ✅ Good
driver.login(Credentials.EMAIL, Credentials.PASSWORD)
```

### 3. Wait for Elements
Use explicit waits instead of sleep.

```python
# ❌ Bad
time.sleep(5)

# ✅ Good
WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
```

### 4. Use Meaningful Assertions
```python
# ❌ Bad
assert "Dashboard" in driver.page_source

# ✅ Good
assert "Dashboard" in login_page.get_element_text(login_page.dashboard_locator)
```

### 5. Screenshot on Failures
```python
# Automatic in fixtures
# Or manual when needed
ScreenshotUtils.take_screenshot(driver, "important-state")
```

## CI/CD Integration

### Run in GitHub Actions
```yaml
- name: Run Tests
  run: |
    pip install -r requirements.txt
    pytest --headless --html=report.html
```

### Run in Jenkins
```bash
#!/bin/bash
source venv/bin/activate
pytest -s -v --html=report.html
```

## Troubleshooting

### Tests Won't Run
- Ensure virtual environment is activated: `venv\Scripts\activate`
- Install dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

### Driver Issues
- WebDriver manager auto-downloads correct drivers
- Clear `drivers/` folder if issues persist

### Import Errors
- Verify `conftest.py` is in root directory
- Check `sys.path.insert()` in conftest.py

### Screenshot Issues
- Ensure `screenshots/` folder exists
- Check file permissions in project directory

## Contributing

1. Create a new branch: `git checkout -b feature/new-tests`
2. Add tests following the existing structure
3. Update documentation if needed
4. Commit changes: `git commit -am 'Add new tests'`
5. Push to branch: `git push origin feature/new-tests`
6. Create a Pull Request

## Dependencies

- **selenium** - WebDriver automation
- **pytest** - Test framework
- **pytest-html** - HTML report generation
- **webdriver-manager** - Automatic driver management
- **python-dotenv** - Environment variable management
- **openpyxl** - Excel file operations

See `requirements.txt` for complete list with versions.


## Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Last Updated:** April 2026  
**Framework Version:** 1.0.0
