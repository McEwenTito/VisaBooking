from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from settings import  locators
from settings import config


class GroupsPage(BasePage):

    url = config.LOGIN_URL


    @property
    def continue_button(self):
        locator = Locator(by=By.XPATH, value=locators.continue_button)
        return BaseElement(self.driver, locator)


