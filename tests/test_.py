from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
import json
from pathlib import Path


USERS = "files/users.example.json"
LOGIN_PATH = (Path(__file__).resolve().parents[1] / "src" / "scada_demo_ui_page_under_test.html").as_uri()

def test_login_success(page):
    page.goto(f"{LOGIN_PATH}")
    login = LoginPage(page)
    with open(USERS, "r") as f:
        data = json.load(f)
    users = data["users"]
    login.login(username=users[0]["username"],password=users[0]["password"])
    assert (not login.login_fild.is_visible()
            and not login.login_btn.is_visible()
            and not login.login_btn.is_visible())


def test_sensor_connection(correct_login):
    dashboard = correct_login
    assert dashboard.sensors_connect_check



def test_sensor_one_sec_change(sensor_connection_check):
    dashboard = sensor_connection_check
    sensor_one = dashboard.connected_sensors_list
    old_value = dashboard.connected_sensor_value(sensor_one[0])
    dashboard.wait_seconds(1)
    assert old_value != dashboard.connected_sensor_value(sensor_one[0])

