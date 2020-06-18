import time
from datetime import datetime, timedelta
from datetime import timedelta
import calendar
import unittest
import random
from selenium import webdriver
import Check
import Config.Calendar
from Config.Calendar import main_calendar
from main_app_window import Maw, driver_instance
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytz

mgd = Maw.get_devices()
cal = Config.Calendar.main_calendar.Elements
driver_instance.implicitly_wait(5)
wait = WebDriverWait(mgd, 10)
timezone_default = 'Asia/Yekaterinburg'


def setUpModule():
    print('Start: basics_calendar_tests.py\n')


def tearDownModule():
    print('End: basics_calendar_tests.py\n')
    driver_instance.quit()


@unittest.skip('Ok')
class Test1WeekView(unittest.TestCase):
    def setUp(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

    def tearDown(self):
        pass

    def test_week_to_day_view(self):
        Check.check_week_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        Check.check_day_date(cal.navigation_title)

    def test_week_to_month_view(self):
        Check.check_week_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')

        Check.check_month_date(cal.navigation_title)
        current_time = datetime.now()
        today = current_time.strftime("%d")
        if today[0] == '0':
            today = today[1:]
        id_grid_cell = 'grid-month-cell-' + today
        today_grid_cell = mgd.find_element_by_id(id_grid_cell).get_attribute(name='class')
        if 'is-today' in today_grid_cell:
            print('Check - Day in month grid'),
        else:
            raise Exception('Day in month grid is incorrect')

    def test_week_to_year_view(self):
        Check.check_week_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Year View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                raise Exception('Year view is not selectable')

        Check.check_year_date(cal.navigation_title)


@unittest.skip('Ok')
class Test1DayView(unittest.TestCase):
    def setUp(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

    def tearDown(self):
        pass

    def test_day_to_week_view(self):
        Check.check_day_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')
        print('123')
        Check.check_week_date(cal.navigation_title)
        print('456')

    def test_day_to_month_view(self):
        Check.check_day_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')

        Check.check_month_date(cal.navigation_title)
        current_time = datetime.now()
        today = current_time.strftime("%d")
        if today[0] == '0':
            today = today[1:]
        id_grid_cell = 'grid-month-cell-' + today
        today_grid_cell = mgd.find_element_by_id(id_grid_cell).get_attribute(name='class')
        if 'is-today' in today_grid_cell:
            print('Check - Day in month grid'),
        else:
            raise Exception('Day in month grid is incorrect')

    def test_day_to_year_view(self):
        Check.check_day_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Year View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                raise Exception('Year view is not selectable')

        Check.check_year_date(cal.navigation_title)


@unittest.skip('Ok')
class Test1MonthView(unittest.TestCase):
    def setUp(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')

    def tearDown(self):
        pass

    def test_month_to_day_view(self):
        Check.check_month_date(cal.navigation_title)
        current_time = datetime.now()
        today = current_time.strftime("%d")
        if today[0] == '0':
            today = today[1:]
        id_grid_cell = 'grid-month-cell-' + today
        today_grid_cell = mgd.find_element_by_id(id_grid_cell).get_attribute(name='class')
        if 'is-today' in today_grid_cell:
            print('Check - Day in month grid'),
        else:
            raise Exception('Day in month grid is incorrect')

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        Check.check_day_date(cal.navigation_title)

    def test_month_to_week_view(self):
        Check.check_month_date(cal.navigation_title)
        current_time = datetime.now()
        today = current_time.strftime("%d")
        if today[0] == '0':
            today = today[1:]
        id_grid_cell = 'grid-month-cell-' + today
        today_grid_cell = mgd.find_element_by_id(id_grid_cell).get_attribute(name='class')
        if 'is-today' in today_grid_cell:
            print('Check - Day in month grid'),
        else:
            raise Exception('Day in month grid is incorrect')

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        Check.check_week_date(cal.navigation_title)

    def test_month_to_year_view(self):
        Check.check_month_date(cal.navigation_title)
        current_time = datetime.now()
        today = current_time.strftime("%d")
        if today[0] == '0':
            today = today[1:]
        id_grid_cell = 'grid-month-cell-' + today
        today_grid_cell = mgd.find_element_by_id(id_grid_cell).get_attribute(name='class')
        if 'is-today' in today_grid_cell:
            print('Check - Day in month grid'),
        else:
            raise Exception('Day in month grid is incorrect')

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Year View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                raise Exception('Year view is not selectable')

        Check.check_year_date(cal.navigation_title)


@unittest.skip('Ok')
class Test1YearView(unittest.TestCase):
    def setUp(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Year View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                raise Exception('Year view is not selectable')

    def tearDown(self):
        pass

    def test_year_to_day_view(self):
        Check.check_year_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        Check.check_day_date(cal.navigation_title)

    def test_year_to_week_view(self):
        Check.check_year_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        Check.check_week_date(cal.navigation_title)

    def test_year_to_month_view(self):
        Check.check_year_date(cal.navigation_title)

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')

        Check.check_month_date(cal.navigation_title)
        current_time = datetime.now()
        today = current_time.strftime("%d")
        if today[0] == '0':
            today = today[1:]
        id_grid_cell = 'grid-month-cell-' + today
        today_grid_cell = mgd.find_element_by_id(id_grid_cell).get_attribute(name='class')
        if 'is-today' in today_grid_cell:
            print('Check - Day in month grid'),
        else:
            raise Exception('Day in month grid is incorrect')


@unittest.skip('Ok')
class Test2Navigate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

    def setUp(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

    def tearDown(self):
        pass

    def test_day_left_right(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        Check.check_day_date(cal.navigation_title)

        mgd.find_element_by_class_name(cal.navigation_left).click()
        print('Check - Left button')
        Check.check_day_date_minus(cal.navigation_title)

        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')
        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')
        Check.check_day_date_plus(cal.navigation_title)

    def test_week_left_right(self):
        Check.check_week_date(cal.navigation_title)

        mgd.find_element_by_class_name(cal.navigation_left).click()
        print('Check - Left button')
        Check.check_week_date_minus(cal.navigation_title)

        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')
        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')
        Check.check_week_date_plus(cal.navigation_title)

    def test_month_left_right(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')

        Check.check_month_date(cal.navigation_title)
        mgd.find_element_by_class_name(cal.navigation_left).click()
        print('Check - Left button')
        Check.check_month_date_minus(cal.navigation_title)

        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')
        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')
        Check.check_month_date_plus(cal.navigation_title)

    def test_year_left_right(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Year View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                raise Exception('Year view is not selectable')

        Check.check_year_date(cal.navigation_title)
        mgd.find_element_by_class_name(cal.navigation_left).click()
        print('Check - Left button')
        Check.check_year_date_minus(cal.navigation_title)

        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')
        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')
        Check.check_year_date_plus(cal.navigation_title)


# @unittest.skip('Ok')
class Test3CreateNewEventButtonsDelete(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        #
        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        # time.sleep(2)
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Day View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Day View is selected')
        #     else:
        #         raise Exception('Day view is not selectable')
        #
        # mgd.find_element_by_id(cal.add_event_button).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        # print('Check - The event editor is open')

    def tearDown(self):
        driver_instance.implicitly_wait(5)

    def test1_close_editor_button_day_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        mgd.find_element_by_id(cal.close_edit_button).click()
        driver_instance.implicitly_wait(1)
        print(Check.check_exists_by_class_name(cal.edit_event))
        if Check.check_exists_by_class_name(cal.edit_event) == False:
            print('Check - close editor button')
        else:
            raise Exception('The event editor is not closed')

    def test1_close_editor_button_week_view(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        mgd.find_element_by_id(cal.close_edit_button).click()
        driver_instance.implicitly_wait(1)
        print(Check.check_exists_by_class_name(cal.edit_event))
        if Check.check_exists_by_class_name(cal.edit_event) == False:
            print('Check - close editor button')
        else:
            raise Exception('The event editor is not closed')

    def test2_yes_editor_button_day_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        starts = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
        starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
        starts_time_cut = str(starts_time)[11:16]
        event_name = 'Test_event_d ' + starts_time_cut
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        # time.sleep(1)
        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name).click()
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_class_name_and_text(cal.event_name_prvw, event_name)
        print('Check - Event create')

        ##############
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Cancel').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Cancel button')
        else:
            raise Exception('Block wrapper exist')
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')
        ##############
        if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
            print('Check - Event deleted')
        else:
            raise Exception('Event not deleted')

    def test2_yes_editor_button_week_view(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        starts = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
        starts_time_cut = str(starts_time)[11:16]
        event_name = 'Test_event_w ' + starts_time_cut
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        mgd.find_element_by_id(cal.yes_edit_button).click()

        cell_list = Check.find_cell_week_number(starts_time_cut)
        cell = str(cell_list[0]) + '-' + str(cell_list[1])
        xpath = '//*[@id="grid-week-cell-' + cell + '"]/div/div/span[1]'
        mgd.find_element_by_xpath(xpath).click()
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_class_name_and_text(cal.event_name_prvw, event_name)
        print('Check - Event create')

        ##############
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Cancel').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Cancel button')
        else:
            raise Exception('Block wrapper exist')
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')
        ##############
        print(len(mgd.find_elements_by_xpath(xpath)))

    def test2_yes_editor_button_month_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        starts = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
        starts_time_cut = str(starts_time)[11:16]
        event_name = 'Test_event_m ' + starts_time_cut
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        # time.sleep(1)
        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        elem = Check.find_element_by_class_name_and_text(cal.event_name_prvw, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')
        # Check.find_element_by_class_name_and_text(cal.event_name_prvw, event_name).click()
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_class_name_and_text(cal.event_name_prvw, event_name)
        print('Check - Event create')

        ##############
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Cancel').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Cancel button')
        else:
            raise Exception('Block wrapper exist')
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')
        ##############
        if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
            print('Check - Event deleted')
        else:
            raise Exception('Event not deleted')

    def test3_no_apply_unsaved_changes_day_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        event_name = 'Test_event_1_no_d'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)

        mgd.find_element_by_id(cal.close_edit_button).click()

        ##############
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
            print('Check - No button')
        else:
            raise Exception('Block wrapper exist')
        ##############

        driver_instance.implicitly_wait(1)
        print(Check.check_exists_by_class_name(cal.edit_event))
        if Check.check_exists_by_class_name(cal.edit_event) == False:
            print('Check - The event editor is closed')
        else:
            raise Exception('The event editor is not closed')

    def test3_no_apply_unsaved_changes_week_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        event_name = 'Test_event_1_no_w'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)

        mgd.find_element_by_id(cal.close_edit_button).click()

        ##############
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
            print('Check - No button')
        else:
            raise Exception('Block wrapper exist')
        ##############

        driver_instance.implicitly_wait(1)
        print(Check.check_exists_by_class_name(cal.edit_event))
        if Check.check_exists_by_class_name(cal.edit_event) == False:
            print('Check - The event editor is closed')
        else:
            raise Exception('The event editor is not closed')

    def test3_cancel_apply_unsaved_changes_day_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        event_name = 'Test_event_1_cancel_d'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)

        mgd.find_element_by_id(cal.close_edit_button).click()

        ##############
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Cancel').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
            print('Check - Cancel button')
        else:
            raise Exception('Block wrapper exist')

        mgd.find_element_by_id(cal.close_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
            print('Check - No button')
        else:
            raise Exception('Block wrapper exist')
        ##############

        driver_instance.implicitly_wait(1)
        print(Check.check_exists_by_class_name(cal.edit_event))
        if Check.check_exists_by_class_name(cal.edit_event) == False:
            print('Check - The event editor is closed')
        else:
            raise Exception('The event editor is not closed')

    def test3_cancel_apply_unsaved_changes_week_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        event_name = 'Test_event_1_cancel_w'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)

        mgd.find_element_by_id(cal.close_edit_button).click()

        ##############
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Cancel').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
            print('Check - Cancel button')
        else:
            raise Exception('Block wrapper exist')

        mgd.find_element_by_id(cal.close_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
            print('Check - No button')
        else:
            raise Exception('Block wrapper exist')
        ##############

        driver_instance.implicitly_wait(1)
        print(Check.check_exists_by_class_name(cal.edit_event))
        if Check.check_exists_by_class_name(cal.edit_event) == False:
            print('Check - The event editor is closed')
        else:
            raise Exception('The event editor is not closed')

    def test3_yes_apply_unsaved_changes_day_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Day View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                raise Exception('Day view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')
        starts = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
        starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
        starts_time_cut = str(starts_time)[11:16]
        event_name = 'Test_event_1_yes_d'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)

        mgd.find_element_by_id(cal.close_edit_button).click()

        ##############
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Yes').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
            print('Check - Yes button')
        else:
            raise Exception('Block wrapper exist')
        ##############
        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        print(Check.check_exists_by_class_name(cal.edit_event))
        if Check.check_exists_by_class_name(cal.edit_event) == False:
            print('Check - The event editor is closed')
        else:
            raise Exception('The event editor is not closed')

        Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name).click()
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_class_name_and_text(cal.event_name_prvw, event_name)
        print('Check - Event create')

        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')

    def test3_yes_apply_unsaved_changes_week_view(self):
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.add_event_button).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
        print('Check - The event editor is open')

        starts = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
        starts_time_cut = str(starts_time)[11:16]
        event_name = 'Test_event_1_yes_w'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)

        mgd.find_element_by_id(cal.close_edit_button).click()

        ##############
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Yes').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
            print('Check - Yes button')
        else:
            raise Exception('Block wrapper exist')
        ##############
        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        driver_instance.implicitly_wait(1)
        print(Check.check_exists_by_class_name(cal.edit_event))
        if Check.check_exists_by_class_name(cal.edit_event) == False:
            print('Check - The event editor is closed')
        else:
            raise Exception('The event editor is not closed')

        cell_list = Check.find_cell_week_number(starts_time_cut)
        cell = str(cell_list[0]) + '-' + str(cell_list[1])
        xpath = '//*[@id="grid-week-cell-' + cell + '"]/div/div/span[1]'
        mgd.find_element_by_xpath(xpath).click()
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_class_name_and_text(cal.event_name_prvw, event_name)
        print('Check - Event create')

        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')


@unittest.skip('Ok')
class Test4StartsEndsDrum(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            if Check.check_exists_by_id(cal.close_edit_button):
                mgd.find_element_by_id(cal.close_edit_button).click()
            if Check.check_exists_by_class_name(cal.apply_unsaved_changes):
                print('Block wrapper "Apply unsaved changes" - exist')
                mgd.find_element_by_xpath(cal.no_apply_unsaved_changes).click()

            mgd.find_element_by_class_name(cal.today_button).click()
            view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                view_button.click()
                view_button_select = view_button.get_attribute(name='class')
                if 'selected' in view_button_select:
                    print('Check - Week View is selected')
                else:
                    raise Exception('Week view is not selectable')

            mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                view_button.click()
                view_button_select = view_button.get_attribute(name='class')
                if 'selected' in view_button_select:
                    print('Check - Day View is selected')
                else:
                    raise Exception('Day view is not selectable')

        @classmethod
        def tearDownClass(cls):
            pass

        def setUp(self):
            mgd.find_element_by_id(cal.add_event_button).click()
            wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
            print('Check - window Edit event is open\n')

        def tearDown(self):
            if Check.check_exists_by_id(cal.close_edit_button):
                mgd.find_element_by_id(cal.close_edit_button).click()
            if Check.check_exists_by_class_name(cal.apply_unsaved_changes):
                print('Block wrapper "Apply unsaved changes" - exist')
                mgd.find_element_by_xpath(cal.no_apply_unsaved_changes).click()

        def test2_drum_starts_hours_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=60)
            time_delta_2 = timedelta(hours=11)
            modify_time = starts_time_1 + time_delta
            modify_time_2 = starts_time_1 - time_delta_2
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_hours)
            first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if second_value == '12':
                if modify_time_2 == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif second_value != '12':
                if modify_time == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_ends_hours_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=60)
            time_delta_2 = timedelta(hours=11)
            modify_time = ends_time_1 + time_delta
            modify_time_2 = ends_time_1 - time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_hours)
            first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

            if second_value == '12':
                if modify_time_2 == ends_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif second_value != '12':
                if modify_time == ends_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_starts_minutes_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=5)
            modify_time = starts_time_1 + time_delta
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_minutes)
            first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_minutes_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=5)
            modify_time = ends_time_1 + time_delta
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_minutes)
            first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

            if modify_time == ends_time_2:
                print('Check - Ends time is right')
            else:
                raise Exception('Ends time is incorrect')

        def test2_drum_starts_hours_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=60)
            time_delta_2 = timedelta(hours=11)
            modify_time = starts_time_1 - time_delta
            modify_time_2 = starts_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_hours)
            first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_hours_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
            time.sleep(1)

            second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            if second_value == '11':
                if modify_time_2 == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif second_value != '11':
                if modify_time == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_ends_hours_up(self):

            now_timezone = mgd.find_element_by_xpath(cal.timezone).get_attribute('innerText')
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(hours=1)
            time_delta_2 = timedelta(hours=11)
            modify_time = ends_time_1 - time_delta
            modify_time_2 = ends_time_1 - time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_hours)
            first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_hours_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')

            drum_container = mgd.find_element_by_id(cal.drum_container).get_attribute(name='data-value')
            print('drum_container ', drum_container)
            drum_container_time = datetime.strptime(drum_container[:19], "%Y-%m-%dT%H:%M:%S")
            container_time_tz = drum_container_time.astimezone(pytz.timezone(now_timezone))
            print('tz name ', datetime.tzname(container_time_tz))
            print('drum_container_time ', drum_container_time)
            print('ends_time_1 ', ends_time_1)
            print('container_time_tz ', container_time_tz)
            modify_time = ends_time_1 - time_delta
            print('modify_time ', modify_time)
            if container_time_tz == modify_time:
                print('container_time_tz == modify_time - YES')
            else:
                print('container_time_tz == modify_time - NO')

        def test2_drum_starts_minutes_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=5)
            time_delta_2 = timedelta(minutes=55)
            modify_time = starts_time_1 - time_delta
            modify_time_2 = starts_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_minutes)
            first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if second_value == '55':
                if modify_time_2 == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif second_value != '55':
                if modify_time == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_ends_minutes_up(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=5)
            time_delta_2 = timedelta(minutes=55)
            modify_time = ends_time_1 - time_delta
            modify_time_2 = ends_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_minutes)
            first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

            if second_value == '55':
                if modify_time_2 == ends_time_2:
                    print('Check - Ends time is right')
                else:
                    raise Exception('Ends time is incorrect')
            elif second_value != '55':
                if modify_time == ends_time_2:
                    print('Check - Ends time is right')
                else:
                    raise Exception('Ends time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_starts_am_pm(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(hours=12)
            modify_time = starts_time_1 + time_delta
            modify_time_2 = starts_time_1 - time_delta
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_ampm)
            first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            if first_value == 'AM':
                hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_down)
                actions = ActionChains(driver_instance)

                actions.move_to_element(hover_drum).click().perform()

                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                try:
                    actions.click(hidden_arrow).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                time.sleep(1)
                second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('second_value', second_value)
                ############
                if second_value == 'PM':
                    print('Check - change of value')
                else:
                    raise Exception('The value is the same')
                mgd.find_element_by_id(cal.yes_edit_button).click()
                time.sleep(1)
                starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

                if second_value == 'PM':
                    if modify_time == starts_time_2:
                        print('Check - Starts time is right')
                    else:
                        raise Exception('Starts time is incorrect')
                else:
                    raise Exception('Something went wrong')

                # second
                mgd.find_element_by_xpath(cal.starts_day_view).click()
                hover_drum = mgd.find_element_by_id(cal.drum_ampm)
                first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('first_value', first_value)
                if first_value == 'PM':
                    hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
                    actions = ActionChains(driver_instance)

                    actions.move_to_element(hover_drum).click().perform()

                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                    try:
                        actions.click(hidden_arrow).perform()
                    except:
                        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                    time.sleep(1)
                    second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                    print('second_value', second_value)
                    ############
                    if second_value == 'AM':
                        print('Check - change of value')
                    else:
                        raise Exception('The value is the same')
                    mgd.find_element_by_id(cal.yes_edit_button).click()
                    time.sleep(1)
                    starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                    starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

                    if second_value == 'AM':
                        if starts_time_1 == starts_time_2:
                            print('Check - Starts time is right')
                        else:
                            raise Exception('Starts time is incorrect')
                    else:
                        raise Exception('Something went wrong')
                else:
                    raise Exception('Wrong interval')
            elif first_value == 'PM':
                hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
                actions = ActionChains(driver_instance)

                actions.move_to_element(hover_drum).click().perform()

                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                try:
                    actions.click(hidden_arrow).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                time.sleep(1)
                second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('second_value', second_value)
                ############
                if second_value == 'AM':
                    print('Check - change of value')
                else:
                    raise Exception('The value is the same')
                mgd.find_element_by_id(cal.yes_edit_button).click()
                time.sleep(1)
                starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

                if second_value == 'AM':
                    if modify_time_2 == starts_time_2:
                        print('Check - Starts time is right')
                    else:
                        raise Exception('Starts time is incorrect')
                else:
                    raise Exception('Something went wrong')

                # second
                mgd.find_element_by_xpath(cal.starts_day_view).click()
                hover_drum = mgd.find_element_by_id(cal.drum_ampm)
                first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('first_value', first_value)
                if first_value == 'AM':
                    hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_down)
                    actions = ActionChains(driver_instance)

                    actions.move_to_element(hover_drum).click().perform()

                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                    try:
                        actions.click(hidden_arrow).perform()
                    except:
                        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                    time.sleep(1)
                    second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                    print('second_value', second_value)
                    ############
                    if second_value == 'PM':
                        print('Check - change of value')
                    else:
                        raise Exception('The value is the same')
                    mgd.find_element_by_id(cal.yes_edit_button).click()
                    time.sleep(1)
                    starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                    starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

                    if second_value == 'PM':
                        print(modify_time)
                        print(modify_time_2)

                        if starts_time_1 == starts_time_2:
                            print('Check - Starts time is right')
                        else:
                            raise Exception('Starts time is incorrect')
                    else:
                        raise Exception('Something went wrong')
                else:
                    raise Exception('Wrong interval')
            else:
                raise Exception('Something went wrong')

        def test2_drum_ends_am_pm(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(hours=12)
            modify_time = ends_time_1 + time_delta
            modify_time_2 = ends_time_1 - time_delta
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_ampm)
            first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            if first_value == 'AM':
                hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_down)
                actions = ActionChains(driver_instance)

                actions.move_to_element(hover_drum).click().perform()

                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                try:
                    actions.click(hidden_arrow).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                time.sleep(1)
                second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('second_value', second_value)
                ############
                if second_value == 'PM':
                    print('Check - change of value')
                else:
                    raise Exception('The value is the same')
                time.sleep(1)
                yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                if 'disabled' in yes_button_attr:
                    print('Check - Yes button not disabled')
                else:
                    raise Exception('For Yes button "disabled" is missing')
                message = 'The date should be after'
                error_message = mgd.find_element_by_class_name(cal.data_error_drum).get_attribute('innerText')
                if message not in error_message:
                    raise Exception('Error message not found', 'error_message -', error_message)
                print('Check - error message')

                # second
                mgd.find_element_by_xpath(cal.ends_day_view).click()
                hover_drum = mgd.find_element_by_id(cal.drum_ampm)
                first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('first_value', first_value)
                if first_value == 'PM':
                    hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
                    actions = ActionChains(driver_instance)

                    actions.move_to_element(hover_drum).click().perform()

                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                    try:
                        actions.click(hidden_arrow).perform()
                    except:
                        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                    time.sleep(1)
                    second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                    print('second_value', second_value)
                    ############
                    if second_value == 'AM':
                        print('Check - change of value')
                    else:
                        raise Exception('The value is the same')
                    yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                    if 'disabled' in yes_button_attr:
                        print('Check - Yes button not disabled')
                    else:
                        raise Exception('For Yes button "disabled" is missing')
                    Check.find_element_by_class_name_and_text(cal.data_error_drum, 'The date should be after')
                    print('Check - error message')
                    # mgd.find_element_by_id(cal.yes_edit_button).click()
                    # time.sleep(1)
                    # ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
                    # ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

                #     if second_value == 'AM':
                #         if ends_time_1 == ends_time_2:
                #             print('Check - 2Ends time is right')
                #         else:
                #             raise Exception('Ends time is incorrect')
                #     else:
                #         raise Exception('Something went wrong')
                # else:
                #     raise Exception('Wrong interval')
            elif first_value == 'PM':
                hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
                actions = ActionChains(driver_instance)

                actions.move_to_element(hover_drum).click().perform()

                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                try:
                    actions.click(hidden_arrow).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                time.sleep(1)
                second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('second_value', second_value)
                ############
                if second_value == 'AM':
                    print('Check - change of value')
                else:
                    raise Exception('The value is the same')
                yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                if 'disabled' in yes_button_attr:
                    print('Check - Yes button disabled')
                else:
                    raise Exception('For Yes button "disabled" is missing')
                Check.find_element_by_class_name_and_text(cal.data_error_drum, 'The date should be after')
                print('Check - error message')
                # mgd.find_element_by_id(cal.yes_edit_button).click()
                # time.sleep(1)
                # ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
                # ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
                #
                # if second_value == 'AM':
                #     if modify_time_2 == ends_time_2:
                #         print('Check - 3Ends time is right')
                #     else:
                #         raise Exception('Ends time is incorrect')
                # else:
                #     raise Exception('Something went wrong')

                # second

                # mgd.find_element_by_xpath(cal.ends_day_view).click()
                hover_drum = mgd.find_element_by_id(cal.drum_ampm)
                first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('first_value', first_value)
                if first_value == 'AM':
                    hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_down)
                    actions = ActionChains(driver_instance)

                    actions.move_to_element(hover_drum).click().perform()

                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                    try:
                        actions.click(hidden_arrow).perform()
                    except:
                        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                    time.sleep(1)
                    second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                    print('second_value', second_value)
                    ############
                    if second_value == 'PM':
                        print('Check - change of value')
                    else:
                        raise Exception('The value is the same')
                    yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                    if 'disabled' in yes_button_attr:
                        raise Exception('Check - Yes button not disabled')

                    if Check.find_element_by_class_name_and_text(
                            cal.data_error_drum, 'The date should be after') is not None:
                        raise Exception('Error message exist')

                    mgd.find_element_by_id(cal.yes_edit_button).click()
                    time.sleep(1)
                    ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
                    ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

                    if second_value == 'PM':
                        print(modify_time)
                        print(modify_time_2)

                        if ends_time_1 == ends_time_2:
                            print('Check - 4Ends time is right')
                        else:
                            raise Exception('Ends time is incorrect')
                    else:
                        raise Exception('Something went wrong')
                else:
                    raise Exception('Wrong interval')
            else:
                raise Exception('Something went wrong')

        def test2_drum_starts_day_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1)
            time_delta_2 = timedelta(days=11)
            modify_time = starts_time_1 + time_delta
            modify_time_2 = starts_time_1 - time_delta
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_day)
            first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')
            #
            # if second_value == '12':
            #     if modify_time_2 == starts_time_2:
            #         print('Check - Starts time is right')
            #     else:
            #         raise Exception('Starts time is incorrect')
            # elif second_value != '12':
            #     if modify_time == starts_time_2:
            #         print('Check - Starts time is right')
            #     else:
            #         raise Exception('Starts time is incorrect')
            # else:
            #     raise Exception('Something went wrong')

        def test2_drum_ends_day_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1)
            time_delta_2 = timedelta(days=11)
            modify_time = ends_time_1 + time_delta
            modify_time_2 = ends_time_1 - time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_day)
            first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

            if modify_time == ends_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

            # if second_value == '12':
            #     if modify_time_2 == ends_time_2:
            #         print('Check - Starts time is right')
            #     else:
            #         raise Exception('Starts time is incorrect')
            # elif second_value != '12':
            #     if modify_time == ends_time_2:
            #         print('Check - Starts time is right')
            #     else:
            #         raise Exception('Starts time is incorrect')
            # else:
            #     raise Exception('Something went wrong')

        def test2_drum_starts_day_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1)
            time_delta_2 = timedelta(days=1)
            modify_time = starts_time_1 - time_delta
            modify_time_2 = starts_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_day)
            first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
            time.sleep(1)

            second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_day_up(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1)
            time_delta_2 = timedelta(days=11)
            modify_time = ends_time_1 - time_delta
            modify_time_2 = ends_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_day)
            first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
            if 'disabled' in yes_button_attr:
                print('Check - Yes button disabled')
            else:
                raise Exception('For Yes button "disabled" is missing')
            Check.find_element_by_class_name_and_text(cal.data_error_drum, 'The date should be after')
            # mgd.find_element_by_id(cal.yes_edit_button).click()
            # time.sleep(1)
            # ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            # ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
            #
            # if modify_time == ends_time_2:
            #     print('Check - Starts time is right')
            # else:
            #     raise Exception('Starts time is incorrect')

            # if second_value == '12':
            #     if modify_time_2 == ends_time_2:
            #         print('Check - Starts time is right')
            #     else:
            #         raise Exception('Starts time is incorrect')
            # elif second_value != '12':
            #     if modify_time == ends_time_2:
            #         print('Check - Starts time is right')
            #     else:
            #         raise Exception('Starts time is incorrect')
            # else:
            #     raise Exception('Something went wrong')

        def test2_drum_starts_month_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=4)
            modify_time = starts_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_month)
            first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(starts_time_2)
            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_month_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=4)
            modify_time = ends_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_month)
            first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(ends_time_2)
            if modify_time == ends_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_starts_month_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=4)
            modify_time = starts_time_1 - time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_month)
            first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
            time.sleep(1)

            second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(starts_time_2)
            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_month_up(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=4)
            modify_time = ends_time_1 - time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_month)
            first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
            if 'disabled' in yes_button_attr:
                print('Check - Yes button disabled')
            else:
                raise Exception('For Yes button "disabled" is missing')
            Check.find_element_by_class_name_and_text(cal.data_error_drum, 'The date should be after')
            # mgd.find_element_by_id(cal.yes_edit_button).click()
            # time.sleep(1)
            # ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            # ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
            # modify_time = modify_time.replace(day=int(today_day))
            # print(modify_time)
            # print(ends_time_2)
            # if modify_time == ends_time_2:
            #     print('Check - Starts time is right')
            # else:
            #     raise Exception('Starts time is incorrect')

        def test2_drum_starts_year_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=52)
            modify_time = starts_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_year)
            first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(starts_time_2)
            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_year_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=52)
            modify_time = ends_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_year)
            first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(ends_time_2)
            if modify_time == ends_time_2:
                print('Check - Ends time is right')
            else:
                raise Exception('Ends time is incorrect')

        def test2_drum_starts_year_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=2608)
            modify_time = starts_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_year)
            first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_year_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(starts_time_2)
            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_year_up(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=2608)
            modify_time = ends_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_year)
            first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_year_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(ends_time_2)
            if modify_time == ends_time_2:
                print('Check - Ends time is right')
            else:
                raise Exception('Ends time is incorrect')


# @unittest.skip('Ok')
class Test6RepeatedEvents(unittest.TestCase):
    def setUp(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

    def tearDown(self):
        # driver_instance.implicitly_wait(1)
        name = 'Test6RepEvent_'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        now_data = current_time.strftime('%Y %m %d')
        split = now_data.split(' ')
        now_data_year = split[0]
        now_data_month = split[1]
        now_data_day = split[2]
        if now_data_month[0] == '0':
            now_data_month = now_data_month[1:]
        if now_data_day[0] == '0':
            now_data_day = now_data_day[1:]

        if now_day[0] == '0':
            now_day = now_day[1:]

        block_overlay_xpath = '//*[@id="place-button-add"]/div[1]'
        block_overlay = mgd.find_element_by_xpath(block_overlay_xpath).get_attribute(name='style')
        if 'display: block' in block_overlay:
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions = ActionChains(driver_instance)
            actions.move_to_element(element).move_by_offset(-10, -10).click().perform()
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?'):
                print('Check - Block wrapper')
                Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()
                driver_instance.implicitly_wait(1)
                if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Apply unsaved changes?') is None:
                    print('Check - No button')
                else:
                    raise Exception('Block wrapper exist')
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)

        i = 0
        while i <= 6:
            event_name = name + str(i)

            cell_list = Check.find_cell_week_number(now_time)
            cell_mod = cell_list[0] + i
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
            # if Check.find_element_by_css_selector_and_text(css_name, event_name) == None:
            #     print('1', Check.find_element_by_css_selector_and_text(css_name, event_name))
            #     time.sleep(2)
            i += 1
            if Check.find_element_by_css_selector_and_text(css_name, event_name) is not None:
                print('2', Check.find_element_by_css_selector_and_text(css_name, event_name))
                mgd.find_element_by_id(id_elem).click()

                mgd.find_element_by_class_name(cal.delete_prvw).click()
                Check.find_element_by_class_name_and_text(cal.block_wrapper,
                                                          'Update single appointment or the whole sequence?')
                print('Check - Block wrapper')
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
                if Check.find_element_by_class_name_and_text(
                        cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
                    print('Check - Delete button')
                else:
                    raise Exception('Block wrapper exist')
                if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
                    print('Check - Event deleted')
                else:
                    raise Exception('Event not deleted')
        # driver_instance.implicitly_wait(5)

    @classmethod
    def setUpClass(cls):
        pass
        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected\n')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        #
        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))

    @classmethod
    def tearDownClass(cls):
        pass
        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        #
        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        # time.sleep(2)
        #
        # #############
        # # add delete for all event
        # #############

    def test1_create_rep_event_every_day(self):
        event_name = 'Test6RepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0]) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        # mgd.find_element_by_class_name(cal.event_preview)
        # print('Check - Event preview is open')
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        # добавить проверки для каждоо дня \\ done
        Check.event_in_cells(event_name, 30, cell)
        print('Check - Event sequence')

        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        # time.sleep(1)
        # css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        # if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
        #     time.sleep(2)
        # mgd.find_element_by_id(id_elem).click()
        #
        # mgd.find_element_by_class_name(cal.delete_prvw).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        # if Check.find_element_by_class_name_and_text(
        #         cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
        # if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
        #     print('Check - Event deleted')
        # else:
        #     raise Exception('Event not deleted')

    def test2_create_rep_event_custom(self):
        event_name = 'Test6RepEvent_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Week').click()
        if now_week != '6':
            if now_week != '7':
                Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'Custom').click()

        day_of_week_option = 'day-of-week-option-'
        id_elem_day_of_week_now = day_of_week_option + now_week
        day_of_week_selected = mgd.find_element_by_id(id_elem_day_of_week_now).get_attribute(name="class")
        if 'selected' in day_of_week_selected:
            print('Check - Today is selected')
        else:
            raise Exception('Today not selected')
        mgd.find_element_by_id(id_elem_day_of_week_now).click()
        if 'selected' in day_of_week_selected:
            print('Check - Today is selected')
        else:
            raise Exception('Today not selected')

        sequence = [0, 1, 2, 3, 4, 5, 6]
        sequence.remove(int(now_week))
        day_1 = random.choice(sequence)
        print('d1', day_1)
        sequence.remove(day_1)
        day_2 = random.choice(sequence)
        print('d2', day_2)
        sequence.remove(day_2)
        day_3 = random.choice(sequence)
        print('d3', day_3)
        sequence.remove(day_3)

        day_index = list()
        day_index.append(int(now_week))
        day_index.append(int(day_1))
        day_index.append(int(day_2))
        day_index.append(int(day_3))

        for day_i in day_index:
            id_elem_day_of_week_now = day_of_week_option + str(day_i)
            mgd.find_element_by_id(id_elem_day_of_week_now).click()

        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        day_index.sort()
        time.sleep(2)
        Check.event_in_cells_custom(event_name, day_index, 30, cell)

        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        # time.sleep(1)
        # css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        # if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
        #     time.sleep(2)
        # mgd.find_element_by_id(id_elem).click()
        #
        # mgd.find_element_by_class_name(cal.delete_prvw).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        # if Check.find_element_by_class_name_and_text(
        #         cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
        # if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
        #     print('Check - Event deleted')
        # else:
        #     raise Exception('Event not deleted')

    def test3_create_rep_event_weekdays(self):
        event_name = 'Test6RepEvent_2'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)
        if int(now_week) == 6 or int(now_week) == 7:
            raise Exception('Today this repeat mod inactive')

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 2
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Week').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On weekdays')

        day_index = list([1, 2, 3, 4, 5])

        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        day_index.sort()
        time.sleep(2)
        Check.event_in_cells_custom(event_name, day_index, 30, cell)

        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        # time.sleep(1)
        # css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        # if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
        #     time.sleep(2)
        # mgd.find_element_by_id(id_elem).click()
        #
        # mgd.find_element_by_class_name(cal.delete_prvw).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        # if Check.find_element_by_class_name_and_text(
        #         cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
        # if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
        #     print('Check - Event deleted')
        # else:
        #     raise Exception('Event not deleted')

    def test4_create_rep_event_on_day_of_month(self):
        event_name = 'Test6RepEvent_3'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 3
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Month').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of month')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')

        month_selector = '#grid-month-cell-' + now_day + ' .subject'

        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')

        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()

        Check.event_in_cells_month(event_name, 12, month_selector)

        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        # time.sleep(1)
        # css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        # if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
        #     time.sleep(2)
        # mgd.find_element_by_id(id_elem).click()
        #
        # mgd.find_element_by_class_name(cal.delete_prvw).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        # if Check.find_element_by_class_name_and_text(
        #         cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
        # if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
        #     print('Check - Event deleted')
        # else:
        #     raise Exception('Event not deleted')

    def test5_create_rep_event_on_day_of_week(self):
        event_name = 'Test6RepEvent_4'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        now_data = current_time.strftime('%Y %m %d')
        split = now_data.split(' ')
        print(split)
        now_data_year = split[0]
        now_data_month = split[1]
        now_data_day = split[2]
        if now_data_month[0] == '0':
            now_data_month = now_data_month[1:]
        if now_data_day[0] == '0':
            now_data_day = now_data_day[1:]

        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 4
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Month').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of week').click()
        empty = []
        if mgd.find_elements_by_xpath(cal.on_day_of_week) == empty:
            day_of_week = mgd.find_element_by_xpath(cal.on_day_of_week_four).get_attribute('innerText')
            print('day_of_week_four', day_of_week)
        else:
            day_of_week = mgd.find_element_by_xpath(cal.on_day_of_week).get_attribute('innerText')
            print('day_of_week', day_of_week)
        if mgd.find_elements_by_xpath(cal.number_day_of_week) == empty:
            number_day_of_week = mgd.find_element_by_xpath(cal.number_day_of_week_four).get_attribute('innerText')
            print('number_day_of_week_four', number_day_of_week)
        else:
            number_day_of_week = mgd.find_element_by_xpath(cal.number_day_of_week).get_attribute('innerText')
            print('number_day_of_week', number_day_of_week)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')
        driver_instance.implicitly_wait(5)
        value = 0
        while value < 15:

            month_title = mgd.find_element_by_class_name(cal.navigation_title).get_attribute('innerText')
            month_title_list = month_title.split(' ')
            print('month_title_list', month_title_list)
            new_month_year = month_title_list[1]
            new_month_month_abbr = month_title_list[0]
            #
            new_month_month = time.strptime(new_month_month_abbr, '%b').tm_mon
            print('new_month_year', new_month_year)
            print('new_month_month', new_month_month)
            if len(str(new_month_month)) == 1:
                new_month_month = '0' + str(new_month_month)
            print('new_month_month', new_month_month)

            month_cell = Check.day_of_week_in_month(str(new_month_year), new_month_month, number_day_of_week, day_of_week)

            month_cell_selector = '#grid-month-cell-' + str(month_cell) + ' .subject'
            print('month_cell_selector', month_cell_selector)
            time.sleep(1)
            elem = Check.find_element_by_css_selector_and_text(month_cell_selector, event_name)
            if elem is None:
                raise Exception('ERRRRRRROR')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            value += 1
            mgd.find_element_by_class_name(cal.navigation_right).click()
            print('Check - Right button')

        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        # time.sleep(1)
        # css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        # if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
        #     time.sleep(2)
        # mgd.find_element_by_id(id_elem).click()
        #
        # mgd.find_element_by_class_name(cal.delete_prvw).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        # if Check.find_element_by_class_name_and_text(
        #         cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
        # if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
        #     print('Check - Event deleted')
        # else:
        #     raise Exception('Event not deleted')

    def test6_create_rep_event_on_date(self):
        event_name = 'Test6RepEvent_5'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        now_data = current_time.strftime('%Y %m %d')
        split = now_data.split(' ')
        print(split)
        now_data_year = split[0]
        now_data_month = split[1]
        now_data_day = split[2]
        if now_data_month[0] == '0':
            now_data_month = now_data_month[1:]
        if now_data_day[0] == '0':
            now_data_day = now_data_day[1:]

        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 5
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Year').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On date').click()
        on_date_date = mgd.find_element_by_xpath(cal.on_date).get_attribute('innerText')
        print('on_date_date', on_date_date)
        date = on_date_date.split(' ')
        date_month = date[0]
        print('date_month', date_month)
        date_day = date[1][:-2]
        print('date_day', date_day)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value = 0
        while value <= 10:
            view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                view_button.click()
                view_button_select = view_button.get_attribute(name='class')
                if 'selected' in view_button_select:
                    print('Check - Year View is selected')
                else:
                    raise Exception('Year view is not selectable')

            mgd.find_element_by_class_name(cal.navigation_right).click()
            print('Check - Right button')

            mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            print('date_month -3:', date_month[:3])
            Check.find_element_by_class_name_and_text(cal.month_title_year_view, date_month[:3].upper()).click()

            month_selector = '#grid-month-cell-' + date_day + ' .subject'

            elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
            if elem is None:
                raise Exception('ERRRRRRROR')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            value += 1

        ##################################################################
        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        # time.sleep(1)
        # css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        # if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
        #     time.sleep(2)
        # mgd.find_element_by_id(id_elem).click()
        #
        # mgd.find_element_by_class_name(cal.delete_prvw).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        # if Check.find_element_by_class_name_and_text(
        #         cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
        # if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
        #     print('Check - Event deleted')
        # else:
        #     raise Exception('Event not deleted')

    def test7_create_rep_event_year_on_day_of_week(self):
        event_name = 'Test6RepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        now_data = current_time.strftime('%Y %m %d')
        split = now_data.split(' ')
        print(split)
        now_data_year = split[0]
        now_data_month = split[1]
        now_data_day = split[2]
        if now_data_month[0] == '0':
            now_data_month = now_data_month[1:]
        if now_data_day[0] == '0':
            now_data_day = now_data_day[1:]

        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 6
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Year').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of week').click()
        empty = []
        if mgd.find_elements_by_xpath(cal.year_on_day_of_week) == empty:
            year_on_day_of_week = mgd.find_element_by_xpath(cal.year_on_day_of_week_four).get_attribute('innerText')
            print('year_on_day_of_week', year_on_day_of_week)
        else:
            year_on_day_of_week = mgd.find_element_by_xpath(cal.year_on_day_of_week).get_attribute('innerText')
            print('year_on_day_of_week', year_on_day_of_week)
        if mgd.find_elements_by_xpath(cal.year_number_day_of_week) == empty:
            year_number_day_of_week = mgd.find_element_by_xpath(cal.year_number_day_of_week_four).get_attribute('innerText')
            print('year_number_day_of_week_four', year_number_day_of_week)
        else:
            year_number_day_of_week = mgd.find_element_by_xpath(cal.year_number_day_of_week).get_attribute('innerText')
            print('year_number_day_of_week', year_number_day_of_week)

        year_day_of_week_month = mgd.find_element_by_xpath(cal.year_day_of_week_month).get_attribute('innerText')
        print('year_day_of_week_month', year_day_of_week_month)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(5)
        value = 0
        while value <= 10:
            view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                view_button.click()
                view_button_select = view_button.get_attribute(name='class')
                if 'selected' in view_button_select:
                    print('Check - Year View is selected')
                else:
                    raise Exception('Year view is not selectable')

            mgd.find_element_by_class_name(cal.navigation_right).click()
            print('Check - Right button')

            mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)
            #######################################
            print('year_day_of_week_month 3', year_day_of_week_month[:3])
            Check.find_element_by_class_name_and_text(cal.month_title_year_view, year_day_of_week_month[:3].upper()).click()
            ##############

            month_title = mgd.find_element_by_class_name(cal.navigation_title).get_attribute('innerText')
            month_title_list = month_title.split(' ')
            print('month_title_list', month_title_list)
            new_month_year = month_title_list[1]
            new_month_month_abbr = month_title_list[0]
            #
            new_month_month = time.strptime(new_month_month_abbr, '%b').tm_mon
            print('new_month_year', new_month_year)
            print('new_month_month', new_month_month)
            if len(str(new_month_month)) == 1:
                new_month_month = '0' + str(new_month_month)
            print('new_month_month', new_month_month)

            month_cell = Check.day_of_week_in_month(
                str(new_month_year), new_month_month, year_number_day_of_week, year_on_day_of_week)

            month_cell_selector = '#grid-month-cell-' + str(month_cell) + ' .subject'
            time.sleep(1)
            elem = Check.find_element_by_css_selector_and_text(month_cell_selector, event_name)
            time.sleep(1)
            if elem is None:
                raise Exception('ERRRRRRROR')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()

            value += 1

        ##################################################################
        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        # time.sleep(1)
        # css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        # if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
        #     time.sleep(2)
        # mgd.find_element_by_id(id_elem).click()
        #
        # mgd.find_element_by_class_name(cal.delete_prvw).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        # if Check.find_element_by_class_name_and_text(
        #         cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
        # if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
        #     print('Check - Event deleted')
        # else:
        #     raise Exception('Event not deleted')


# @unittest.skip('Ok')
class Test7Alerts(unittest.TestCase):
    def setUp(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview) != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Yes').click()


    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test1_alerts(self):
        event_name = 'TestAlerts'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        count = 1
        cell_count = 1
        while count != 7:
            print('Alert count', count)
            print('cell_count', cell_count)
            cell_list = Check.find_cell_week_number(now_time)
            if cell_count == 1:
                plus_number = 1
                cell_count += 1
            elif cell_count == 2:
                plus_number = 2
                cell_count += 1
            elif cell_count == 3:
                plus_number = 3
                cell_count += 1
            elif cell_count == 4:
                plus_number = 4
                cell_count = 1
            print('plus_number', plus_number)
            cell_mod = cell_list[0] + plus_number
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'The event has been deleted on another device') is not None:
                mgd.find_element_by_xpath(cal.overlay).click()
                mgd.find_element_by_id(id_elem).click()
            mgd.find_element_by_id(cal.title_input).send_keys(event_name + str(count))

            Check.find_element_by_class_name_and_text(cal.title_class, 'Alert').click()
            xpath_alert = mgd.find_element_by_xpath(
                '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(count) + ']/div[1]')
            actions = ActionChains(driver_instance)
            actions.move_to_element(xpath_alert).click().perform()
            alert_name = xpath_alert.get_attribute('innerText')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            alert_value = mgd.find_element_by_xpath(cal.alert_value).get_attribute('innerText')
            if alert_name == alert_value:
                print('Check - Alert value:', alert_value)
            else:
                raise Exception('Wrong Alert Value')

            mgd.find_element_by_id(cal.yes_edit_button).click()
            mgd.find_element_by_id(id_elem).click()
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'The event has been deleted on another device') is not None:
                mgd.find_element_by_xpath(cal.overlay).click()
            alert_prvw = Check.find_element_by_class_name_and_text('value', alert_name)
            alert_value_prvw = alert_prvw.get_attribute('innerText')
            if alert_name == alert_value_prvw:
                print('Check - Alert value prvw:', alert_value_prvw)
            else:
                raise Exception('Wrong Alert Value prvw')

            mgd.find_element_by_class_name(cal.delete_prvw).click()
            Check.find_element_by_class_name_and_text(cal.block_wrapper,
                                                      'Delete this event?')
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            if Check.find_element_by_class_name_and_text(
                    cal.block_wrapper, 'Delete this event?') is None:
                print('Check - Delete button')
            else:
                raise Exception('Block wrapper exist')
            # time.sleep(2)
            mgd.find_element_by_id(cal.spinner).click()
            print('Spinner click')
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            css = '#' + id_elem + ' > div > div > span:nth-child(1)'
            count += 1

    def test2_alerts(self):
        event_name = 'TestAlerts'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        count = 8
        cell_count = 1
        while count != 23:
            print('Alert count', count)
            print('cell_count', cell_count)
            cell_list = Check.find_cell_week_number(now_time)
            if cell_count == 1:
                plus_number = 1
                cell_count += 1
            elif cell_count == 2:
                plus_number = 2
                cell_count += 1
            elif cell_count == 3:
                plus_number = 3
                cell_count += 1
            elif cell_count == 4:
                plus_number = 4
                cell_count = 1
            print('plus_number', plus_number)
            cell_mod = cell_list[0] + plus_number
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'The event has been deleted on another device') is not None:
                mgd.find_element_by_xpath(cal.overlay).click()
                mgd.find_element_by_id(id_elem).click()
            mgd.find_element_by_id(cal.title_input).send_keys(event_name + str(count))

            Check.find_element_by_class_name_and_text(cal.title_class, 'Alert').click()
            xpath_alert = mgd.find_element_by_xpath(
                '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(count) + ']/div[1]')
            actions = ActionChains(driver_instance)
            actions.move_to_element(xpath_alert).click().perform()
            alert_name = xpath_alert.get_attribute('innerText')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            alert_value = mgd.find_element_by_xpath(cal.alert_value).get_attribute('innerText')
            if alert_name == alert_value:
                print('Check - Alert value:', alert_value)
            else:
                raise Exception('Wrong Alert Value')

            mgd.find_element_by_id(cal.yes_edit_button).click()
            mgd.find_element_by_id(id_elem).click()
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'The event has been deleted on another device') is not None:
                mgd.find_element_by_xpath(cal.overlay).click()
            alert_prvw = Check.find_element_by_class_name_and_text('value', alert_name)
            alert_value_prvw = alert_prvw.get_attribute('innerText')
            if alert_name == alert_value_prvw:
                print('Check - Alert value prvw:', alert_value_prvw)
            else:
                raise Exception('Wrong Alert Value prvw')

            mgd.find_element_by_class_name(cal.delete_prvw).click()
            Check.find_element_by_class_name_and_text(cal.block_wrapper,
                                                      'Delete this event?')
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            if Check.find_element_by_class_name_and_text(
                    cal.block_wrapper, 'Delete this event?') is None:
                print('Check - Delete button')
            else:
                raise Exception('Block wrapper exist')
            # time.sleep(2)
            mgd.find_element_by_id(cal.spinner).click()
            print('Spinner click')
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            css = '#' + id_elem + ' > div > div > span:nth-child(1)'
            count += 1

    def test3_alerts(self):
        event_name = 'TestAlerts'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        count = 24
        cell_count = 1
        while count != 31:
            print('Alert count', count)
            print('cell_count', cell_count)
            cell_list = Check.find_cell_week_number(now_time)
            if cell_count == 1:
                plus_number = 1
                cell_count += 1
            elif cell_count == 2:
                plus_number = 2
                cell_count += 1
            elif cell_count == 3:
                plus_number = 3
                cell_count += 1
            elif cell_count == 4:
                plus_number = 4
                cell_count = 1
            print('plus_number', plus_number)
            cell_mod = cell_list[0] + plus_number
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'The event has been deleted on another device') is not None:
                mgd.find_element_by_xpath(cal.overlay).click()
                mgd.find_element_by_id(id_elem).click()
            mgd.find_element_by_id(cal.title_input).send_keys(event_name + str(count))

            Check.find_element_by_class_name_and_text(cal.title_class, 'Alert').click()
            xpath_alert = mgd.find_element_by_xpath(
                '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(count) + ']/div[1]')
            actions = ActionChains(driver_instance)
            actions.move_to_element(xpath_alert).click().perform()
            alert_name = xpath_alert.get_attribute('innerText')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            alert_value = mgd.find_element_by_xpath(cal.alert_value).get_attribute('innerText')
            if alert_name == alert_value:
                print('Check - Alert value:', alert_value)
            else:
                raise Exception('Wrong Alert Value')

            mgd.find_element_by_id(cal.yes_edit_button).click()
            mgd.find_element_by_id(id_elem).click()
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'The event has been deleted on another device') is not None:
                mgd.find_element_by_xpath(cal.overlay).click()
            alert_prvw = Check.find_element_by_class_name_and_text('value', alert_name)
            alert_value_prvw = alert_prvw.get_attribute('innerText')
            if alert_name == alert_value_prvw:
                print('Check - Alert value prvw:', alert_value_prvw)
            else:
                raise Exception('Wrong Alert Value prvw')

            mgd.find_element_by_class_name(cal.delete_prvw).click()
            Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
                print('Check - Delete button')
            else:
                raise Exception('Block wrapper exist')
            # time.sleep(2)
            mgd.find_element_by_id(cal.spinner).click()
            print('Spinner click')
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            css = '#' + id_elem + ' > div > div > span:nth-child(1)'
            count += 1


# @unittest.skip('Ok')
class Test7Invitees(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        pass

    def test1_invitees(self):
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        event_name = 'TestEventInvitees_', now_time
        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 5
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        Check.find_element_by_class_name_and_text(cal.no_invitees, 'There are no invitees')
        print('Check - Text: There are no invitees')
        mgd.find_element_by_class_name(cal.plus_icon).click()
        mgd.find_element_by_class_name(cal.contact_items)
        print('Check - invitees items')
        Check.find_element_by_class_name_and_text(cal.contact_name, 'AAAppolo').click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.block_wrapper)))
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Close').click()
        search_input = 'exadel2'
        mgd.find_element_by_class_name(cal.contact_search).send_keys(search_input)
        time.sleep(1)
        xpath = '//*[@id="contactList"]/li/a/div'
        xpath2 = '//*[@id="contactList"]/li[2]/a/div'
        xpath3 = '//*[@id="contactList"]/li[3]/a/div'
        elem = mgd.find_element_by_xpath(xpath)
        elem.click()
        mgd.find_element_by_class_name(cal.clear_search).click()
        mgd.find_element_by_class_name(cal.contact_search).send_keys('contact for')
        time.sleep(1)
        mgd.find_element_by_xpath(xpath).click()
        mgd.find_element_by_xpath(xpath2).click()
        mgd.find_element_by_xpath(xpath3).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.email_invitees, 'exadel2@botf03.net')
        len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        print('len_of_list', len_of_list)
        if len_of_list != 4:
            raise Exception('Not all contacts added')
        garbage1 = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/i'
        garbage2 = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/i'
        garbage3 = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/i'
        garbage4 = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[4]/div[2]/div/i'
        email_in_1_row = mgd.find_element_by_xpath(
            '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[1]/div[1]/div').get_attribute(
            'innerText')
        email_in_2_row = mgd.find_element_by_xpath(
            '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[2]/div[1]/div').get_attribute(
            'innerText')
        email_in_3_row = mgd.find_element_by_xpath(
            '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[3]/div[1]/div').get_attribute(
            'innerText')
        email_in_4_row = mgd.find_element_by_xpath(
            '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[4]/div[1]/div').get_attribute(
            'innerText')
        mgd.find_element_by_xpath(garbage4).click()
        mgd.find_element_by_xpath(garbage2).click()
        time.sleep(1)
        new_len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        print('new_len_of_list', new_len_of_list)
        if new_len_of_list != 2:
            raise Exception('Contacts not deleted')

        new_email_in_1_row = mgd.find_element_by_xpath(
            '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[1]/div[1]/div').get_attribute(
            'innerText')
        new_email_in_2_row = mgd.find_element_by_xpath(
            '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[2]/div[1]/div').get_attribute(
            'innerText')

        if new_email_in_1_row != email_in_1_row:
            raise Exception('First email incorrect')
        if new_email_in_2_row != email_in_3_row:
            raise Exception('Second email incorrect')

        mgd.find_element_by_id(cal.yes_edit_button).click()
        if  Check.find_element_by_class_name_and_text(cal.invitees_count, '2') == []:
            raise Exception('Wrong number of contacts')
        note = now_time + ' auto-test for invitees'
        mgd.find_element_by_id(cal.notes_input).send_keys(note)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        if Check.find_element_by_class_name_and_text(cal.invitees_count, '2') == []:
            raise Exception('Wrong number of contacts')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        print('len_of_list', len_of_list)
        if len_of_list != 2:
            raise Exception('Wrong number of contacts in the list')
        mgd.find_element_by_xpath(garbage1).click()
        time.sleep(1)
        new_len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        print('new_len_of_list', new_len_of_list)
        if new_len_of_list != 1:
            raise Exception('Contacts not deleted')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        if Check.find_element_by_class_name_and_text(cal.invitees_count, '1') == []:
            raise Exception('Wrong number of contacts')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        print('len_of_list', len_of_list)
        if len_of_list != 1:
            raise Exception('Wrong number of contacts in the list')
        mgd.find_element_by_id(cal.close_edit_button).click()
        mgd.find_element_by_id(cal.delete_event_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Cancel').click()
        print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?'))
        driver_instance.implicitly_wait(1)
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Cancel button')
        else:
            raise Exception('Block wrapper exist')
        mgd.find_element_by_id(cal.delete_event_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')


# @unittest.skip('Ok')
class Test8EditSingleEvents(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview) != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Yes').click()

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')    # @unittest.skip('Ok')

    def test1_1single_event_location(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()

        mgd.find_element_by_id(cal.edit_prvw).click()
        location_name = 'Morrowind'
        time.sleep(1)
        mgd.find_element_by_id(cal.location_input).send_keys(location_name)
        mgd.find_element_by_id(cal.yes_edit_button).click()

        mgd.find_element_by_id(id_elem).click()
        time.sleep(1)
        location_preview = mgd.find_element_by_class_name(cal.location_prvw).get_attribute('innerText')
        print('location_preview', location_preview)
        if location_name != location_preview:
            raise Exception('Invalid Location preview')
        mgd.find_element_by_id(cal.edit_prvw).click()
        location_input = mgd.find_element_by_id(cal.location_input).get_attribute(name='value')
        if location_input != location_name:
            raise Exception('Location is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_1single_event_notes(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        notes_text = 'The Nerevar will come!'
        time.sleep(1)
        mgd.find_element_by_id(cal.notes_input).send_keys(notes_text)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(id_elem).click()
        time.sleep(1)
        notes_preview = mgd.find_element_by_class_name(cal.notes_prvw).get_attribute('innerText')
        if notes_text != notes_preview:
            raise Exception('Invalid Notes preview')
        mgd.find_element_by_id(cal.edit_prvw).click()
        notes_input = mgd.find_element_by_id(cal.notes_input).get_attribute('value')
        print('notes_input', notes_input)
        if notes_text != notes_input:
            raise Exception('Notes is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_1single_event_timezone(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        timezone_base = mgd.find_element_by_xpath(cal.timezone_value).get_attribute('innerText')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Timezone').click()
        Check.find_element_by_class_name_and_text(cal.time_zones_name, 'Asia/Colombo (UTC+05:30)').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        timezone_first = mgd.find_element_by_xpath(cal.timezone_value).get_attribute('innerText')
        if timezone_base == timezone_first:
            raise Exception('Timezone still the same')
        if timezone_first != 'Asia/Colombo':
            raise Exception('Timezone does not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        cell_m = str(cell_mod - 1) + '-0'
        id_elem_mod = 'grid-week-cell-' + cell_m + ''
        mgd.find_element_by_id(id_elem_mod).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        timezone_second = mgd.find_element_by_xpath(cal.timezone_value).get_attribute('innerText')
        if timezone_first != timezone_second:
            raise Exception('Timezone still the same')

        Check.find_element_by_class_name_and_text(cal.title_class, 'Timezone').click()
        Check.find_element_by_class_name_and_text(cal.time_zones_name, 'Asia/Yekaterinburg (UTC+05:00)').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        timezone_third = mgd.find_element_by_xpath(cal.timezone_value).get_attribute('innerText')
        if timezone_second == timezone_third:
            raise Exception('Timezone still the same')
        if timezone_third != timezone_base:
            raise Exception('Timezone does not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_1single_event_alert(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Alert').click()
        Check.find_element_by_class_name_and_text(cal.alert_title, '1 hour').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        alert_value = mgd.find_element_by_xpath(cal.alert_value).get_attribute('innerText')
        if alert_value != '1 hour':
            raise Exception('Wrong Alert')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        prvw_xpath = '//*[@id="tooltip-container-undefined"]/div/div[2]/div[2]/div[2]'
        alert_value_prvw = mgd.find_element_by_xpath(prvw_xpath).get_attribute('innerText')
        print('alert_value_prvw', alert_value_prvw)
        if alert_value_prvw != alert_value:
            raise Exception('Wrong prvw Alert', '1', alert_value_prvw, '2',  alert_value)
        mgd.find_element_by_id(cal.edit_prvw).click()
        alert_value_2 = mgd.find_element_by_xpath(cal.alert_value).get_attribute('innerText')
        if alert_value != alert_value_2:
            raise Exception('Alert does not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_2single_event_invitees(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        Check.find_element_by_class_name_and_text(cal.no_invitees, 'There are no invitees')
        print('Check - Text: There are no invitees')
        mgd.find_element_by_class_name(cal.plus_icon).click()
        driver_instance.implicitly_wait(1)
        mgd.find_element_by_class_name(cal.contact_items)
        print('Check - invitees items')
        driver_instance.implicitly_wait(5)
        Check.find_element_by_class_name_and_text(cal.contact_name, 'Contact for autotest 1').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.email_invitees, '1cont@autotest.ab')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        if Check.find_element_by_class_name_and_text(cal.invitees_count, '1') == []:
            raise Exception('Wrong number of contacts')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        if Check.find_element_by_class_name_and_text(cal.invitees_count, '1') == []:
            raise Exception('Wrong number of contacts')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        Check.find_element_by_class_name_and_text(cal.email_invitees, '1cont@autotest.ab')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_1single_event_color(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        css_elem = '#' + id_elem + '> div > div'
        css_color_attribute = mgd.find_element_by_css_selector(css_elem).get_attribute(name='class')
        css_color_split = css_color_attribute.split(' ')
        color_default_grid = css_color_split[1].lower()
        print('color_default_grid - ', color_default_grid)

        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        color_attribute_edit_event = mgd.find_element_by_class_name(cal.color_field).get_attribute(name='class')
        color_split_edit_event = color_attribute_edit_event.split(' ')
        color_default_edit_event = color_split_edit_event[1].lower()
        print('color_default_edit_event - ', color_default_edit_event)
        if color_default_grid != color_default_edit_event:
            raise Exception('Color does not match')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Color').click()
        number_of_colors = len(mgd.find_elements_by_class_name(cal.timezone_text_class))
        print('number_of_colors', number_of_colors)
        new_color_number = random.randrange(1, number_of_colors, 1)
        print('new_color_number', new_color_number)
        color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(new_color_number) + ']'
        mgd.find_element_by_xpath(color_xpath).click()
        name_color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(new_color_number) + ']/div[2]/div'
        new_color_name = mgd.find_element_by_xpath(name_color_xpath).get_attribute(name='class')
        new_color_name_split = new_color_name.split(' ')
        new_color = new_color_name_split[1].lower()
        print('new_color', new_color)
        while new_color == color_default_grid:
            new_color_number = random.randrange(1, number_of_colors, 1)
            print('new_color_number', new_color_number)
            color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(
                new_color_number) + ']'
            mgd.find_element_by_xpath(color_xpath).click()
            name_color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(
                new_color_number) + ']/div[1]'
            new_color_name = mgd.find_element_by_xpath(name_color_xpath).get_attribute('innerText')
            new_color_name_split = new_color_name.split(' ')
            new_color = new_color_name_split[0].lower()
            print('new_color', new_color)

        mgd.find_element_by_id(cal.yes_edit_button).click()
        color_new_attribute_edit_event = mgd.find_element_by_class_name(cal.color_field).get_attribute(name='class')
        color_new_split_edit_event = color_new_attribute_edit_event.split(' ')
        color_new_default_edit_event = color_new_split_edit_event[1].lower()
        print('color_new_default_edit_event', color_new_default_edit_event)
        if new_color != color_new_default_edit_event:
            raise Exception('Color does not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        css_new_color_attribute = mgd.find_element_by_css_selector(css_elem).get_attribute(name='class')
        css_new_color_split = css_new_color_attribute.split(' ')
        color_new_grid = css_new_color_split[1].lower()
        print('color_new_grid - ', color_new_grid)
        if color_new_grid != new_color:
            raise Exception('Color does not match')

    # @unittest.skip('Ok')
    def test1_3single_event_starts_date_day(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_1 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
        time_delta = timedelta(days=1)
        modify_time = starts_time_1 + time_delta
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        # mgd.find_element_by_xpath(cal.starts_other_view).click()

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        starts_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
        if modify_time == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        cell_2 = str(cell_mod) + '-1'
        id_elem_2 = 'grid-week-cell-' + cell_2 + ''
        mgd.find_element_by_id(id_elem_2).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_3 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_3 = datetime.strptime(starts_3, "%d %b %Y %I:%M %p")
        if starts_time_3 == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        starts_4 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_4 = datetime.strptime(starts_4, "%d %b %Y %I:%M %p")
        if starts_time_4 == starts_time_1:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_5 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_5 = datetime.strptime(starts_5, "%d %b %Y %I:%M %p")
        if starts_time_4 == starts_time_5:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_3single_event_starts_date_month(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_1 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
        starts_split = starts_1.split(' ')
        starts_year = starts_split[2]
        print('starts_year', starts_year)
        starts_month = time.strptime(starts_split[1], '%b').tm_mon
        print('starts_month', starts_month)
        days_in_month = calendar.monthrange(int(starts_year), int(starts_month))
        print('days_in_month', days_in_month)
        time_delta = timedelta(days=days_in_month[1])
        modify_time = starts_time_1 + time_delta
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        starts_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
        day_from_starts = starts_time_2.strftime('%d')
        if day_from_starts[0] == '0':
            day_from_starts = day_from_starts[1]
        print('day_from_starts', day_from_starts)
        if modify_time == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        # cell_2 = str(cell_mod) + '-0'
        # id_elem_2 = 'grid-week-cell-' + cell_2 + ''
        # mgd.find_element_by_id(id_elem_2).click()

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')
        mgd.find_element_by_class_name(cal.navigation_right).click()
        month_selector = '#grid-month-cell-' + day_from_starts + ' .subject'

        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')

        # actions = ActionChains(driver_instance)
        # element = mgd.find_element_by_xpath(cal.overlay)
        # actions.move_to_element(element).move_by_offset(-450, -300).click().perform()

        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_3 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_3 = datetime.strptime(starts_3, "%d %b %Y %I:%M %p")
        if starts_time_3 == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        starts_4 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_4 = datetime.strptime(starts_4, "%d %b %Y %I:%M %p")
        if starts_time_4 == starts_time_1:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_5 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_5 = datetime.strptime(starts_5, "%d %b %Y %I:%M %p")
        if starts_time_4 == starts_time_5:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_3single_event_starts_date_year(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_1 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
        starts_split = starts_1.split(' ')
        starts_year = starts_split[2]
        print('starts_year', starts_year)
        starts_month = time.strptime(starts_split[1], '%b').tm_mon
        print('starts_month', starts_month)
        days_in_month = calendar.monthrange(int(starts_year), int(starts_month))
        print('days_in_month', days_in_month)
        # time_delta = timedelta(days=days_in_month[1])
        # modify_time = starts_time_1 + time_delta
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        starts_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
        starts_2_split = starts_2.split(' ')
        starts_2_year = starts_2_split[2]
        print('starts_year', starts_year)
        # starts_2_month_int = time.strptime(starts_2_split[1], '%b').tm_mon
        starts_2_month = starts_2_split[1]

        print('starts_month', starts_month)
        # days_in_month = calendar.monthrange(int(starts_2_year), int(starts_2_month_int))
        # print('days_in_month', days_in_month)

        day_from_starts = starts_time_2.strftime('%d')
        if day_from_starts[0] == '0':
            day_from_starts = day_from_starts[1]
        print('day_from_starts', day_from_starts)
        # if modify_time == starts_time_2:
        #     print('Check - Starts time is right')
        # else:
        #     raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Year View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                raise Exception('Year view is not selectable')

        mgd.find_element_by_class_name(cal.navigation_right).click()
        print('Check - Right button')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        print('starts_2_month', starts_2_month)
        Check.find_element_by_class_name_and_text(cal.month_title_year_view, starts_2_month.upper()).click()

        month_selector = '#grid-month-cell-' + day_from_starts + ' .subject'

        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')

        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_3 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_3 = datetime.strptime(starts_3, "%d %b %Y %I:%M %p")
        if starts_time_3 == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        starts_4 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_4 = datetime.strptime(starts_4, "%d %b %Y %I:%M %p")
        if starts_time_4 == starts_time_1:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_5 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_5 = datetime.strptime(starts_5, "%d %b %Y %I:%M %p")
        if starts_time_4 == starts_time_5:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_3single_event_ends_date_month(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_1 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
        ends_split = ends_1.split(' ')
        ends_year = ends_split[2]
        print('ends_year', ends_year)
        ends_month = time.strptime(ends_split[1], '%b').tm_mon
        print('ends_month', ends_month)
        days_in_month = calendar.monthrange(int(ends_year), int(ends_month))
        print('days_in_month', days_in_month)
        time_delta = timedelta(days=days_in_month[1])
        modify_time = ends_time_1 + time_delta
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        ends_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
        day_from_ends = ends_time_2.strftime('%d')
        if day_from_ends[0] == '0':
            day_from_ends = day_from_ends[1]
        print('day_from_ends', day_from_ends)
        if modify_time == ends_time_2:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        # cell_2 = str(cell_mod) + '-0'
        # id_elem_2 = 'grid-week-cell-' + cell_2 + ''
        # mgd.find_element_by_id(id_elem_2).click()

        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Month View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Month View is selected')
        #     else:
        #         raise Exception('Month view is not selectable')
        # mgd.find_element_by_class_name(cal.navigation_right).click()
        # month_selector = '#grid-month-cell-' + day_from_ends + ' .subject'
        #
        # elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        # if elem is None:
        #     raise Exception('ERRRRRRROR')
        # time.sleep(1)
        # actions = ActionChains(driver_instance)
        # actions.move_to_element(elem).click().perform()
        # print('Check - Event in cell')

        # actions = ActionChains(driver_instance)
        # element = mgd.find_element_by_xpath(cal.overlay)
        # actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        ends_3 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_3 = datetime.strptime(ends_3, "%d %b %Y %I:%M %p")
        if ends_time_3 == ends_time_2:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        ends_4 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_4 = datetime.strptime(ends_4, "%d %b %Y %I:%M %p")
        if ends_time_4 == ends_time_1:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button_select = view_button.get_attribute(name='class')
        # if 'selected' in view_button_select:
        #     print('Check - Week View is selected')
        # else:
        #     view_button.click()
        #     view_button_select = view_button.get_attribute(name='class')
        #     if 'selected' in view_button_select:
        #         print('Check - Week View is selected')
        #     else:
        #         raise Exception('Week view is not selectable')
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_5 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_5 = datetime.strptime(ends_5, "%d %b %Y %I:%M %p")
        if ends_time_4 == ends_time_5:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_3single_event_ends_date_day(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_1 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
        time_delta = timedelta(days=1)
        modify_time = ends_time_1 + time_delta
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        ends_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
        if modify_time == ends_time_2:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        # cell_2 = str(cell_mod) + '-1'
        # id_elem_2 = 'grid-week-cell-' + cell_2 + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        ends_3 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_3 = datetime.strptime(ends_3, "%d %b %Y %I:%M %p")
        if ends_time_3 == ends_time_2:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        ends_4 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_4 = datetime.strptime(ends_4, "%d %b %Y %I:%M %p")
        if ends_time_4 == ends_time_1:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_5 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_5 = datetime.strptime(ends_5, "%d %b %Y %I:%M %p")
        if ends_time_4 == ends_time_5:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_3single_event_ends_date_year(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_1 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
        ends_split = ends_1.split(' ')
        ends_year = ends_split[2]
        print('ends_year', ends_year)
        ends_month = time.strptime(ends_split[1], '%b').tm_mon
        print('ends_month', ends_month)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        ends_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
        day_from_ends = ends_time_2.strftime('%d')
        if day_from_ends[0] == '0':
            day_from_ends = day_from_ends[1]
        print('day_from_ends', day_from_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        ends_3 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_3 = datetime.strptime(ends_3, "%d %b %Y %I:%M %p")
        if ends_time_3 == ends_time_2:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        ends_4 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_4 = datetime.strptime(ends_4, "%d %b %Y %I:%M %p")
        if ends_time_4 == ends_time_1:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_5 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_5 = datetime.strptime(ends_5, "%d %b %Y %I:%M %p")
        if ends_time_4 == ends_time_5:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_3single_event_starts_time(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_up)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
        time.sleep(1)

        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

        cell_1 = str(cell_mod - 2) + '-0'
        id_elem_mod_1 = 'grid-week-cell-' + cell_1 + ''

        mgd.find_element_by_id(id_elem_mod_1).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # print('date_prvw_mod', date_prvw_mod)
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        if value_time_for_compare not in date_prvw_mod:
            raise Exception('Wrong Time preview')
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
        #################
        time.sleep(1)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(2)

        cell_2 = str(cell_mod + 0) + '-0'
        id_elem_mod_2 = 'grid-week-cell-' + cell_2 + ''

        mgd.find_element_by_id(id_elem_mod_2).click()
        # actions = ActionChains(driver_instance)
        # element = mgd.find_element_by_id(id_elem_mod_2).click()
        # actions.move_to_element(element).move_by_offset(5, 13).click().perform()

        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        if value_time_for_compare not in date_prvw_mod:
            raise Exception('Wrong Time preview')
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()

        ############
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        ############
        time.sleep(1)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        if value_time_for_compare not in date_prvw_mod:
            raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_3single_event_ends_time(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        time.sleep(1)

        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

        # cell_1 = str(cell_mod + 2) + '-0'
        # id_elem_mod_1 = 'grid-week-cell-' + cell_1 + ''

        # mgd.find_element_by_id(id_elem_mod_1).click()
        mgd.find_element_by_id(id_elem).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # print('date_prvw_mod', date_prvw_mod)
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_up)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

        mgd.find_element_by_id(id_elem).click()
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        if value_time_for_compare not in date_prvw_mod:
            raise Exception('Wrong Time preview')
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
        #################
        time.sleep(1)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

        # cell_2 = str(cell_mod + 1) + '-0'
        # id_elem_mod_2 = 'grid-week-cell-' + cell_2 + ''
        #
        # mgd.find_element_by_id(id_elem_mod_2).click
        mgd.find_element_by_id(id_elem).click()
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        if value_time_for_compare not in date_prvw_mod:
            raise Exception('Wrong Time preview')
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()

        ############
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        ############
        time.sleep(1)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        if value_time_for_compare not in date_prvw_mod:
            raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('NOT Ok')
    def test1_4single_event_all_day(self):
        event_name = 'Test8EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_time_ampm = current_time.strftime("%I %M %p")
        now_week = current_time.strftime('%w')
        print('now_time', now_time)
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[:10]
        value_time_ends = value_time_ends_full[:10]
        mgd.find_element_by_css_selector(cal.all_day_button).click()
        mgd.find_element_by_class_name(cal.all_day_checked)
        value_2_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_2_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_2_time_starts = value_2_time_starts_full
        value_2_time_ends = value_2_time_ends_full
        if value_time_starts != value_2_time_starts:
            raise Exception('Wrong Starts Time')
        if value_time_ends != value_2_time_ends:
            raise Exception('Wrong Ends Time')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        if value_2_time_starts[:5] not in date_prvw_mod:
            raise Exception('Wrong Time preview')
        mgd.find_element_by_id(cal.edit_prvw).click()
        value_3_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_3_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_3_time_starts = value_3_time_starts_full
        value_3_time_ends = value_3_time_ends_full
        if value_3_time_starts != value_2_time_starts:
            raise Exception('Wrong Starts Time')
        if value_3_time_ends != value_2_time_ends:
            raise Exception('Wrong Ends Time')
        mgd.find_element_by_css_selector(cal.all_day_button).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()

        value_time_starts_full_split = value_time_starts_full.split(' ')
        print('value_time_starts_full_split', value_time_starts_full_split)
        value_time_starts_split = value_time_starts_full_split[3].split(':')
        print('value_time_starts_split', value_time_starts_split)
        value_time_starts_hour = value_time_starts_split[0]
        print('value_time_starts_hour', value_time_starts_hour)
        # if len(value_time_starts_hour) == 1:
        #     value_time_starts_hour = '0' + value_time_starts_hour
        # print('value_time_starts_hour', value_time_starts_hour)

        hover_drum_hours = mgd.find_element_by_id(cal.drum_hours)
        first_value_hours = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value_hours', first_value_hours)
        difference_hours = int(first_value_hours) - int(value_time_starts_hour)
        #################
        hidden_arrow_hours = mgd.find_element_by_id(cal.drum_hours_up)
        data_separator = mgd.find_element_by_class_name('date-separator')
        actions = ActionChains(driver_instance)
        if difference_hours != 0:
            value_hours = 0
            while value_hours != difference_hours:
                actions.move_to_element(hover_drum_hours).perform()
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
                print('00000')
                try:
                    actions.click(hidden_arrow_hours).perform()
                    print('1111111')
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
                    print('222222')
                time.sleep(1)
                value_hours += 1
        #################

        hover_drum_minutes = mgd.find_element_by_id(cal.drum_minutes)
        first_value_minutes = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value_minutes', first_value_minutes)
        difference_minutes = int(first_value_minutes) - int(value_time_starts_split[1])
        ################
        hidden_arrow_minutes = mgd.find_element_by_id(cal.drum_minutes_down)
        actions = ActionChains(driver_instance)

        if difference_minutes != 0:
            value_hours = 0
            while value_hours != 6:
                actions.move_to_element(hover_drum_minutes).click().perform()
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
                try:
                    actions.click(hidden_arrow_minutes).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
                time.sleep(1)
                value_hours += 1
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_ampm)
        first_value_ampm = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
        print('first_value_ampm', first_value_ampm)
        hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
        actions = ActionChains(driver_instance)

        if first_value_ampm != value_time_starts_full_split[-1]:
            actions.move_to_element(hover_drum).click().perform()
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
            print('second_value', second_value)

        time.sleep(1)

        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_4_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_4_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        if value_4_time_starts_full != value_time_starts:
            raise Exception('Wrong Starts Time')
        if value_4_time_ends_full != value_time_ends:
            raise Exception('Wrong Ends Time')
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # time.sleep(1)


# @unittest.skip('Ok')
class Test8EditSingleEventsRepeat(unittest.TestCase):
    def setUp(self):
        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    def tearDown(self):

        if mgd.find_elements_by_class_name(cal.event_preview):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6'):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button):
            Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)


        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
            time.sleep(2)
        mgd.find_element_by_id(id_elem).click()

        mgd.find_element_by_class_name(cal.delete_prvw).click()
        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        if Check.find_element_by_class_name_and_text(
                cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')
        if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
            print('Check - Event deleted')
        else:
            raise Exception('Event not deleted')

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        pass

    # @unittest.skip('Ok')
    def test1_1single_event_repeat_every_day(self):
        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        # добавить проверки для каждоо дня \\ done
        Check.event_in_cells(event_name, 10, cell)
        print('Check - Event sequence')

        # css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        # if Check.find_element_by_css_selector_and_text(css_name, event_name) == []:
        #     time.sleep(2)
        # mgd.find_element_by_id(id_elem).click()
        #
        # mgd.find_element_by_class_name(cal.delete_prvw).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Update single appointment or the whole sequence?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        # if Check.find_element_by_class_name_and_text(
        #         cal.block_wrapper, 'Update single appointment or the whole sequence?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
        # if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
        #     print('Check - Event deleted')
        # else:
        #     raise Exception('Event not deleted')

    # @unittest.skip('Ok')
    def test1_2single_event_repeat_every_week_custom(self):
        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Week').click()
        if now_week != '6':
            if now_week != '7':
                Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'Custom').click()

        day_of_week_option = 'day-of-week-option-'
        id_elem_day_of_week_now = day_of_week_option + now_week
        day_of_week_selected = mgd.find_element_by_id(id_elem_day_of_week_now).get_attribute(name="class")
        # if 'selected' in day_of_week_selected:
        #     print('Check - Today is selected')
        # else:
        #     raise Exception('Today not selected')
        # mgd.find_element_by_id(id_elem_day_of_week_now).click()
        # if 'selected' in day_of_week_selected:
        #     print('Check - Today is selected')
        # else:
        #     raise Exception('Today not selected')

        sequence = [0, 1, 2, 3, 4, 5, 6]
        sequence.remove(int(now_week))
        day_1 = random.choice(sequence)
        print('d1', day_1)
        sequence.remove(day_1)
        day_2 = random.choice(sequence)
        print('d2', day_2)
        sequence.remove(day_2)
        day_3 = random.choice(sequence)
        print('d3', day_3)
        sequence.remove(day_3)

        day_index = list()
        day_index.append(int(now_week))
        day_index.append(int(day_1))
        day_index.append(int(day_2))
        day_index.append(int(day_3))

        for day_i in day_index:
            id_elem_day_of_week_now = day_of_week_option + str(day_i)
            mgd.find_element_by_id(id_elem_day_of_week_now).click()

        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        day_index.sort()
        time.sleep(2)
        Check.event_in_cells_custom(event_name, day_index, 10, cell)

    # @unittest.skip('Ok')
    def test1_3single_event_repeat_every_week_weekdays(self):
        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Week').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On weekdays')

        day_index = list([1, 2, 3, 4, 5])

        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        day_index.sort()
        time.sleep(2)
        Check.event_in_cells_custom(event_name, day_index, 10, cell)

    # @unittest.skip('Ok')
    def test1_4single_event_repeat_on_day_of_month(self):
        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Month').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of month')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')

        month_selector = '#grid-month-cell-' + now_day + ' .subject'

        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')

        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()

        Check.event_in_cells_month(event_name, 5, month_selector)

    # @unittest.skip('Ok')
    def test1_5single_event_repeat_on_day_of_week(self):
        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Month').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of week').click()
        empty = []
        if mgd.find_elements_by_xpath(cal.on_day_of_week) == empty:
            day_of_week = mgd.find_element_by_xpath(cal.on_day_of_week_four).get_attribute('innerText')
            print('day_of_week_four', day_of_week)
        else:
            day_of_week = mgd.find_element_by_xpath(cal.on_day_of_week).get_attribute('innerText')
            print('day_of_week', day_of_week)
        if mgd.find_elements_by_xpath(cal.number_day_of_week) == empty:
            number_day_of_week = mgd.find_element_by_xpath(cal.number_day_of_week_four).get_attribute('innerText')
            print('number_day_of_week_four', number_day_of_week)
        else:
            number_day_of_week = mgd.find_element_by_xpath(cal.number_day_of_week).get_attribute('innerText')
            print('number_day_of_week', number_day_of_week)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Month View is selected')
            else:
                raise Exception('Month view is not selectable')
        driver_instance.implicitly_wait(5)
        value = 0
        while value < 10:

            month_title = mgd.find_element_by_class_name(cal.navigation_title).get_attribute('innerText')
            month_title_list = month_title.split(' ')
            print('month_title_list', month_title_list)
            new_month_year = month_title_list[1]
            new_month_month_abbr = month_title_list[0]
            #
            new_month_month = time.strptime(new_month_month_abbr, '%b').tm_mon
            print('new_month_year', new_month_year)
            print('new_month_month', new_month_month)
            if len(str(new_month_month)) == 1:
                new_month_month = '0' + str(new_month_month)
            print('new_month_month', new_month_month)

            month_cell = Check.day_of_week_in_month(str(new_month_year), new_month_month, number_day_of_week, day_of_week)

            month_cell_selector = '#grid-month-cell-' + str(month_cell) + ' .subject'
            print('month_cell_selector', month_cell_selector)
            time.sleep(1)
            elem = Check.find_element_by_css_selector_and_text(month_cell_selector, event_name)
            if elem is None:
                raise Exception('ERRRRRRROR')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            value += 1
            mgd.find_element_by_class_name(cal.navigation_right).click()
            print('Check - Right button')

    # @unittest.skip('Ok')
    def test1_6single_event_repeat_on_date(self):
        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Year').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On date').click()
        on_date_date = mgd.find_element_by_xpath(cal.on_date).get_attribute('innerText')
        print('on_date_date', on_date_date)
        date = on_date_date.split(' ')
        date_month = date[0]
        print('date_month', date_month)
        date_day = date[1][:-2]
        print('date_day', date_day)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value = 0
        while value <= 10:
            view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                view_button.click()
                view_button_select = view_button.get_attribute(name='class')
                if 'selected' in view_button_select:
                    print('Check - Year View is selected')
                else:
                    raise Exception('Year view is not selectable')

            mgd.find_element_by_class_name(cal.navigation_right).click()
            print('Check - Right button')

            mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            print('date_month -3:', date_month[:3])
            Check.find_element_by_class_name_and_text(cal.month_title_year_view, date_month[:3].upper()).click()

            month_selector = '#grid-month-cell-' + date_day + ' .subject'
            time.sleep(2)
            elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
            if elem is None:
                raise Exception('ERRRRRRROR')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            value += 1

    # @unittest.skip('Ok')
    def test1_7single_event_repeat_year_on_day_of_week(self):
        event_name = 'Test8EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Year').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of week').click()
        empty = []
        if mgd.find_elements_by_xpath(cal.year_on_day_of_week) == empty:
            year_on_day_of_week = mgd.find_element_by_xpath(cal.year_on_day_of_week_four).get_attribute('innerText')
            print('year_on_day_of_week', year_on_day_of_week)
        else:
            year_on_day_of_week = mgd.find_element_by_xpath(cal.year_on_day_of_week).get_attribute('innerText')
            print('year_on_day_of_week', year_on_day_of_week)
        if mgd.find_elements_by_xpath(cal.year_number_day_of_week) == empty:
            year_number_day_of_week = mgd.find_element_by_xpath(cal.year_number_day_of_week_four).get_attribute('innerText')
            print('year_number_day_of_week_four', year_number_day_of_week)
        else:
            year_number_day_of_week = mgd.find_element_by_xpath(cal.year_number_day_of_week).get_attribute('innerText')
            print('year_number_day_of_week', year_number_day_of_week)

        year_day_of_week_month = mgd.find_element_by_xpath(cal.year_day_of_week_month).get_attribute('innerText')
        print('year_day_of_week_month', year_day_of_week_month)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(5)
        value = 0
        while value <= 5:
            view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Year View is selected')
            else:
                view_button.click()
                view_button_select = view_button.get_attribute(name='class')
                if 'selected' in view_button_select:
                    print('Check - Year View is selected')
                else:
                    raise Exception('Year view is not selectable')

            mgd.find_element_by_class_name(cal.navigation_right).click()
            print('Check - Right button')

            mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)
            #######################################
            print('year_day_of_week_month 3', year_day_of_week_month[:3])
            Check.find_element_by_class_name_and_text(cal.month_title_year_view, year_day_of_week_month[:3].upper()).click()
            ##############

            month_title = mgd.find_element_by_class_name(cal.navigation_title).get_attribute('innerText')
            month_title_list = month_title.split(' ')
            print('month_title_list', month_title_list)
            new_month_year = month_title_list[1]
            new_month_month_abbr = month_title_list[0]
            #
            new_month_month = time.strptime(new_month_month_abbr, '%b').tm_mon
            print('new_month_year', new_month_year)
            print('new_month_month', new_month_month)
            if len(str(new_month_month)) == 1:
                new_month_month = '0' + str(new_month_month)
            print('new_month_month', new_month_month)

            month_cell = Check.day_of_week_in_month(
                str(new_month_year), new_month_month, year_number_day_of_week, year_on_day_of_week)

            month_cell_selector = '#grid-month-cell-' + str(month_cell) + ' .subject'
            time.sleep(2)
            elem = Check.find_element_by_css_selector_and_text(month_cell_selector, event_name)
            if elem is None:
                raise Exception('ERRRRRRROR')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()

            value += 1


# @unittest.skip('Ok (add 1 more)')
class Test9EditSequence1Events(unittest.TestCase):
    def setUp(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    def tearDown(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        time.sleep(1)
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # @unittest.skip('Ok')
    def test1_rep_event_in_date(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        day_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        month_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        year_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        end_repeat_date_value = day_value + ' ' + str(int(month_value) + 1) + ' ' + year_value

        end_repeat = mgd.find_element_by_xpath(cal.end_of_repeat_field_other_view).get_attribute('innerText')
        print('end_repeat_date_value', end_repeat_date_value)
        print('end_repeat', end_repeat)
        end_repeat_strptime = datetime.strptime(end_repeat, "%d %b %Y")
        print('end_repeat_strptime', end_repeat_strptime)
        starts_time_value = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        end_repeat_in_date_strptime = datetime.strptime(end_repeat_date_value, "%d %m %Y")
        print('end_repeat_in_date_strptime', end_repeat_in_date_strptime)
        starts_time = datetime.strptime(starts_time_value, "%d %b %Y %I:%M %p")
        print('starts_time', starts_time)
        starts_time_modify = starts_time.replace(hour=0, minute=0)
        print('starts_time_modify', starts_time_modify)
        repeat_duration = 7
        time_delta = timedelta(days=repeat_duration)
        if end_repeat_strptime != end_repeat_in_date_strptime:
            raise Exception('End Repeat date not match')
        if starts_time_modify + time_delta != end_repeat_in_date_strptime:
            raise Exception('End Repeat date incorrect')
        # iii = end_repeat_in_date_strptime - starts_time_modify
        # print('iii', iii)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        drop_sequence = 'If you have changed certain events in the sequence, these events will be ' \
                'canceled and the corresponding events will again correspond to the sequence; ' \
                'deleted events of the sequence will be restored as well'
        Check.find_element_by_class_name_and_text(cal.block_wrapper, drop_sequence)
        print('Check - Block wrapper with drop sequence')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        end_repeat_2 = mgd.find_element_by_xpath(cal.end_of_repeat_field_other_view).get_attribute('innerText')
        if end_repeat != end_repeat_2:
            raise Exception('End Repeat date not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.event_in_cells(event_name, repeat_duration + 1, cell)

    # @unittest.skip('Ok')
    def test3_rep_event_occurrences(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'After a number of occurrences').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        end_repeat = mgd.find_element_by_xpath(cal.end_of_repeat_field_other_view).get_attribute('innerText')
        if 'After 10 occurrences' not in end_repeat:
            raise Exception('End Repeat incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        drop_sequence = 'If you have changed certain events in the sequence, these events will be ' \
                'canceled and the corresponding events will again correspond to the sequence; ' \
                'deleted events of the sequence will be restored as well'
        Check.find_element_by_class_name_and_text(cal.block_wrapper, drop_sequence)
        print('Check - Block wrapper with drop sequence')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        end_repeat_2 = mgd.find_element_by_xpath(cal.end_of_repeat_field_other_view).get_attribute('innerText')
        if end_repeat != end_repeat_2:
            raise Exception('End Repeat not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.event_in_cells(event_name, 10, cell)


# @unittest.skip('Ok')
class Test9EditSequence2EventsToException(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        time.sleep(1)
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_name(self):
        event_name = 'Test9EditRepEvent_0'
        event_name_2 = 'Test9CreateException'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.title_input).clear()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name_2)
        mgd.find_element_by_id(cal.yes_edit_button).click()

        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        time.sleep(1)
        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        event_name_preview = mgd.find_element_by_class_name(cal.event_name_prvw).get_attribute('innerText')
        if event_name_2 != event_name_preview:
            raise Exception('Name is incorrect')

    # @unittest.skip('Ok')
    def test2_rep_event_exception_location(self):
        event_name = 'Test9EditRepEvent_0'
        location_name = 'Grand Canyon'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.location_input).send_keys(location_name)
        mgd.find_element_by_id(cal.yes_edit_button).click()

        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        mgd.find_element_by_id(id_elem).click()
        location_preview = mgd.find_element_by_class_name(cal.location_prvw).get_attribute('innerText')
        if location_name != location_preview:
            raise Exception('Location is incorrect')

    # @unittest.skip('Ok')
    def test3_rep_event_exception_notes(self):
        event_name = 'Test9EditRepEvent_0'
        notes_text = 'Too deep to quietly fall'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        elem = mgd.find_element_by_id(cal.notes_input)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()

        elem.send_keys(notes_text)
        mgd.find_element_by_id(cal.yes_edit_button).click()

        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        mgd.find_element_by_id(id_elem).click()
        notes_preview = mgd.find_element_by_class_name(cal.notes_prvw).get_attribute('innerText')
        if notes_preview != notes_text:
            raise Exception('Notes is incorrect')

    # @unittest.skip('Ok')
    def test4_rep_event_exception_all_day(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 5, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        # value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        # value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        # value_time_starts = value_time_starts_full[:11]
        # value_time_ends = value_time_ends_full[:11]
        mgd.find_element_by_css_selector(cal.all_day_button).click()
        mgd.find_element_by_class_name(cal.all_day_checked)
        value_2_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        # value_2_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_2_time_starts = value_2_time_starts_full
        # value_2_time_ends = value_2_time_ends_full
        # print('value_time_starts', value_time_starts)
        # print('value_2_time_starts', value_2_time_starts)
        # if value_time_starts != value_2_time_starts:
        #     raise Exception('Wrong Starts Time')
        # if value_time_ends != value_2_time_ends:
        #     raise Exception('Wrong Ends Time')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        if value_2_time_starts[:5] not in date_prvw_mod:
            raise Exception('Wrong Time preview')
        # mgd.find_element_by_id(cal.edit_prvw).click()
        # value_3_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        # value_3_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        # value_3_time_starts = value_3_time_starts_full
        # value_3_time_ends = value_3_time_ends_full
        # if value_3_time_starts != value_2_time_starts_full:
        #     raise Exception('Wrong Starts Time')
        # if value_3_time_ends != value_2_time_ends_full:
        #     raise Exception('Wrong Ends Time')

    # @unittest.skip('Ok')
    def test5_rep_event_exception_alert(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 6, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Alert').click()
        count = random.randint(1, 32)
        xpath_alert = mgd.find_element_by_xpath(
            '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(count) + ']/div[1]')
        actions = ActionChains(driver_instance)
        actions.move_to_element(xpath_alert).click().perform()
        alert_name = xpath_alert.get_attribute('innerText')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        alert_value = mgd.find_element_by_xpath(cal.alert_value_repeat).get_attribute('innerText')
        print('alert_name', alert_name)
        print('alert_value', alert_value)
        if alert_name == alert_value:
            print('Check - Alert value:', alert_value)
        else:
            raise Exception('Wrong Alert Value')

        mgd.find_element_by_id(cal.yes_edit_button).click()

        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 6, cell)
        mgd.find_element_by_id(id_elem).click()
        alert_prvw = Check.find_element_by_class_name_and_text('value', alert_name)
        alert_value_prvw = alert_prvw.get_attribute('innerText')
        print('alert_value_prvw', alert_value_prvw)
        time.sleep(2)
        mgd.find_element_by_id(cal.edit_prvw).click()
        time.sleep(2)
        alert_value_2 = mgd.find_element_by_xpath(cal.alert_value_exception).get_attribute('innerText')
        print('alert_value_2', alert_value_2)
        if alert_value_prvw == alert_value_2:
            print('Check - Alert value:', alert_value_2)
        else:
            raise Exception('Wrong Alert Value 2', alert_value_2)

    # @unittest.skip('Ok')
    def test6_rep_event_exception_invitees(self):
        event_name = 'Test9EditRepEvent_0'
        invitees_email_name = '3cont@autotest.ab'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        invitees_field = Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees')
        actions = ActionChains(driver_instance)
        actions.move_to_element(invitees_field).click().perform()
        mgd.find_element_by_class_name(cal.plus_icon).click()
        mgd.find_element_by_class_name(cal.contact_items)
        invitees_found = Check.find_element_by_class_name_and_text(cal.contact_email, invitees_email_name)
        actions = ActionChains(driver_instance)
        actions.move_to_element(invitees_found).click().perform()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        check_email = Check.find_element_by_class_name_and_text(cal.email_invitees, invitees_email_name)
        if not check_email:
            raise Exception('Email ' + invitees_email_name + ' not found')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        invitees_field = Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees')
        actions = ActionChains(driver_instance)
        actions.move_to_element(invitees_field).click().perform()
        check_email_2 = Check.find_element_by_class_name_and_text(cal.email_invitees, invitees_email_name)
        if not check_email_2:
            raise Exception('Email ' + invitees_email_name + ' not found')

    # @unittest.skip('Ok')
    def test6_rep_event_exception_color(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
#########################
        css_elem = '#' + id_elem + '> div > div'
        css_color_attribute = mgd.find_element_by_css_selector(css_elem).get_attribute(name='class')
        css_color_split = css_color_attribute.split(' ')
        color_default_grid = css_color_split[1].lower()
        print('color_default_grid - ', color_default_grid)

        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        color_attribute_edit_event = mgd.find_element_by_class_name(cal.color_field).get_attribute(name='class')
        color_split_edit_event = color_attribute_edit_event.split(' ')
        color_default_edit_event = color_split_edit_event[1].lower()
        print('color_default_edit_event - ', color_default_edit_event)
        if color_default_grid != color_default_edit_event:
            raise Exception('Color does not match')

        color_field = Check.find_element_by_class_name_and_text(cal.title_class, 'Color')
        actions = ActionChains(driver_instance)
        actions.move_to_element(color_field).click().perform()
        number_of_colors = len(mgd.find_elements_by_class_name(cal.timezone_text_class))
        print('number_of_colors', number_of_colors)
        new_color_number = random.randrange(1, number_of_colors, 1)
        print('new_color_number', new_color_number)
        color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(new_color_number) + ']'
        mgd.find_element_by_xpath(color_xpath).click()
        name_color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(new_color_number) + ']/div[2]/div'
        new_color_name = mgd.find_element_by_xpath(name_color_xpath).get_attribute(name='class')
        new_color_name_split = new_color_name.split(' ')
        new_color = new_color_name_split[1].lower()
        print('new_color', new_color)
        while new_color == color_default_grid:
            new_color_number = random.randrange(1, number_of_colors, 1)
            print('new_color_number', new_color_number)
            color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(
                new_color_number) + ']'
            mgd.find_element_by_xpath(color_xpath).click()
            name_color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(
                new_color_number) + ']/div[1]'
            new_color_name = mgd.find_element_by_xpath(name_color_xpath).get_attribute('innerText')
            new_color_name_split = new_color_name.split(' ')
            new_color = new_color_name_split[0].lower()
            print('new_color', new_color)

        mgd.find_element_by_id(cal.yes_edit_button).click()
        color_new_attribute_edit_event = mgd.find_element_by_class_name(cal.color_field).get_attribute(name='class')
        color_new_split_edit_event = color_new_attribute_edit_event.split(' ')
        color_new_default_edit_event = color_new_split_edit_event[1].lower()
        print('color_new_default_edit_event', color_new_default_edit_event)
        if new_color != color_new_default_edit_event:
            raise Exception('Color does not match')

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        css_elem = '#' + id_elem + '> div > div'
        css_new_color_attribute = mgd.find_element_by_css_selector(css_elem).get_attribute(name='class')
        css_new_color_split = css_new_color_attribute.split(' ')
        color_new_grid = css_new_color_split[1].lower()
        print('color_new_grid - ', color_new_grid)
        if color_new_grid != new_color:
            raise Exception('Color does not match')

        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        color_2_attribute_edit_event = mgd.find_element_by_class_name(cal.color_field).get_attribute(name='class')
        color_2_split_edit_event = color_2_attribute_edit_event.split(' ')
        color_2_default_edit_event = color_2_split_edit_event[1].lower()
        print('color_2_default_edit_event - ', color_2_default_edit_event)

        if color_new_grid != color_2_default_edit_event:
            raise Exception('Color does not match')

    # @unittest.skip('Ok')
    def test7_1rep_event_exception_starts_time_hours_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 9, cell)
#########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

#########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 9, cell)
        time.sleep(1)
        print('id_elem', id_elem)
        id_elem_split = id_elem.split('-')
        id_elem_new_cell = int(id_elem_split[3]) + 2
        id_elem_mod_1 = 'grid-week-cell-' + str(id_elem_new_cell) + '-' + id_elem_split[4] + ''
        mgd.find_element_by_id(id_elem_mod_1).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test7_1rep_event_exception_starts_time_hours_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 10, cell)
#########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

#########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 10, cell)
        time.sleep(1)
        print('id_elem', id_elem)
        id_elem_split = id_elem.split('-')
        id_elem_new_cell = int(id_elem_split[3]) - 2
        id_elem_mod_1 = 'grid-week-cell-' + str(id_elem_new_cell) + '-' + id_elem_split[4] + ''
        mgd.find_element_by_id(id_elem_mod_1).click()
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test7_1rep_event_exception_starts_time_minutes_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 11, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 11, cell)
        time.sleep(1)
        # print('id_elem', id_elem)
        # id_elem_split = id_elem.split('-')
        # id_elem_new_cell = int(id_elem_split[3]) + 2
        # id_elem_mod_1 = 'grid-week-cell-' + str(id_elem_new_cell) + '-' + id_elem_split[4] + ''
        mgd.find_element_by_id(id_elem).click()
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('NOT Ok')
    def test7_1rep_event_exception_starts_time_minutes_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 12, cell)
#########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

#########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 12, cell)
        time.sleep(1)
        print('id_elem', id_elem)
        id_elem_split = id_elem.split('-')
        if second_value == '55':
            print('1')
            id_elem_new_cell = int(id_elem_split[3]) + 1
            id_elem_mod_1 = 'grid-week-cell-' + str(id_elem_new_cell) + '-' + id_elem_split[4] + ''
            element = mgd.find_element_by_id(id_elem_mod_1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(element).move_by_offset(-1, 14).click().perform()

        else:
            print('2')
            mgd.find_element_by_id(id_elem).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test7_2rep_event_exception_ends_time_hours_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 13, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 13, cell)
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        # print('__' + value_time_ends + '__')
        # value_time_for_compare = value_time_starts + ' –' + value_time_ends
        # print('value_time_for_compare', value_time_for_compare)
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # print('date_prvw_mod', date_prvw_mod)
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test7_2rep_event_exception_ends_time_hours_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 14, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_hours)
        first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_hours_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 14, cell)
        time.sleep(1)
        # print('id_elem', id_elem)
        # id_elem_split = id_elem.split('-')
        # id_elem_new_cell = int(id_elem_split[3]) - 2
        # id_elem_mod_1 = 'grid-week-cell-' + str(id_elem_new_cell) + '-' + id_elem_split[4] + ''
        mgd.find_element_by_id(id_elem).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test7_2rep_event_exception_ends_time_minutes_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 15, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 15, cell)
        time.sleep(1)
        # print('id_elem', id_elem)
        # id_elem_split = id_elem.split('-')
        # id_elem_new_cell = int(id_elem_split[3]) + 2
        # id_elem_mod_1 = 'grid-week-cell-' + str(id_elem_new_cell) + '-' + id_elem_split[4] + ''
        mgd.find_element_by_id(id_elem).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')
        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test7_2rep_event_exception_ends_time_minutes_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 16, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        id_elem = Check.event_in_specific_cells(event_name, 16, cell)
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')


# @unittest.skip('Ok')
class Test9EditSequence3EventsToExceptionStartsDay(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        # Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        # ############
        # hover_drum = mgd.find_element_by_id(cal.drum_hours)
        # first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        # print('first_value', first_value)
        # hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        # actions = ActionChains(driver_instance)
        # actions.move_to_element(hover_drum).click().perform()
        # wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        # try:
        #     actions.click(hidden_arrow).perform()
        # except:
        #     wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        # time.sleep(1)
        # second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        # print('second_value', second_value)
        # ############
        # if first_value != second_value:
        #     print('Check - change of value')
        # else:
        #     raise Exception('The value is the same')
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        #
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        time.sleep(1)
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_starts_day_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test2_rep_event_exception_starts_day_down_work(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        time.sleep(1)
        print('id_elem', id_elem)
        id_elem_split = id_elem.split('-')
        id_elem_new_cell = int(id_elem_split[4]) + 1
        id_elem_mod_1 = 'grid-week-cell-' + id_elem_split[3] + '-' + str(id_elem_new_cell) + ''
        mgd.find_element_by_id(id_elem_mod_1).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test3_rep_event_exception_starts_day_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test4_rep_event_exception_starts_day_up_work(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 1, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        id_elem = Check.event_in_specific_cells(event_name, 1, cell)
        time.sleep(1)
        print('id_elem', id_elem)
        id_elem_split = id_elem.split('-')
        id_elem_new_cell = int(id_elem_split[4]) - 1
        id_elem_mod_1 = 'grid-week-cell-' + id_elem_split[3] + '-' + str(id_elem_new_cell) + ''
        mgd.find_element_by_id(id_elem_mod_1).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')


# @unittest.skip('Ok')
class Test9EditSequence4EventsToExceptionEndsDay(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        # Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        # ############
        # hover_drum = mgd.find_element_by_id(cal.drum_hours)
        # first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        # print('first_value', first_value)
        # hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        # actions = ActionChains(driver_instance)
        # actions.move_to_element(hover_drum).click().perform()
        # wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        # try:
        #     actions.click(hidden_arrow).perform()
        # except:
        #     wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        # time.sleep(1)
        # second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        # print('second_value', second_value)
        # ############
        # if first_value != second_value:
        #     print('Check - change of value')
        # else:
        #     raise Exception('The value is the same')
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        #
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        time.sleep(1)
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_ends_day_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test2_rep_event_exception_ends_day_down_work(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        time.sleep(1)
        print('id_elem', id_elem)
        mgd.find_element_by_id(id_elem).click()

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('NOT Ok change other error_message')
    def test3_rep_event_exception_ends_day_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
        if 'disabled' in yes_button_attr:
            print('Check - Yes button not disabled')
        else:
            raise Exception('For Yes button "disabled" is missing')

        message = 'The date should be after'
        error_message = mgd.find_element_by_class_name(cal.data_error_drum).get_attribute('innerText')
        if message not in error_message:
            raise Exception('Error message not found', 'error_message -', error_message)
        print('Check - error message')

        # value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        # value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        # value_time_starts = value_time_starts_full[11:]
        # value_time_ends = value_time_ends_full[11:]
        # print('value_time_starts_full', value_time_starts)
        # print('value_time_ends', value_time_ends)
        #
        # #########################
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # message = 'Update single appointment or the whole sequence?'
        # update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        # if update_appointment:
        #     print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        # time.sleep(1)
        # message = "Repeat fields are shared across the sequence and won't be saved"
        # update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        # if update_appointment:
        #     print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        # message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        # error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        # if error_appoinment:
        #     print('Check - Error block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()


# @unittest.skip('Ok')
class Test9EditSequence5EventsToExceptionStartsMonth(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        # Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        # ############
        # hover_drum = mgd.find_element_by_id(cal.drum_hours)
        # first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        # print('first_value', first_value)
        # hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        # actions = ActionChains(driver_instance)
        # actions.move_to_element(hover_drum).click().perform()
        # wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        # try:
        #     actions.click(hidden_arrow).perform()
        # except:
        #     wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        # time.sleep(1)
        # second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        # print('second_value', second_value)
        # ############
        # if first_value != second_value:
        #     print('Check - change of value')
        # else:
        #     raise Exception('The value is the same')
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        #
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        time.sleep(1)
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_starts_month_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test2_rep_event_exception_starts_month_down_work(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        time.sleep(1)

#####################
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button.click()

        mgd.find_element_by_class_name(cal.navigation_right).click()
        mgd.find_element_by_id(cal.spinner).click()
        time.sleep(2)

        starts_split = value_time_starts_full.split(' ')
        print('starts_split[0]', starts_split[0])
        month_selector = '#grid-month-cell-' + starts_split[0] + ' .subject'
        print('month_selector', month_selector)

        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')
        time.sleep(2)
###############
        # id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        # time.sleep(1)
        # id_elem_mod_1 = 'grid-week-cell-' + id_elem_split[3] + '-' + str(id_elem_new_cell) + ''
        # mgd.find_element_by_id(id_elem_mod_1).click()
        # # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # # if value_time_for_compare not in date_prvw_mod:
        # #     raise Exception('Wrong Time preview')
        #
        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test3_rep_event_exception_starts_month_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test4_rep_event_exception_starts_month_up_work(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 1, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        time.sleep(1)
        #####################
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
        view_button.click()

        mgd.find_element_by_class_name(cal.navigation_left).click()
        mgd.find_element_by_id(cal.spinner).click()
        time.sleep(2)

        starts_split = value_time_starts_full.split(' ')
        print('starts_split[0]', starts_split[0])
        month_selector = '#grid-month-cell-' + starts_split[0] + ' .subject'
        print('month_selector', month_selector)

        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')
        time.sleep(2)

        # mgd.find_element_by_class_name(cal.today_button).click()
        # view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        # view_button.click()
        #
        # id_elem = Check.event_in_specific_cells(event_name, 1, cell)
        # time.sleep(1)
        # print('id_elem', id_elem)
        # id_elem_split = id_elem.split('-')
        # id_elem_new_cell = int(id_elem_split[4]) - 1
        # id_elem_mod_1 = 'grid-week-cell-' + id_elem_split[3] + '-' + str(id_elem_new_cell) + ''
        # mgd.find_element_by_id(id_elem_mod_1).click()
        # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')


# @unittest.skip('Ok')
class Test9EditSequence6EventsToExceptionEndsMonth(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        # Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        # ############
        # hover_drum = mgd.find_element_by_id(cal.drum_hours)
        # first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        # print('first_value', first_value)
        # hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
        # actions = ActionChains(driver_instance)
        # actions.move_to_element(hover_drum).click().perform()
        # wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        # try:
        #     actions.click(hidden_arrow).perform()
        # except:
        #     wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
        # time.sleep(1)
        # second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
        # print('second_value', second_value)
        # ############
        # if first_value != second_value:
        #     print('Check - change of value')
        # else:
        #     raise Exception('The value is the same')
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        #
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        # Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        time.sleep(1)
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_ends_month_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test2_rep_event_exception_ends_month_down_work(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        time.sleep(1)
        print('id_elem', id_elem)
        mgd.find_element_by_id(id_elem).click()

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test3_rep_event_exception_ends_month_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
        if 'disabled' in yes_button_attr:
            print('Check - Yes button not disabled')
        else:
            raise Exception('For Yes button "disabled" is missing')

        message = 'The date should be after'
        error_message = mgd.find_element_by_class_name(cal.data_error_drum).get_attribute('innerText')
        if message not in error_message:
            raise Exception('Error message not found', 'error_message -', error_message)
        print('Check - error message')

        # value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        # value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        # value_time_starts = value_time_starts_full[11:]
        # value_time_ends = value_time_ends_full[11:]
        # print('value_time_starts_full', value_time_starts)
        # print('value_time_ends', value_time_ends)
        #
        # #########################
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # message = 'Update single appointment or the whole sequence?'
        # update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        # if update_appointment:
        #     print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        # time.sleep(1)
        # message = "Repeat fields are shared across the sequence and won't be saved"
        # update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        # if update_appointment:
        #     print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        # message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        # error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        # if error_appoinment:
        #     print('Check - Error block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()


# @unittest.skip('Ok')
class Test9EditSequence7EventsToExceptionStartsYear(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        event_name = 'Test9EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        time.sleep(1)
        event_name = 'Test9EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_starts_year_down(self):
        event_name = 'Test9EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('NOT Ok')
    def test2_rep_event_exception_starts_year_down_work(self):
        event_name = 'Test9EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        time.sleep(1)

#####################
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Year')
        view_button.click()

        mgd.find_element_by_class_name(cal.navigation_right).click()
        mgd.find_element_by_id(cal.spinner).click()
        starts_split = value_time_starts_full.split(' ')
        print('starts_split[1]', starts_split[1])
        Check.find_element_by_class_name_and_text(cal.month_title_year_view, starts_split[1].upper()).click()
        time.sleep(2)

        print('starts_split[0]', starts_split[0])
        month_selector = '#grid-month-cell-' + starts_split[0] + ' .subject'
        print('month_selector', month_selector)

        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')
        time.sleep(2)
###############
        # id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        # time.sleep(1)
        # id_elem_mod_1 = 'grid-week-cell-' + id_elem_split[3] + '-' + str(id_elem_new_cell) + ''
        # mgd.find_element_by_id(id_elem_mod_1).click()
        # # value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # # if value_time_for_compare not in date_prvw_mod:
        # #     raise Exception('Wrong Time preview')
        #
        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('Ok')
    def test3_rep_event_exception_starts_year_up(self):
        event_name = 'Test9EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Repeat fields are shared across the sequence and won't be saved"
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()


# @unittest.skip('Ok')
class Test9EditSequence8EventsToExceptionEndsYear(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if mgd.find_elements_by_class_name(cal.event_preview):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name('small-6') != []:
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        if mgd.find_elements_by_class_name(cal.bw_button) != []:
            Check.find_element_by_class_name_and_text(cal.bw_button, 'No').click()

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'End Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'In date').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Week View is selected\n')
        else:
            view_button.click()
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected\n')
            else:
                raise Exception('Week view is not selectable')

        time.sleep(1)
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_ends_year_down(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test2_rep_event_exception_ends_year_down_work(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)

        #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        id_elem = Check.event_in_specific_cells(event_name, 8, cell)
        time.sleep(1)
        print('id_elem', id_elem)
        mgd.find_element_by_id(id_elem).click()

        mgd.find_element_by_id(cal.edit_prvw).click()
        name_exception = mgd.find_element_by_id(cal.title_input).get_attribute(name='value')
        print('name_exception', name_exception)
        if event_name != name_exception:
            raise Exception('Wrong event name')

        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts_2 = value_time_starts_full_2[11:]
        value_time_ends_2 = value_time_ends_full_2[11:]
        print('value_time_starts_full_2', value_time_starts_2)
        print('value_time_ends_2', value_time_ends_2)
        if value_time_starts_2 != value_time_starts:
            raise Exception('Starts field does not match')
        if value_time_ends_2 != value_time_ends:
            raise Exception('Ends field does not match')

    # @unittest.skip('NOT Ok')
    def test3_rep_event_exception_ends_year_up(self):
        event_name = 'Test9EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        # id_elem = 'grid-week-cell-' + cell + ''
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        #########################
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        Check.find_element_by_class_name_and_text(cal.title_class, 'Ends').click()
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_year)
        first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_year_up)
        actions = ActionChains(driver_instance)
        actions.move_to_element(hover_drum).click().perform()
        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
        try:
            actions.click(hidden_arrow).perform()
        except:
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
        time.sleep(1)
        second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
        print('second_value', second_value)
        ############
        if first_value != second_value:
            print('Check - change of value')
        else:
            raise Exception('The value is the same')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        value_time_starts = value_time_starts_full[11:]
        value_time_ends = value_time_ends_full[11:]
        print('value_time_starts_full', value_time_starts)
        print('value_time_ends', value_time_ends)
        #
        # #########################
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        time.sleep(1)

        message = "Two occurrences of a sequence can't occur on the same day, overlap, or occur in different order than the initial one"
        error_appoinment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if error_appoinment:
            print('Check - Error block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

