from appium.webdriver.common.appiumby import AppiumBy

def is_logged_in(driver):
    try:
        driver.find_element(AppiumBy.ID, "com.demo:id/home_title")
        return True
    except Exception:
        return False

def is_error_banner_visible(driver):
    try:
        driver.find_element(AppiumBy.ID, "com.demo:id/error_banner")
        return True
    except Exception:
        return False