from .base_page import BasePage

class LoginPage(BasePage):
    @property
    def login_btn(self):
        return self.page.locator("#login-btn")

    @property
    def login_fild(self):
        return self.page.locator('#username')

    @property
    def password_fild(self):
        return self.page.locator('#password')

    def login(self,*, username: str, password: str):
        self.fill(locator=self.login_fild, value=username)
        self.fill(locator=self.password_fild, value=password)
        self.click(self.login_btn)