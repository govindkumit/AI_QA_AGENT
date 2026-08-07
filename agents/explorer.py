import json
import os

from playwright.sync_api import sync_playwright
from config.settings import BASE_URL
from config.settings import HEADLESS
from config.settings import TIMEOUT


class Explorer:

    def explore(self):

        print("\n===============================")
        print("AI EXPLORER STARTED")
        print("===============================\n")

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=HEADLESS
            )

            page = browser.new_page()

            page.set_default_timeout(TIMEOUT)

            print(f"Opening : {BASE_URL}")

            page.goto(BASE_URL)

            application = {}

            application["application"] = page.title()

            application["url"] = page.url

            # ----------------------------
            # INPUTS
            # ----------------------------

            inputs = []

            all_inputs = page.locator("input").all()

            for item in all_inputs:

                inputs.append(
                    {
                        "id": item.get_attribute("id"),
                        "name": item.get_attribute("name"),
                        "type": item.get_attribute("type"),
                        "placeholder": item.get_attribute("placeholder")
                    }
                )

            application["inputs"] = inputs

            # ----------------------------
            # BUTTONS
            # ----------------------------

            buttons = []

            all_buttons = page.locator("button,input[type='submit']").all()

            for item in all_buttons:

                text = item.inner_text()

                if text == "":
                    text = item.get_attribute("value")

                buttons.append(
                    {
                        "text": text,
                        "id": item.get_attribute("id")
                    }
                )

            application["buttons"] = buttons

            # ----------------------------
            # SAVE JSON
            # ----------------------------

            os.makedirs("memory", exist_ok=True)

            with open(
                "memory/application.json",
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(application, f, indent=4)

            browser.close()

        print("\nExplorer Finished")

        print("application.json created successfully")