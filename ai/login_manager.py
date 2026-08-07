from playwright.sync_api import Page


class LoginManager:

    def login(self, page: Page):

        print("\nLogging into application...")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        page.click("#login-button")

        page.wait_for_load_state("networkidle")

        print("Login Successful")