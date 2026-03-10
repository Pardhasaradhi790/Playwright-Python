from pages.base_page import BasePage
from locators.search_locators import SearchLocators

class SearchPage(BasePage):
    def __init__(self, page, env_config):
        super().__init__(page)
        self.url = env_config["search_url"]

    def load(self):
        self.navigate(self.url)

    def search(self, phrase):
        self.fill(SearchLocators.SEARCH_INPUT, phrase)
        self.page.locator(SearchLocators.SEARCH_INPUT).press("Enter")

    def get_results_count(self):
        self.wait_for_selector(SearchLocators.RESULTS_LOCATOR)
        return self.page.locator(SearchLocators.RESULTS_LOCATOR).count()
