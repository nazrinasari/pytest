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

    def test_productCount(self):
        lp = LoginPage(self.driver, self.config)
        lp.login()

        # Verify there are 6 products displayed
        pp = ProductsPage(self.driver)
        product_count = pp.get_product_count()
        self.assertEqual(product_count, 6, f"Expected 6 products, but found {product_count}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()