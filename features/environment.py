import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playwright.sync_api import sync_playwright
from config.environments import ENVIRONMENTS

def before_all(context):
    env_key = context.config.userdata.get("env", "qa")
    if env_key not in ENVIRONMENTS:
        raise ValueError(f"Environment '{env_key}' is not defined in config/environments.py")
    context.env_config = ENVIRONMENTS[env_key]
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def after_all(context):
    context.browser.close()
    context.playwright.stop()

def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()

def after_scenario(context, scenario):
    context.page.close()
    context.browser_context.close()
