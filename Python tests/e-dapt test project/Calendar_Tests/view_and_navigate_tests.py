import time
from datetime import datetime, timedelta
from datetime import timedelta
import calendar
import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
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
    print('Start: calendar_tests.py\n')


def tearDownModule():
    print('End: calendar_tests.py\n')
    # driver_instance.quit()


# @unittest.skip('Ok')
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


# @unittest.skip('Ok')
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


# @unittest.skip('Ok')
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


# @unittest.skip('Ok')
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


# @unittest.skip('Ok')
class Test1Navigate(unittest.TestCase):
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


