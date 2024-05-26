import unittest
from setup import setUp
from pages.login_page import LoginPage

class LoginTests(unittest.TestCase):

    def setUp(self):
        setUp(self)

    def test_validLogin(self):
        self.driver.get(self.baseURL)

        lp = LoginPage(self.driver, self.config)  # Pass config to LoginPage
        lp.login()

    def tearDown(self):
        self.driver.quit()