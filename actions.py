import logging, time, datetime
from selenium import webdriver

import retry
from pages.appointment_page import AppointmentPage
from pages.continue_actions_page import ContinueActionsPage
from pages.groups_page import GroupsPage
from pages.login_page import LoginPage
from settings import config, locators, secrets
import sys, importlib, os

logging.basicConfig(filename='info.log', level=logging.INFO, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

try:
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("start-maximized");
    browser = webdriver.Chrome(options=chrome_options)
    browser.set_page_load_timeout(60)
except Exception as e:
    logging.exception(e)


def __scroll_down_page(to=1000):
    browser.execute_script(f"window.scrollTo(0, {to})")


def select_user(user):
    return secrets.users[user]


def login():
    user = select_user("caracand")
    login_page = LoginPage(browser)
    login_page.go()
    __scroll_down_page()
    login_page.username_input.input_text(user["username"])
    login_page.password_input.input_text(user["password"])
    login_page.privacy_checkbox.click()
    login_page.login_button.click()


def groups_continue():
    groups_page = GroupsPage(browser)
    groups_page.continue_button.click()


def reschedule_action():
    actions_page = ContinueActionsPage(browser)
    actions_page.reschedule_drop.click()
    actions_page.reschedule_button.click()


appointment_page = AppointmentPage(browser)


def drop_calender():
    appointment_page.date_dropdown.click()


def move_calender_right():
    appointment_page.calender_right_button.click()


def convert_to_date(date_element):
    date = datetime.datetime(int(date_element.get_attribute("data-year")),
                                    int(date_element.get_attribute("data-month")) + 1, int(date_element.text))
    return str(date.date())


def find_earlier_date():
    print(f"starting find {datetime.datetime.now()}")
    dates = []
    if appointment_page.free_dates.web_elements:
        dates = appointment_page.free_dates.web_elements
        date_dict = {}
        for date in dates:
            date_dict[convert_to_date(date)] = date

        earliest_date = {}
        earliest_date["date"] = min(date_dict.keys())
        earliest_date["element"] = date_dict[min(date_dict.keys())]
        # earliest_date.update({min(date_dict.keys()): date_dict[min(date_dict.keys())]})
        print(earliest_date)
        print(f"got date at {datetime.datetime.now()}")
        return earliest_date

    else:
        print(f"found nothing at {datetime.datetime.now()}, moving on")
        move_calender_right()
        find_earlier_date()



filepath = os.getcwd()
def update_current_date(file_name, date):
    temp_path = filepath + file_name
    with open(file_name, 'w') as f:
        f.write(f'current_date = "{date}"')
    print('Execution completed.')


def book_time_and_reschedule(date):
    appointment_page.time_drop.click()
    appointment_page.time_slot.click()
    appointment_page.final_resscchedule.click()
    # appointment_page.confirm_button.click()
    update_current_date("current.py", date)


def book_earlier_date(current_date, available_date):
    print(available_date)
    if available_date["date"] < current_date:
        available_date["element"].click()
        book_time_and_reschedule(available_date["date"])
        logging.info(f'booking date {available_date}')
    else:
        logging.info(f'current date {current_date} earlier than available date {available_date["date"]}')


