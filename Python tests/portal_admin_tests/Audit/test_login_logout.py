import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import LoginLogoutElements, Other, Elements
import driver_settings
import time
import datetime
from selenium.webdriver import ActionChains
import calendar
import os

CE = LoginLogoutElements
CElem = Elements
CO = Other

# Dev
# server_address = 'https://128.66.200.154:9613/edapt-admin'

# QA Server
# server_address = 'https://dev-msa-qa.botf03.net:9613/edapt-admin'

# QA Stag Server
server_address = 'https://dev-msa-qa-stag.botf03.net:9613/edapt-admin'


class LoginLogout01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_ll_url = server_address + '/page/loginlogoutstatistics.jsf'
        cls.driver.get(cls.test_ll_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(15)

    def tearDown(self):
        pass

    def test1_check_page(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_ll_url)
        wait = WebDriverWait(self.driver, 15)

        content_list = [CE.filter_header, CE.filter_content, CE.user_input, CE.application_label,
                        CE.start_date_input, CE.end_date_input, CE.apply_filter_button, CE.login_logout_table,
                        CE.paginator, CE.user_column, CE.device_column, CE.login_column, CE.logout_column,
                        CE.working_time_column, CE.application_column]
        # count_123 = 0
        for elem in content_list:
            # print('len(content_list)', len(content_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

    def test2_paginator(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_ll_url)
        wait = WebDriverWait(self.driver, 15)

        # Session Start for first session before
        login_css_column = r'tr.ui-widget-content:nth-child(1) > td:nth-child(3)'
        login_column_data = driver.find_element_by_css_selector(login_css_column).get_attribute('textContent')
        login_split_column_data = login_column_data.split()
        login_split_column_time = login_split_column_data[1].split(':')
        print('login_split_column_time', login_split_column_time)

        driver.find_elements_by_class_name(CE.date_picker_trigger)[1].click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        login_list = []
        # Session Start for first session first page
        login_column_data_first = driver.find_element_by_css_selector(login_css_column).get_attribute('textContent')
        print('start_column_data_first', login_column_data_first)
        login_list.append(login_column_data_first)

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
            login_column_data_n = driver.find_element_by_css_selector(login_css_column).get_attribute('textContent')
            print('login_column_data in', count_page, 'page', login_column_data_n)
            login_list.append(login_column_data_n)
            count_page += 1

        print('login_list', login_list)
        if login_list[0] != login_list[5]:
            print('login_list[0]', login_list[0], 'login_list[5]', login_list[5])
            raise Exception('Wrong item')
        count_check = 0
        while count_check <= 4:
            print('login_list[' + str(count_check) + ']', login_list[count_check],
                  'login_list[' + str(count_check + 1) + ']', login_list[count_check + 1])
            if login_list[count_check] == login_list[count_check + 1]:
                raise Exception('Wrong item')
            count_check += 1

    def test3_check_user_filter(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_ll_url)
        wait = WebDriverWait(self.driver, 15)

        # User column. We count the number of users other than exadel1
        count_rows = 1
        count_pages = 1
        not_exadel1_user = 0
        driver.implicitly_wait(2)
        while count_pages < 3:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(1)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                # print('count_rows', count_rows)
                if find_row[0].get_attribute('textContent') != 'exadel1':
                    not_exadel1_user += 1
                count_rows += 1
            else:
                # print('count_rows:', count_rows, 'not found')
                next_button = driver.find_element_by_class_name(CE.paginator_next_button)
                if 'ui-state-disabled' not in next_button.get_attribute(name='class'):
                    # print('ui-state-disabled not in')
                    next_button.click()
                    Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
                    count_rows = 1
                    count_pages += 1
                else:
                    break
        driver.implicitly_wait(15)

        print('not_exadel1_user:', not_exadel1_user)
        if not_exadel1_user == 0:
            raise Exception('All users - exadel1')

        # User filter
        driver.find_element_by_id(CE.user_input).send_keys('exadel1')

        # Apply
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        # User column. We count the number of users other than exadel1
        count_rows = 1
        count_pages = 1
        not_exadel1_user = 0
        driver.implicitly_wait(2)
        while count_pages < 3:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(1)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                # print('count_rows', count_rows)
                if find_row[0].get_attribute('textContent') != 'exadel1':
                    not_exadel1_user += 1
                count_rows += 1
            else:
                # print('count_rows:', count_rows, 'not found')
                next_button = driver.find_element_by_class_name(CE.paginator_next_button)
                if 'ui-state-disabled' not in next_button.get_attribute(name='class'):
                    # print('ui-state-disabled not in')
                    next_button.click()
                    Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
                    count_rows = 1
                    count_pages += 1
                else:
                    break
        driver.implicitly_wait(15)

        print('not_exadel1_user:', not_exadel1_user)
        if not_exadel1_user != 0:
            raise Exception('Not all users - exadel1')

    def test4_check_application_filter(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_ll_url)
        wait = WebDriverWait(self.driver, 15)

        # Application column. We count the number of application other than edge
        count_rows = 1
        count_pages = 1
        not_edge_app = 0
        driver.implicitly_wait(2)
        while count_pages < 3:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                # print('count_rows', count_rows)
                # print(find_row[0].get_attribute('textContent'))
                if find_row[0].get_attribute('textContent') != 'edge':
                    not_edge_app += 1
                count_rows += 1
            else:
                # print('count_rows:', count_rows, 'not found')
                next_button = driver.find_element_by_class_name(CE.paginator_next_button)
                if 'ui-state-disabled' not in next_button.get_attribute(name='class'):
                    # print('ui-state-disabled not in')
                    next_button.click()
                    Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
                    count_rows = 1
                    count_pages += 1
                else:
                    break
        driver.implicitly_wait(15)

        print('not_edge_app:', not_edge_app)

        # Application list
        application_list = []
        driver.find_element_by_id(CE.application_label).click()
        driver.find_element_by_id(CE.application_items)
        app_count = 0
        driver.implicitly_wait(2)
        while app_count <= 10:
            items = driver.find_elements_by_id(CE.application_string + str(app_count + 1))
            if items:
                print("Add", items[0].get_attribute('textContent'), 'item in list')
                application_list.append(items[0].get_attribute('textContent'))
            else:
                break
            app_count += 1
        driver.implicitly_wait(15)
        driver.find_element_by_id(CE.application_label).click()

        print('application_list', application_list)

        # Check Applications
        application_list_used = 1
        while application_list_used <= len(application_list):
            # Application filter select
            print('application_list_used', application_list_used)
            driver.find_element_by_id(CE.application_label).click()
            time.sleep(2)
            driver.find_element_by_id(CE.application_string + str(application_list_used)).click()

            # Apply
            driver.find_element_by_id(CE.apply_filter_button).click()
            Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
            time.sleep(2)

            # Check Application column
            count_rows = 1
            count_pages = 1
            new_app_cell = 0
            driver.implicitly_wait(2)
            while count_pages < 3:
                css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
                find_row = driver.find_elements_by_css_selector(css_selector)
                if find_row:
                    print('count_rows', count_rows)
                    # print('find_row[0]', find_row[0].get_attribute('textContent'),
                    #       'application_list[application_list_used]', application_list[application_list_used - 1])
                    if find_row[0].get_attribute('textContent') == application_list[application_list_used - 1]:
                        new_app_cell += 1
                    else:
                        raise Exception('Wrong application')
                    count_rows += 1
                else:
                    print('count_rows:', count_rows, 'not found')
                    next_button = driver.find_element_by_class_name(CE.paginator_next_button)
                    if 'ui-state-disabled' not in next_button.get_attribute(name='class'):
                        print('ui-state-disabled not in')
                        next_button.click()
                        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
                        count_rows = 1
                        count_pages += 1
                    else:
                        break
            driver.implicitly_wait(15)
            if new_app_cell == 0:
                empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
                if CO.no_records_found not in empty_message:
                    raise Exception('"No records found." message is missing')
                else:
                    print('"No records found." message found')
            application_list_used += 1

    def test5_start_time_calendar(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_ll_url)
        wait = WebDriverWait(self.driver, 15)

        # Paginator
        driver.find_element_by_class_name(CE.paginator_last_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Count strings
        count_rows = 1
        while count_rows < 51:
            row = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(1)'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                # print('count_rows', count_rows)
                count_rows += 1
            else:
                # print('row:', row, 'not found')
                break

        # Login for last session
        css_last_string = 'tr.ui-widget-content:nth-child(' + str(count_rows - 1) + ') > td:nth-child(3)'
        lstring_time = driver.find_element_by_css_selector(css_last_string).get_attribute('textContent')

        # Start datepicker
        driver.find_elements_by_class_name(CE.date_picker_trigger)[0].click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        print('now_month_decimal', now_month_decimal)

        standard_yesterday = now - datetime.timedelta(days=30)
        yesterday = now - datetime.timedelta(days=2)
        yesterday_day = yesterday.strftime('%d')
        standard_yesterday_month_decimal = standard_yesterday.strftime('%m')
        yesterday_month_decimal = yesterday.strftime('%m')
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year
        print('standard_yesterday_month_decimal', standard_yesterday_month_decimal)
        print('yesterday_month_decimal', yesterday_month_decimal)
        if standard_yesterday_month_decimal != yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_next).click()
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
        print('yesterday_day', yesterday_day)
        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)

        start_date_input = driver.find_element_by_id(CE.start_date_input).get_attribute(name='value')
        start_date_input_split = start_date_input.split()
        print('start_date_input_split[0]', start_date_input_split[0])
        print('start_time_set_yesterday', start_time_set_yesterday)
        if start_date_input_split[0] != start_time_set_yesterday:
            print('start_date_input_split[0]', start_date_input_split[0])
            raise Exception('Input contain wrong data')

        # Apply
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        # Paginator
        driver.find_element_by_class_name(CE.paginator_last_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Count strings

        count_rows = 1
        while count_rows < 51:
            row = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(1)'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                # print('count_rows', count_rows)
                count_rows += 1
            else:
                print('row:', row, 'not found')
                break

        # Login for last session
        css_last_string = 'tr.ui-widget-content:nth-child(' + str(count_rows - 1) + ') > td:nth-child(3)'
        lstring_time_2 = driver.find_element_by_css_selector(css_last_string).get_attribute('textContent')
        print('lstring_time_2', lstring_time_2)
        print('lstring_time', lstring_time)

        if lstring_time == lstring_time_2:
            raise Exception('Wrong item displayed')

        lstring_time_2_split = lstring_time_2.split()
        lstring_time_2_date = lstring_time_2_split[0].split('.')
        if lstring_time_2_date[0] != yesterday.strftime('%d'):
            raise Exception('Wrong day')
        if lstring_time_2_date[1] != yesterday_month_decimal:
            raise Exception("Wrong month")
        if lstring_time_2_date[2] != yesterday_year:
            raise Exception("Wrong year")

    def test6_end_time_calendar(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_ll_url)
        wait = WebDriverWait(self.driver, 15)

        # Login for first session
        css_first_string = 'tr.ui-widget-content:nth-child(1) > td:nth-child(3)'
        fstring_time = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')

        # Date picker
        driver.find_elements_by_class_name(CE.date_picker_trigger)[1].click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)
        actionChains = ActionChains(driver)
        css_hour_slider = '.ui_tpicker_hour_slider > span:nth-child(1)'
        css_minute_slider = '.ui_tpicker_minute_slider > span:nth-child(1)'
        source = driver.find_element_by_css_selector(css_hour_slider)
        source_2 = driver.find_element_by_css_selector(css_minute_slider)
        date_picker_title = driver.find_element_by_class_name(CE.date_picker_title)

        actionChains.click(date_picker_title).drag_and_drop_by_offset(source, 113, 0). \
            drag_and_drop_by_offset(source_2, 113,  0).perform()
        time.sleep(1)

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        print('now_month_decimal', now_month_decimal)

        yesterday = now - datetime.timedelta(days=1)
        yesterday_day = yesterday.strftime('%d')
        yesterday_month_decimal = yesterday.strftime('%m')
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year

        if now_month_decimal != yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_prev).click()
        print('yesterday_day', yesterday_day)
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]

        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)

        end_date_input = driver.find_element_by_id(CE.end_date_input).get_attribute(name='value')
        end_date_input_split = end_date_input.split()

        print('end_date_input_split[0]', end_date_input_split[0])
        print('start_time_set_yesterday', start_time_set_yesterday)
        if end_date_input_split[0] != start_time_set_yesterday:
            print('end_date_input_split[0]', end_date_input_split[0])
            raise Exception('Input contain wrong data')

        # Apply
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        # Login for first session
        fstring_time_2 = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')
        print('fstring_time_2', fstring_time_2)
        print('fstring_time', fstring_time)

        if fstring_time == fstring_time_2:
            raise Exception('Wrong item displayed')

        # fstring_time_2_split = fstring_time_2.split()
        # fstring_time_2_date = fstring_time_2_split[0].split('.')
        # if fstring_time_2_date[0] != yesterday.strftime('%d'):
        #     raise Exception('Wrong day')
        # if fstring_time_2_date[1] != yesterday_month_decimal:
        #     raise Exception("Wrong month")
        # if fstring_time_2_date[2] != yesterday_year:
        #     raise Exception("Wrong year")

    def test7_end_time_sliders(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_ll_url)
        wait = WebDriverWait(self.driver, 15)

        # end date
        end_date_input = driver.find_element_by_id(CE.end_date_input).get_attribute(name="value")
        end_date_input_split = end_date_input.split('/')

        # Login for first session
        css_first_string = 'tr.ui-widget-content:nth-child(1) > td:nth-child(3)'
        fstring_time = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')
        # fstring_time_strptime = time.mktime(datetime.datetime.strptime(fstring_time, "%m/%d/%Y %H:%M").timetuple())
        # print('fstring_time_strptime', fstring_time_strptime)
        split_fstring_time = fstring_time.split()
        split_time = split_fstring_time[1].split(':')
        split_date = split_fstring_time[0].split('.')
        print('split_time', split_time)
        print('split_date', split_date)

        # End datepicker
        driver.find_elements_by_class_name(CE.date_picker_trigger)[1].click()
        time.sleep(2)
        if split_date[0] != end_date_input_split[1]:
            picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, split_date[0])
            time.sleep(1)
            picker_day_to_select.click()
            time.sleep(1)
        driver.find_element_by_id(CE.date_picker)
        actionChains = ActionChains(driver)
        css_hour_slider = '.ui_tpicker_hour_slider > span:nth-child(1)'
        css_minute_slider = '.ui_tpicker_minute_slider > span:nth-child(1)'
        source = driver.find_element_by_css_selector(css_hour_slider)
        source_2 = driver.find_element_by_css_selector(css_minute_slider)
        date_picker_title = driver.find_element_by_class_name(CE.date_picker_title)
        if int(split_time[1]) - 1 < 0:
            split_time = [int(split_time[0]) - 1, 59]
            print('new split_time', split_time)

        offset_hour = int(split_time[0]) * 4.887391304347826
        offset_minutes = (int(split_time[1]) - 1) * 1.905254237288136
        actionChains.click(date_picker_title).drag_and_drop_by_offset(source, -113, 0).\
            drag_and_drop_by_offset(source, offset_hour,  0).\
            drag_and_drop_by_offset(source_2, -113,  0).\
            drag_and_drop_by_offset(source_2, offset_minutes,  0).perform()
        time.sleep(1)
        picker = 'ui_tpicker_time_input'
        val = driver.find_element_by_class_name(picker).get_attribute(name='value')
        print('hour:', int(split_time[0]), 'minutes:', (int(split_time[1])))
        print('offset_hour:', offset_hour, 'offset_minutes:', offset_minutes - 1, 'time value:', val)
        time.sleep(2)

        # Apply
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        # Login for first session
        fstring_time_2 = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')
        print('fstring_time_2', fstring_time_2)

        if fstring_time == fstring_time_2:
            raise Exception('Wrong item displayed')

    def test8_start_time_sliders(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_ll_url)
        wait = WebDriverWait(self.driver, 15)

        # start date
        start_date_input = driver.find_element_by_id(CE.start_date_input).get_attribute(name="value")
        start_date_input_split = start_date_input.split('/')

        # Paginator
        driver.find_element_by_class_name(CE.paginator_last_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Count strings
        count_rows = 1
        while count_rows < 51:
            row = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(1)'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                # print('count_rows', count_rows)
                count_rows += 1
            else:
                # print('row:', row, 'not found')
                break

        # Login for last session
        css_last_string = 'tr.ui-widget-content:nth-child(' + str(count_rows - 1) + ') > td:nth-child(3)'
        lstring_time = driver.find_element_by_css_selector(css_last_string).get_attribute('textContent')
        split_lstring_time = lstring_time.split()
        split_time = split_lstring_time[1].split(':')
        split_date = split_lstring_time[0].split('.')
        print('split_time', split_time)
        print('split_date', split_date)

        # Start datepicker
        driver.find_elements_by_class_name(CE.date_picker_trigger)[0].click()
        time.sleep(2)
        if split_date[0] != start_date_input_split[1]:
            picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, split_date[0])
            time.sleep(1)
            picker_day_to_select.click()
            time.sleep(1)
        driver.find_element_by_id(CE.date_picker)
        actionChains = ActionChains(driver)
        css_hour_slider = '.ui_tpicker_hour_slider > span:nth-child(1)'
        css_minute_slider = '.ui_tpicker_minute_slider > span:nth-child(1)'
        source = driver.find_element_by_css_selector(css_hour_slider)
        source_2 = driver.find_element_by_css_selector(css_minute_slider)
        date_picker_title = driver.find_element_by_class_name(CE.date_picker_title)
        if int(split_time[1]) - 1 < 0:
            split_time = [int(split_time[0]) - 1, 59]
            print('new split_time', split_time)

        offset_hour = int(split_time[0]) * 4.887391304347826
        offset_minutes = (int(split_time[1]) + 1) * 1.905254237288136
        actionChains.click(date_picker_title).drag_and_drop_by_offset(source, -113, 0).\
            drag_and_drop_by_offset(source, offset_hour,  0).\
            drag_and_drop_by_offset(source_2, -113,  0).\
            drag_and_drop_by_offset(source_2, offset_minutes,  0).perform()
        time.sleep(1)
        picker = 'ui_tpicker_time_input'
        val = driver.find_element_by_class_name(picker).get_attribute(name='value')
        print('hour:', int(split_time[0]), 'minutes:', (int(split_time[1])))
        print('offset_hour:', offset_hour, 'offset_minutes:', offset_minutes + 1, 'time value:', val)
        time.sleep(2)
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        # Paginator
        driver.find_element_by_class_name(CE.paginator_last_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Count strings
        count_rows = 1
        while count_rows < 51:
            row = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(1)'
            find_row = driver.find_elements_by_css_selector(row)
            if find_row:
                # print('count_rows', count_rows)
                count_rows += 1
            else:
                # print('row:', row, 'not found')
                break

        # Login for last session
        css_last_string = 'tr.ui-widget-content:nth-child(' + str(count_rows - 1) + ') > td:nth-child(3)'
        lstring_time_2 = driver.find_element_by_css_selector(css_last_string).get_attribute('textContent')
        print('lstring_time_2', lstring_time_2)
        print('lstring_time', lstring_time)

        if lstring_time == lstring_time_2:
            raise Exception('Wrong item displayed')

