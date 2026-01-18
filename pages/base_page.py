from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: Locator):
        expect(locator).to_be_visible()
        expect(locator).to_be_enabled()
        locator.click()


    def fill(self, *, locator: Locator, value: str):
        expect(locator).to_be_visible()
        locator.fill(value)

    def wait_visible(self,*, locator: Locator, timeout_ms: int = 2000):
        try:
            locator.wait_for(state="visible", timeout=timeout_ms)
            return True
        except TimeoutError:
            return False


    def wait_seconds(self, time: float):
        self.page.wait_for_timeout(1000 * time)