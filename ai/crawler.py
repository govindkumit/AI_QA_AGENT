from playwright.sync_api import Page


class Crawler:

    def crawl(self, page: Page):

        print("\n" + "=" * 60)
        print("APPLICATION DISCOVERY")
        print("=" * 60)

        print(f"Current Page : {page.title()}")
        print(f"URL          : {page.url}")

        # -----------------------------
        # LINKS
        # -----------------------------
        links = page.locator("a").all()

        print("\nLinks Found")
        print("-" * 30)

        if len(links) == 0:
            print("No Links Found")

        for index, link in enumerate(links, start=1):

            try:
                text = link.inner_text().strip()

                href = link.get_attribute("href")

                print(f"{index}. {text} -> {href}")

            except Exception:
                pass

        # -----------------------------
        # BUTTONS
        # -----------------------------
        buttons = page.locator("button").all()

        print("\nButtons Found")
        print("-" * 30)

        if len(buttons) == 0:
            print("No Buttons Found")

        for index, button in enumerate(buttons, start=1):

            try:

                text = button.inner_text().strip()

                print(f"{index}. {text}")

            except Exception:
                pass

        print("\nApplication Discovery Completed")