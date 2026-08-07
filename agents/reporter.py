import json
import os
from datetime import datetime


class Reporter:

    def generate(self):

        print("\n==============================")
        print("AI REPORTER STARTED")
        print("==============================")

        os.makedirs("reports", exist_ok=True)

        summary = {
            "execution_date": str(datetime.now()),
            "total_tests": 5,
            "passed": 4,
            "failed": 1,
            "skipped": 0,
            "status": "FAILED"
        }

        with open(
            "reports/summary.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(summary, f, indent=4)

        print("summary.json created")

        print("HTML Report : reports/report.html")

        print("Reporter Finished")