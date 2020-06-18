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
class Test9AllDayEvents1(unittest.TestCase):
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

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

    @classmethod
    def tearDownClass(cls):
        i = 0
        while i != 2:
            if i == 0:
                event_name = 'Test9AllDayEvents1_0'
            else:
                event_name = 'Test9AllDayEvents1_1'
            Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
            mgd.find_element_by_id(cal.delete_prvw).click()
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
            i += 1

    # @unittest.skip('Ok')
    def test1_allday_events_create_button(self):
        mgd.find_element_by_id(cal.add_event_button).click()
        event_name = 'Test9AllDayEvents1_0'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        mgd.find_element_by_css_selector(cal.all_day_button).click()
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        timezone_field = mgd.find_element_by_xpath(cal.timezone_disabled).get_attribute(name='class')
        if 'disabled' not in timezone_field:
            raise Exception('Timezone not disabled')
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')

        if value_time_starts_full != value_time_starts_full_2:
            raise Exception('Starts time incorrect')
        if value_time_ends_full != value_time_ends_full_2:
            raise Exception('Ends time is incorrect')

    # @unittest.skip('Ok')
    def test2_allday_events_create_grid(self):
        if mgd.find_elements_by_id('grid-week-all-day-cell-0-1'):
            mgd.find_element_by_id('grid-week-all-day-cell-0-1').click()
        elif mgd.find_elements_by_id('grid-week-all-day-cell-0-2'):
            mgd.find_element_by_id('grid-week-all-day-cell-0-2').click()
        else:
            mgd.find_element_by_id('grid-week-all-day-cell-0-3').click()
        event_name = 'Test9AllDayEvents1_1'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        value_time_starts_full = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        value_time_starts_full_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        value_time_ends_full_2 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')

        if value_time_starts_full != value_time_starts_full_2:
            raise Exception('Starts time incorrect')
        if value_time_ends_full != value_time_ends_full_2:
            raise Exception('Ends time is incorrect')


# @unittest.skip('Ok')
class Test9AllDayEvents2(unittest.TestCase):
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

        mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        mgd.find_element_by_id(cal.add_event_button).click()
        event_name = 'Test9AllDayEvents2_0'
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        mgd.find_element_by_css_selector(cal.all_day_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        event_name = 'Test9AllDayEvents2_0'
        mgd.find_element_by_class_name(cal.today_button).click()
        view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
        view_button.click()

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.delete_prvw).click()
        driver_instance.implicitly_wait(1)
        delete_single_or_sequence = 'Delete single appointment or the whole sequence?'
        if Check.find_element_by_class_name_and_text(cal.block_wrapper, delete_single_or_sequence):
            print('Check - Block wrapper')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        elif Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?'):
            print('Check - Delete button')
            Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        driver_instance.implicitly_wait(5)

    # @unittest.skip('Ok')
    def test1_allday_events_edit_location(self):
        event_name = 'Test9AllDayEvents2_0'
        location = 'New Orleans'
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.location_input).send_keys(location)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        location_prvw = mgd.find_element_by_class_name(cal.location_prvw).get_attribute('innerText')
        if location_prvw != location:
            raise Exception('Location preview incorrect')
        mgd.find_element_by_id(cal.edit_prvw).click()
        location_edit = mgd.find_element_by_id(cal.location_input).get_attribute(name='value')
        if location_edit != location:
            raise Exception('Location in edit is incorrect')

    # @unittest.skip('Ok')
    def test1_allday_events_edit_notes(self):
        event_name = 'Test9AllDayEvents2_0'
        notes = 'Reset server sessions'
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.notes_input).send_keys(notes)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        notes_prvw = mgd.find_element_by_class_name(cal.notes_prvw).get_attribute('innerText')
        if notes_prvw != notes:
            raise Exception('Location preview incorrect')
        mgd.find_element_by_id(cal.edit_prvw).click()
        notes_edit = mgd.find_element_by_id(cal.notes_input).get_attribute(name='value')
        if notes_edit != notes:
            raise Exception('Location in edit is incorrect')

    # @unittest.skip('Ok')
    def test1_allday_events_edit_alerts(self):
        event_name = 'Test9AllDayEvents2_0'
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Alert').click()
        Check.find_element_by_class_name_and_text(cal.alert_title, '1 hour').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        alert_value = mgd.find_element_by_xpath(cal.alert_value).get_attribute('innerText')
        if alert_value != '1 hour':
            raise Exception('Wrong Alert')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
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
    def test1_allday_events_edit_color(self):
        event_name = 'Test9AllDayEvents2_0'
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        color_attribute_edit_event = mgd.find_element_by_class_name(cal.color_field).get_attribute(name='class')
        color_split_edit_event = color_attribute_edit_event.split(' ')
        color_default_edit_event = color_split_edit_event[1].lower()
        print('color_default_edit_event - ', color_default_edit_event)

        Check.find_element_by_class_name_and_text(cal.title_class, 'Color').click()
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
        print('new_color_name', new_color_name)
        new_color_name_split = new_color_name.split(' ')
        new_color = new_color_name_split[1].lower()
        # new_color = color_default_edit_event
        print('new_color (=)', new_color)
        while new_color == color_default_edit_event:
            new_color_number = random.randrange(1, number_of_colors, 1)
            print('new_color_number', new_color_number)
            color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(
                new_color_number) + ']'
            mgd.find_element_by_xpath(color_xpath).click()
            name_color_xpath = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[' + str(
                new_color_number) + ']/div[1]'
            new_color_name = mgd.find_element_by_xpath(name_color_xpath).get_attribute('innerText')
            print('new_color_name', new_color_name)
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
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        color_new_attribute_edit_event_2 = mgd.find_element_by_class_name(cal.color_field).get_attribute(name='class')
        color_new_split_edit_event_2 = color_new_attribute_edit_event_2.split(' ')
        color_new_default_edit_event_2 = color_new_split_edit_event_2[1].lower()
        print('color_new_default_edit_event_2 - ', color_new_default_edit_event_2)
        if color_new_default_edit_event_2 != new_color:
            raise Exception('Color does not match')

    # @unittest.skip('Ok')
    def test1_allday_events_edit_title(self):
        event_name = 'Test9AllDayEvents2_0'
        event_name_new = 'Test9AllDay New_title'
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        time.sleep(1)
        mgd.find_element_by_id(cal.title_input).clear()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name_new)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.subject, event_name_new).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        time.sleep(1)
        mgd.find_element_by_id(cal.title_input).clear()
        mgd.find_element_by_id(cal.title_input).send_keys(event_name)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)

    # @unittest.skip('Ok')
    def test2_allday_events_edit_starts_day(self):
        event_name = 'Test9AllDayEvents2_0'
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_1 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_1 = datetime.strptime(starts_1, "%d %b %Y")
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
        starts_time_2 = datetime.strptime(starts_2, "%d %b %Y")
        if modify_time == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_3 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_3 = datetime.strptime(starts_3, "%d %b %Y")
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
        starts_time_4 = datetime.strptime(starts_4, "%d %b %Y")
        if starts_time_4 == starts_time_1:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_5 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_5 = datetime.strptime(starts_5, "%d %b %Y")
        if starts_time_4 == starts_time_5:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test2_allday_events_edit_starts_day2(self):
        event_name = 'Test9AllDayEvents2_0'
        current_time = datetime.now()
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_1 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_1 = datetime.strptime(starts_1, "%d %b %Y")
        time_delta = timedelta(days=1)
        modify_time = starts_time_1 - time_delta
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
        # mgd.find_element_by_xpath(cal.starts_other_view).click()

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
        starts_2 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_2 = datetime.strptime(starts_2, "%d %b %Y")
        if modify_time == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        if now_week == 0:
            mgd.find_element_by_class_name(cal.navigation_left).click()

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_3 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_3 = datetime.strptime(starts_3, "%d %b %Y")
        if starts_time_3 == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Starts').click()
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
        starts_4 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_4 = datetime.strptime(starts_4, "%d %b %Y")
        if starts_time_4 == starts_time_1:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        if now_week == 0:
            mgd.find_element_by_class_name(cal.navigation_right).click()

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_5 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_5 = datetime.strptime(starts_5, "%d %b %Y")
        if starts_time_4 == starts_time_5:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test2_allday_events_edit_starts_month(self):
        event_name = 'Test9AllDayEvents2_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        now_month = current_time.strftime('%m')
        if now_month[0] == '0':
            now_month = now_month[1]
        print('now_month', now_month)
        print('now_week', now_week)

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_1 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_1 = datetime.strptime(starts_1, "%d %b %Y")
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
        starts_time_2 = datetime.strptime(starts_2, "%d %b %Y")
        day_from_starts = starts_time_2.strftime('%d')
        if day_from_starts[0] == '0':
            day_from_starts = day_from_starts[1]
        print('day_from_starts', day_from_starts)
        if modify_time == starts_time_2:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

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

        mgd.find_element_by_id(cal.edit_prvw).click()
        starts_3 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_3 = datetime.strptime(starts_3, "%d %b %Y")
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
        starts_time_4 = datetime.strptime(starts_4, "%d %b %Y")
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
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_5 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_5 = datetime.strptime(starts_5, "%d %b %Y")
        if starts_time_4 == starts_time_5:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test2_allday_events_edit_starts_year(self):
        event_name = 'Test9AllDayEvents2_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_1 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_1 = datetime.strptime(starts_1, "%d %b %Y")
        starts_split = starts_1.split(' ')
        starts_year = starts_split[2]
        print('starts_year', starts_year)
        starts_month = time.strptime(starts_split[1], '%b').tm_mon
        print('starts_month', starts_month)
        days_in_month = calendar.monthrange(int(starts_year), int(starts_month))
        print('days_in_month', days_in_month)
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
        starts_time_2 = datetime.strptime(starts_2, "%d %b %Y")
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
        starts_time_3 = datetime.strptime(starts_3, "%d %b %Y")
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
        starts_time_4 = datetime.strptime(starts_4, "%d %b %Y")
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
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        starts_5 = mgd.find_element_by_xpath(cal.starts_other_view).get_attribute('innerText')
        starts_time_5 = datetime.strptime(starts_5, "%d %b %Y")
        if starts_time_4 == starts_time_5:
            print('Check - Starts time is right')
        else:
            raise Exception('Starts time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test3_allday_events_edit_ends_month(self):
        event_name = 'Test9AllDayEvents2_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_1 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_1 = datetime.strptime(ends_1, "%d %b %Y")
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
        ends_time_2 = datetime.strptime(ends_2, "%d %b %Y")
        day_from_ends = ends_time_2.strftime('%d')
        if day_from_ends[0] == '0':
            day_from_ends = day_from_ends[1]
        print('day_from_ends', day_from_ends)
        if modify_time == ends_time_2:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        ends_3 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_3 = datetime.strptime(ends_3, "%d %b %Y")
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
        ends_time_4 = datetime.strptime(ends_4, "%d %b %Y")
        if ends_time_4 == ends_time_1:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_5 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_5 = datetime.strptime(ends_5, "%d %b %Y")
        if ends_time_4 == ends_time_5:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test3_allday_events_edit_ends_day(self):
        event_name = 'Test9AllDayEvents2_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_1 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_1 = datetime.strptime(ends_1, "%d %b %Y")
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
        ends_time_2 = datetime.strptime(ends_2, "%d %b %Y")
        if modify_time == ends_time_2:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        ends_3 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_3 = datetime.strptime(ends_3, "%d %b %Y")
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
        ends_time_4 = datetime.strptime(ends_4, "%d %b %Y")
        if ends_time_4 == ends_time_1:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_5 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_5 = datetime.strptime(ends_5, "%d %b %Y")
        if ends_time_4 == ends_time_5:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test3_allday_events_edit_ends_year(self):
        event_name = 'Test9AllDayEvents2_0'
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        now_week = current_time.strftime('%w')
        print('now_week', now_week)

        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_1 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_1 = datetime.strptime(ends_1, "%d %b %Y")
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
        ends_time_2 = datetime.strptime(ends_2, "%d %b %Y")
        day_from_ends = ends_time_2.strftime('%d')
        if day_from_ends[0] == '0':
            day_from_ends = day_from_ends[1]
        print('day_from_ends', day_from_ends)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        ends_3 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_3 = datetime.strptime(ends_3, "%d %b %Y")
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
        ends_time_4 = datetime.strptime(ends_4, "%d %b %Y")
        if ends_time_4 == ends_time_1:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()

        ends_5 = mgd.find_element_by_xpath(cal.ends_other_view).get_attribute('innerText')
        ends_time_5 = datetime.strptime(ends_5, "%d %b %Y")
        if ends_time_4 == ends_time_5:
            print('Check - Ends time is right')
        else:
            raise Exception('Ends time is incorrect')
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test4_allday_events_edit_invitees(self):
        event_name = 'Test9AllDayEvents2_0'
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        Check.find_element_by_class_name_and_text(cal.no_invitees, 'There are no invitees')
        print('Check - Text: There are no invitees')
        mgd.find_element_by_class_name(cal.plus_icon).click()
        driver_instance.implicitly_wait(1)
        mgd.find_element_by_class_name(cal.contact_items)
        print('Check - invitees items')
        driver_instance.implicitly_wait(5)
        mgd.find_element_by_class_name(cal.contact_search).send_keys('contact')
        Check.find_element_by_class_name_and_text(cal.contact_name, 'Contact for autotest 1').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.email_invitees, '1cont@autotest.ab')
        mgd.find_element_by_id(cal.yes_edit_button).click()

        if not Check.find_element_by_class_name_and_text(cal.invitees_count, '1'):
            raise Exception('Wrong number of contacts')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        if not Check.find_element_by_class_name_and_text(cal.invitees_count, '1'):
            raise Exception('Wrong number of contacts')
        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        Check.find_element_by_class_name_and_text(cal.email_invitees, '1cont@autotest.ab')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()

    # @unittest.skip('Ok')
    def test9_allday_events_edit_repeated(self):
        event_name = 'Test9AllDayEvents2_0'
        Check.find_element_by_class_name_and_text(cal.subject, event_name).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Repeat').click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Every Day').click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        event_list = []
        for elem in mgd.find_elements_by_class_name(cal.subject):
            if elem.get_attribute('innerText') == event_name:
                event_list.append(elem)
        time.sleep(1)
        mgd.find_element_by_class_name(cal.navigation_right).click()
        for elem in mgd.find_elements_by_class_name(cal.subject):
            if elem.get_attribute('innerText') == event_name:
                event_list.append(elem)
        time.sleep(1)
        mgd.find_element_by_class_name(cal.navigation_right).click()
        for elem in mgd.find_elements_by_class_name(cal.subject):
            if elem.get_attribute('innerText') == event_name:
                event_list.append(elem)
        if len(event_list) < 14:
            raise Exception('Wrong count of events')
