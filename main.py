# main.py
from ga.evolve import evolve
import plotly.express as px
import pandas as pd
import os, time

def save_report(best_inds, history):
    ts = time.strftime("%Y%m%d-%H%M%S")
    out = f"reports/latest_run/{ts}"
    os.makedirs(out, exist_ok=True)
    df = pd.DataFrame(history, columns=["gen", "max", "avg"])
    fig = px.line(df, x="gen", y=["max","avg"], title="Evolution fitness")
    fig.write_html(os.path.join(out, "fitness.html"))
    with open(os.path.join(out, "best.txt"), "w") as f:
        for ind in best_inds:
            f.write(str(ind) + "\n")

if __name__ == "__main__":
    best, history = evolve()
    save_report(best, history)
    print("Evolution complete. Reports generated.")

# main.py (at the end)
from dashboard.dashboard import open_latest_report

if __name__ == "__main__":
    best, history = evolve()
    print("Evolution complete. Reports generated.")
    open_latest_report()