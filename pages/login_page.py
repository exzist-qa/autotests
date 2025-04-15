from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.BASIC_LOGIN

    USERNAME_FIELD = ("xpath", "//input[@placeholder='Username']")
    PASSWORD_FIELD = ("xpath", "//input[@placeholder='Password']")
    LOGIN_BUTTON = ("xpath", "//button[text()='Login']")

    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickablele(self.USERNAME_FIELD)).send_keys(login)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickablele(self.PASSWORD_FIELD)).send_keys(password)

    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickablele(self.LOGIN_BUTTON)).click()