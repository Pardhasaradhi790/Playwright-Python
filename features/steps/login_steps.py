from behave import given, when, then
from pages.login_page import LoginPage

@given("the user is on the OrangeHRM login page")
def step_impl(context):
    context.login_page = LoginPage(context.page, context.env_config)
    context.login_page.load()

@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@then("the user should be redirected to the dashboard")
def step_impl(context):
    context.page.wait_for_load_state("networkidle")
    assert "dashboard" in context.page.url.lower()
