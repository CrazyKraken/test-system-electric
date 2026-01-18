import json
import pytest
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from pathlib import Path


USERS = "files/users.example.json"
LOGIN_PATH = (Path(__file__).resolve().parents[1] / "src" / "scada_demo_ui_page_under_test.html").as_uri()

@pytest.fixture
def correct_login(page):
   page.goto(f"{LOGIN_PATH}")
   login = LoginPage(page)
   with open(USERS, "r") as f:
      data = json.load(f)
   users = data["users"]
   login.login(username=users[0]["username"], password=users[0]["password"])
   assert (not login.login_fild.is_visible()
           and not login.login_btn.is_visible()
           and not login.login_btn.is_visible())
   yield Dashboard(page)

@pytest.fixture
def sensor_connection_check(correct_login):
   dashboard = correct_login
   assert dashboard.sensors_connect_check
   yield dashboard

