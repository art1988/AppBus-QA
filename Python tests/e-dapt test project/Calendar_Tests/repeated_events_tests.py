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


# @unittest.skip('in on_day_of_month add check, Ok')
class Test4RepeatedEvents(unittest.TestCase):
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

        name = 'Test4RepEvent_'
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
                delete_single_or_sequence = 'Delete single appointment or the whole sequence?'

                if Check.find_element_by_class_name_and_text(cal.block_wrapper, delete_single_or_sequence):
                    print('Check - Block wrapper')
                    Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
                if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?'):
                    print('Check - Delete button')
                    Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
                driver_instance.implicitly_wait(1)
                if Check.find_element_by_class_name_and_text(cal.event_name_in_cell, event_name) is None:
                    print('Check - Event deleted')
                else:
                    raise Exception('Event not deleted')
        driver_instance.implicitly_wait(5)

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

    def test1_create_rep_event_every_day(self):
        event_name = 'Test4RepEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0]) + '-' + str(cell_list[1])
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
        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        # добавить проверки для каждого дня \\ done
        Check.event_in_cells(event_name, 15, cell)
        print('Check - Event sequence')

    def test2_create_rep_event_custom(self):
        event_name = 'Test4RepEvent_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
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

    def test3_create_rep_event_weekdays(self):
        event_name = 'Test4RepEvent_2'
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
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Week').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On weekdays')
        interval_value = mgd.find_element_by_xpath(cal.selector_for_interval).get_attribute('innerText')
        print('interval_value', interval_value)
        if interval_value != '1':
            raise Exception('Wrong Interval value')

        day_index = list([1, 2, 3, 4, 5])

        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        day_index.sort()
        time.sleep(2)
        Check.event_in_cells_custom(event_name, day_index, 30, cell)

    def test4_create_rep_event_on_day_of_month(self):
        event_name = 'Test4RepEvent_3'
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
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Month').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of month')
        interval_value = mgd.find_element_by_xpath(cal.selector_for_interval).get_attribute('innerText')
        print('interval_value', interval_value)
        if interval_value != '1':
            raise Exception('Wrong Interval value')
        day_of_month_value = mgd.find_element_by_xpath(cal.selector_for_day_of_month).get_attribute('innerText')
        print('day_of_month_value', day_of_month_value)
        if day_of_month_value != now_day:
            raise Exception('Wrong Day of Month value')

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

        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()

        Check.event_in_cells_month(event_name, 10, month_selector)

    def test5_create_rep_event_on_day_of_week(self):
        event_name = 'Test4RepEvent_4'
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
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Month').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of week').click()
        interval_value = mgd.find_element_by_xpath(cal.selector_for_interval).get_attribute('innerText')
        print('interval_value', interval_value)
        if interval_value != '1':
            raise Exception('Wrong Interval value')

        weekday_value = mgd.find_element_by_xpath(cal.selector_for_weekdays).get_attribute('innerText')
        print('weekday_value', weekday_value)
        week_number_value = mgd.find_element_by_xpath(cal.selector_for_week).get_attribute('innerText')
        print('week_number_value', week_number_value)

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

            month_cell = Check.day_of_week_in_month(str(new_month_year), new_month_month, week_number_value, weekday_value)

            month_cell_selector = '#grid-month-cell-' + str(month_cell) + ' .subject'
            print('month_cell_selector', month_cell_selector)
            time.sleep(1)
            if Check.find_element_by_css_selector_and_text(month_cell_selector, event_name) is None:
                time.sleep(2)
            elem = Check.find_element_by_css_selector_and_text(month_cell_selector, event_name)
            if elem is None:
                raise Exception('ERRRRRRROR')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event' + str(value) + 'in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            value += 1
            mgd.find_element_by_class_name(cal.navigation_right).click()
            print('Check - Right button')

    def test6_create_rep_event_on_date(self):
        event_name = 'Test4RepEvent_5'
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
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Year').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On date').click()
        interval_value = mgd.find_element_by_xpath(cal.selector_for_interval).get_attribute('innerText')
        print('interval_value', interval_value)
        if interval_value != '1':
            raise Exception('Wrong Interval value')
        day_of_month_value = mgd.find_element_by_xpath(cal.selector_for_day_of_month).get_attribute('innerText')
        print('day_of_month_value', day_of_month_value)
        month_select_value = mgd.find_element_by_xpath(cal.selector_for_month).get_attribute('innerText')
        print('month_select_value', month_select_value)
        date_month = month_select_value
        print('date_month', date_month)
        date_day = day_of_month_value
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

            # mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            print('date_month -3:', date_month[:3])
            Check.find_element_by_class_name_and_text(cal.month_title_year_view, date_month[:3].upper()).click()

            month_selector = '#grid-month-cell-' + date_day + ' .subject'

            if Check.find_element_by_css_selector_and_text(month_selector, event_name) is None:
                time.sleep(2)
            elem = Check.find_element_by_css_selector_and_text(month_selector, event_name)
            if elem is None:
                raise Exception('Event not found')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event' + str(value) + 'in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            value += 1

    def test7_create_rep_event_year_on_day_of_week(self):
        event_name = 'Test4RepEvent_6'
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
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Year').click()
        Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'On day of week').click()
        interval_value = mgd.find_element_by_xpath(cal.selector_for_interval).get_attribute('innerText')
        print('interval_value', interval_value)
        if interval_value != '1':
            raise Exception('Wrong Interval value')

        week_number_value = mgd.find_element_by_xpath(cal.selector_for_week).get_attribute('innerText')
        print('week_number_value', week_number_value)
        month_select_value = mgd.find_element_by_xpath(cal.selector_for_month).get_attribute('innerText')
        print('month_select_value', month_select_value)
        weekday_value = mgd.find_element_by_xpath(cal.selector_for_weekdays).get_attribute('innerText')
        print('weekday_value', weekday_value)

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
            print('month_select_value 3', month_select_value[:3])
            Check.find_element_by_class_name_and_text(cal.month_title_year_view, month_select_value[:3].upper()).click()
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

            month_cell = Check.day_of_week_in_month(str(new_month_year), new_month_month,
                                                    week_number_value, weekday_value)

            month_cell_selector = '#grid-month-cell-' + str(month_cell) + ' .subject'
            time.sleep(1)
            elem = Check.find_element_by_css_selector_and_text(month_cell_selector, event_name)
            time.sleep(1)
            if elem is None:
                raise Exception('ERRRRRRROR')
            time.sleep(1)
            actions = ActionChains(driver_instance)
            actions.move_to_element(elem).click().perform()
            print('Check - Event' + str(value) + 'in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()

            value += 1