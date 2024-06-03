from base.selenium_driver import SeleniumDriver
from utils.config_loader import load_config
from locators import *
import unittest


class LoginPage(SeleniumDriver):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def enterEmail(self, email):
        self.sendKeys(email, LoginPageLocators.EMAIL_FIELD)

    def enterPassword(self, password):
        self.sendKeys(password, LoginPageLocators.PASSWORD_FIELD, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(LoginPageLocators.LOGIN_BUTTON, locatorType="id")

    def login(self):
        self.driver.get(self.config['url'])  # Navigate to the URL based on config
        self.enterEmail(self.config['username'])  # Use username from config
        self.enterPassword(self.config['password'])  # Use password from config
        self.clickLoginButton()

    def invalid_login(self):
        self.driver.get(self.config['url'])  # Navigate to the URL based on config
        self.enterEmail(self.config['invalid_username'])  # Use username from config
        self.enterPassword(self.config['invalid_password'])  # Use password from config
        self.clickLoginButton()

    def get_error_message(self):
        login_error = self.waitForElement(ProductPageLocators.ERROR, locatorType="css", timeout=10)
        return login_error.text


