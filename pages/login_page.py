from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, page, env_config):
        super().__init__(page)
        self.url = env_config["orangehrm_url"]

    def load(self):
        self.navigate(self.url)

    def login(self, username, password):
        self.wait_for_selector(LoginLocators.USERNAME_INPUT)
        self.fill(LoginLocators.USERNAME_INPUT, username)
        self.fill(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)
