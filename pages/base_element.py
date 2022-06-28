from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging, datetime

logging.basicConfig(filename=datetime.datetime.now().strftime('logs/app_%H_%M_%d_%m_%Y.log'), level=logging.INFO, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.web_elements = None
        self.find()

    def find(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located(locator=self.locator)
            )
            logging.info(f"Found Element with text: {element.text}")

            elements = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(locator=self.locator)
            )
            logging.info(f"Found Elements with text: {[element.text for element in elements]}")
            self.web_element = element
            self.web_elements = elements

        except Exception as e:
            logging.exception("Failed to find element")

        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(mark=self.locator)
        )
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text

