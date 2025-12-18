import time
from appium_helpers.actions import tap, input_text, swipe_up
from appium_helpers.driver import get_driver
from utils.vision import is_logged_in, is_error_banner_visible

def run_sequence(chromosome):
    driver = get_driver()
    start = time.time()
    crash = 0
    try:
        for gene in chromosome:
            kind = gene[0]
            if kind == "tap":
                tap(gene[1], driver)
            elif kind == "input":
                input_text(gene[1], gene[2], driver)
            elif kind == "swipe":
                swipe_up(driver)
        latency = time.time() - start
    except Exception:
        crash = 1
        latency = time.time() - start
    finally:
        # Outcome checks before quitting
        success = is_logged_in(driver)
        error = is_error_banner_visible(driver)
        driver.quit()

    # Fitness scoring
    score = 0
    if success:
        score += 10
    if error:
        score -= 5
    score -= crash * 5
    score -= min(latency / 5.0, 3.0)  # small penalty for slow sequences
    score -= len(chromosome) * 0.1    # discourage very long sequences

    return score