from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from locators import ProductPageLocators

class ProductsPage(SeleniumDriver):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def get_product_count(self):
        product_elements = self.getElement(ProductPageLocators.PRODUCTS, locatorType="CLASS_NAME")
        print(product_elements)
        # num_products = len(product_elements)
        # print("Number of products displayed:", num_products)

