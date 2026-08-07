import json
import os


class Analyzer:

    def analyze(self):

        print("\n==============================")
        print("AI ANALYZER STARTED")
        print("==============================")

        # -------------------------------------------------
        # Create required folders
        # -------------------------------------------------

        os.makedirs("memory", exist_ok=True)
        os.makedirs("reports", exist_ok=True)
        os.makedirs("screenshots", exist_ok=True)

        # -------------------------------------------------
        # Read execution results
        # -------------------------------------------------

        execution_file = "memory/execution_results.json"

        if not os.path.exists(execution_file):

            print("execution_results.json not found.")

            return

        with open(
            execution_file,
            "r",
            encoding="utf-8"
        ) as f:

            execution_results = json.load(f)

        # -------------------------------------------------
        # Analyze Results
        # -------------------------------------------------

        bugs = []

        bug_id = 1

        for result in execution_results:

            status = result.get("status", "").upper()

            if status == "FAIL":

                bug = {

                    "bug_id": f"BUG-{bug_id:03}",

                    "testcase": result.get("testcase"),

                    "status": status,

                    "severity": "High",

                    "priority": "P1",

                    "reason": "Execution Failed",

                    "recommendation": "Investigate application behaviour."

                }

                bugs.append(bug)

                bug_id += 1

        # -------------------------------------------------
        # Save bugs.json
        # -------------------------------------------------

        with open(
            "memory/bugs.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                bugs,
                f,
                indent=4
            )

        print(f"\n{len(bugs)} Bug(s) Found")

        print("bugs.json created")

        # -------------------------------------------------
        # Generate Markdown Report
        # -------------------------------------------------

        self.generate_bug_report(bugs)

        print("AI_Bug_Report.md created")

        print("Analyzer Finished")

    # -----------------------------------------------------

    def generate_bug_report(self, bugs):

        report_file = "reports/AI_Bug_Report.md"

        with open(
            report_file,
            "w",
            encoding="utf-8"
        ) as report:

            report.write("# AI Bug Report\n\n")

            if len(bugs) == 0:

                report.write("## No Bugs Found\n")

                return

            for bug in bugs:

                report.write(f"## {bug['bug_id']}\n\n")

                report.write(f"**Test Case :** {bug['testcase']}\n\n")

                report.write(f"**Status :** {bug['status']}\n\n")

                report.write(f"**Severity :** {bug['severity']}\n\n")

                report.write(f"**Priority :** {bug['priority']}\n\n")

                report.write(f"**Reason :** {bug['reason']}\n\n")

                report.write(
                    f"**Recommendation :** {bug['recommendation']}\n\n"
                )

                report.write("---\n\n")