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
        self.assertEqual(current_url, expected_url, f"Expected URL {expected_url}, but got {current_url}")

if __name__ == "__main__":
    unittest.main()