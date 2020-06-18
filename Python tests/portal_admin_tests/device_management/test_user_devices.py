import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import Elements, Other
import driver_settings
import time
import datetime
import calendar
import os

CE = Elements
CO = Other

# DEV Server
server_address = 'https://128.66.200.154:9613/edapt-admin'


class UserDevices01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_pc_url = server_address + '/page/userdevices.jsf'
        cls.driver.get(cls.test_pc_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login_to_dev(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        pass

    def test1_ud_check_tabs(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        wait = WebDriverWait(self.driver, 15)

        tab_1 = Check.by_class_name_and_text(driver, CE.ud_tabs_to_select, CO.find_devices_tab)
        if 'false' in tab_1.get_attribute(name='aria-selected'):
            raise Exception('Tab is not selected')

        tab_2 = Check.by_class_name_and_text(driver, CE.ud_tabs_to_select, CO.review_wipe_list_tab)
        if 'true' in tab_2.get_attribute(name='aria-selected'):
            raise Exception('Tab is not selected')

        tab_3 = Check.by_class_name_and_text(driver, CE.ud_tabs_to_select, CO.os_versions_tab)
        if 'true' in tab_3.get_attribute(name='aria-selected'):
            raise Exception('Tab is not selected')

        driver.find_element_by_id(CE.find_devices_content)

        # Tab 2 content
        tab_2.click()
        time.sleep(2)
        driver.find_element_by_id(CE.wipe_list_content)

        # Tab 3 content
        tab_3.click()
        time.sleep(2)
        driver.find_element_by_id(CE.os_version_content)

        # Tab 1 content
        tab_1.click()
        time.sleep(2)
        driver.find_element_by_id(CE.find_devices_content)
        driver.find_element_by_class_name(CE.user_dd_select)
        driver.find_element_by_name(CE.user_input)
        driver.find_element_by_id(CE.lookup_button)

    def test2_ud_find_devices_tab(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        wait = WebDriverWait(self.driver, 15)

        # Tab 1 drop down
        driver.find_element_by_name(CE.user_input).send_keys('exadel1')
        driver.find_element_by_id(CE.lookup_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        value = driver.find_element_by_css_selector(
            r'#form\3a tabs\3a dataTableForm > span').get_attribute('textContent')
        if "Found" not in value:
            raise Exception('value', value)
        value_split = value.split()
        driver.find_element_by_id(CE.fd_select_column)
        driver.find_element_by_id(CE.fd_device_id_column)
        driver.find_element_by_id(CE.fd_last_login_column)
        driver.find_element_by_id(CE.fd_last_status_column)
        driver.find_element_by_id(CE.fd_table)
        row_count = 0
        while row_count <= int(value_split[1]) + 1:
            rows = driver.find_elements_by_css_selector(Check.user_device_row(row_count + 1))
            if rows:
                print('Row', row_count + 1, 'exist')
            else:
                print('Founded', row_count, 'row_count')
                break
            row_count += 1
        if row_count != int(value_split[1]):
            raise Exception('Wrong number of rows')

        row_number = random.randint(1, int(value_split[1]))

        # Check checkboxes
        row = driver.find_element_by_css_selector(Check.user_device_row(row_number))
        row.get_attribute(name='class')
        if CE.row_highlight in row.get_attribute(name='class'):
            raise Exception('Row', row_number, 'is selected')
        if row.get_attribute(name=CE.row_aria_selected) != 'false':
            raise Exception('Row', row_number, 'is selected')

        # Select main checkbox
        driver.find_element_by_class_name(CE.check_box_main).click()

        row = driver.find_element_by_css_selector(Check.user_device_row(row_number))
        row.get_attribute(name='class')
        if CE.row_highlight not in row.get_attribute(name='class'):
            raise Exception('Row', row_number, 'is not selected')
        if row.get_attribute(name=CE.row_aria_selected) != 'true':
            raise Exception('Row', row_number, 'is not selected')

        # Deselect main checkbox
        driver.find_element_by_class_name(CE.check_box_main).click()

        row = driver.find_element_by_css_selector(Check.user_device_row(row_number))
        row.get_attribute(name='class')
        if CE.row_highlight in row.get_attribute(name='class'):
            raise Exception('Row', row_number, 'is selected')
        if row.get_attribute(name=CE.row_aria_selected) != 'false':
            raise Exception('Row', row_number, 'is selected')

        device_id = r'#form\3a tabs\3a dataTable_data > tr:nth-child(1) > td:nth-child(2) > span'
        last_login = r'#form\3a tabs\3a dataTable_data > tr:nth-child(1) > td:nth-child(3)'
        status = r'#form\3a tabs\3a dataTable_data > tr:nth-child(1) > td:nth-child(4)'
        table_device_id = driver.find_element_by_css_selector(device_id).get_attribute('textContent')
        table_last_login = driver.find_element_by_css_selector(last_login).get_attribute('textContent')
        table_status = driver.find_element_by_css_selector(status).get_attribute('textContent')

        device_id_value = '35067437-8949-42f1-b0c3-2f8afc8161da'
        last_login_value = '2019-04-24T18:18:19.200'
        status_value = 'NOT_ACTIVE'

        if device_id_value not in table_device_id:
            raise Exception('Wrong field - device id:', table_device_id)
        if last_login_value not in table_last_login:
            raise Exception('Wrong field - last login:', table_last_login)
        if status_value not in table_status:
            raise Exception('Wrong field - status:', table_status)

        row_to_select = random.randint(1, int(value_split[1]))
        checkbox_in_row = r'#form\3a tabs\3a dataTable_data > tr:nth-child(' + \
                          str(row_to_select) + ') > td.ui-selection-column > div'

        # Select row
        checkbox_n = driver.find_element_by_css_selector(checkbox_in_row)
        checkbox_n.click()

        row = driver.find_element_by_css_selector(Check.user_device_row(row_to_select))
        row.get_attribute(name='class')
        if CE.row_highlight not in row.get_attribute(name='class'):
            raise Exception('Row', row_to_select, 'is not selected')
        if row.get_attribute(name=CE.row_aria_selected) != 'true':
            raise Exception('Row', row_to_select, 'is not selected')

        # Deselect row
        checkbox_n.click()
        row = driver.find_element_by_css_selector(Check.user_device_row(row_to_select))
        row.get_attribute(name='class')
        if CE.row_highlight in row.get_attribute(name='class'):
            raise Exception('Row', row_to_select, 'is selected')
        if row.get_attribute(name=CE.row_aria_selected) != 'false':
            raise Exception('Row', row_to_select, 'is selected')

        row_to_wipe = random.randint(1, int(value_split[1]))
        checkbox_in_row = r'#form\3a tabs\3a dataTable_data > tr:nth-child(' + \
                          str(row_to_wipe) + ') > td.ui-selection-column > div'

        # Select row
        checkbox_n = driver.find_element_by_css_selector(checkbox_in_row)
        checkbox_n.click()
        driver.find_element_by_id(CE.wipe_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

    def test3_ud_os_version_tab(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        wait = WebDriverWait(self.driver, 15)

        tab_3 = Check.by_class_name_and_text(driver, CE.ud_tabs_to_select, CO.os_versions_tab)
        tab_3.click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        driver.find_element_by_id(CE.os_version_content)
        list_of_elem = [CE.os_type_dd, CE.os_type_dd_list, CE.os_start_date, CE.os_ends_date, CE.os_apply_button,
                        CE.os_detailed_chart]
        elem_count = 0
        while elem_count <= len(list_of_elem) - 1:
            # print('elem:', list_of_elem[elem_count], 'Check')
            driver.find_element_by_id(list_of_elem[elem_count])
            elem_count += 1

        # IOS input
        dropdown_input = driver.find_element_by_id(CE.os_type_dd).get_attribute('textContent')
        if CO.ios_input not in dropdown_input:
            raise Exception('Wrong input:', dropdown_input, 'instead:', CO.ios_input)

        driver.find_element_by_id(CE.os_type_dd).click()
        first_select = driver.find_element_by_id(CE.os_dd_list_n_string + str(0))
        first_select.get_attribute(name='class')
        if CE.row_highlight not in first_select.get_attribute(name='class'):
            raise Exception('Item not selected')

        cart_panel = driver.find_element_by_css_selector(CE.cart_panel).get_attribute('outerHTML')

        if CO.ios_input.lower() not in cart_panel.lower():
            raise Exception(CO.ios_input.lower(), 'not contain in', cart_panel.lower())

        count = 0
        list_of_incorrect = [CO.windows_input, CO.android_input, CO.osx_input]
        while count <= 2:
            if list_of_incorrect[count].lower() in cart_panel.lower():
                raise Exception(list_of_incorrect[count].lower(), 'contain in', cart_panel.lower())
            count += 1

        # ANDROID input
        second_select = driver.find_element_by_id(CE.os_dd_list_n_string + str(1))
        second_select.click()
        driver.find_element_by_id(CE.os_apply_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        dropdown_input = driver.find_element_by_id(CE.os_type_dd).get_attribute('textContent')
        if CO.android_input not in dropdown_input:
            raise Exception('Wrong input:', dropdown_input, 'instead:', CO.android_input)

        driver.find_element_by_id(CE.os_type_dd).click()
        first_select = driver.find_element_by_id(CE.os_dd_list_n_string + str(1))
        first_select.get_attribute(name='class')
        if CE.row_highlight not in first_select.get_attribute(name='class'):
            raise Exception('Item not selected')

        cart_panel = driver.find_element_by_css_selector(CE.cart_panel).get_attribute('outerHTML')

        if CO.android_input.lower() not in cart_panel.lower():
            raise Exception(CO.android_input.lower(), 'not contain in', cart_panel.lower())

        count = 0
        list_of_incorrect = [CO.windows_input, CO.ios_input, CO.osx_input]
        while count <= 2:
            if list_of_incorrect[count].lower() in cart_panel.lower():
                raise Exception(list_of_incorrect[count].lower(), 'contain in', cart_panel.lower())
            count += 1

        # WINDOWS input
        second_select = driver.find_element_by_id(CE.os_dd_list_n_string + str(2))
        second_select.click()
        driver.find_element_by_id(CE.os_apply_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        dropdown_input = driver.find_element_by_id(CE.os_type_dd).get_attribute('textContent')
        if CO.windows_input not in dropdown_input:
            raise Exception('Wrong input:', dropdown_input, 'instead:', CO.windows_input)

        driver.find_element_by_id(CE.os_type_dd).click()
        first_select = driver.find_element_by_id(CE.os_dd_list_n_string + str(2))
        first_select.get_attribute(name='class')
        if CE.row_highlight not in first_select.get_attribute(name='class'):
            raise Exception('Item not selected')

        cart_panel = driver.find_element_by_css_selector(CE.cart_panel).get_attribute('outerHTML')

        if CO.windows_input.lower() not in cart_panel.lower():
            raise Exception(CO.windows_input.lower(), 'not contain in', cart_panel.lower())

        count = 0
        list_of_incorrect = [CO.android_input, CO.ios_input, CO.osx_input]
        while count <= 2:
            if list_of_incorrect[count].lower() in cart_panel.lower():
                raise Exception(list_of_incorrect[count].lower(), 'contain in', cart_panel.lower())
            count += 1

        # OSX input
        second_select = driver.find_element_by_id(CE.os_dd_list_n_string + str(3))
        second_select.click()
        driver.find_element_by_id(CE.os_apply_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        dropdown_input = driver.find_element_by_id(CE.os_type_dd).get_attribute('textContent')
        if CO.osx_input not in dropdown_input:
            raise Exception('Wrong input:', dropdown_input, 'instead:', CO.osx_input)

        driver.find_element_by_id(CE.os_type_dd).click()
        first_select = driver.find_element_by_id(CE.os_dd_list_n_string + str(3))
        first_select.get_attribute(name='class')
        if CE.row_highlight not in first_select.get_attribute(name='class'):
            raise Exception('Item not selected')

        cart_panel = driver.find_element_by_css_selector(CE.cart_panel).get_attribute('outerHTML')

        if CO.osx_input.lower() not in cart_panel.lower():
            raise Exception(CO.osx_input.lower(), 'not contain in', cart_panel.lower())

        count = 0
        list_of_incorrect = [CO.android_input, CO.ios_input, CO.windows_input]
        while count <= 2:
            if list_of_incorrect[count].lower() in cart_panel.lower():
                raise Exception(list_of_incorrect[count].lower(), 'contain in', cart_panel.lower())
            count += 1

    @unittest.skip('empty tab')
    def test4_ud_wipe_list_tab(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        wait = WebDriverWait(self.driver, 15)

        tab_2 = Check.by_class_name_and_text(driver, CE.ud_tabs_to_select, CO.review_wipe_list_tab)
        tab_2.click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        driver.find_element_by_id(CE.wipe_list_content)
        # list_of_elem = [CE.osv_filter_header, CE.osv_filter, CE.os_type_dd, CE.os_type_dd_list, CE.os_start_date,
        #                 CE.os_ends_date, CE.os_apply_button]
        # elem_count = 0
        # while elem_count <= len(list_of_elem) - 1:
        #     # print('elem:', list_of_elem[elem_count], 'Check')
        #     driver.find_element_by_id(list_of_elem[elem_count])
        #     elem_count += 1
