import json
import os


class Planner:

    def generate_test_cases(self):

        print("\n==============================")
        print("AI PLANNER STARTED")
        print("==============================")

        application_file = "memory/application.json"

        if not os.path.exists(application_file):
            print("application.json not found.")
            return

        with open(application_file, "r", encoding="utf-8") as file:
            application = json.load(file)

        test_cases = []

        # -----------------------
        # Login Tests
        # -----------------------

        if len(application.get("inputs", [])) >= 2:

            test_cases.append({
                "id": 1,
                "name": "Valid Login",
                "priority": "High",
                "expected": "User should login successfully"
            })

            test_cases.append({
                "id": 2,
                "name": "Invalid Login",
                "priority": "High",
                "expected": "Error message should appear"
            })

            test_cases.append({
                "id": 3,
                "name": "Blank Username",
                "priority": "Medium",
                "expected": "Username validation message"
            })

            test_cases.append({
                "id": 4,
                "name": "Blank Password",
                "priority": "Medium",
                "expected": "Password validation message"
            })

        # -----------------------
        # Button Tests
        # -----------------------

        for button in application.get("buttons", []):

            button_name = button.get("text", "").strip()

            if button_name:

                test_cases.append({
                    "id": len(test_cases) + 1,
                    "name": f"Verify '{button_name}' Button",
                    "priority": "Medium",
                    "expected": f"{button_name} button should work correctly"
                })

        os.makedirs("memory", exist_ok=True)

        with open(
                "memory/testcases.json",
                "w",
                encoding="utf-8"
        ) as file:

            json.dump(
                test_cases,
                file,
                indent=4
            )

        print(f"\n{len(test_cases)} Test Cases Generated")

        print("testcases.json created successfully")

        print("Planner Finished")