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
class Test2CreateNewEventButtonsDelete(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        mgd.find_element_by_class_name(cal.today_button).click()

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
        if not Check.check_exists_by_class_name(cal.edit_event):
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
        if not Check.check_exists_by_class_name(cal.edit_event):
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
        Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name)
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
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name)
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

    def test2_yes_editor_button_month_view(self):
        current_time = datetime.now()
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

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
        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        month_selector = '#grid-month-cell-' + now_day + ' .subject'

        time.sleep(2)

        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            time.sleep(2)
        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('Event name preview not found')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name)
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
        if not Check.check_exists_by_class_name(cal.edit_event):
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
        if not Check.check_exists_by_class_name(cal.edit_event):
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
        if not Check.check_exists_by_class_name(cal.edit_event):
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
        if not Check.check_exists_by_class_name(cal.edit_event):
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
        # starts = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
        # starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
        # starts_time_cut = str(starts_time)[11:16]
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
        if not Check.check_exists_by_class_name(cal.edit_event):
            print('Check - The event editor is closed')
        else:
            raise Exception('The event editor is not closed')

        Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name).click()
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name)
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
        if not Check.check_exists_by_class_name(cal.edit_event):
            print('Check - The event editor is closed')
        else:
            raise Exception('The event editor is not closed')

        cell_list = Check.find_cell_week_number(starts_time_cut)
        cell = str(cell_list[0]) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.event_preview)
        print('Check - Event preview is open')
        Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name)
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
