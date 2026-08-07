import json
import os


class Analyzer:

    def analyze(self):

        print("\n==============================")
        print("AI ANALYZER STARTED")
        print("==============================")

        if not os.path.exists("memory/execution_results.json"):

            print("execution_results.json not found")
            return

        with open(
            "memory/execution_results.json",
            "r",
            encoding="utf-8"
        ) as file:

            execution_results = json.load(file)

        bugs = []

        bug_id = 1

        for result in execution_results:

            if result["status"] == "FAIL":

                bug = {
                    "Bug ID": bug_id,
                    "Test Case": result["testcase"],
                    "Severity": "High",
                    "Priority": "High",
                    "Status": "Open",
                    "Reason": result["error"] if result["error"] else "Unexpected application behaviour"
                }

                bugs.append(bug)

                bug_id += 1

        with open(
            "memory/bugs.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                bugs,
                file,
                indent=4
            )

        self.generate_bug_report(bugs)

        print(f"\n{len(bugs)} Bugs Found")

        print("bugs.json created")

        print("AI_Bug_Report.md created")

        print("Analyzer Finished")

    def generate_bug_report(self, bugs):

        with open(
            "reports/AI_Bug_Report.md",
            "w",
            encoding="utf-8"
        ) as report:

            report.write("# AI QA Bug Report\n\n")

            if len(bugs) == 0:

                report.write("## No Bugs Found\n")

                return

            for bug in bugs:

                report.write(f"## Bug {bug['Bug ID']}\n\n")

                report.write(f"**Test Case:** {bug['Test Case']}\n\n")

                report.write(f"**Severity:** {bug['Severity']}\n\n")

                report.write(f"**Priority:** {bug['Priority']}\n\n")

                report.write(f"**Status:** {bug['Status']}\n\n")

                report.write(f"**Reason:** {bug['Reason']}\n\n")

                report.write("---\n\n")