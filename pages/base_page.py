import logging

logging.basicConfig(filename='info.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver
        # logging.info(f"On page {self.url}")

    def go(self):
        print(self.url)
        self.driver.get(self.url)