# appium/actions.py
from time import sleep

def tap(resource_id, driver):
    el = driver.find_element("id", resource_id)
    el.click(); sleep(0.3)

def input_text(resource_id, text, driver):
    el = driver.find_element("id", resource_id)
    el.clear(); el.send_keys(text); sleep(0.3)

def swipe_up(driver):
    size = driver.get_window_size()
    x = size["width"] // 2
    driver.swipe(x, int(size["height"]*0.8), x, int(size["height"]*0.2), 400); sleep(0.3)