import json
from pathlib import Path


class DOMAnalyzer:

    def analyze(self, page):

        inventory = {}

        inventory["title"] = page.title()
        inventory["url"] = page.url

        # -------------------------
        # Inputs
        # -------------------------
        inventory["inputs"] = page.locator("input").evaluate_all(
            """
            els => els.map(e => ({
                type: e.type,
                name: e.name,
                id: e.id,
                placeholder: e.placeholder
            }))
            """
        )

        # -------------------------
        # Buttons
        # -------------------------
        inventory["buttons"] = page.locator("button").evaluate_all(
            """
            els => els.map(e => ({
                text: e.innerText,
                id: e.id
            }))
            """
        )

        # -------------------------
        # Links
        # -------------------------
        inventory["links"] = page.locator("a").evaluate_all(
            """
            els => els.map(e => ({
                text: e.innerText,
                href: e.href
            }))
            """
        )

        # -------------------------
        # Select Dropdowns
        # -------------------------
        inventory["dropdowns"] = page.locator("select").count()

        return inventory

    def save(self, inventory):

        Path("data").mkdir(exist_ok=True)

        with open(
            "data/page_inventory.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                inventory,
                f,
                indent=4
            )