from playwright.sync_api import expect
from .base_page import BasePage

class Dashboard(BasePage):
    @property
    def sensors(self):
        return self.page.locator("#sensors-body tr")


    @property
    def sensors_connect_check(self):
        return self.wait_visible(locator =self.sensors.first)


    @property
    def connected_sensors_list(self):
        headers = self.page.get_by_test_id("sensors-table").locator("thead th").all_text_contents()
        if "Sensor ID" not in headers:
            raise AssertionError("'Sensor ID' not found")
        id_col = headers.index("Sensor ID") + 1
        return self.page.locator(f"#sensors-body tr td:nth-child({id_col})").all_text_contents()


    def _sensor_locator(self, sensor_id: str):
        for i in range(self.sensors.count()):
            sensor = self.sensors.nth(i)
            current_id = sensor.locator("td").first.inner_text().strip()
            if current_id == sensor_id:
                return sensor
        raise AssertionError(f"Sensor '{sensor_id}' not found")


    def connected_sensor_value(self, sensor_id: str):
        return  self._sensor_locator(sensor_id).get_by_test_id("sensor-value").inner_text().strip()


    def connected_sensor_last_update(self, sensor_id: str):
        return self._sensor_locator(sensor_id).get_by_test_id("sensor-updated").inner_text().strip()