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
class Test5Alerts(unittest.TestCase):
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
            message_delete_on_another = 'The event has been deleted on another device'
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, message_delete_on_another) is not None:
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
            message_delete_on_another = 'The event has been deleted on another device'
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, message_delete_on_another) is not None:
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
            time.sleep(2)
            mgd.find_element_by_id(cal.spinner).click()
            print('Spinner click')
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            # time.sleep(2)

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
            message_delete_on_another = 'The event has been deleted on another device'
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, message_delete_on_another) is not None:
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
            message_delete_on_another = 'The event has been deleted on another device'
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, message_delete_on_another) is not None:
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
            time.sleep(2)
            mgd.find_element_by_id(cal.spinner).click()
            print('Spinner click')
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            # time.sleep(2)

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
            message_delete_on_another = 'The event has been deleted on another device'
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, message_delete_on_another) is not None:
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
            message_delete_on_another = 'The event has been deleted on another device'
            if Check.find_element_by_class_name_and_text(cal.block_wrapper, message_delete_on_another) is not None:
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
            time.sleep(2)
            mgd.find_element_by_id(cal.spinner).click()
            print('Spinner click')
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            # time.sleep(2)

            css = '#' + id_elem + ' > div > div > span:nth-child(1)'
            count += 1