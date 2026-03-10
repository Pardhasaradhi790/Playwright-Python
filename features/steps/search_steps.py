from behave import given, when, then
from pages.search_page import SearchPage

@given("the DuckDuckGo home page is displayed")
def step_impl(context):
    context.search_page = SearchPage(context.page, context.env_config)
    context.search_page.load()

@when('the user searches for "{phrase}"')
def step_impl(context, phrase):
    context.search_page.search(phrase)

@then('search results are shown for "{phrase}"')
def step_impl(context, phrase):
    context.page.wait_for_load_state("networkidle")
    assert phrase in context.page.title()
