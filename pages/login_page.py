from base.selenium_driver import SeleniumDriver
from utils.config_loader import load_config
from locators import LoginPageLocators

class LoginPage(SeleniumDriver):
    def __init__(self, driver, config):  # Pass config as a parameter
        self.driver = driver
        self.config = config  # Set config as an attribute

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


