# appium_helpers/driver.py
import os, json
from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    # Load capabilities from JSON
    with open(os.path.join(os.path.dirname(__file__), "capabilities.json")) as f:
        caps = json.load(f)

    # Create options object
    options = UiAutomator2Options()
    for key, value in caps.items():
        options.set_capability(key, value)

    # Connect to Appium server
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
    return driver