import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import TotalLoginsElements, Other, Elements
import driver_settings
import time
import datetime
from selenium.webdriver import ActionChains
import calendar
import os

CE = TotalLoginsElements
CElem = Elements
CO = Other

# DEV Server
server_address = 'https://128.66.200.154:9613/edapt-admin'


class TotalLogins01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_tl_url = server_address + '/page/statisticsuser.jsf'
        cls.driver.get(cls.test_tl_url)
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
        driver.get(self.test_tl_url)
        wait = WebDriverWait(self.driver, 15)

        content_list = [CE.filter, CE.filter_content, CE.user_group, CE.application, CE.start_date_input,
                        CE.end_date_input, CE.apply_button, CE.tl_table]
        # count_123 = 0
        for elem in content_list:
            # print('len(content_list)', len(content_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

    def test2_start_date(self):
        driver = self.driver
        driver.get(self.test_tl_url)
        wait = WebDriverWait(self.driver, 15)

        # Check Start Date - End Date
        start_date = driver.find_element_by_name(CE.start_date_input).get_attribute(name='value')
        end_date = driver.find_element_by_name(CE.end_date_input).get_attribute(name='value')

        clock_start_time = '00:00'
        clock_end_time = '23:59'

        now = datetime.datetime.now()
        now_month = now.strftime('%B')
        prev_month = now - datetime.timedelta(days=30)
        prev_month_b = prev_month.strftime('%B')
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        prev_month_decimal = prev_month.strftime('%m')
        now_day = now.strftime('%d')

        yesterday = now - datetime.timedelta(days=5)
        yesterday_day = yesterday.strftime('%d')
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)
        yesterday_month_decimal = yesterday.strftime('%m')
        if yesterday_month_decimal[0] == '0':
            yesterday_month_decimal = yesterday_month_decimal[1]
            print('yesterday_month_decimal', yesterday_month_decimal)
        yesterday_month = yesterday.strftime('%B')
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        yesterday_last_day_of_month = calendar.monthrange(int(now_year), int(yesterday.strftime('%m')))
        print('yesterday_last_day_of_month[1]', yesterday_last_day_of_month[1])
        prev_last_day_of_month = calendar.monthrange(int(prev_month.strftime('%Y')), int(prev_month.strftime('%m')))
        print('prev_last_day_of_month', prev_last_day_of_month)

        start_time_today = prev_month_decimal + '/' + now_day + '/' + now_year + ' ' + clock_start_time
        if start_time_today != start_date:
            print('start_time_today', start_time_today, 'start_date', start_date)
            print('now_day', now_day)
            if int(now_day) > 28:
                if prev_month_decimal[0] == '0':
                    prev_month_decimal = prev_month_decimal[1]
                    monthrange_data = calendar.monthrange(int(now_year), int(prev_month_decimal))
                    start_time_today = '0' + prev_month_decimal + '/' + str(
                        monthrange_data[1]) + '/' + now_year + ' ' + clock_start_time
                else:
                    monthrange_data = calendar.monthrange(now_year, prev_month_decimal)
                    start_time_today = prev_month_decimal + '/' + str(
                        monthrange_data[1]) + '/' + now_year + ' ' + clock_start_time
                if start_time_today != start_date:
                    print('start_time_today', start_time_today)
                    raise Exception('Wrong Start time')

        end_time_today = now_month_decimal + '/' + now_day + '/' + now_year + ' ' + clock_end_time
        if end_time_today != end_date:
            raise Exception('Wrong End time')

        # date pickers
        driver.find_elements_by_class_name(CE.date_picker_trigger)[0].click()

        if now_day[0] == '0':
            now_day = now_day[1]

        picker_year = driver.find_element_by_class_name(CE.date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.date_picker_month).get_attribute('textContent')
        time.sleep(1)
        for picker_elem in driver.find_elements_by_class_name(CE.date_picker_day):
            if CE.date_picker_active in picker_elem.get_attribute(name='class'):
                picker_day = picker_elem.get_attribute('textContent')

        if now_year != picker_year:
            print('now_year', now_year, '- picker_year', picker_year)
            raise Exception('Year does not match')
        if prev_month_b != picker_month:
            print('prev_month_b', prev_month_b, '- picker_month', picker_month)
            raise Exception('Month does not match')
        if now_day != picker_day:
            print('now_day', now_day, '- picker_day', picker_day)
            if int(prev_last_day_of_month[1]) != int(picker_day):
                print('prev_last_day_of_month[1]', prev_last_day_of_month[1], '- picker_day', picker_day)
                raise Exception('Day does not match')
        # if now_day == str(last_day_of_month[1]):
        #     time.sleep(1)
        #     driver.find_element_by_class_name(CE.date_picker_next).click()
        if prev_month_b != yesterday_month:
            driver.find_element_by_class_name(CE.date_picker_next).click()
        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)

        # Check exadel1 login count
        string_count = 1
        while string_count <= 30:
            css = 'tr.ui-widget-content:nth-child(' + str(string_count) + ') > td:nth-child(2)'

            css_content = driver.find_element_by_css_selector(css).get_attribute('textContent')
            print('css_content', css_content)
            if 'exadel1' in css_content:
                break
            else:
                string_count += 1

        css_exadel1_count = 'tr.ui-widget-content:nth-child(' + str(string_count) + ') > td:nth-child(3)'
        exadel1_count = driver.find_element_by_css_selector(css_exadel1_count).get_attribute('textContent')
        print('exadel1_count', exadel1_count)

        # Apply
        driver.find_element_by_id(CE.apply_button).click()
        time.sleep(1)

        # Check exadel1 login count again
        class_content = 'ui-widget-content'
        string_count_new = 1
        while string_count_new <= 30:
            css = 'tr.ui-widget-content:nth-child(' + str(string_count_new) + ') > td:nth-child(2)'

            css_content = driver.find_element_by_css_selector(css).get_attribute('textContent')
            if 'exadel1' in css_content:
                break
            else:
                string_count_new += 1

        css_exadel1_count_new = 'tr.ui-widget-content:nth-child(' + str(string_count_new) + ') > td:nth-child(3)'
        exadel1_count_new = driver.find_element_by_css_selector(css_exadel1_count_new).get_attribute('textContent')
        print('exadel1_count_new', exadel1_count_new)

        if int(exadel1_count_new) >= int(exadel1_count):
            raise Exception('Wrong numbers of exadel1 logins')

    def test3_end_date(self):
        driver = self.driver
        driver.get(self.test_tl_url)
        wait = WebDriverWait(self.driver, 15)

        now = datetime.datetime.now()
        now_month = now.strftime('%B')
        prev_month = now - datetime.timedelta(days=30)
        prev_month_b = prev_month.strftime('%B')
        now_year = now.strftime('%Y')
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]

        yesterday = now - datetime.timedelta(days=7)
        yesterday_day = yesterday.strftime('%d')
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)
        yesterday_month_decimal = yesterday.strftime('%m')
        if yesterday_month_decimal[0] == '0':
            yesterday_month_decimal = yesterday_month_decimal[1]
            print('yesterday_month_decimal', yesterday_month_decimal)
        yesterday_month = yesterday.strftime('%B')

        # date pickers
        driver.find_elements_by_class_name(CE.date_picker_trigger)[1].click()

        picker_year = driver.find_element_by_class_name(CE.date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.date_picker_month).get_attribute('textContent')
        time.sleep(1)
        for picker_elem in driver.find_elements_by_class_name(CE.date_picker_day):
            if CE.date_picker_active in picker_elem.get_attribute(name='class'):
                picker_day = picker_elem.get_attribute('textContent')

        if now_year != picker_year:
            print('now_year', now_year, '- picker_year', picker_year)
            raise Exception('Year does not match')
        if now_month != picker_month:
            print('now_month', now_month, '- picker_month', picker_month)
            raise Exception('Month does not match')
        if now_day != picker_day:
            print('now_day', now_day, '- picker_day', picker_day)
            raise Exception('Day does not match')
        if yesterday_month != now_month:
            driver.find_element_by_class_name(CE.date_picker_prev).click()
        picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)

        # Check exadel1 login count
        string_count = 1
        while string_count <= 30:
            css = 'tr.ui-widget-content:nth-child(' + str(string_count) + ') > td:nth-child(2)'

            css_content = driver.find_element_by_css_selector(css).get_attribute('textContent')
            print('css_content', css_content)
            if 'exadel1' in css_content:
                break
            else:
                string_count += 1

        css_exadel1_count = 'tr.ui-widget-content:nth-child(' + str(string_count) + ') > td:nth-child(3)'
        exadel1_count = driver.find_element_by_css_selector(css_exadel1_count).get_attribute('textContent')
        # print('exadel1_count', exadel1_count)

        # Apply
        driver.find_element_by_id(CE.apply_button).click()
        time.sleep(1)

        # Check exadel1 login count again
        class_content = 'ui-widget-content'
        string_count_new = 1
        while string_count_new <= 30:
            css = 'tr.ui-widget-content:nth-child(' + str(string_count_new) + ') > td:nth-child(2)'

            css_content = driver.find_element_by_css_selector(css).get_attribute('textContent')
            if 'exadel1' in css_content:
                break
            else:
                string_count_new += 1

        css_exadel1_count_new = 'tr.ui-widget-content:nth-child(' + str(string_count_new) + ') > td:nth-child(3)'
        exadel1_count_new = driver.find_element_by_css_selector(css_exadel1_count_new).get_attribute('textContent')
        # print('exadel1_count_new', exadel1_count_new)

        if int(exadel1_count_new) >= int(exadel1_count):
            raise Exception('Wrong numbers of exadel1 logins')

    def test4_expand(self):
        driver = self.driver
        driver.get(self.test_tl_url)
        wait = WebDriverWait(self.driver, 15)

        now = datetime.datetime.now()
        prev_month = now - datetime.timedelta(days=30)
        now_year = now.strftime('%Y')
        prev_year = prev_month.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        prev_month_decimal = prev_month.strftime('%m')

        # Check exadel1 string
        number = 1
        while number <= 30:
            css = 'tr.ui-widget-content:nth-child(' + str(number) + ') > td:nth-child(2)'
            css_content = driver.find_element_by_css_selector(css).get_attribute('textContent')
            # print('css_content', css_content)
            if 'exadel1' in css_content:
                number -= 1
                break
            else:
                number += 1

        # print('number', number)
        css_expand = 'tr.ui-widget-content:nth-child(' + str(number + 1) + ') > td:nth-child(1)'
        driver.find_element_by_css_selector(css_expand).click()
        time.sleep(1)

        id_table_head = 'dataTableForm:dataTableCount:' + str(number) + ':rowExpansionTable_head'
        id_user_table = 'dataTableForm:dataTableCount:' + str(number) + ':rowExpansionTable:rowExpansionUserColumn'
        id_date_table = 'dataTableForm:dataTableCount:' + str(number) + ':rowExpansionTable:rowExpansionDateColumn'
        id_count_table = 'dataTableForm:dataTableCount:' + str(number) + ':rowExpansionTable:rowExpansionCountColumn'

        content_list = [id_table_head, id_user_table, id_date_table, id_count_table]
        # count_123 = 0
        for elem in content_list:
            # print('len(content_list)', len(content_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

        css_exadel1_count = 'tr.ui-widget-content:nth-child(' + str(number + 1) + ') > td:nth-child(3)'
        exadel1_count = driver.find_element_by_css_selector(css_exadel1_count).get_attribute('textContent')

        # User column
        string_numbers_user = 1
        while string_numbers_user <= 35:
            css_user = '#dataTableForm\:dataTableCount\:' + str(
                number) + '\:rowExpansionTable_data > tr:nth-child(' + str(
                string_numbers_user) + ') > td:nth-child(1)'
            if not driver.find_elements_by_css_selector(css_user):
                string_numbers_user -= 1
                break
            else:
                string_numbers_user += 1
                if not driver.find_elements_by_css_selector(css_user)[0].get_attribute('textContent'):
                    raise Exception('String empty')
                else:
                    text_content_user = driver.find_element_by_css_selector(css_user).get_attribute('textContent')
                    if text_content_user != 'exadel1':
                        raise Exception('Wrong name in string')

        # Date column
        string_numbers_date = 1
        day_for_split = 32
        while string_numbers_date <= 35:
            css_date = '#dataTableForm\:dataTableCount\:' + str(
                number) + '\:rowExpansionTable_data > tr:nth-child(' + str(
                string_numbers_date) + ') > td:nth-child(2)'
            css_date_2 = '#dataTableForm\:dataTableCount\:' + str(
                number) + '\:rowExpansionTable_data > tr:nth-child(' + str(
                string_numbers_date - 1) + ') > td:nth-child(2)'
            if not driver.find_elements_by_css_selector(css_date):
                string_numbers_date -= 1
                break
            else:
                string_numbers_date += 1
                if not driver.find_elements_by_css_selector(css_date)[0].get_attribute('textContent'):
                    raise Exception('String empty')
                else:
                    text_content_date = driver.find_element_by_css_selector(css_date).get_attribute('textContent')
                    split_date = text_content_date.split('-')
                    if split_date[0] != now_year and split_date[0] != prev_year:
                        print('split_date[0]', split_date[0])
                        raise Exception('Wrong Year')
                    if split_date[1] != now_month_decimal and split_date[1] != prev_month_decimal:
                        print('split_date[1]', split_date[1])
                        raise Exception('Wrong month')
                    if int(split_date[2]) >= int(day_for_split):
                        print('split_date[2]', split_date[2], 'day_for_split', day_for_split)
                        text_content_date_2 = driver.find_element_by_css_selector(css_date_2).get_attribute('textContent')
                        if text_content_date == text_content_date_2:
                            raise Exception('Wrong day')
                        else:
                            day_for_split = split_date[2]
                    else:
                        print('split_date[2]', split_date[2], 'day_for_split', day_for_split)
                        day_for_split = split_date[2]

        # Count column
        string_numbers_count = 1
        sum_count = 0
        while string_numbers_count <= 35:
            css_count = '#dataTableForm\:dataTableCount\:' + str(
                number) + '\:rowExpansionTable_data > tr:nth-child(' + str(
                string_numbers_count) + ') > td:nth-child(3)'
            if not driver.find_elements_by_css_selector(css_count):
                string_numbers_count -= 1
                break
            else:
                string_numbers_count += 1
                if not driver.find_element_by_css_selector(css_count).get_attribute('textContent'):
                    raise Exception('String empty')
                count = driver.find_element_by_css_selector(css_count).get_attribute('textContent')
                sum_count += int(count)

        print('string_numbers_user', string_numbers_user)
        print('string_numbers_date', string_numbers_date)
        print('string_numbers_count', string_numbers_count)
        if string_numbers_user != string_numbers_date or string_numbers_date != string_numbers_count:
            raise Exception('Wrong string numbers')
        print('exadel1_count', exadel1_count)
        print('sum_count', sum_count)
        if sum_count != int(exadel1_count):
            raise Exception('Count value not correct')
