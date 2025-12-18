# dashboard/dashboard.py
import os, webbrowser

def open_latest_report():
    root = "reports/latest_run"
    latest = sorted(os.listdir(root))[-1]
    path = os.path.abspath(os.path.join(root, latest, "fitness.html"))
    webbrowser.open(f"file:///{path}")

if __name__ == "__main__":
    open_latest_report()