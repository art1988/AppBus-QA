import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import ContainerElements, Other, Elements
import driver_settings
import time
import datetime
from selenium.webdriver import ActionChains
import calendar
import os
import warnings

CE = ContainerElements
CElem = Elements
CO = Other

# Dev
# server_address = 'https://128.66.200.154:9613/edapt-admin'

# QA Server
# server_address = 'https://dev-msa-qa.botf03.net:9613/edapt-admin'

# QA Stag Server
server_address = 'https://dev-msa-qa-stag.botf03.net:9613/edapt-admin'


class Container01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_c_url = server_address + '/page/logs.jsf'
        cls.driver.get(cls.test_c_url)
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
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        content_list = [CE.filter_panel, CE.start_date, CE.end_date, CE.severity_label, CE.device_type_label,
                        CE.visible_columns_label, CE.user_filter, CE.reset_filter_button, CE.apply_filter_button,
                        CE.cont_log_table, CE.table_head, CE.start_date_column, CE.first_name_column,
                        CE.first_name_column_filter, CE.last_name_column, CE.last_name_column_filter, CE.user_column,
                        CE.user_column_filter, CE.session_column, CE.session_column_filter, CE.device_type_column,
                        CE.context_column, CE.context_column_filter, CE.message_column]
        # count_123 = 0
        for elem in content_list:
            # print('len(content_list)', len(content_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

    def test2_time_interval(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        now = datetime.datetime.now()
        # now_month = now.strftime('%B')
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        now_day = now.strftime('%d')
        clock_hours = now.strftime('%H')
        clock_minutes = now.strftime('%M')
        clock_time = clock_hours + ':' + clock_minutes

        yesterday = now - datetime.timedelta(days=1)
        yesterday_day = yesterday.strftime('%d')
        yesterday_month_decimal = yesterday.strftime('%m')
        # yesterday_month = yesterday.strftime('%B')
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        yesterday_last_day_of_month = calendar.monthrange(int(now_year), int(yesterday.strftime('%m')))
        print('yesterday_last_day_of_month[1]', yesterday_last_day_of_month[1])

        start_time_today = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year + ' ' + clock_time
        end_time_today = now_month_decimal + '/' + now_day + '/' + now_year + ' ' + clock_time

        start_date = driver.find_element_by_id(CE.start_date).get_attribute(name='value')
        print('start_date', start_date)
        end_date = driver.find_element_by_id(CE.end_date).get_attribute(name='value')
        print('end_date', end_date)

        if start_time_today != start_date:
            print('start_time_today', start_time_today, 'start_date', start_date)
            raise Exception('Wrong Start time')

        if end_time_today != end_date:
            print('end_time_today', end_time_today, 'end_date', end_date)
            raise Exception('Wrong End time')

        css_first_string = 'tr.ui-widget-content:nth-child(1) > td:nth-child(1)'
        fstring_time = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')
        fstring_time.split()

        fstring_time_strptime = time.mktime(datetime.datetime.strptime(fstring_time, "%m/%d/%Y %H:%M").timetuple())
        start_date_strptime = time.mktime(datetime.datetime.strptime(start_date, "%m/%d/%Y %H:%M").timetuple())
        end_date_strptime = time.mktime(datetime.datetime.strptime(end_date, "%m/%d/%Y %H:%M").timetuple())
        print('fstring_time_strptime', fstring_time_strptime)
        print('start_date_strptime', start_date_strptime)
        print('end_date_strptime', end_date_strptime)

        if fstring_time_strptime < start_date_strptime or fstring_time_strptime > end_date_strptime:
            raise Exception('Wrong date in table')

    def test3_paginator(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Session Start for first session before
        start_css_column = r'tr.ui-widget-content:nth-child(1) > td:nth-child(1)'
        start_column_data = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
        start_split_column_data = start_column_data.split()
        start_split_column_time = start_split_column_data[1].split(':')
        print('start_split_column_time', start_split_column_time)

        driver.find_elements_by_class_name(CE.date_picker_trigger)[1].click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        star_session_list = []
        # Session Start for first session first page
        start_column_data_first = driver.find_element_by_css_selector(start_css_column).get_attribute('textContent')
        print('start_column_data_first', start_column_data_first)
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
            print('count_page', count_page)
            if count_page == 1:
                elem_to_select = str(2)
                message = 'Second'
                Check.by_class_name_and_text(driver, CE.paginator_button, elem_to_select).click()
            elif count_page == 2:
                elem_to_select = str(3)
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

    def test4_end_time_sliders(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Session Start for first session
        css_first_string = 'tr.ui-widget-content:nth-child(1) > td:nth-child(1)'
        fstring_time = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')
        fstring_time_strptime = time.mktime(datetime.datetime.strptime(fstring_time, "%m/%d/%Y %H:%M").timetuple())
        print('fstring_time_strptime', fstring_time_strptime)
        split_fstring_time = fstring_time.split()
        split_time = split_fstring_time[1].split(':')
        print('split_time', split_time)

        # End datepicker
        driver.find_elements_by_class_name(CE.date_picker_trigger)[1].click()
        time.sleep(2)
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

        # Session Start for first session
        fstring_time_2 = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')
        print('fstring_time_2', fstring_time_2)

        if fstring_time == fstring_time_2:
            raise Exception('Wrong item displayed')

    def test5_start_time_sliders(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
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

        # Session Start for last session
        css_last_string = 'tr.ui-widget-content:nth-child(' + str(count_rows - 1) + ') > td:nth-child(1)'
        lstring_time = driver.find_element_by_css_selector(css_last_string).get_attribute('textContent')
        split_lstring_time = lstring_time.split()
        split_time = split_lstring_time[1].split(':')
        print('split_time', split_time)

        # Start datepicker
        driver.find_elements_by_class_name(CE.date_picker_trigger)[0].click()
        time.sleep(2)
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

        # Session Start for last session
        css_last_string = 'tr.ui-widget-content:nth-child(' + str(count_rows - 1) + ') > td:nth-child(1)'
        lstring_time_2 = driver.find_element_by_css_selector(css_last_string).get_attribute('textContent')
        print('lstring_time_2', lstring_time_2)
        print('lstring_time', lstring_time)

        if lstring_time == lstring_time_2:
            raise Exception('Wrong item displayed')

    def test6_start_time_calendar(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
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

        # Session Start for last session
        css_last_string = 'tr.ui-widget-content:nth-child(' + str(count_rows - 1) + ') > td:nth-child(1)'
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

        standard_yesterday = now - datetime.timedelta(days=1)
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
            driver.find_element_by_class_name(CE.date_picker_prev).click()
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
        print('yesterday_day', yesterday_day)
        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)

        time.sleep(10)

        start_date_input = driver.find_element_by_id(CE.start_date).get_attribute(name='value')
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
                # print('row:', row, 'not found')
                break

        # Session Start for last session
        css_last_string = 'tr.ui-widget-content:nth-child(' + str(count_rows - 1) + ') > td:nth-child(1)'
        lstring_time_2 = driver.find_element_by_css_selector(css_last_string).get_attribute('textContent')
        print('lstring_time_2', lstring_time_2)
        print('lstring_time', lstring_time)

        if lstring_time == lstring_time_2:
            raise Exception('Wrong item displayed')

    def test7_end_time_calendar(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Session Start for first session
        css_first_string = 'tr.ui-widget-content:nth-child(1) > td:nth-child(1)'
        fstring_time = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')

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

        end_date_input = driver.find_element_by_id(CE.end_date).get_attribute(name='value')
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

        # Session Start for first session
        fstring_time_2 = driver.find_element_by_css_selector(css_first_string).get_attribute('textContent')
        print('fstring_time_2', fstring_time_2)
        print('fstring_time', fstring_time)

        if fstring_time == fstring_time_2:
            raise Exception('Wrong item displayed')

    def test8_user(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # User column. We count the number of users other than exadel1
        count_rows = 1
        count_pages = 1
        not_exadel1_user = 0
        driver.implicitly_wait(2)
        while count_pages < 3:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(4)'
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
        driver.find_element_by_id(CE.user_filter).send_keys('exadel1')

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
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(4)'
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


class Container02Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_c_url = server_address + '/page/logs.jsf'
        cls.driver.get(cls.test_c_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(15)

    def tearDown(self):
        pass

    def test1_all_columns_visible(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Column list
        column_list = [CE.start_date_column, CE.first_name_column, CE.first_name_column_filter, CE.last_name_column,
                       CE.last_name_column_filter, CE.user_column, CE.user_column_filter, CE.session_column,
                       CE.session_column_filter, CE.device_type_column, CE.context_column, CE.context_column_filter,
                       CE.message_column]
        # count_123 = 0
        for elem in column_list:
            # print('len(column_list)', len(column_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

        # Select columns
        driver.find_element_by_id(CE.visible_columns_label).click()
        driver.find_element_by_id(CE.visible_columns_panel)

        default_checked_list = [1, 3, 4, 5, 8, 17, 20]
        checked_list = []
        string_number = 0
        number = 1
        while string_number <= 19:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            string_class = elem.get_attribute(name='class')
            string_name = elem.get_attribute('textContent')
            if CO.item_checked in string_class:
                checked_list.append(number)
            else:
                elem.click()
                Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
            string_number += 1
            number += 1

        if default_checked_list != checked_list:
            print('default_checked_list', default_checked_list)
            print('checked_list', checked_list)
            raise Exception('Lists not equals')

        # New column list
        column_list = [CE.start_date_column, CE.first_name_column, CE.first_name_column_filter, CE.last_name_column,
                       CE.last_name_column_filter, CE.user_column, CE.user_column_filter, CE.session_column,
                       CE.session_column_filter, CE.device_type_column, CE.context_column, CE.context_column_filter,
                       CE.message_column, CE.end_date_column, CE.device_column, CE.device_column_filter,
                       CE.domain_column, CE.severity_column, CE.component_column, CE.type_column, CE.tags_column,
                       CE.tags_column_filter, CE.os_type_column, CE.os_version_column, CE.os_version_column_filter,
                       CE.address_column, CE.address_column_filter, CE.device_ip_column, CE.device_ip_column_filter,
                       CE.latitude_column, CE.longitude_column]
        # count_123 = 0
        for elem in column_list:
            # print('len(column_list)', len(column_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

        string_number = 0
        number = 1
        while string_number <= 19:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            string_class = elem.get_attribute(name='class')
            if CO.item_unchecked in string_class:
                raise Exception('Found unchecked item')
            string_number += 1
            number += 1

    def test2_new_columns_visible(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Column list
        column_list = [CE.start_date_column, CE.first_name_column, CE.first_name_column_filter, CE.last_name_column,
                       CE.last_name_column_filter, CE.user_column, CE.user_column_filter, CE.session_column,
                       CE.session_column_filter, CE.device_type_column, CE.context_column, CE.context_column_filter,
                       CE.message_column]
        # count_123 = 0
        for elem in column_list:
            # print('len(column_list)', len(column_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
                # else:
                #     count_123 += 1
                # print(count_123)

        # Select columns
        driver.find_element_by_id(CE.visible_columns_label).click()
        driver.find_element_by_id(CE.visible_columns_panel)

        default_checked_list = [1, 3, 4, 5, 8, 17, 20]
        checked_list = []
        string_number = 0
        number = 1
        while string_number <= 19:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            string_class = elem.get_attribute(name='class')
            string_name = elem.get_attribute('textContent')
            if CO.item_checked in string_class:
                checked_list.append(number)
                elem.click()
                Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
            else:
                elem.click()
                Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
            string_number += 1
            number += 1

        if default_checked_list != checked_list:
            print('default_checked_list', default_checked_list)
            print('checked_list', checked_list)
            raise Exception('Lists not equals')

        # New column list
        column_list = [CE.message_column, CE.end_date_column, CE.device_column, CE.device_column_filter,
                       CE.domain_column, CE.severity_column, CE.component_column, CE.type_column, CE.tags_column,
                       CE.tags_column_filter, CE.os_type_column, CE.os_version_column, CE.os_version_column_filter,
                       CE.address_column, CE.address_column_filter, CE.device_ip_column, CE.device_ip_column_filter,
                       CE.latitude_column, CE.longitude_column]
        # count_123 = 0
        for elem in column_list:
            # print('len(column_list)', len(column_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
                # else:
                #     count_123 += 1
                # print(count_123)

        checked_list = []
        string_number = 0
        number = 1
        while string_number <= 19:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            string_class = elem.get_attribute(name='class')
            if CO.item_checked in string_class:
                checked_list.append(number)
            string_number += 1
            number += 1

        print('default_checked_list', default_checked_list)
        print('checked_list', checked_list)

        for item in checked_list:
            if item in default_checked_list:
                raise Exception('Found wrong checked item:', item)

    def test3_one_column_visible(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Column list
        column_list = [CE.start_date_column, CE.first_name_column, CE.first_name_column_filter, CE.last_name_column,
                       CE.last_name_column_filter, CE.user_column, CE.user_column_filter, CE.session_column,
                       CE.session_column_filter, CE.device_type_column, CE.context_column, CE.context_column_filter,
                       CE.message_column]
        # count_123 = 0
        for elem in column_list:
            # print('len(column_list)', len(column_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
                # else:
                #     count_123 += 1
                # print(count_123)

        # Select columns
        driver.find_element_by_id(CE.visible_columns_label).click()
        driver.find_element_by_id(CE.visible_columns_panel)

        default_checked_list = [1, 3, 4, 5, 8, 17, 20]
        checked_list = []
        string_number = 0
        number = 1
        while string_number <= 19:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            string_class = elem.get_attribute(name='class')
            if CO.item_checked in string_class:
                checked_list.append(number)
                elem.click()
                Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
            string_number += 1
            number += 1

        if default_checked_list != checked_list:
            print('default_checked_list', default_checked_list)
            print('checked_list', checked_list)
            raise Exception('Lists not equals')

        # New column list
        column_list = [CE.message_column]
        # count_123 = 0
        for elem in column_list:
            # print('len(column_list)', len(column_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
                # else:
                #     count_123 += 1
                # print(count_123)

        checked_list = []
        string_number = 0
        number = 1
        while string_number <= 19:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            string_class = elem.get_attribute(name='class')
            if CO.item_checked in string_class:
                checked_list.append(number)
            string_number += 1
            number += 1

        print('default_checked_list', default_checked_list)
        print('checked_list', checked_list)

        if len(checked_list) > 0:
            raise Exception('Some item checked')

    def test4_rnd_columns_visible(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Column list
        column_list = [CE.start_date_column, CE.first_name_column, CE.first_name_column_filter, CE.last_name_column,
                       CE.last_name_column_filter, CE.user_column, CE.user_column_filter, CE.session_column,
                       CE.session_column_filter, CE.device_type_column, CE.context_column, CE.context_column_filter,
                       CE.message_column]
        # count_123 = 0
        for elem in column_list:
            # print('len(column_list)', len(column_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

        # Select columns
        driver.find_element_by_id(CE.visible_columns_label).click()
        driver.find_element_by_id(CE.visible_columns_panel)

        default_checked_list = [1, 3, 4, 5, 8, 17, 20]
        checked_list = []

        for item in default_checked_list:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(item) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            elem.click()
            Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        for x in range(10):
            checked_list.append(x + 1)
        random.shuffle(checked_list)
        print(checked_list)
        print('checked_list[0: 3]', checked_list[0: 3])

        checked_list_name = []
        for item in checked_list[0: 3]:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(item) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            string_name = elem.get_attribute('textContent')
            checked_list_name.append(string_name)
            elem.click()
            Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Find column by name
        for elem in checked_list_name:
            if elem == 'Start date':
                elem = 'Start Date'
            elif elem == 'End date':
                elem = 'End Date'
            elif elem == 'Username':
                elem = 'User'
            elif elem == 'OS type':
                elem = 'OS Type'
            elif elem == 'OS version':
                elem = 'OS Version'
            elif elem == 'Device type':
                elem = 'Device Type'
            if not Check.by_class_name_and_text(driver, CE.column_title, elem):
                raise Exception(elem, 'not found')

        item_checked = 0
        string_number = 0
        number = 1
        while string_number <= 19:
            checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number) + ')'
            elem = driver.find_element_by_css_selector(checkbox_css)
            string_class = elem.get_attribute(name='class')
            if CO.item_checked in string_class:
                item_checked += 1
            string_number += 1
            number += 1

        if item_checked != 3:
            raise Exception('Wrong number of items', string_number)


class Container03Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_c_url = server_address + '/page/logs.jsf'
        cls.driver.get(cls.test_c_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(15)

    def tearDown(self):
        pass

    def test1_severity(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Select severity column
        driver.find_element_by_id(CE.visible_columns_label).click()
        driver.find_element_by_id(CE.visible_columns_panel)

        severity_checkbox_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(9)'
        severity_item = driver.find_element_by_css_selector(severity_checkbox_css)
        string_class = severity_item.get_attribute(name='class')
        string_name = severity_item.get_attribute('textContent')
        if string_name != 'Severity':
            raise Exception('Wrong string')
        severity_item.click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        driver.find_element_by_id(CE.visible_columns_label).click()

        # Check Severity column
        count_rows = 1
        count_pages = 1
        info_cell = 0
        warn_cell = 0
        error_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if find_row[0].get_attribute('textContent') == 'INFO':
                    info_cell += 1
                elif find_row[0].get_attribute('textContent') == 'WARN':
                    warn_cell += 1
                elif find_row[0].get_attribute('textContent') == 'ERROR':
                    error_cell += 1
                else:
                    raise Exception('Something wrong')
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
                    if info_cell == 0 and warn_cell == 0 \
                            or warn_cell == 0 and error_cell == 0 \
                            or info_cell == 0 and error_cell == 0:
                        warnings.warn('Only one type of severity found')
                    break
        driver.implicitly_wait(15)
        print('info_cell', info_cell)
        print('warn_cell', warn_cell)
        print('error_cell', error_cell)

        # Container logs pages
        pages = driver.find_element_by_class_name(CE.paginator_current).get_attribute('textContent')
        pages_split = pages.split()

        # Select severity dd
        driver.find_element_by_id(CE.severity_label).click()

        # Select INFO severity
        number_info = 1
        info_severity_css = '#form\:severity_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number_info) + ')'
        driver.find_element_by_css_selector(info_severity_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Container logs pages
        new_pages = driver.find_element_by_class_name(CE.paginator_current).get_attribute('textContent')
        new_pages_split = new_pages.split()

        if pages_split[2] == new_pages_split[2]:
            print('Page numbers not changes')

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_info_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if find_row[0].get_attribute('textContent') == 'INFO':
                    new_info_cell += 1
                else:
                    raise Exception('Something wrong')
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
        if new_info_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')

        # Select severity dd
        driver.find_element_by_id(CE.severity_label).click()

        # Select WARN severity
        number_info = 1
        number_warn = 2
        info_severity_css = '#form\:severity_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number_info) + ')'
        driver.find_element_by_css_selector(info_severity_css).click()
        warn_severity_css = '#form\:severity_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number_warn) + ')'
        driver.find_element_by_css_selector(warn_severity_css).click()

        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_warn_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if find_row[0].get_attribute('textContent') == 'WARN':
                    new_warn_cell += 1
                else:
                    raise Exception('Something wrong')
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
        if new_warn_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')

        # Select severity dd
        driver.find_element_by_id(CE.severity_label).click()

        # Select ERROR severity
        number_warn = 2
        number_error = 3
        warn_severity_css = '#form\:severity_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number_warn) + ')'
        driver.find_element_by_css_selector(warn_severity_css).click()
        error_severity_css = '#form\:severity_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(number_error) + ')'
        driver.find_element_by_css_selector(error_severity_css).click()

        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_error_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if find_row[0].get_attribute('textContent') == 'ERROR':
                    new_error_cell += 1
                else:
                    raise Exception('Something wrong')
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
        if new_error_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')

    def test2_device_type(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Check Device type column
        count_rows = 1
        count_pages = 1
        test_device_type_cell = 0
        win_cell = 0
        mac_cell = 1
        android_cell = 0
        ipad_cell = 0
        iphone_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if find_row[0].get_attribute('textContent') == 'test-device-type':
                    test_device_type_cell += 1
                elif find_row[0].get_attribute('textContent') == 'Windows PC':
                    win_cell += 1
                elif find_row[0].get_attribute('textContent') == 'Mac PC':
                    mac_cell += 1
                elif find_row[0].get_attribute('textContent') == 'ANDROID':
                    android_cell += 1
                elif find_row[0].get_attribute('textContent') == 'iPad':
                    ipad_cell += 1
                elif find_row[0].get_attribute('textContent') == 'iPhone':
                    iphone_cell += 1
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
                    if win_cell == 0 and mac_cell == 0 and ipad_cell == 0 and iphone_cell == 0 \
                            or mac_cell == 0 and android_cell == 0 and ipad_cell == 0 and iphone_cell == 0 \
                            or win_cell == 0 and android_cell == 0 and ipad_cell == 0 and iphone_cell == 0 \
                            or win_cell == 0 and mac_cell == 0 and android_cell == 0 and iphone_cell == 0 \
                            or win_cell == 0 and mac_cell == 0 and android_cell == 0 and ipad_cell == 0:
                        print('test_device_type_cell', test_device_type_cell)
                        print('win_cell', win_cell)
                        print('mac_cell', mac_cell)
                        print('android_cell', android_cell)
                        print('ipad_cell', ipad_cell)
                        print('iphone_cell', iphone_cell)
                        raise Exception('Only one type of device found')
                    break
        driver.implicitly_wait(15)
        print('test_device_type_cell', test_device_type_cell)
        print('win_cell', win_cell)
        print('mac_cell', mac_cell)
        print('android_cell', android_cell)
        print('ipad_cell', ipad_cell)
        print('iphone_cell', iphone_cell)

        # Select Device type dd
        driver.find_element_by_id(CE.device_type_label).click()

        # Select test-device-type
        select = 1
        select_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(
            select) + ')'
        driver.find_element_by_css_selector(select_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_test_device_type_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if not find_row[0].get_attribute('textContent') == 'test-device-type':
                    raise Exception('Wrong type')
                else:
                    new_test_device_type_cell += 1
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
        if new_test_device_type_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        driver.implicitly_wait(15)

        # Select Device type dd
        driver.find_element_by_id(CE.device_type_label).click()

        # Select Windows PC device type
        deselect = 1
        select = 2
        deselect_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(deselect) + ')'
        select_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(select) + ')'
        driver.find_element_by_css_selector(deselect_css).click()
        driver.find_element_by_css_selector(select_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_win_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if not find_row[0].get_attribute('textContent') == 'Windows PC':
                    raise Exception('Wrong type')
                else:
                    new_win_cell += 1
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
        if new_win_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        driver.implicitly_wait(15)

        # Select Device type dd
        driver.find_element_by_id(CE.device_type_label).click()

        # Select Mac PC device type
        deselect = 2
        select = 3
        deselect_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(deselect) + ')'
        select_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(select) + ')'
        driver.find_element_by_css_selector(deselect_css).click()
        driver.find_element_by_css_selector(select_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_mac_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if not find_row[0].get_attribute('textContent') == 'Mac PC':
                    raise Exception('Wrong type')
                else:
                    new_mac_cell += 1
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
        if new_mac_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        driver.implicitly_wait(15)

        # Select Device type dd
        driver.find_element_by_id(CE.device_type_label).click()

        # Select ANDROID device type
        deselect = 3
        select = 4
        deselect_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(deselect) + ')'
        select_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(select) + ')'
        driver.find_element_by_css_selector(deselect_css).click()
        driver.find_element_by_css_selector(select_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_android_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if not find_row[0].get_attribute('textContent') == 'ANDROID':
                    raise Exception('Wrong type')
                else:
                    new_android_cell += 1
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
        if new_android_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        driver.implicitly_wait(15)

        # Select Device type dd
        driver.find_element_by_id(CE.device_type_label).click()

        # Select iPad device type
        deselect = 4
        select = 5
        deselect_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(deselect) + ')'
        select_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(select) + ')'
        driver.find_element_by_css_selector(deselect_css).click()
        driver.find_element_by_css_selector(select_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_ipad_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if not find_row[0].get_attribute('textContent') == 'iPad':
                    raise Exception('Wrong type')
                else:
                    new_ipad_cell += 1
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
        if new_ipad_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        driver.implicitly_wait(15)

        # Select Device type dd
        driver.find_element_by_id(CE.device_type_label).click()

        # Select iPhone device type
        deselect = 5
        select = 6
        deselect_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(deselect) + ')'
        select_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(' + str(select) + ')'
        driver.find_element_by_css_selector(deselect_css).click()
        driver.find_element_by_css_selector(select_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check Severity column
        count_rows = 1
        count_pages = 1
        new_iphone_cell = 0
        driver.implicitly_wait(2)
        while count_pages < 5:
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_rows) + ') > td:nth-child(6)'
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                print('count_rows', count_rows)
                if not find_row[0].get_attribute('textContent') == 'iPhone':
                    raise Exception('Wrong type')
                else:
                    new_iphone_cell += 1
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
        if new_iphone_cell == 0:
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        driver.implicitly_wait(15)


class Container04Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_c_url = server_address + '/page/logs.jsf'
        cls.driver.get(cls.test_c_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(15)

    def tearDown(self):
        pass

    def test1_reset(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_c_url)
        wait = WebDriverWait(self.driver, 15)

        # Select End date columns
        driver.find_element_by_id(CE.visible_columns_label).click()
        driver.find_element_by_id(CE.visible_columns_panel)

        end_date_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2)'
        driver.find_element_by_css_selector(end_date_css).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        class_end_date = driver.find_element_by_css_selector(end_date_css).get_attribute(name='class')
        if CO.item_checked not in class_end_date:
            raise Exception('Item not selected')

        driver.find_element_by_id(CE.end_date_column)

        # Start datepicker
        driver.find_elements_by_class_name(CE.date_picker_trigger)[0].click()
        time.sleep(2)
        driver.find_element_by_id(CE.date_picker)

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        print('now_month_decimal', now_month_decimal)

        standard_yesterday = now - datetime.timedelta(days=1)
        yesterday = now - datetime.timedelta(days=30)
        yesterday_day = yesterday.strftime('%d')
        standard_yesterday_month_decimal = standard_yesterday.strftime('%m')
        standard_yesterday_day = standard_yesterday.strftime('%d')
        standard_yesterday_year = standard_yesterday.strftime('%Y')
        yesterday_month_decimal = yesterday.strftime('%m')
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year
        print('start_time_set_yesterday', start_time_set_yesterday)
        start_time_set_standard_yesterday = standard_yesterday_month_decimal + '/' + standard_yesterday_day + '/' + standard_yesterday_year
        print('start_time_set_standard_yesterday', start_time_set_standard_yesterday)

        if standard_yesterday_month_decimal != yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_prev).click()

        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
        print('yesterday_day', yesterday_day)
        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(2)

        # Apply
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        start_date_input = driver.find_element_by_id(CE.start_date).get_property(name='value')
        start_date_input_split = start_date_input.split()
        print('start_date_input_split[0]', start_date_input_split[0])

        if start_date_input_split[0] != start_time_set_yesterday:
            raise Exception('Input contain wrong data')

        # Select severity dd
        driver.find_element_by_id(CE.severity_label).click()
        # Select INFO severity
        info_severity_css = '#form\:severity_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1)'
        driver.find_element_by_css_selector(info_severity_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        # Select severity dd
        driver.find_element_by_id(CE.severity_label).click()
        severity_info_class = driver.find_element_by_css_selector(info_severity_css).get_attribute(name='class')
        if CO.item_unchecked in severity_info_class:
            raise Exception('Severity INFO unchecked')
        driver.find_element_by_id(CE.severity_label).click()

        # Select Device type dd
        driver.find_element_by_id(CE.device_type_label).click()
        # Select Windows PC device type
        select_css = '#form\:deviceTypeFilter_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2)'
        driver.find_element_by_css_selector(select_css).click()
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        # Select Device type dd
        driver.find_element_by_id(CE.device_type_label).click()
        win_device_class = driver.find_element_by_css_selector(select_css).get_attribute(name='class')
        if CO.item_unchecked in win_device_class:
            raise Exception('Windows PC device type unchecked')

        # User filter
        driver.find_element_by_id(CE.user_filter).send_keys('exadel1')
        # Apply
        driver.find_element_by_id(CE.apply_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        if 'exadel1' not in driver.find_element_by_id(CE.user_filter).get_property(name='value'):
            raise Exception('User is missing')

        #######################################
        # Reset check
        driver.find_element_by_id(CE.reset_filter_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check End date columns
        driver.find_element_by_id(CE.visible_columns_label).click()
        driver.find_element_by_id(CE.visible_columns_panel)

        new_end_date_css = '#form\:visibleColumns_panel > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2)'
        new_class_end_date = driver.find_element_by_css_selector(new_end_date_css).get_attribute(name='class')
        if CO.item_unchecked not in new_class_end_date:
            raise Exception('Item selected')

        if driver.find_elements_by_id(CE.end_date_column):
            raise Exception('Column is found')

        # Check date
        new_start_date_input = driver.find_element_by_id(CE.start_date).get_property(name='value')
        new_start_date_input_split = new_start_date_input.split()
        print('new_start_date_input_split[0]', new_start_date_input_split[0])

        if new_start_date_input_split[0] == start_time_set_yesterday:
            raise Exception('Input contain wrong data')

        if new_start_date_input_split[0] != start_time_set_standard_yesterday:
            raise Exception('Input contain wrong data')

        # Check INFO severity
        driver.find_element_by_id(CE.severity_label).click()
        severity_info_class = driver.find_element_by_css_selector(info_severity_css).get_attribute(name='class')
        if CO.item_checked in severity_info_class:
            raise Exception('Severity INFO checked')
        driver.find_element_by_id(CE.severity_label).click()

        # Check Device type dd
        driver.find_element_by_id(CE.device_type_label).click()
        win_device_class = driver.find_element_by_css_selector(select_css).get_attribute(name='class')
        if CO.item_checked in win_device_class:
            raise Exception('Windows PC device type checked')

        # Check user filter
        if 'exadel1' in driver.find_element_by_id(CE.user_filter).get_property(name='value'):
            raise Exception('User filter exist')
