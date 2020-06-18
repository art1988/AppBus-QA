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
    print('Start: all_events.py\n')


def tearDownModule():
    print('End: all_events.py\n')
    # driver_instance.quit()


# @unittest.skip('Ok')
class TestShowAllOccurrences1(unittest.TestCase):
    def setUp(self):
        pass

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
        if mgd.find_elements_by_id(cal.all_appointments_panel):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'TestShowAllOccurrences1_0'
        location_name = 'Loc_Occurrences_'
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
        loc_name = location_name + str(1)
        mgd.find_element_by_id(cal.location_input).send_keys(loc_name)

        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        count_i = 2
        while count_i <= 7:
            id_elem = Check.event_in_specific_cells(event_name, count_i, cell)
            mgd.find_element_by_id(id_elem).click()
            mgd.find_element_by_id(cal.edit_prvw).click()
            loc_name = location_name + str(count_i)
            location_input = mgd.find_element_by_id(cal.location_input)
            location_input.clear()
            location_input.send_keys(loc_name)
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
            count_i += 1
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
        event_name = 'Test8AllEvents2_0'
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
    def test1_show_all_occurrences(self):
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        event_name = 'TestShowAllOccurrences1_0'

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0]) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_css_selector(cal.show_all_occurrences).click()
        time.sleep(1)
        if len(mgd.find_elements_by_id(cal.all_appointments_panel)) != 1:
            raise Exception('All appointments panel is missing')
        list_of_elem = []
        for elem in mgd.find_elements_by_class_name(cal.all_event_title):
            if elem.get_attribute('innerText') == event_name:
                list_of_elem.append(elem)
            elif elem.get_attribute('innerText') != event_name:
                raise Exception('All appointment panel contain other events')
        value = 0
        while value < 6:
            location_name = 'Loc_Occurrences_' + str(value + 1)
            print('location_name', location_name)
            # print('list_of_elem', list_of_elem)
            elem = list_of_elem[value]
            elem.click()
            time.sleep(1)
            all_prvw_location = mgd.find_element_by_class_name(cal.location_prvw).get_attribute('innerText')
            print('all_prvw_location', all_prvw_location)
            if all_prvw_location != location_name:
                raise Exception('Wrong location')
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
            value += 1


# @unittest.skip('Ok')
class TestShowAllOccurrences2(unittest.TestCase):
    def setUp(self):
        pass

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
        if mgd.find_elements_by_id(cal.all_appointments_panel):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        mgd.find_element_by_id(cal.spinner).click()
        time.sleep(2)

        event_name = 'TestShowAllOccurrences2_0'
        location_name = 'Loc_Occurrences_'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

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
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Week').click()
        if now_week != '6':
            if now_week != '7':
                Check.find_element_by_class_name_and_text(cal.sub_form_tab, 'Custom').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        loc_name = location_name + str(1)
        mgd.find_element_by_id(cal.location_input).send_keys(loc_name)

        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        count_i = 2
        while count_i <= 8:
            mgd.find_element_by_class_name(cal.navigation_right).click()
            time.sleep(2)
            mgd.find_element_by_id(id_elem).click()
            if Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name) is None:
                actions = ActionChains(driver_instance)
                element = mgd.find_element_by_class_name(cal.navigation_left)
                actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
                time.sleep(2)
                mgd.find_element_by_id(id_elem).click()
            mgd.find_element_by_id(cal.edit_prvw).click()
            loc_name = location_name + str(count_i)
            location_input = mgd.find_element_by_id(cal.location_input)
            location_input.clear()
            location_input.send_keys(loc_name)
            mgd.find_element_by_id(cal.yes_edit_button).click()
            message = 'Update single appointment or the whole sequence?'
            update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
            if update_appointment:
                print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
            time.sleep(1)
            count_i += 1
            time.sleep(1)
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

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
        event_name = 'Test8AllEvents2_0'
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
    def test1_show_all_occurrences(self):
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        event_name = 'TestShowAllOccurrences2_0'

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0]) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_class_name(cal.navigation_right).click()
        mgd.find_element_by_class_name(cal.navigation_right).click()
        time.sleep(2)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_css_selector(cal.show_all_occurrences).click()
        time.sleep(1)
        if len(mgd.find_elements_by_id(cal.all_appointments_panel)) != 1:
            raise Exception('All appointments panel is missing')
        list_of_elem = []
        for elem in mgd.find_elements_by_class_name(cal.all_event_title):
            if elem.get_attribute('innerText') == event_name:
                list_of_elem.append(elem)
            elif elem.get_attribute('innerText') != event_name:
                raise Exception('All appointment panel contain other events')
        value = 0
        while value < 6:
            location_name = 'Loc_Occurrences_' + str(value + 1)
            print('location_name', location_name)
            # print('list_of_elem', list_of_elem)
            elem = list_of_elem[value]
            elem.click()
            time.sleep(1)
            all_prvw_location = mgd.find_element_by_class_name(cal.location_prvw).get_attribute('innerText')
            print('all_prvw_location', all_prvw_location)
            if all_prvw_location != location_name:
                raise Exception('Wrong location')
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_left)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
            value += 1

    # @unittest.skip('Ok')
    def test2_show_all_occurrences(self):
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        event_name = 'TestShowAllOccurrences2_0'

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0]) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_xpath(cal.overlay)
        actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_class_name(cal.navigation_right).click()
        mgd.find_element_by_class_name(cal.navigation_right).click()
        time.sleep(2)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_css_selector(cal.show_all_occurrences).click()
        time.sleep(1)
        if len(mgd.find_elements_by_id(cal.all_appointments_panel)) != 1:
            raise Exception('All appointments panel is missing')
        list_of_elem = []
        for elem in mgd.find_elements_by_class_name(cal.all_event_title):
            if elem.get_attribute('innerText') == event_name:
                list_of_elem.append(elem)

        location_name = 'Loc_Occurrences_' + str(4)
        print('location_name', location_name)
        elem = list_of_elem[3]
        elem.click()
        time.sleep(1)
        all_prvw_location = mgd.find_element_by_class_name(cal.location_prvw).get_attribute('innerText')
        print('all_prvw_location', all_prvw_location)
        if all_prvw_location != location_name:
            raise Exception('Wrong location name')
        # mgd.find_element_by_id(cal.show_in_grid_button).click()
        mgd.find_element_by_css_selector('#tooltip-container-undefined > div > div.options-panel > span').click()
        if not mgd.find_element_by_id(cal.location_input).get_attribute('innerText'):
            time.sleep(1)
        location_in_edit = mgd.find_element_by_id(cal.location_input).get_attribute(name='value')
        print('location_in_edit', location_in_edit)
        if location_in_edit != location_name:
            raise Exception('Wrong location name')
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_class_name(cal.navigation_left)
        actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
        time.sleep(2)

        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_css_selector(cal.show_all_occurrences).click()
        time.sleep(1)
        if len(mgd.find_elements_by_id(cal.all_appointments_panel)) != 1:
            raise Exception('All appointments panel is missing')
        list_of_elem = []
        for elem in mgd.find_elements_by_class_name(cal.all_event_title):
            if elem.get_attribute('innerText') == event_name:
                list_of_elem.append(elem)

        location_name = 'Loc_Occurrences_' + str(8)
        print('location_name', location_name)
        actions = ActionChains(driver_instance)
        element = list_of_elem[7]
        actions.move_to_element(element).click().perform()
        time.sleep(1)
        all_prvw_location = mgd.find_element_by_class_name(cal.location_prvw).get_attribute('innerText')
        print('all_prvw_location', all_prvw_location)
        if all_prvw_location != location_name:
            raise Exception('Wrong location name')
        # mgd.find_element_by_id(cal.show_in_grid_button).click()
        mgd.find_element_by_css_selector('#tooltip-container-undefined > div > div.options-panel > span').click()
        if not mgd.find_element_by_id(cal.location_input).get_attribute('innerText'):
            time.sleep(1)
        location_in_edit = mgd.find_element_by_id(cal.location_input).get_attribute(name='value')
        print('location_in_edit', location_in_edit)
        if location_in_edit != location_name:
            raise Exception('Wrong location name')
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_class_name(cal.navigation_left)
        actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
