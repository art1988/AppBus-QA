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
class Test6EditSingleEvents(unittest.TestCase):
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
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Yes').click()

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

        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        if mgd.find_elements_by_id(cal.delete_prvw):
            mgd.find_element_by_id(cal.delete_prvw).click()
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            time.sleep(1)
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

        time.sleep(2)
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-0'
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()

        mgd.find_element_by_id(cal.delete_prvw).click()

        Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
            print('Check - Delete button')
        else:
            raise Exception('Block wrapper exist')

    # @unittest.skip('Ok')
    def test1_1single_event_location(self):
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        mgd.find_element_by_id(cal.edit_prvw).click()

        notes_text = 'The Nerevar will come!'
        time.sleep(1)
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_id(cal.notes_input)
        actions.move_to_element(element).click().perform()
        element.send_keys(notes_text)
        mgd.find_element_by_id(cal.yes_edit_button).click()
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        mgd.find_element_by_id(cal.edit_prvw).click()

        timezone_base = mgd.find_element_by_xpath(cal.timezone_value).get_attribute('innerText')
        print('timezone_base', timezone_base)
        Check.find_element_by_class_name_and_text(cal.title_class, 'Timezone').click()
        Check.find_element_by_class_name_and_text(cal.time_zones_name, 'Asia/Colombo (UTC+05:30)').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        timezone_first = mgd.find_element_by_xpath(cal.timezone_value).get_attribute('innerText')
        print('timezone_first', timezone_first)
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
        print('timezone_second', timezone_second)
        if timezone_first != timezone_second:
            raise Exception('Timezone still the same')

        Check.find_element_by_class_name_and_text(cal.title_class, 'Timezone').click()
        Check.find_element_by_class_name_and_text(cal.time_zones_name, 'Asia/Yekaterinburg (UTC+05:00)').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        timezone_third = mgd.find_element_by_xpath(cal.timezone_value).get_attribute('innerText')
        print('timezone_third', timezone_third)
        if timezone_second == timezone_third:
            raise Exception('Timezone still the same')
        if timezone_third != timezone_base:
            raise Exception('Timezone does not match')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_1single_event_alert(self):
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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

        if not Check.find_element_by_class_name_and_text(cal.invitees_count, '1'):
            raise Exception('Wrong number of contacts')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
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
        mgd.find_element_by_id(cal.edit_prvw).click()
        if not Check.find_element_by_class_name_and_text(cal.invitees_count, '1'):
            raise Exception('Wrong number of contacts')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        Check.find_element_by_class_name_and_text(cal.email_invitees, '1cont@autotest.ab')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_1single_event_color(self):
        event_name = 'Test6EditEvent_0'
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        if second_value == '1':
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        now_month = current_time.strftime('%m')
        if now_month[0] == '0':
            now_month = now_month[1]
        print('now_month', now_month)
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        print('starts_time_1', starts_time_1)
        print('modify_time', modify_time)
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
        view_button.click()
        if int(starts_month) == int(now_month):
            mgd.find_element_by_class_name(cal.navigation_right).click()
        month_selector = '#grid-month-cell-' + day_from_starts + ' .subject'
        if Check.find_element_by_css_selector_and_text(month_selector, event_name) is None:
            time.sleep(2)
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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

        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        print('starts_2_month', starts_2_month)
        Check.find_element_by_class_name_and_text(cal.month_title_year_view, starts_2_month.upper()).click()

        month_selector = '#grid-month-cell-' + day_from_starts + ' .subject'
        if Check.find_element_by_css_selector_and_text(month_selector, event_name) is None:
            time.sleep(2)
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        if second_value == '1':
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')
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
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')
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
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test1_3single_event_ends_time(self):
        event_name = 'Test6EditEvent_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-0'
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
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')
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
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')
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
        value_time_for_compare = value_time_starts + ' – ' + value_time_ends
        # date_prvw_mod = mgd.find_element_by_class_name(cal.date_prvw).get_attribute('innerText')
        # if value_time_for_compare not in date_prvw_mod:
        #     raise Exception('Wrong Time preview')

        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

    @unittest.skip('NOT Ok')
    def test1_4single_event_all_day(self):
        event_name = 'Test6EditEvent_0'
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
class Test6EditSingleEventsRepeat(unittest.TestCase):
    def setUp(self):
        event_name = 'Test6EditEventRep_1'
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

        event_name = 'Test6EditEventRep_1'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        cell_list = Check.find_cell_week_number(now_time)
        cell_mod = cell_list[0] + 1
        cell = str(cell_mod) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        css_name = '#' + id_elem + '> div > div > span:nth-child(1)'
        if not Check.find_element_by_css_selector_and_text(css_name, event_name):
            time.sleep(2)
        mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)

        mgd.find_element_by_id(cal.delete_prvw).click()
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

        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        pass

    # @unittest.skip('Ok')
    def test1_1single_event_repeat_every_day(self):
        event_name = 'Test6EditEventRep_1'
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
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()
        #####################

        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        # добавить проверки для каждоо дня \\ done
        Check.event_in_cells(event_name, 10, cell)
        print('Check - Event sequence')

    # @unittest.skip('Ok')
    def test1_2single_event_repeat_every_week_custom(self):
        event_name = 'Test6EditEventRep_1'
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
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
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
        event_name = 'Test6EditEventRep_1'
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
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()

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
        Check.event_in_cells_custom(event_name, day_index, 10, cell)

    # @unittest.skip('Ok')
    def test1_4single_event_repeat_on_day_of_month(self):
        event_name = 'Test6EditEventRep_1'
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
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()
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

        Check.event_in_cells_month(event_name, 5, month_selector)

    # @unittest.skip('Ok')
    def test1_5single_event_repeat_on_day_of_week(self):
        event_name = 'Test6EditEventRep_1'
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
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()
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
            print('Check - Event in cell')

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            value += 1
            mgd.find_element_by_class_name(cal.navigation_right).click()
            print('Check - Right button')

    # @unittest.skip('Ok')
    def test1_6single_event_repeat_on_date(self):
        event_name = 'Test6EditEventRep_1'
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
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()
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

            # mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            print('date_month -3:', date_month[:3])
            Check.find_element_by_class_name_and_text(cal.month_title_year_view, date_month[:3].upper()).click()

            month_selector = '#grid-month-cell-' + date_day + ' .subject'
            time.sleep(2)
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
            value += 1

    # @unittest.skip('Ok')
    def test1_7single_event_repeat_year_on_day_of_week(self):
        event_name = 'Test6EditEventRep_1'
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
        driver_instance.implicitly_wait(1)
        if not Check.find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_xpath(cal.overlay)
            actions.move_to_element(element).move_by_offset(-450, -300).click().perform()
            cell_mod = cell_list[0]
            cell = str(cell_mod) + '-' + str(cell_list[1])
            id_elem = 'grid-week-cell-' + cell + ''
            mgd.find_element_by_id(id_elem).click()
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_id(cal.edit_prvw).click()
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

            # mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)
            #######################################
            print('year_month_select 3', month_select_value[:3])
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
            time.sleep(2)
            if Check.find_element_by_css_selector_and_text(month_cell_selector, event_name) is None:
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
