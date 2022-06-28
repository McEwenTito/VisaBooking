from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from settings import  locators
from settings import config


class ContinueActionsPage(BasePage):

    url = config.LOGIN_URL


    @property
    def reschedule_drop(self):
        locator = Locator(by=By.XPATH, value=locators.reschedule_drop)
        return BaseElement(self.driver, locator)


    @property
    def reschedule_button(self):
        locator = Locator(by=By.XPATH, value=locators.reschedule_button)
        return BaseElement(self.driver, locator)


