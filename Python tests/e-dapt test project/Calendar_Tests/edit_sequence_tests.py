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


# @unittest.skip('Ok (add 1 more)')
class Test7EditSequence1Events(unittest.TestCase):
    def setUp(self):
        driver_instance.implicitly_wait(1)
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
        if mgd.find_elements_by_id(cal.all_appointments_panel):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
        driver_instance.implicitly_wait(5)

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

        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            if Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            elif Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        if not mgd.find_elements_by_id(cal.delete_prvw):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()

        mgd.find_element_by_id(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    @classmethod
    def setUpClass(cls):
        driver_instance.implicitly_wait(1)
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
        driver_instance.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        pass

    # @unittest.skip('Ok')
    def test1_rep_event_in_date(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not mgd.find_elements_by_id(cal.edit_prvw):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
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
        repeat_duration = 6
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
        driver_instance.implicitly_wait(1)
        if not mgd.find_elements_by_id(cal.edit_prvw):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()
        end_repeat_2 = mgd.find_element_by_xpath(cal.end_of_repeat_field_other_view).get_attribute('innerText')
        if end_repeat != end_repeat_2:
            raise Exception('End Repeat date not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.event_in_cells(event_name, repeat_duration + 1, cell)

    # @unittest.skip('Ok')
    def test3_rep_event_occurrences(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not mgd.find_elements_by_id(cal.edit_prvw):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
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
        driver_instance.implicitly_wait(1)
        if not mgd.find_elements_by_id(cal.edit_prvw):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()
        end_repeat_2 = mgd.find_element_by_xpath(cal.end_of_repeat_field_other_view).get_attribute('innerText')
        if end_repeat != end_repeat_2:
            raise Exception('End Repeat not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.event_in_cells(event_name, 10, cell)


# @unittest.skip('Ok + ref 30.08')
class Test7EditSequence2EventsToException(unittest.TestCase):
    def setUp(self):
        driver_instance.implicitly_wait(1)
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
        if mgd.find_elements_by_id(cal.all_appointments_panel):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
        driver_instance.implicitly_wait(5)

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

    @classmethod
    def setUpClass(cls):
        driver_instance.implicitly_wait(1)
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
        driver_instance.implicitly_wait(5)

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

        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            if Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            elif Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

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
        driver_instance.implicitly_wait(1)
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
        if mgd.find_elements_by_id(cal.all_appointments_panel):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] +2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_name(self):
        event_name = 'Test7EditRepEvent_0'
        event_name_2 = 'Test7CreateException'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        id_elem = Check.event_in_specific_cells(event_name_2, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        event_name_preview = mgd.find_element_by_css_selector(cal.event_name_prvw).get_attribute('innerText')
        if event_name_2 != event_name_preview:
            raise Exception('Name is incorrect')

    # @unittest.skip('Ok')
    def test2_rep_event_exception_location(self):
        event_name = 'Test7EditRepEvent_0'
        location_name = 'Grand Canyon'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        time.sleep(1)
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        print('id_elem', id_elem)

        mgd.find_element_by_id(id_elem).click()
        location_preview = mgd.find_element_by_class_name(cal.location_prvw).get_attribute('innerText')
        if location_name != location_preview:
            raise Exception('Location is incorrect')

    # @unittest.skip('Ok')
    def test3_rep_event_exception_notes(self):
        event_name = 'Test7EditRepEvent_0'
        notes_text = 'Too deep to quietly fall'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        time.sleep(1)
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        mgd.find_element_by_id(id_elem).click()
        notes_preview = mgd.find_element_by_class_name(cal.notes_prvw).get_attribute('innerText')
        if notes_preview != notes_text:
            raise Exception('Notes is incorrect')

    # @unittest.skip('Ok')
    def test4_rep_event_exception_all_day(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        time.sleep(1)
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
        event_name = 'Test7EditRepEvent_0'
        invitees_email_name = '3cont@autotest.ab'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        time.sleep(1)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(
            new_color_number) + ']'
        mgd.find_element_by_xpath(color_xpath).click()
        name_color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(
            new_color_number) + ']/div[2]/div'
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 9, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 10, cell)
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
        if int(first_value) == 12:
            hover_drum = mgd.find_element_by_id(cal.drum_ampm)
            first_value_ampm = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
            print('first_value_ampm', first_value_ampm)
            hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
            actions = ActionChains(driver_instance)
            actions.move_to_element(hover_drum).click().perform()
            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
            time.sleep(1)
            second_value_ampm = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
            print('second_value_ampm', second_value_ampm)
            if second_value_ampm == first_value_ampm:
                raise Exception('AmPm value incorrect')

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 11, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 12, cell)
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
            print('id_elem_mod_1', id_elem_mod_1)
            element = mgd.find_element_by_id(id_elem_mod_1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(element).move_by_offset(-1, 14).click().perform()
        elif second_value == '25':
            print('2')
            id_elem_new_cell = int(id_elem_split[3]) - 1
            id_elem_mod_1 = 'grid-week-cell-' + str(id_elem_new_cell) + '-' + id_elem_split[4] + ''
            print('id_elem_mod_1', id_elem_mod_1)
            element = mgd.find_element_by_id(id_elem_mod_1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(element).move_by_offset(-1, 14).click().perform()

        else:
            print('3')
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 13, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 14, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 15, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 2) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 3) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 16, cell)
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


# @unittest.skip('Ok + ref 30.08')
class Test7EditSequence3EventsToExceptionStartsDay(unittest.TestCase):
    def setUp(self):
        driver_instance.implicitly_wait(1)
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
        if mgd.find_elements_by_id(cal.all_appointments_panel):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
        driver_instance.implicitly_wait(5)

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

    @classmethod
    def setUpClass(cls):
        driver_instance.implicitly_wait(1)
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
        driver_instance.implicitly_wait(5)

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

        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            if Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            elif Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-0'
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_starts_day_down(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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

        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 1, cell)
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
        if first_value < second_value:
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


# @unittest.skip('Ok + ref 30.08')
class Test7EditSequence4EventsToExceptionEndsDay(unittest.TestCase):
    def setUp(self):
        pass

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

    @classmethod
    def setUpClass(cls):
        driver_instance.implicitly_wait(1)
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
        driver_instance.implicitly_wait(5)

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

        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            if Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            elif Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1] + 1)
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_ends_day_down(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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

        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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


# @unittest.skip('Ok + ref 30.08')
class Test7EditSequence5EventsToExceptionStartsMonth(unittest.TestCase):
    def setUp(self):
        pass

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

    @classmethod
    def setUpClass(cls):
        driver_instance.implicitly_wait(1)
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
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            if Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            elif Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1] + 1)
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_starts_month_down(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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

    # @unittest.skip('Проблемы с переходом на 2 месяца NOT Ok')
    def test2_rep_event_exception_starts_month_down_work(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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
        if Check.find_element_by_css_selector_and_text(month_selector, event_name) is None:
            time.sleep(2)
        elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
        if elem is None:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event in cell')
        time.sleep(2)
        ###############
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        if Check.find_element_by_css_selector_and_text(month_selector, event_name) is None:
            time.sleep(2)
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


# @unittest.skip('Ok + ref 30.08')
class Test7EditSequence6EventsToExceptionEndsMonth(unittest.TestCase):
    def setUp(self):
        pass

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

    @classmethod
    def setUpClass(cls):
        driver_instance.implicitly_wait(1)
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
        driver_instance.implicitly_wait(5)

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

        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            if Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            elif Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1] + 1)
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_ends_month_down(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1] + 1)
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1] + 1)
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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

        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1] + 1)
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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


# @unittest.skip('Ok + ref 30.08')
class Test7EditSequence7EventsToExceptionStartsYear(unittest.TestCase):
    def setUp(self):
        pass

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

    @classmethod
    def setUpClass(cls):
        driver_instance.implicitly_wait(1)
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
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            if Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            elif Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1] + 1)
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_starts_year_down(self):
        event_name = 'Test7EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        event_name = 'Test7EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_day = current_time.strftime('%d')
        print('now_day', now_day)
        if now_day[0] == '0':
            now_day = now_day[1:]
        print('now_day', now_day)

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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
        if Check.find_element_by_css_selector_and_text(month_selector, event_name) is None:
            time.sleep(2)
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
        event_name = 'Test7EditRepEvent_6'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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


# @unittest.skip('Ok + ref 30.08')
class Test7EditSequence8EventsToExceptionEndsYear(unittest.TestCase):
    def setUp(self):
        pass

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

    @classmethod
    def setUpClass(cls):
        driver_instance.implicitly_wait(1)
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
        driver_instance.implicitly_wait(5)

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

        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            if Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            elif Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence'):
                Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1] + 1)
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell = str(cell_list[0]) + '-' + str(cell_list[1] + 1)
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()

    # @unittest.skip('Ok')
    def test1_rep_event_exception_ends_year_down(self):
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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

        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
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
        event_name = 'Test7EditRepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            print('11111')
            cell = str(cell_list[0]) + '-' + str(cell_list[1])
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
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
