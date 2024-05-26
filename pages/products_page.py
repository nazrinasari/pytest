from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class ProductsPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _product_grid = "inventory_container"
    _product_item = ".inventory_item"

    def get_product_count(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, self._product_item)
        return len(products)