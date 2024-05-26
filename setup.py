
from selenium import webdriver
from utils.config_loader import load_config

def setUp(self):
    browser_config, environment_config = load_config()  # Load configuration
    self.baseURL = environment_config['url']

    browser_name = browser_config['name']
    if browser_name.lower() == 'chrome':
        self.driver = webdriver.Chrome()
    elif browser_name.lower() == 'firefox':
        self.driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    self.driver.maximize_window()
    self.driver.implicitly_wait(3)

    self.config = environment_config  # Set config attribute