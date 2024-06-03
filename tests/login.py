import unittest
from setup import BaseSetup
from pages.login_page import LoginPage

class LoginTests(BaseSetup, unittest.TestCase):

    def test_validLogin(self):
        self.driver.get(self.baseURL)  # Navigate to the URL based on config
        lp = LoginPage(self.driver, self.config)
        lp.login()
        expected_url = "https://www.saucedemo.com/inventory.html"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url)

    def test_invalidLogin(self):
        self.driver.get(self.baseURL)  # Navigate to the URL based on config
        lp = LoginPage(self.driver, self.config)
        lp.invalid_login()
        current_error = lp.get_error_message
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        self.assertEqual(current_error(), expected_error)

        #
if __name__ == "__main__":
    unittest.main()