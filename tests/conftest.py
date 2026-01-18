import os

from dotenv import load_dotenv
import pytest
from playwright.sync_api import sync_playwright
from fixtures.fixtures import correct_login, sensor_connection_check

load_dotenv()

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=bool(int(os.getenv("HEADLESS"))))
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()
