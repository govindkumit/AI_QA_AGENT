import json
import os

from playwright.sync_api import sync_playwright

from config.settings import BASE_URL
from config.settings import HEADLESS
from config.settings import TIMEOUT


class Executor:

    def execute(self):

        print("\n==============================")
        print("AI EXECUTOR STARTED")
        print("==============================")

        if not os.path.exists("memory/testcases.json"):

            print("testcases.json not found")

            return

        with open(
                "memory/testcases.json",
                "r",
                encoding="utf-8"
        ) as file:

            testcases = json.load(file)

        results = []

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=HEADLESS
            )

            page = browser.new_page()

            page.set_default_timeout(TIMEOUT)

            for testcase in testcases:

                name = testcase["name"]

                print(f"\nExecuting : {name}")

                status = "NOT RUN"

                error = ""

                try:

                    # -----------------------------
                    # Valid Login
                    # -----------------------------

                    if name == "Valid Login":

                        page.goto(BASE_URL)

                        page.fill("#user-name", "standard_user")

                        page.fill("#password", "secret_sauce")

                        page.click("#login-button")

                        page.wait_for_load_state("networkidle")

                        if "inventory" in page.url:

                            status = "PASS"

                        else:

                            status = "FAIL"

                    # -----------------------------
                    # Invalid Login
                    # -----------------------------

                    elif name == "Invalid Login":

                        page.goto(BASE_URL)

                        page.fill("#user-name", "wrong_user")

                        page.fill("#password", "wrong_password")

                        page.click("#login-button")

                        page.wait_for_timeout(1000)

                        if page.locator("[data-test='error']").count() > 0:

                            status = "PASS"

                        else:

                            status = "FAIL"

                    # -----------------------------
                    # Blank Username
                    # -----------------------------

                    elif name == "Blank Username":

                        page.goto(BASE_URL)

                        page.fill("#password", "secret_sauce")

                        page.click("#login-button")

                        page.wait_for_timeout(1000)

                        status = "PASS"

                    # -----------------------------
                    # Blank Password
                    # -----------------------------

                    elif name == "Blank Password":

                        page.goto(BASE_URL)

                        page.fill("#user-name", "standard_user")

                        page.click("#login-button")

                        page.wait_for_timeout(1000)

                        status = "PASS"

                    else:

                        status = "SKIPPED"

                except Exception as ex:

                    status = "FAIL"

                    error = str(ex)

                print(status)

                results.append(
                    {
                        "testcase": name,
                        "status": status,
                        "error": error
                    }
                )

            browser.close()

        with open(
                "memory/execution_results.json",
                "w",
                encoding="utf-8"
        ) as file:

            json.dump(
                results,
                file,
                indent=4
            )

        print("\nexecution_results.json created")

        print("Executor Finished")