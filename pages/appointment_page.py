from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from settings import  locators
from settings import config


class AppointmentPage(BasePage):

    url = config.APPOINTMENT_URL

    @property
    def date_dropdown(self):
        locator = Locator(by=By.XPATH, value=locators.date_dropdown)
        return BaseElement(self.driver, locator)

    @property
    def calender_right_button(self):
        locator = Locator(by=By.XPATH, value=locators.calender_right)
        return BaseElement(self.driver, locator)


    @property
    def free_dates(self):
        locator = Locator(by=By.XPATH, value=locators.free_date)
        return BaseElement(self.driver, locator)

    @property
    def time_drop(self):
        locator = Locator(by=By.XPATH, value=locators.time_drop)
        return BaseElement(self.driver, locator)

    @property
    def time_slot(self):
        locator = Locator(by=By.XPATH, value=locators.time_slot)
        return BaseElement(self.driver, locator)

    @property
    def final_resscchedule(self):
        locator = Locator(by=By.XPATH, value=locators.final_reschedule)
        return BaseElement(self.driver, locator)

    @property
    def confirm_button(self):
        locator = Locator(by=By.XPATH, value=locators.confirm_button)
        return BaseElement(self.driver, locator)





