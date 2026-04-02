import json
import os
from datetime import datetime

def generate_report(summary):
    os.makedirs("data/processed", exist_ok=True)

    report = {
        "generated_at": str(datetime.now()),
        "summary": summary
    }

    with open("data/processed/report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Report saved to data/processed/report.json")
