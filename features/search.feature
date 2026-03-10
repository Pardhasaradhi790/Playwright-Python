Feature: DuckDuckGo Web Search

  @Test_001
  Scenario: Basic Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "Playwright"
    Then search results are shown for "Playwright"
