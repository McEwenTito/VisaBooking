import actions
import retry
from settings import config
import current
import time




def run():
    actions.login()
    actions.groups_continue()
    actions.reschedule_action()

    while True:
        try:
            actions.drop_calender()
            actions.find_earlier_date()
            actions.book_earlier_date(current.current_date, actions.find_earlier_date())
            time.sleep(retry.retry_time)
            actions.appointment_page.go()
        except Exception as e:
            print(f"Excepted: {e}")
            run()



if __name__ == '__main__':
    print("We are running!")
    run()


