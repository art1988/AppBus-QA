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

mgd = Maw.get_devices()
cal = Config.Calendar.main_calendar.Elements
driver_instance.implicitly_wait(5)
wait = WebDriverWait(mgd, 10)
timezone_default = 'Asia/Yekaterinburg'


def setUpModule():
    print('Start: repeat_rules.py\n')


def tearDownModule():
    print('End: repeat_rules.py\n')
    # driver_instance.quit()


# @unittest.skip('OK')
class Test8ThreeRepeatRule1SameDay(unittest.TestCase):
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
        view_button.click()
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

        event_name = 'Test8ThreeRepeatRule_0'
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

        event_name = 'Test8ThreeRepeatRule_0'
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
    def test1_rep_event_occur_on_the_same_day1(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 2, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test1_rep_event_occur_on_the_same_day2(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 2, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test1_rep_event_occur_on_the_same_day3(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 2, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
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

        #################
        hover_drum = mgd.find_element_by_id(cal.drum_month)
        first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).perform()
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()


# @unittest.skip('OK')
class Test8ThreeRepeatRule2DifferentOrder(unittest.TestCase):
    def setUp(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
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

        event_name = 'Test8ThreeRepeatRule_0'
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
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()

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
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        time.sleep(1)

        event_name = 'Test8ThreeRepeatRule_0'
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
    def test1_rep_event_occur_different_order1(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 2, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).perform()
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
        if first_value > second_value:
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test1_rep_event_occur_different_order2(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 6, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 6, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).perform()
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test1_rep_event_occur_different_order3(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 2, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).perform()
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test1_rep_event_occur_different_order4(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 7, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 7, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).perform()
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
        if first_value > second_value:
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()


# @unittest.skip('OK')
class Test8ThreeRepeatRule3Overlap(unittest.TestCase):
    def setUp(self):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        time.sleep(1)

    def tearDown(self):
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()
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

    @classmethod
    def setUpClass(cls):
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test8ThreeRepeatRule_0'
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
        id_elem = Check.event_in_specific_cells(event_name, 4, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
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
        mgd.find_element_by_class_name(cal.delete_prvw).click()
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
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
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
        mgd.find_element_by_id(id_elem).click()
        time.sleep(1)
        mgd.find_element_by_id(cal.edit_prvw).click()
        location_name = 'exp'
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
        id_elem = Check.event_in_specific_cells(event_name, 11, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_class_name(cal.delete_prvw).click()
        message = 'Delete this event?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
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
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()
        time.sleep(1)

        event_name = 'Test8ThreeRepeatRule_0'
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
    def test1_rep_event_occur_overlap1(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 1, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 1, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.ends_other_view).click()
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
        if first_value > second_value:
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
        ############

        mgd.find_element_by_id(cal.yes_edit_button).click()

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test1_rep_event_occur_overlap2(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 2, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.ends_other_view).click()
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
        if first_value > second_value:
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test1_rep_event_occur_overlap3(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 3, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.ends_other_view).click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).perform()
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
        if first_value > second_value:
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
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            print('Check - Block wrapper with notification')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'OK').click()

    # @unittest.skip('Ok')
    def test1_rep_event_occur_overlap4(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 3, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 3, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.ends_other_view).click()
        #################
        hover_drum = mgd.find_element_by_id(cal.drum_day)
        first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).perform()
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
        if first_value > second_value:
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
        ############
        hover_drum = mgd.find_element_by_id(cal.drum_minutes)
        first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
        print('first_value', first_value)
        hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_drum).click().perform()

        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
        try:
            actions.click(hidden_arrow).click(hidden_arrow).click(hidden_arrow).click(hidden_arrow).\
                click(hidden_arrow).click(hidden_arrow).perform()
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
        if first_value < second_value:
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

        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        driver_instance.implicitly_wait(1)
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            time.sleep(2)
            raise Exception('Overlap notification  - exist')
        driver_instance.implicitly_wait(5)

    # @unittest.skip('Ok')
    def test1_rep_event_occur_overlap5(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 5, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 5, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
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
        if first_value > second_value:
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
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        driver_instance.implicitly_wait(1)
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            raise Exception('Overlap notification  - exist')
        driver_instance.implicitly_wait(5)

    # @unittest.skip('Ok')
    def test1_rep_event_occur_overlap6(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 9, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 9, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
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
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        driver_instance.implicitly_wait(1)
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            raise Exception('Overlap notification  - exist')
        driver_instance.implicitly_wait(5)

    # @unittest.skip('Ok падает из-за бага')
    def test1_rep_event_occur_overlap7(self):
        event_name = 'Test8ThreeRepeatRule_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = Check.event_in_specific_cells(event_name, 12, cell)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = Check.event_in_specific_cells(event_name, 12, cell)
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.edit_prvw).click()

        mgd.find_element_by_xpath(cal.starts_other_view).click()
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
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, message):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
        wont_be_saved_sequence = "Repeat fields are shared across the sequence and won't be saved"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, wont_be_saved_sequence):
            print('Check - Block wrapper with drop sequence')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Edit anyway').click()
        driver_instance.implicitly_wait(1)
        notification = "Two occurrences of a sequence can't occur on the same day, " \
                       "overlap, or occur in different order than the initial one"
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, notification):
            raise Exception('Overlap notification  - exist')
        driver_instance.implicitly_wait(5)
