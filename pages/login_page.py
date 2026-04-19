from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.email_locator = (By.XPATH,"//input[@id='email']")
        self.password_locator = (By.XPATH,"//input[@id='password']")
        self.login_button_locator = (By.XPATH,"//button[@type='submit']")

    def login(self, email, password):
        self.enter_text(self.email_locator,email)
        self.enter_text(self.password_locator,password)
        self.click_element(self.login_button_locator)