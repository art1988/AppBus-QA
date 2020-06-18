import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import DeviceLogElements, Other, Elements
import driver_settings
import time
import datetime
from selenium.webdriver import ActionChains
import calendar
import os

CE = DeviceLogElements
CElem = Elements
CO = Other

# Dev
# server_address = 'https://128.66.200.154:9613/edapt-admin'

# QA Server
# server_address = 'https://dev-msa-qa.botf03.net:9613/edapt-admin'

# QA Stag Server
server_address = 'https://dev-msa-qa-stag.botf03.net:9613/edapt-admin'

project_path = os.path.dirname(os.path.dirname(__file__))
files_path = os.path.join(project_path, 'files')


class DeviceLog01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_dl_url = server_address + '/page/devicelog.jsf'
        cls.driver.get(cls.test_dl_url)
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
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        content_list = [CE.log_folder, CE.crash_log_table, CE.device_upload_button, CE.upload_decoded_log_dialog,
                        CE.upload_decoded_log_close, CE.file_name_column, CE.file_name_filter, CE.platform_column,
                        CE.platform_drop_down_filter, CE.device_id_column, CE.device_id_filter, CE.when_column,
                        CE.when_filter, CE.size_column, CE.action_column, CE.view_action_first_str,
                        CE.download_action_first_str, CE.delete_action_first_str, CE.log_dialog, CE.log_dialog_ok,
                        CE.delete_dialog, CE.delete_dialog_yes, CE.delete_dialog_no]
        # count_123 = 0
        for elem in content_list:
            # print('len(content_list)', len(content_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

    def test2_folders(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        # Check folder
        folder_name = driver.find_element_by_id(CE.log_folder_label).get_attribute('textContent')
        if folder_name != CO.decoded_folder:
            print('folder_name', folder_name)
            raise Exception("Wrong folder name")

        file_name_list = []
        file_name_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(1)'

        # Decoded folder file name
        if not driver.find_elements_by_css_selector(file_name_css):
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        else:
            file_name_list.append(driver.find_element_by_css_selector(file_name_css).get_attribute('textContent'))

        # Select Encoded folder
        driver.find_element_by_id(CE.log_folder).click()
        driver.find_element_by_id(CE.folder_list)
        driver.find_element_by_id('tabs:deviceLog:selectedFolder_1').click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check folder
        if driver.find_element_by_id(CE.log_folder_label).get_attribute('textContent') != CO.encoded_folder:
            raise Exception("Wrong folder name")

        # Encoded folder file name
        if not driver.find_elements_by_css_selector(file_name_css):
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        else:
            file_name_list.append(driver.find_element_by_css_selector(file_name_css).get_attribute('textContent'))

        # Select Failed folder
        driver.find_element_by_id(CE.log_folder).click()
        driver.find_element_by_id(CE.folder_list)
        driver.find_element_by_id('tabs:deviceLog:selectedFolder_2').click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check folder
        if driver.find_element_by_id(CE.log_folder_label).get_attribute('textContent') != CO.failed_folder:
            raise Exception("Wrong folder name")

        # Failed folder file name
        if not driver.find_elements_by_css_selector(file_name_css):
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        else:
            file_name_list.append(driver.find_element_by_css_selector(file_name_css).get_attribute('textContent'))

        # Select Temporary folder
        driver.find_element_by_id(CE.log_folder).click()
        driver.find_element_by_id(CE.folder_list)
        driver.find_element_by_id('tabs:deviceLog:selectedFolder_3').click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check folder
        if driver.find_element_by_id(CE.log_folder_label).get_attribute('textContent') != CO.temporary_folder:
            raise Exception("Wrong folder name")

        # Temporary folder file name
        if not driver.find_elements_by_css_selector(file_name_css):
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        else:
            file_name_list.append(driver.find_element_by_css_selector(file_name_css).get_attribute('textContent'))

        # Select Decoded folder
        driver.find_element_by_id(CE.log_folder).click()
        driver.find_element_by_id(CE.folder_list)
        driver.find_element_by_id('tabs:deviceLog:selectedFolder_0').click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check folder
        if driver.find_element_by_id(CE.log_folder_label).get_attribute('textContent') != CO.decoded_folder:
            raise Exception("Wrong folder name")

        # Decoded folder file name
        if not driver.find_elements_by_css_selector(file_name_css):
            empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
            if CO.no_records_found not in empty_message:
                raise Exception('"No records found." message is missing')
        else:
            decoded_folder_file_name = driver.find_element_by_css_selector(file_name_css).get_attribute('textContent')

        print('file_name_list', file_name_list)

        if file_name_list[0] != decoded_folder_file_name:
            raise Exception('Wrong file name')

        len_file_name_list = len(file_name_list)
        count = 0
        while count <= len_file_name_list - 2:
            print('count', count)
            if file_name_list[count] == file_name_list[count + 1]:
                raise Exception('Match file names')
            count += 1

    def test3_paginator(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        file_name_list = []
        file_name_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(1)'

        # File Name for first session first page
        file_name_column_data_first = driver.find_element_by_css_selector(file_name_css).get_attribute('textContent')
        print('file_name_column_data_first', file_name_column_data_first)
        file_name_list.append(file_name_column_data_first)

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

            # File Name for first session n page
            file_name_column_data_n = driver.find_element_by_css_selector(file_name_css).get_attribute('textContent')
            print('file_name_column_data in', count_page, 'page', file_name_column_data_n)
            file_name_list.append(file_name_column_data_n)
            count_page += 1

        print('file_name_list', file_name_list)
        if file_name_list[0] != file_name_list[5]:
            print('file_name_list[0]', file_name_list[0], 'file_name_list[5]', file_name_list[5])
            raise Exception('Wrong item')
        count_check = 0
        while count_check <= 4:
            print('file_name_list[' + str(count_check) + ']', file_name_list[count_check],
                  'file_name_list[' + str(count_check + 1) + ']', file_name_list[count_check + 1])
            if file_name_list[count_check] == file_name_list[count_check + 1]:
                raise Exception('Wrong item')
            count_check += 1

    def test4_view_last_200_lines(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        driver.find_element_by_id(CE.view_action_first_str).click()
        driver.find_element_by_id(CE.log_dialog)
        driver.find_element_by_class_name(CE.log_dialog_container)
        if not driver.find_element_by_class_name(CE.preformatted).get_attribute('textContent'):
            raise Exception('No content')
        driver.find_element_by_id(CE.log_dialog_ok).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.log_dialog)))


class DeviceLog02Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        downloads_folder = os.path.expanduser('~/Downloads')

        set_driver = set_driver = driver_settings.driver_with_firefox_txt_download(cls, downloads_folder)
        cls.driver = set_driver

        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("browser.download.manager.showWhenStarting", False)
        # profile.set_preference("browser.download.folderList", 2)
        # profile.set_preference("browser.download.dir", downloads_folder)
        # profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")
        # cls.driver = webdriver.Firefox(profile)

        cls.test_dl_url = server_address + '/page/devicelog.jsf'
        cls.driver.get(cls.test_dl_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(15)

    def tearDown(self):
        pass

    def test1_download(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        file_name_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(1)'
        file_name = driver.find_element_by_css_selector(file_name_css).get_attribute('textContent')

        # Download
        downloads_folder = os.path.expanduser('~/Downloads')
        driver.find_element_by_id(CE.download_action_first_str).click()
        time.sleep(5)
        file_path = str(downloads_folder) + r'/' + file_name
        print('file_path', file_path)
        time.sleep(1)

        x = 0
        while x < 5:
            print('while')
            if not os.path.exists(file_path):
                time.sleep(1)
                print('if not')
            elif os.path.exists(file_path):
                print('File - OK')
                break
            x += 1
            if x >= 5:
                raise Exception('File not found')

        time.sleep(5)
        os.remove(file_path)
        print('Remove - OK')


class DeviceLog03Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_dl_url = server_address + '/page/devicelog.jsf'
        cls.driver.get(cls.test_dl_url)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(15)

    def tearDown(self):
        pass

    def test1_file_name_column_sort(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)
        actionChains = ActionChains(driver)

        file_name_first_str_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(1)'

        # Default sorting
        aria_sort = driver.find_element_by_id(CE.file_name_column).get_attribute(name='aria-sort')
        if CO.aria_sort_other not in aria_sort:
            print('aria_sort', aria_sort)
            raise Exception('Wrong sorting mode')
        first_file_name = driver.find_element_by_css_selector(file_name_first_str_css).get_attribute('textContent')

        # New sorting (ascending)
        elem = driver.find_element_by_id(CE.file_name_column)
        actionChains.move_to_element(elem).move_by_offset(0, 20).click().perform()
        time.sleep(5)
        aria_sort = driver.find_element_by_id(CE.file_name_column).get_attribute(name='aria-sort')
        if CO.aria_sort_ascending not in aria_sort:
            print('aria_sort', aria_sort)
            raise Exception('Wrong sorting mode')
        second_file_name = driver.find_element_by_css_selector(file_name_first_str_css).get_attribute('textContent')

        if first_file_name != second_file_name:
            raise Exception('Wrong file in first line')

        # New sorting (descending)
        elem = driver.find_element_by_id(CE.file_name_column)
        actionChains.move_to_element(elem).move_by_offset(0, 20).click().perform()
        time.sleep(5)
        aria_sort = driver.find_element_by_id(CE.file_name_column).get_attribute(name='aria-sort')
        if CO.aria_sort_descending not in aria_sort:
            print('aria_sort', aria_sort)
            raise Exception('Wrong sorting mode')
        third_file_name = driver.find_element_by_css_selector(file_name_first_str_css).get_attribute('textContent')

        if second_file_name == third_file_name:
            raise Exception('Match file names')

    def test2_when_column_sort(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)
        actionChains = ActionChains(driver)

        when_first_str_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(4)'

        # Default sorting
        # aria_sort = driver.find_element_by_id(CE.when_column).get_attribute(name='aria-sort')
        # if CO.aria_sort_other not in aria_sort:
        #     print('aria_sort', aria_sort)
        #     raise Exception('Wrong sorting mode')
        if driver.find_elements_by_id(CE.when_column)[0].get_attribute(name='aria-sort'):
            raise Exception('aria-sort attribute exist')
        first_when = driver.find_element_by_css_selector(when_first_str_css).get_attribute('textContent')

        # New sorting (ascending)
        elem = driver.find_element_by_id(CE.when_column)
        actionChains.move_to_element(elem).move_by_offset(0, 20).click().perform()
        time.sleep(5)
        aria_sort = driver.find_element_by_id(CE.when_column).get_attribute(name='aria-sort')
        if CO.aria_sort_ascending not in aria_sort:
            print('aria_sort', aria_sort)
            raise Exception('Wrong sorting mode')
        second_when = driver.find_element_by_css_selector(when_first_str_css).get_attribute('textContent')

        if first_when != second_when:
            raise Exception('Wrong file in first line')

        # New sorting (descending)
        elem = driver.find_element_by_id(CE.when_column)
        actionChains.move_to_element(elem).move_by_offset(0, 20).click().perform()
        time.sleep(5)
        aria_sort = driver.find_element_by_id(CE.when_column).get_attribute(name='aria-sort')
        if CO.aria_sort_descending not in aria_sort:
            print('aria_sort', aria_sort)
            raise Exception('Wrong sorting mode')
        third_when = driver.find_element_by_css_selector(when_first_str_css).get_attribute('textContent')

        if second_when == third_when:
            raise Exception('Match file names')

    @unittest.skip('Bug https://jira.51-maps.com/browse/ED-4020')
    def test3_file_name_column_input(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

    def test4_device_id_column_input(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        device_id_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(3)'
        first_device_id = driver.find_element_by_css_selector(device_id_css).get_attribute('textContent')

        # Find device id for search
        search_device_id = first_device_id
        while first_device_id == search_device_id:
            driver.find_element_by_class_name(CE.paginator_next_button).click()
            Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
            new_page_device_id = driver.find_element_by_css_selector(device_id_css).get_attribute('textContent')
            if new_page_device_id != first_device_id:
                search_device_id = new_page_device_id
        driver.find_element_by_class_name(CE.paginator_first_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        print('first_device_id', first_device_id)
        print('search_device_id', search_device_id)

        # Use search
        driver.find_element_by_id(CE.device_id_filter).click()
        driver.find_element_by_id(CE.device_id_filter).send_keys(search_device_id)
        driver.find_element_by_css_selector(device_id_css).click()
        time.sleep(5)

        # Compare
        new_first_device_id = driver.find_element_by_css_selector(device_id_css).get_attribute('textContent')
        if new_first_device_id != search_device_id:
            raise Exception('Wrong device id')

        # Clear search
        driver.find_element_by_id(CE.device_id_filter).click()
        driver.find_element_by_id(CE.device_id_filter).clear()
        driver.find_element_by_css_selector(device_id_css).click()
        time.sleep(5)

        # Compare
        new_first_device_id_2 = driver.find_element_by_css_selector(device_id_css).get_attribute('textContent')
        if new_first_device_id_2 != first_device_id:
            raise Exception('Wrong device id')

    def test5_when_column_date_picker(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month_decimal = now.strftime('%m')
        print('now_month_decimal', now_month_decimal)

        days = 1
        empty_message = 1
        while empty_message:
            # Start datepicker
            driver.find_element_by_id(CE.when_filter).click()
            # Set yesterday date
            yesterday = now - datetime.timedelta(days=days)
            yesterday_day = yesterday.strftime('%d')
            yesterday_month = yesterday.strftime('%B')
            yesterday_month_decimal = yesterday.strftime('%m')
            yesterday_year = yesterday.strftime('%Y')
            last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
            print('last_day_of_month[1]', last_day_of_month[1])
            start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year
            print('start_time_set_yesterday', start_time_set_yesterday)
            month = driver.find_element_by_class_name(CE.date_picker_month).get_attribute('textContent')
            if month != yesterday_month:
                driver.find_element_by_class_name(CE.date_picker_next).click()
            if yesterday_day[0] == '0':
                yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)
            picker_day_to_select = Check.by_css_selector_and_text(driver, CE.date_picker_day_css, yesterday_day)
            time.sleep(1)
            picker_day_to_select.click()
            time.sleep(2)

            if not driver.find_elements_by_class_name(CE.empty_message):
                empty_message = 0
            else:
                days += 1

        when_first_str_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(4)'
        when_date = driver.find_element_by_css_selector(when_first_str_css).get_attribute('textContent')
        if start_time_set_yesterday not in when_date:
            print('when_date', when_date)
            raise Exception('Wrong date')

    def test6_platform_type_column_drop_down(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        platform_type_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(2)'
        first_platform_type = driver.find_element_by_css_selector(platform_type_css).get_attribute('textContent')

        driver.find_element_by_id(CE.platform_drop_down_filter).click()
        driver.find_element_by_id(CE.platform_drop_down_table)
        platform_type_item = 'tabs:logForm:deviceLogTable:j_idt253_'    # plus number

        # All type check
        all_type_class = driver.find_element_by_id(platform_type_item + str(0)).get_attribute(name='class')
        if CE.row_highlight not in all_type_class:
            raise Exception('All type not selected')
        driver.find_element_by_id(CE.platform_drop_down_filter).click()

        # Check type
        type_list = ['All', 'UNKNOWN', 'ANDROID', 'MAC', 'WINDOWS', 'iOS']
        count = 1
        while count <= 5:
            print('count', count)
            print('str(type_list[count])', str(type_list[count]))
            driver.implicitly_wait(5)
            driver.find_element_by_id(CE.platform_drop_down_filter).click()

            driver.find_element_by_id(platform_type_item + str(count)).click()
            time.sleep(5)
            Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

            if not driver.find_elements_by_css_selector(platform_type_css):
                empty_message = driver.find_element_by_class_name(CE.empty_message).get_attribute('textContent')
                if CO.no_records_found not in empty_message:
                    raise Exception('"No records found." message is missing')
            else:
                type_in_str = driver.find_element_by_css_selector(platform_type_css).get_attribute('textContent')
                if str(type_list[count]) not in type_in_str:
                    print('type_in_str', type_in_str)
                    raise Exception('Wrong type in first string')
            count += 1
        driver.implicitly_wait(15)

    def test7_upload_device_log(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        address = files_path + r"\encrypted-W-test_log_file.log"
        print(address, address)
        data_file_upload = 0
        while data_file_upload < 2:
            driver.find_element_by_id(CE.upload_device_log_button).click()
            driver.find_element_by_id(CE.upload_decoded_log_dialog)
            time.sleep(1)
            element = driver.find_element_by_id(CE.upload_device_log_choose_button)
            element.send_keys(address)
            file_name = 'encrypted-W-test_log_file.log'
            file_name_first_str_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(1)'
            upload_file_name = driver.find_element_by_class_name(CE.upload_file_name).get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')

            if data_file_upload == 0:
                data_file_upload += 1
                # Select Cancel
                driver.find_element_by_id(CE.upload_decoded_log_close).click()
                first_file_name = driver.find_element_by_css_selector(file_name_first_str_css).get_attribute(
                    'textContent')
                if file_name in first_file_name:
                    raise Exception('Wrong file name')
            else:
                data_file_upload += 1
                # Select upload
                driver.find_element_by_id(CE.upload_decoded_log_upload).click()
                if driver.find_elements_by_class_name(CE.main_notification_message):
                    print(driver.find_element_by_class_name(CE.main_notification_message).get_attribute('textContent'))
                time.sleep(5)
                first_file_name = driver.find_element_by_css_selector(file_name_first_str_css).get_attribute(
                    'textContent')
                print('first_file_name', first_file_name)
                if file_name not in first_file_name:
                    raise Exception('Wrong file name')

    def test5_delete_device_log(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_dl_url)
        wait = WebDriverWait(self.driver, 15)

        file_name_first_str_css = 'tr.ui-datatable-even:nth-child(1) > td:nth-child(1)'
        first_file_name = driver.find_element_by_css_selector(file_name_first_str_css).get_attribute('textContent')

        if 'encrypted-W-test_log_file.log' not in first_file_name:
            raise Exception('Wrong file name')

        # Delete - No
        driver.find_element_by_id(CE.delete_action_first_str).click()
        driver.find_element_by_id(CE.delete_dialog)
        driver.find_element_by_id(CE.delete_dialog_no).click()

        # Check log file
        first_file_name_2 = driver.find_element_by_css_selector(file_name_first_str_css).get_attribute('textContent')
        if 'encrypted-W-test_log_file.log' not in first_file_name_2:
            raise Exception('Wrong file name')

        # Delete - Yes
        time.sleep(2)
        driver.find_element_by_id(CE.delete_action_first_str).click()
        driver.find_element_by_id(CE.delete_dialog)
        driver.find_element_by_id(CE.delete_dialog_yes).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check log file
        first_file_name_2 = driver.find_element_by_css_selector(file_name_first_str_css).get_attribute('textContent')
        if 'encrypted-W-test_log_file.log' in first_file_name_2:
            raise Exception('Wrong file name')
