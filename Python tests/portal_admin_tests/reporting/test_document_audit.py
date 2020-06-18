import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import DocumentAuditElements, Other, Elements
import driver_settings
import time
import datetime
from selenium.webdriver import ActionChains
import calendar
import os

CE = DocumentAuditElements
CElem = Elements
CO = Other

# DEV
server_address = 'https://128.66.200.154:9613/edapt-admin'


class DocumentAudit01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_da_url = server_address + '/page/documentsstatistic.jsf'
        cls.driver.get(cls.test_da_url)
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
        driver.get(self.test_da_url)
        wait = WebDriverWait(self.driver, 15)

        doc_usage_folder_class = driver.find_element_by_css_selector(CE.documents_usage_folder).get_attribute(name='class')
        if 'ui-tabs-selected' not in doc_usage_folder_class:
            raise Exception('Documents Usage folder not selected')

        driver.find_element_by_css_selector(CE.users_folder).click()
        time.sleep(1)
        users_folder_class = driver.find_element_by_css_selector(CE.users_folder).get_attribute(name='class')
        if 'ui-tabs-selected' not in users_folder_class:
            raise Exception('Documents Usage folder not selected')

        content_list = [CE.overall_users_statistic_header, CE.overall_users_statistic]

        for elem in content_list:
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')

        driver.find_element_by_css_selector(CE.documents_usage_folder).click()
        time.sleep(1)
        doc_usage_folder_class = driver.find_element_by_css_selector(
            CE.documents_usage_folder).get_attribute(name='class')
        if 'ui-tabs-selected' not in doc_usage_folder_class:
            raise Exception('Documents Usage folder not selected')

        content_list = [CE.filter_header, CE.filter, CE.start_date, CE.end_date, CE.apply_filter, CE.od_statistic,
                        CE.od_content, CE.download_per_file_type_header, CE.download_per_file_type,
                        CE.opens_per_file_type_header, CE.opens_per_file_type, CE.total_usage_per_file_type_header,
                        CE.total_usage_per_file_type]
        # count_123 = 0
        for elem in content_list:
            # print('len(content_list)', len(content_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

    def test2_check_user_filter(self):
        driver = self.driver
        driver.get(self.test_da_url)
        wait = WebDriverWait(self.driver, 15)
        total_opened_files = '#mainForm\:j_idt53\:j_idt69_content > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > b:nth-child(1)'
        count = driver.find_element_by_css_selector(total_opened_files).get_attribute('textContent')

        # Set username
        driver.find_element_by_name(CE.username_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_filter).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        count_2 = driver.find_element_by_css_selector(total_opened_files).get_attribute('textContent')
        if int(count) == int(count_2):
            print('count', count, '| count_2', count_2)
            raise Exception('The number of open files has not changed')

    def test3_start_date_filter(self):
        driver = self.driver
        driver.get(self.test_da_url)
        wait = WebDriverWait(self.driver, 15)
        total_opened_files = '#mainForm\:j_idt53\:j_idt69_content > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > b:nth-child(1)'
        count = driver.find_element_by_css_selector(total_opened_files).get_attribute('textContent')

        driver.find_element_by_id(CE.start_date).click()

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        print('now_month_decimal', now_month_decimal)

        yesterday = now - datetime.timedelta(days=7)
        yesterday_day = yesterday.strftime('%d')
        yesterday_month_decimal = yesterday.strftime('%m')
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year

        if now_month_decimal == yesterday_month_decimal:
            driver.find_element_by_class_name(CE.date_picker_next).click()
            if yesterday_day[0] == '0':
                yesterday_day = yesterday_day[1]
                print('yesterday_day', yesterday_day)

        picker_day_to_select = Check.by_class_name_and_text(driver, CE.date_picker_day, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()

        # Set username
        # driver.find_element_by_name(CE.username_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_filter).click()
        # wait.until(EC.invisibility_of_element_located((By.ID, CElem.loading_bar)))
        time.sleep(1)

        count_2 = driver.find_element_by_css_selector(total_opened_files).get_attribute('textContent')
        if int(count) == int(count_2):
            print('count', count, '| count_2', count_2)
            raise Exception('The number of open files has not changed')

    def test4_end_date_filter(self):
        driver = self.driver
        driver.get(self.test_da_url)
        wait = WebDriverWait(self.driver, 15)
        total_opened_files = '#mainForm\:j_idt53\:j_idt69_content > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > b:nth-child(1)'
        count = driver.find_element_by_css_selector(total_opened_files).get_attribute('textContent')

        driver.find_element_by_id(CE.end_date).click()
        time.sleep(1)

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        print('now_month_decimal', now_month_decimal)

        yesterday = now - datetime.timedelta(days=7)
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
        time.sleep(1)
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.date_picker_day, yesterday_day)
        time.sleep(1)
        picker_day_to_select.click()

        # Set username
        # driver.find_element_by_name(CE.username_input).send_keys('exadel1')
        driver.find_element_by_id(CE.apply_filter).click()
        # wait.until(EC.invisibility_of_element_located((By.ID, CElem.loading_bar)))
        time.sleep(1)

        count_2 = driver.find_element_by_css_selector(total_opened_files).get_attribute('textContent')
        if int(count) == int(count_2):
            print('count', count, '| count_2', count_2)
            raise Exception('The number of open files has not changed')



