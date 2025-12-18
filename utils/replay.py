# utils/replay.py
import ast
from appium.webdriver.common.appiumby import AppiumBy

ACTION_ID = AppiumBy.ID

def load_best_sequence(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    # Each line is a Python tuple repr; safely parse
    return [ast.literal_eval(ln) for ln in lines]

def run_action(driver, action):
    kind = action[0]
    if kind == "tap":
        locator = action[1]
        el = driver.find_element(ACTION_ID, locator)
        el.click()
        return True
    elif kind == "input":
        locator, text = action[1], action[2]
        el = driver.find_element(ACTION_ID, locator)
        el.clear()
        el.send_keys(text)
        return True
    elif kind == "swipe":
        # Basic swipe down; tune coordinates to your app
        size = driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.8)
        end_y = int(size["height"] * 0.2)
        driver.swipe(start_x, start_y, start_x, end_y, 400)
        return True
    else:
        return False

def replay_sequence(driver, sequence):
    results = []
    for step in sequence:
        try:
            ok = run_action(driver, step)
            results.append({"step": step, "ok": ok})
        except Exception as e:
            results.append({"step": step, "ok": False, "error": str(e)})
    return results