from selenium import webdriver
from utils.config_loader import load_config

class BaseSetup:
    @classmethod
    def setUpClass(cls):
        browser_config, environment_config = load_config()

        browser_name = browser_config['name']
        if browser_name.lower() == 'chrome':
            cls.driver = webdriver.Chrome()
        elif browser_name.lower() == 'firefox':
            cls.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

        cls.baseURL = environment_config['url']
        cls.config = environment_config

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
