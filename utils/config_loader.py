import configparser

def load_config():
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')

        selected_environment = config['selected_environment']['environment']
        browser_config = dict(config['selected_browser'])
        environment_config = dict(config[selected_environment])

        return browser_config, environment_config
    except (KeyError, FileNotFoundError) as e:
        print(f"Error loading configuration: {e}")
        return None, None