class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)
        
    def wait_for_selector(self, selector):
        self.page.wait_for_selector(selector)
