import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import UserDetailsElements, Other, Elements
import driver_settings
import time
import datetime
from selenium.webdriver import ActionChains
import calendar
import os

CE = UserDetailsElements
CElem = Elements
CO = Other

# DEV Server
server_address = 'https://128.66.200.154:9613/edapt-admin'


class UserDetails01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_ud_url = server_address + '/page/useractivestatistic.jsf'
        cls.driver.get(cls.test_ud_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login_to_dev(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        pass

    def test1_check_page(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        list_of_elem = [CE.filter_form, CE.filter_toggler, CE.filter_header, CE.user_dropdown,
                        CE.start_date, CE.end_date, CE.apply_button, CE.user_session_statistic_table]
        elem_count = 0
        while elem_count <= len(list_of_elem) - 1:
            print('elem:', list_of_elem[elem_count], 'Check')
            driver.find_element_by_id(list_of_elem[elem_count])
            elem_count += 1

    def test2_no_records(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        driver.find_element_by_name(CE.user_input).send_keys('testuser985')
        time.sleep(1)
        driver.find_element_by_id(CE.apply_button).click()
        # wait.until(EC.invisibility_of_element_located((By.ID, CElem.loading_bar)))

        title = driver.find_elements_by_class_name(
            CElem.main_notification_title)
        message = driver.find_elements_by_class_name(
            CElem.main_notification_message)
        if title:
            print('title', title[0].get_attribute('textContent'))
        if message:
            print('message', message[0].get_attribute('textContent'))

        notification_message = driver.find_element_by_class_name(
            CElem.main_notification_title).get_attribute('textContent')
        if notification_message != CO.user_details_no_records:
            raise Exception('Wrong notification message')

    def test3_user_filter_and_rows_in_table(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        driver.find_element_by_name(CE.user_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        driver.find_element_by_id(CE.statistic_table_head)
        driver.find_element_by_id(CE.statistic_table_data)
        table_data = driver.find_element_by_id(CE.statistic_table_data).get_attribute('textContent')
        if 'No records found.' in table_data:
            raise Exception('"No records found." in the table')

        # Check Start - End
        start_input = driver.find_element_by_id(CE.start_date).get_attribute(name='value')
        end_input = driver.find_element_by_id(CE.end_date).get_attribute(name='value')
        clock_start_time = '00:00'
        clock_end_time = '23:59'
        split_start_input = start_input.split()
        split_end_input = end_input.split()
        if split_end_input[0] != split_start_input[0]:
            raise Exception('Wrong date. Start:', split_start_input[0], 'End:', split_end_input[0])

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        now_day = now.strftime('%d')

        start_time_today = now_month_decimal + '/' + now_day + '/' + now_year + ' ' + clock_start_time
        if start_time_today != start_input:
            raise Exception('Wrong Start time')

        end_time_today = now_month_decimal + '/' + now_day + '/' + now_year + ' ' + clock_end_time
        if end_time_today != end_input:
            raise Exception('Wrong End time')

        # Check rows
        count_rows = 1
        row_list = []
        while count_rows <= 50:
            row = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows) + ')'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                row_list.append(find_row)
                count_rows += 1
            else:
                print('row:', row, 'else')
                break
        print('count_rows', count_rows)
        print('row_list', len(row_list))

        # Check data in columns
        count_check = 1
        while count_check <= len(row_list):
            date_column_numbers = [1, 4, 8, 10]
            row_number = count_check
            for elem in date_column_numbers:
                css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + \
                             str(row_number) + ') > td:nth-child(' + str(elem) + ')'
                column_data = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
                if column_data:
                    split_column_data = column_data.split()
                    if split_column_data[0] != split_start_input[0]:
                        raise Exception('Wrong data in column', 'split_column_data:', split_column_data[0])
                    print('column', elem, 'in', count_check, 'row is checked')
                else:
                    print('empty column', elem, 'in', count_check, 'row')

            ok_mark_column_numbers = [2, 3]
            for elem in ok_mark_column_numbers:
                css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + \
                             str(row_number) + ') > td:nth-child(' + str(elem) + ')'
                column_data = driver.find_element_by_css_selector(css_column).get_attribute('innerHTML')
                if column_data:
                    if '/edapt-admin/images/ok-mark-24.png' not in column_data:
                        css_column_9 = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + \
                                     str(row_number) + ') > td:nth-child(9)'
                        column_data_9 = driver.find_element_by_css_selector(css_column_9).get_attribute('innerHTML')
                        if "0:0:0" in column_data_9:
                            if '/edapt-admin/images/x-mark-24.png' not in column_data:
                                raise Exception('Wrong data in column', 'column_data:', column_data)
                    print('column', elem, 'in', count_check, 'row is checked')
                else:
                    print('empty column', elem, 'in', count_check, 'row')
                    # raise Exception('empty column', elem, 'in', count_check, 'row')
            activities_column_number = 5
            css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + \
                         str(row_number) + ') > td:nth-child(' + str(activities_column_number) + ')'
            column_data = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
            if column_data:
                print('column', activities_column_number, 'in', count_check, 'row is checked')
            else:
                raise Exception('empty column', activities_column_number, 'in', count_check, 'row')
            session_duration_number = 9
            css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + \
                         str(row_number) + ') > td:nth-child(' + str(session_duration_number) + ')'
            column_data = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
            split_column_data = column_data.split(':')
            if len(split_column_data) == 3:
                print('column', session_duration_number, 'in', count_check, 'row is checked')
            else:
                print('split_column_data', split_column_data, 'len(split_column_data)', len(split_column_data))
                raise Exception('Wrong data in ', session_duration_number, 'column in', count_check, 'row')
            if driver.find_elements_by_id('dataTableForm:dataTable:' + str(
                            count_check - 1) + ':navigationActionsButton'):
                print('column 11 in', count_check, 'row is checked')
            else:
                raise Exception('Missing Navigation Action Button in', count_check, 'row')
            rdp_column_numbers = [6, 7]
            row_number = count_check
            for elem in rdp_column_numbers:
                css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + \
                             str(row_number) + ') > td:nth-child(' + str(elem) + ')'
                column_data = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
                if column_data:
                    print('column', elem, 'in', count_check, 'row is checked')
                    raise Exception('Wrong data in column', 'split_column_data:', split_column_data[0])
                else:
                    print('empty column', elem, 'in', count_check, 'row')
            count_check += 1

    def test4_navigation_actions(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        now_day = now.strftime('%d')

        time_today = now_month_decimal + '/' + now_day + '/' + now_year + ' '

        driver.find_element_by_name(CE.user_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)
        driver.find_element_by_id(CE.statistic_table_head)
        driver.find_element_by_id(CE.statistic_table_data)

        # Select item
        data_value = 0
        row_number = 1
        while row_number <= 10:
            css_column = r'#dataTableForm\:dataTable_data > tr:nth-child(' + \
                         str(row_number) + ') > td:nth-child(5)'
            column_data = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
            if int(column_data) > 2:
                print(column_data)
                driver.find_element_by_id('dataTableForm:dataTable:' + str(
                    row_number - 1) + ':navigationActionsButton').click()
                data_value = int(column_data)
                break
            else:

                row_number += 1

        # Check content
        wait.until(EC.visibility_of_element_located((By.ID, CE.navigation_actions_head)))
        driver.find_element_by_id(CE.navigation_actions_head)
        driver.find_element_by_id(CE.navigation_actions_data)
        driver.find_element_by_id(CE.close_nav_actions_button)

        number = 1
        max_number = data_value
        while number <= max_number:
            selector = r'#dataTableForm\3a navigationTable_data > tr:nth-child(' + str(number) + ')'
            driver.find_element_by_css_selector(selector)
            selector_column_1 = r'#dataTableForm\3a navigationTable_data > tr:nth-child(' + \
                                str(number) + ') > td:nth-child(1)'
            selector_column_2 = r'#dataTableForm\3a navigationTable_data > tr:nth-child(' + \
                                str(number) + ') > td:nth-child(1)'
            column_1_row_n = driver.find_element_by_css_selector(selector_column_1).get_attribute('textContent')
            column_2_row_n = driver.find_element_by_css_selector(selector_column_2).get_attribute('textContent')
            if time_today not in column_1_row_n:
                print('column_1_row_n', column_1_row_n)
                raise Exception('column_1 in', number, 'row have wrong date')
            if not column_2_row_n:
                print('column_2_row_n', column_2_row_n)
                raise Exception('column_2 in', number, 'row is empty')
            number += 1
        time.sleep(1)
        driver.find_element_by_id(CE.close_nav_actions_button).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.navigation_actions_head)))

    def test5_start_time_sliders(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        driver.find_element_by_name(CE.user_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)
        driver.find_element_by_id(CE.statistic_table_head)
        driver.find_element_by_id(CE.statistic_table_data)

        # Session Start for first session
        css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(1) > td:nth-child(1)'
        column_data = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
        split_column_data = column_data.split()
        split_column_time = split_column_data[1].split(':')
        print('split_column_time', split_column_time)
        if int(split_column_time[1]) == 59:
            split_column_time = [int(split_column_time[0]) + 1, 0]
        print('split_column_time after if', split_column_time)

        driver.find_element_by_css_selector(CE.start_calendar_button).click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)
        actionChains = ActionChains(driver)
        css_hour_slider = '#ui-datepicker-div > div.ui-timepicker-div > dl > dd.ui_tpicker_hour > div > span'
        css_minute_slider = '#ui-datepicker-div > div.ui-timepicker-div > dl > dd.ui_tpicker_minute > div > span'
        source = driver.find_element_by_css_selector(css_hour_slider)
        source_2 = driver.find_element_by_css_selector(css_minute_slider)
        date_picker_month = driver.find_element_by_class_name(CE.date_picker_month)
        offset_hour = int(split_column_time[0]) * 4.887391304347826
        offset_minutes = (int(split_column_time[1]) + 1) * 1.905254237288136
        actionChains.click(date_picker_month).drag_and_drop_by_offset(source, offset_hour,  0).\
            drag_and_drop_by_offset(source_2, offset_minutes,  0).perform()
        time.sleep(1)
        # actionChains.drag_and_drop_by_offset(source_2, offset_minutes,  0).perform()
        picker = 'ui_tpicker_time_input'
        val = driver.find_element_by_class_name(picker).get_attribute(name='value')
        print('hour:', int(split_column_time[0]), 'minutes:', (int(split_column_time[1]) + 1))
        print('offset_hour:', offset_hour, 'offset_minutes:', offset_minutes, 'time value:', val)
        time.sleep(2)
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)
        column_data_2 = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
        print('column_data_2', column_data_2)
        if column_data == column_data_2:
            raise Exception('Wrong item displayed')

    def test6_end_time_sliders(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        driver.find_element_by_name(CE.user_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)
        driver.find_element_by_id(CE.statistic_table_head)
        driver.find_element_by_id(CE.statistic_table_data)

        # Check rows
        count_rows = 1
        row_list = []
        while count_rows <= 50:
            row = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows) + ')'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                row_list.append(find_row)
                count_rows += 1
            else:
                print('row:', row, 'else')
                break
        print('count_rows', count_rows)
        print('row_list', len(row_list))

        # Session Start for last session
        css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows - 1) + ') > td:nth-child(1)'
        column_data = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
        split_column_data = column_data.split()
        split_column_time = split_column_data[1].split(':')
        print('split_column_time', split_column_time)

        driver.find_element_by_css_selector(CE.end_calendar_button).click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)
        actionChains = ActionChains(driver)
        css_hour_slider = '#ui-datepicker-div > div.ui-timepicker-div > dl > dd.ui_tpicker_hour > div > span'
        css_minute_slider = '#ui-datepicker-div > div.ui-timepicker-div > dl > dd.ui_tpicker_minute > div > span'
        source = driver.find_element_by_css_selector(css_hour_slider)
        source_2 = driver.find_element_by_css_selector(css_minute_slider)
        date_picker_month = driver.find_element_by_class_name(CE.date_picker_month)
        offset_hour = int(split_column_time[0]) * 4.887391304347826
        offset_minutes = (int(split_column_time[1]) - 1) * 1.905254237288136
        default_offset = -112.41
        actionChains.click(date_picker_month).drag_and_drop_by_offset(source, default_offset,  0).\
            drag_and_drop_by_offset(source_2, default_offset,  0).drag_and_drop_by_offset(source, offset_hour,  0).\
            drag_and_drop_by_offset(source_2, offset_minutes,  0).perform()
        time.sleep(1)
        # actionChains.drag_and_drop_by_offset(source_2, offset_minutes,  0).perform()
        picker = 'ui_tpicker_time_input'
        val = driver.find_element_by_class_name(picker).get_attribute(name='value')
        print('hour:', int(split_column_time[0]), 'minutes:', (int(split_column_time[1]) + 1))
        print('offset_hour:', offset_hour, 'offset_minutes:', offset_minutes, 'time value:', val)
        time.sleep(2)
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        # Check rows
        count_rows = 1
        row_list = []
        while count_rows <= 50:
            row = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows) + ')'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                row_list.append(find_row)
                count_rows += 1
            else:
                print('row:', row, 'else')
                break
        print('count_rows', count_rows)
        print('row_list', len(row_list))

        # Session Start for last session
        css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows - 1) + ') > td:nth-child(1)'
        column_data_2 = driver.find_element_by_css_selector(css_column).get_attribute('textContent')
        print('column_data_2', column_data_2)
        if column_data == column_data_2:
            raise Exception('Wrong item displayed')

    def test7_start_time_calendar(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        driver.find_element_by_name(CE.user_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)
        driver.find_element_by_id(CE.statistic_table_head)
        driver.find_element_by_id(CE.statistic_table_data)

        # Session Start for first session
        start_css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(1) > td:nth-child(1)'
        start_column_data = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
        start_split_column_data = start_column_data.split()
        start_split_column_time = start_split_column_data[1].split(':')
        print('start_split_column_time', start_split_column_time)

        driver.find_element_by_css_selector(CE.start_calendar_button).click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        # if now_month_decimal[0] == '0':
        #     now_month_decimal = now_month_decimal[1]
        print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        # if now_day[0] == '0':
        #     now_day = now_day[1]
        #     print('now_day', now_day)

        yesterday = now - datetime.timedelta(days=1)
        yesterday_day = yesterday.strftime('%d')
        yesterday_month_decimal = yesterday.strftime('%m')
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year

        if now_month_decimal != yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_prev).click()
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)

        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()

        # Apply
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Session Start for first session
        start_column_data_2 = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
        print('start_column_data_2', start_column_data_2)
        if start_column_data == start_column_data_2:
            raise Exception('Same item displayed')
        split_start_column_data_2 = start_column_data_2.split()
        if split_start_column_data_2[0] != start_time_set_yesterday:
            raise Exception('Wrong item data')

    def test8_start_end_time_calendar(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        driver.find_element_by_name(CE.user_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)
        driver.find_element_by_id(CE.statistic_table_head)
        driver.find_element_by_id(CE.statistic_table_data)

        # Check rows
        count_rows = 1
        row_list = []
        while count_rows <= 50:
            row = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows) + ')'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                row_list.append(find_row)
                count_rows += 1
            else:
                print('row:', row, 'else')
                break
        print('count_rows', count_rows)
        print('row_list', len(row_list))

        # Session Start for last session
        end_css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows - 1) + ') > td:nth-child(1)'
        end_column_data = driver.find_element_by_css_selector(end_css_column).get_attribute('textContent')
        end_split_column_data = end_column_data.split()
        end_split_column_time = end_split_column_data[1].split(':')
        print('end_split_column_time', end_split_column_time)

        # Session Start for first session
        start_css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(1) > td:nth-child(1)'
        start_column_data = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
        start_split_column_data = start_column_data.split()
        start_split_column_time = start_split_column_data[1].split(':')
        print('start_split_column_time', start_split_column_time)

        # Start date calendar form
        driver.find_element_by_css_selector(CE.start_calendar_button).click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        # if now_month_decimal[0] == '0':
        #     now_month_decimal = now_month_decimal[1]
        print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')

        yesterday = now - datetime.timedelta(days=1)
        yesterday_day = yesterday.strftime('%d')
        yesterday_month_decimal = yesterday.strftime('%m')
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year

        if now_month_decimal != yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_prev).click()
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)

        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()

        # End date calendar form
        driver.find_element_by_css_selector(CE.end_calendar_button).click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        if now_month_decimal != yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_prev).click()
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)

        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()

        # Apply
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Session Start for first session
        start_column_data_2 = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
        print('start_column_data_2', start_column_data_2)
        if start_column_data == start_column_data_2:
            raise Exception('Same item displayed')
        split_start_column_data_2 = start_column_data_2.split()
        if split_start_column_data_2[0] != start_time_set_yesterday:
            raise Exception('Wrong item data')

        # Check rows
        count_rows = 1
        row_list = []
        while count_rows <= 50:
            row = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows) + ')'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                row_list.append(find_row)
                count_rows += 1
            else:
                print('row:', row, 'else')
                break
        print('count_rows', count_rows)
        print('row_list', len(row_list))
        if len(row_list) == 50:
            print('len(row_list) == 50')
            elem = Check.by_class_name_and_custom_attribute(driver,
                                                            CE.paginator_last_button, 'class', 'ui-state-disabled')
            if not elem:
                print('if not elem')
                driver.find_element_by_class_name(CE.paginator_last_button).click()
                Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
                # Check rows
                count_rows = 1
                row_list = []
                while count_rows <= 50:
                    row = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows) + ')'
                    find_row = driver.find_elements_by_css_selector(row)
                    if find_row:
                        row_list.append(find_row)
                        count_rows += 1
                    else:
                        print('row:', row, 'else')
                        break
                print('count_rows', count_rows)
                print('row_list', len(row_list))

        # Session Start for last session
        end_css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + \
                         str(count_rows - 1) + ') > td:nth-child(1)'
        end_column_data_2 = driver.find_element_by_css_selector(end_css_column).get_attribute('textContent')
        print('end_column_data_2', end_column_data_2)
        if end_column_data == end_column_data_2:
            raise Exception('Same item displayed')
        split_end_column_data_2 = end_column_data_2.split()
        if split_end_column_data_2[0] != start_time_set_yesterday:
            raise Exception('Wrong item data')

    def test9_paginator(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        time.sleep(2)
        driver.find_element_by_id(CE.statistic_table_head)
        driver.find_element_by_id(CE.statistic_table_data)

        # Session Start for first session before
        start_css_column = r'#dataTableForm\3a dataTable_data > tr:nth-child(1) > td:nth-child(1)'
        start_column_data = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
        start_split_column_data = start_column_data.split()
        start_split_column_time = start_split_column_data[1].split(':')
        print('start_split_column_time', start_split_column_time)

        driver.find_element_by_css_selector(CE.start_calendar_button).click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        # if now_month_decimal[0] == '0':
        #     now_month_decimal = now_month_decimal[1]
        print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        # if now_day[0] == '0':
        #     now_day = now_day[1]
        #     print('now_day', now_day)

        yesterday = now - datetime.timedelta(days=10)
        if yesterday.strftime('%w') == '6':
            print('week', yesterday.strftime('%w'))
            yesterday = now - datetime.timedelta(days=11)
        elif yesterday.strftime('%w') == '0':
            print('week', yesterday.strftime('%w'))
            yesterday = now - datetime.timedelta(days=9)
        yesterday_day = yesterday.strftime('%d')
        yesterday_month_decimal = yesterday.strftime('%m')
        print('yesterday_month_decimal', yesterday_month_decimal)
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year

        if now_month_decimal != yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_prev).click()
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)

        # time.sleep(1)
        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()

        # Apply
        driver.find_element_by_id(CE.apply_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        star_session_list = []
        # Session Start for first session first page
        start_column_data_first = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
        print('start_column_data_first', start_column_data_first)
        if start_column_data == start_column_data_first:
            raise Exception('Same item displayed')
        split_start_column_data_first = start_column_data_first.split()
        if split_start_column_data_first[0] != start_time_set_yesterday:
            print('split_start_column_data_first[0]', split_start_column_data_first[0], 'start_time_set_yesterday',
                  start_time_set_yesterday)
            raise Exception('Wrong item data')
        star_session_list.append(start_column_data_first)

        count_page = 1
        paginator_current = driver.find_element_by_class_name(CE.paginator_current).get_attribute('textContent')
        paginator_current = paginator_current[1:-1]
        print(paginator_current)
        split_paginator_current = paginator_current.split()
        page_active = Check.by_class_name_and_text(driver, CE.paginator_button, str(1))
        page_active_class = page_active.get_attribute(name='class')
        if 'ui-state-active' not in page_active_class:
            raise Exception('First page not active')

        while count_page < 6:
            if count_page == 1:
                elem_to_select = str(2)
                message = 'Second'
                Check.by_class_name_and_text(driver, CE.paginator_button, elem_to_select).click()
            elif count_page == 2:
                elem_to_select = '3'
                message = 'Third'
                driver.find_element_by_class_name(CE.paginator_next_button).click()
            elif count_page == 3:
                elem_to_select = str(split_paginator_current[2])
                message = 'Last'
                driver.find_element_by_class_name(CE.paginator_last_button).click()
            elif count_page == 4:
                elem_to_select = str(int(split_paginator_current[2]) - 1)
                message = 'Penultimate'
                driver.find_element_by_class_name(CE.paginator_prev_button).click()
            elif count_page == 5:
                elem_to_select = '1'
                message = 'First'
                driver.find_element_by_class_name(CE.paginator_first_button).click()
            else:
                raise Exception('Something wrong')
            Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
            page_active = Check.by_class_name_and_text(driver, CE.paginator_button, elem_to_select)
            page_active_class = page_active.get_attribute(name='class')
            if 'ui-state-active' not in page_active_class:
                raise Exception(message, 'page not active')

            # Session Start for first session n page
            start_column_data_n = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
            print('start_column_data in', count_page, 'page', start_column_data_n)
            star_session_list.append(start_column_data_n)
            count_page += 1

        print('star_session_list', star_session_list)
        if star_session_list[0] != star_session_list[5]:
            print('star_session_list[0]', star_session_list[0], 'star_session_list[5]', star_session_list[5])
            raise Exception('Wrong item')
        count_check = 0
        while count_check <= 4:
            print('star_session_list[' + str(count_check) + ']', star_session_list[count_check],
                  'star_session_list[' + str(count_check + 1) + ']', star_session_list[count_check + 1])
            if star_session_list[count_check] == star_session_list[count_check + 1]:
                raise Exception('Wrong item')
            count_check += 1


class UserDetails02Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_ud_url = server_address + '/page/useractivestatistic.jsf'
        cls.driver.get(cls.test_ud_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login_to_dev(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        pass

    def test1_paginator_50_results_per_page(self):
        driver = self.driver
        driver.get(self.test_ud_url)
        wait = WebDriverWait(self.driver, 15)

        time.sleep(2)
        driver.find_element_by_id(CE.statistic_table_head)
        driver.find_element_by_id(CE.statistic_table_data)

        driver.find_element_by_css_selector(CE.start_calendar_button).click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        print('now_month_decimal', now_month_decimal)

        yesterday = now - datetime.timedelta(days=2)
        yesterday_day = yesterday.strftime('%d')
        yesterday_month_decimal = yesterday.strftime('%m')
        print('yesterday_month_decimal', yesterday_month_decimal)
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year

        if now_month_decimal != yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_prev).click()
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)

        # time.sleep(1)
        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()

        # Apply
        driver.find_element_by_id(CE.apply_button).click()
        # wait.until(EC.invisibility_of_element_located((By.ID, CElem.loading_bar)))

        notification = driver.find_element_by_class_name(CElem.main_notification_title)
        message = notification.get_attribute('innerText')
        print('message', message)
        message_split = message.split()
        records_value = int(message_split[2])
        print('records_value', records_value)

        rpp_value = 50
        page_count = records_value // rpp_value
        print('page_count', page_count)
        remainder_count = records_value % rpp_value
        print('remainder_count', remainder_count)
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        # Check rows

        next_value = 0
        total_count = 0
        # row_list = []
        'tr.ui-datatable-even:nth-child(1)'
        'tr.ui-widget-content:nth-child(50)'

        while next_value < page_count:
            count_rows = 1
            while count_rows < rpp_value + 1:
                row = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows) + ')'
                find_row = driver.find_elements_by_css_selector(row)
                if find_row:
                    # print('count_rows', count_rows, 'page:', next_value + 1)
                    count_rows += 1
                    total_count += 1
                else:
                    # print('row:', row, 'not found, page:', next_value + 1)
                    if count_rows - 1 != rpp_value:
                        raise Exception('Wrong count_rows:', count_rows)

            next_button_class = driver.find_element_by_class_name(CE.paginator_next_button).get_attribute('textContent')
            if 'ui-state-disabled' in next_button_class:
                raise Exception("else: 'ui-state-disabled' in next_button_class")
            else:
                Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
                driver.find_element_by_class_name(CE.paginator_next_button).click()
                next_value += 1
                # print('total_count', total_count)

        next_button_class = driver.find_element_by_class_name(CE.paginator_next_button).get_attribute('textContent')
        if 'ui-state-disabled' in next_button_class:
            raise Exception("else: 'ui-state-disabled' in next_button_class")
        else:
            Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
            driver.find_element_by_class_name(CE.paginator_next_button).click()
            next_value += 1

        count_rows = 1
        while count_rows < remainder_count + 1:
            row = r'#dataTableForm\3a dataTable_data > tr:nth-child(' + str(count_rows) + ')'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                # print('count_rows', count_rows, 'page:', next_value + 1)
                count_rows += 1
                total_count += 1

            else:
                # print('row:', row, 'not found')
                if count_rows - 1 != remainder_count:
                    raise Exception('Wrong count_rows:', count_rows)
            # print('total_count', total_count)
        if total_count != records_value:
            time.sleep(20)
            raise Exception('Wrong number of records:', total_count, '!=', records_value)

