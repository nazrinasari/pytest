from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = 'user-name'
    PASSWORD_FIELD = 'password'
    LOGIN_BUTTON = 'login-button'

class ProductPageLocators:
    PRODUCTS = 'inventory_item'
    ERROR = '[data-test="error"]'