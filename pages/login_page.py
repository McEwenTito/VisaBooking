from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from settings import  locators
from settings import config


class LoginPage(BasePage):

    url = config.LOGIN_URL


    @property
    def username_input(self):
        locator = Locator(by=By.XPATH, value=locators.username_input)
        return BaseElement(self.driver, locator)

    @property
    def password_input(self):
        locator = Locator(by=By.XPATH, value=locators.password_input)
        return BaseElement(self.driver, locator)

    @property
    def login_button(self):
        locator = Locator(by=By.XPATH, value=locators.login_button)
        return BaseElement(self.driver, locator)

    @property
    def privacy_checkbox(self):
        locator = Locator(by=By.XPATH, value=locators.privacy_checkbox)
        return BaseElement(self.driver, locator)

