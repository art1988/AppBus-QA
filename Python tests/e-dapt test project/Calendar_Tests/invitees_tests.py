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
class Test5Invitees(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

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
                print('Check - Week View is selected')
            else:
                raise Exception('Week view is not selectable')

        # mgd.find_element_by_id(cal.spinner).click()
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
        # Check.find_element_by_class_name_and_text(cal.contact_name, 'AAAppolo').click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.block_wrapper)))
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Close').click()
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
        if not Check.find_element_by_class_name_and_text(cal.invitees_count, '2'):
            raise Exception('Wrong number of contacts')
        note = now_time + ' auto-test for invitees'
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_id(cal.notes_input)
        actions.move_to_element(element).click().perform()
        element.send_keys(note)
        mgd.find_element_by_id(cal.yes_edit_button).click()
        time.sleep(1)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        if not Check.find_element_by_class_name_and_text(cal.invitees_count, '2'):
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
        if not Check.find_element_by_class_name_and_text(cal.invitees_count, '1'):
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


@unittest.skip('NOT OK')
class Test5Invitees2(unittest.TestCase):
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

        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

        event_name = 'TestInvitees_rep+ex'
        location_name = 'Canyon_'
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

        id_elem = Check.event_in_specific_cells(event_name, 2, cell)
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        mgd.find_element_by_id(cal.location_input).send_keys(location_name + '1')
        mgd.find_element_by_id(cal.yes_edit_button).click()
        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Single').click()
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

        event_name = 'TestInvitees_rep+ex'
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

    def test1_invitees(self):
        current_time = datetime.now()
        now_time = current_time.strftime("%H:%M")
        event_name = 'TestInvitees_rep+ex'

        cell_list = Check.find_cell_week_number(now_time)
        cell = str(cell_list[0] + 1) + '-' + str(cell_list[1])
        id_elem = 'grid-week-cell-' + cell + ''
        mgd.find_element_by_id(id_elem).click()
        mgd.find_element_by_id(cal.edit_prvw).click()
        Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        mgd.find_element_by_class_name(cal.plus_icon).click()
        mgd.find_element_by_class_name(cal.contact_items)
        print('Check - invitees items')
        search_input = 'exadel2'
        search_input_2 = 'contact for'
        mgd.find_element_by_class_name(cal.contact_search).send_keys(search_input)
        time.sleep(1)
        xpath = '//*[@id="contactList"]/li/a/div'
        xpath2 = '//*[@id="contactList"]/li[2]/a/div'
        xpath3 = '//*[@id="contactList"]/li[3]/a/div'
        elem = mgd.find_element_by_xpath(xpath)
        elem.click()
        mgd.find_element_by_class_name(cal.clear_search).click()
        mgd.find_element_by_class_name(cal.contact_search).send_keys(search_input_2)
        time.sleep(1)
        mgd.find_element_by_xpath(xpath).click()
        # mgd.find_element_by_xpath(xpath2).click()
        # mgd.find_element_by_xpath(xpath3).click()
        mgd.find_element_by_id(cal.yes_edit_button).click()
        Check.find_element_by_class_name_and_text(cal.email_invitees, 'exadel2@botf03.net')
        len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        print('len_of_list', len_of_list)
        if len_of_list != 2:
            raise Exception('Not all contacts added')
        garbage1 = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/i'
        garbage2 = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/i'
        garbage3 = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/i'
        garbage4 = '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[4]/div[2]/div/i'
        # email_in_1_row = mgd.find_element_by_xpath(
        #     '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[1]/div[1]/div').get_attribute(
        #     'innerText')
        # email_in_2_row = mgd.find_element_by_xpath(
        #     '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[2]/div[1]/div').get_attribute(
        #     'innerText')
        # email_in_3_row = mgd.find_element_by_xpath(
        #     '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[3]/div[1]/div').get_attribute(
        #     'innerText')
        # email_in_4_row = mgd.find_element_by_xpath(
        #     '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[4]/div[1]/div').get_attribute(
        #     'innerText')
        # mgd.find_element_by_xpath(garbage4).click()
        # mgd.find_element_by_xpath(garbage2).click()
        # time.sleep(1)
        # new_len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        # print('new_len_of_list', new_len_of_list)
        # if new_len_of_list != 2:
        #     raise Exception('Contacts not deleted')
        #
        # new_email_in_1_row = mgd.find_element_by_xpath(
        #     '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[1]/div[1]/div').get_attribute(
        #     'innerText')
        # new_email_in_2_row = mgd.find_element_by_xpath(
        #     '//*[@id="tooltip-container-undefined"]/div/div/div[2]/div[1]/div/div[2]/div[1]/div').get_attribute(
        #     'innerText')
        #
        # if new_email_in_1_row != email_in_1_row:
        #     raise Exception('First email incorrect')
        # if new_email_in_2_row != email_in_3_row:
        #     raise Exception('Second email incorrect')

        mgd.find_element_by_id(cal.yes_edit_button).click()
        if not Check.find_element_by_class_name_and_text(cal.invitees_count, '2'):
            raise Exception('Wrong number of contacts')
        note = now_time + ' auto-test for invitees'
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_id(cal.notes_input)
        actions.move_to_element(element).click().perform()
        element.send_keys(note)
        mgd.find_element_by_id(cal.yes_edit_button).click()

        message = 'Update single appointment or the whole sequence?'
        update_appointment = Check.find_element_by_class_name_and_text(cal.block_wrapper, message)
        if update_appointment:
            print('Check - Block wrapper')
        Check.find_element_by_class_name_and_text(cal.bw_button, 'Sequence').click()
        time.sleep(1)
        # time.sleep(1)
        # mgd.find_element_by_id(id_elem).click()
        # mgd.find_element_by_id(cal.edit_prvw).click()
        # if not Check.find_element_by_class_name_and_text(cal.invitees_count, '2'):
        #     raise Exception('Wrong number of contacts')
        # Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        # len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        # print('len_of_list', len_of_list)
        # if len_of_list != 2:
        #     raise Exception('Wrong number of contacts in the list')
        # mgd.find_element_by_xpath(garbage1).click()
        # time.sleep(1)
        # new_len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        # print('new_len_of_list', new_len_of_list)
        # if new_len_of_list != 1:
        #     raise Exception('Contacts not deleted')
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # mgd.find_element_by_id(cal.yes_edit_button).click()
        # time.sleep(1)
        # mgd.find_element_by_id(id_elem).click()
        # mgd.find_element_by_id(cal.edit_prvw).click()
        # if not Check.find_element_by_class_name_and_text(cal.invitees_count, '1'):
        #     raise Exception('Wrong number of contacts')
        # Check.find_element_by_class_name_and_text(cal.title_class, 'Invitees').click()
        # len_of_list = len(mgd.find_elements_by_class_name(cal.email_invitees))
        # print('len_of_list', len_of_list)
        # if len_of_list != 1:
        #     raise Exception('Wrong number of contacts in the list')
        # mgd.find_element_by_id(cal.close_edit_button).click()
        # mgd.find_element_by_id(cal.delete_event_edit_button).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Cancel').click()
        # print(Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?'))
        # driver_instance.implicitly_wait(1)
        # if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
        #     print('Check - Cancel button')
        # else:
        #     raise Exception('Block wrapper exist')
        # mgd.find_element_by_id(cal.delete_event_edit_button).click()
        # Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?')
        # print('Check - Block wrapper')
        # Check.find_element_by_class_name_and_text(cal.bw_button, 'Delete').click()
        # if Check.find_element_by_class_name_and_text(cal.block_wrapper, 'Delete this event?') is None:
        #     print('Check - Delete button')
        # else:
        #     raise Exception('Block wrapper exist')
