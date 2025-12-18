import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.replay import load_best_sequence, replay_sequence
from utils.vision import is_logged_in, is_error_banner_visible
from appium_helpers.driver import get_driver  # your existing helper

def find_latest_best():
    root = "reports/latest_run"
    latest = sorted(os.listdir(root))[-1]
    return os.path.join(root, latest, "best.txt")

if __name__ == "__main__":
    best_path = find_latest_best()
    seq = load_best_sequence(best_path)
    driver = get_driver()
    results = replay_sequence(driver, seq)

    print("Replay results:")
    for r in results:
        status = "OK" if r["ok"] else f"FAIL ({r.get('error','')})"
        print(f"- {r['step']}: {status}")

    # Final outcome check with early exit
    if is_logged_in(driver):
        print("\nOutcome: Login SUCCESS ✅")
        driver.quit()
        sys.exit(0)   # <-- ensures script stops here

    elif is_error_banner_visible(driver):
        print("\nOutcome: Error banner shown ❌")
    else:
        print("\nOutcome: No clear login or error state")

    driver.quit()