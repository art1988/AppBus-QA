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

# QA Server
# server_address = 'https://dev-msa-qa.botf03.net:9613/edapt-admin'

# QA Stag Server
server_address = 'https://dev-msa-qa-stag.botf03.net:9613/edapt-admin'

project_path = os.path.dirname(os.path.dirname(__file__))
files_path = os.path.join(project_path, 'files')


class ProvisioningConfig01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        driver = cls.driver

        # Select current config
        driver.find_element_by_id(CE.config_select_label).click()
        # Delete config
        if Check.select_config(driver, wait, CO.upcoming_config):
            if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
                driver.find_element_by_id(CE.config_select_label).click()
            if not driver.find_element_by_id(CE.config_select_list):
                raise Exception('The list of configs is missing')
            if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
                Check.select_config(driver, wait, CO.upcoming_config)
                time.sleep(1)
                driver.find_element_by_id(CE.config_delete).click()
                time.sleep(1)
                Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
                time.sleep(1)
                if driver.find_elements_by_class_name(CE.main_notification_title):
                    notification_message = driver.find_element_by_class_name(CE.main_notification_title).get_attribute(
                        'textContent')
                    if notification_message != CO.message_successfully_deleted:
                        print('notification_message', notification_message)
                        raise Exception('Wrong notification message')
        # Delete end
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
            if not driver.find_element_by_id(CE.config_select_list):
                raise Exception('The list of configs is missing')
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.get(cls.test_pc_url)
        wait = WebDriverWait(driver, 15)

        # Delete config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
            Check.select_config(driver, wait, CO.upcoming_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            time.sleep(1)
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(CE.main_notification_title).get_attribute(
                    'textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
        # Delete end

        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        pass

    def test1_pc_add_and_revert(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        if not Check.by_class_name_and_text(driver, CE.titlebar_panel, CO.provisioning_config_panel_title):
            raise Exception('Wrong title bar name')

        if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
            raise Exception(CO.select_configuration, 'is missing')

        start_time_disabled = driver.find_element_by_id(CE.config_start_time).get_attribute(name='aria-disabled')
        if start_time_disabled != 'true':
            raise Exception('Start time is not disabled')

        driver.find_element_by_id(CE.config_add).click()
        driver.find_element_by_id(CE.config_start_time_for_new_config)
        pop_up_title = driver.find_element_by_id(CE.config_start_time_for_new_config_title).get_attribute('textContent')
        if pop_up_title != CO.add_new_config_title:
            raise Exception('Pop-up title incorrect')
        time.sleep(1)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        start_time_set_today = now_month_decimal + '/' + now_day + '/' + now_year[-2:]

        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')

        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
                picker_day = picker_elem.get_attribute('textContent')
                picker_day_to_select = picker_elem

        if now_year != picker_year:
            print('now_year', now_year, '- picker_year', picker_year)
            raise Exception('Year does not match')
        if now_month != picker_month:
            print('now_month', now_month, '- picker_month', picker_month)
            raise Exception('Month does not match')
        if now_day != picker_day:
            print('now_day', now_day, '- picker_day', picker_day)
            raise Exception('Day does not match')

        picker_day_to_select.click()
        time.sleep(1)
        new_start_time = driver.find_element_by_id(CE.config_set_new_start_time).get_attribute(name='value')
        if new_start_time != start_time_set_today:
            print('new_start_time', new_start_time, "- start_time_set_today", start_time_set_today)
            raise Exception('Date is incorrect')

        driver.find_element_by_id(CE.config_start_time_ok_button).click()
        time.sleep(2)
        sets_start_time = driver.find_element_by_id(CE.config_start_time).get_attribute(name='value')
        if sets_start_time != start_time_set_today:
            print('sets_start_time', sets_start_time, "- start_time_set_today", start_time_set_today)
            raise Exception('Date is incorrect')
        new_config = driver.find_element_by_id(CE.config_select_label).get_attribute('textContent')
        if new_config != CO.new_config:
            raise Exception('Wrong config name')

        driver.find_element_by_id(CE.config_revert).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        time.sleep(1)
        if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
            raise Exception(CO.select_configuration, 'is missing')

    def test2_pc_add_empty_upcoming(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        if not Check.by_class_name_and_text(driver, CE.titlebar_panel, CO.provisioning_config_panel_title):
            raise Exception('Wrong title bar name')

        if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
            raise Exception(CO.select_configuration, 'is missing')

        start_time_disabled = driver.find_element_by_id(CE.config_start_time).get_attribute(name='aria-disabled')
        if start_time_disabled != 'true':
            raise Exception('Start time is not disabled')

        driver.find_element_by_id(CE.config_add).click()
        driver.find_element_by_id(CE.config_start_time_for_new_config)
        pop_up_title = driver.find_element_by_id(CE.config_start_time_for_new_config_title).get_attribute('textContent')
        if pop_up_title != CO.add_new_config_title:
            raise Exception('Pop-up title incorrect')
        time.sleep(1)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        if tomorrow_day[0] == '0':
            tomorrow_day = tomorrow_day[1]
            print('tomorrow_day', tomorrow_day)
        tomorrow_month_decimal = tomorrow.strftime('%m')
        if tomorrow_month_decimal[0] == '0':
            tomorrow_month_decimal = tomorrow_month_decimal[1]
            print('tomorrow_month_decimal', tomorrow_month_decimal)
        tomorrow_year = tomorrow.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_tomorrow = tomorrow_month_decimal + '/' + tomorrow_day + '/' + tomorrow_year[-2:]

        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')

        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
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
        if now_day == str(last_day_of_month[1]):
            driver.find_element_by_class_name(CE.config_date_picker_next).click()
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day, tomorrow_day)

        picker_day_to_select.click()
        new_start_time = driver.find_element_by_id(CE.config_set_new_start_time).get_attribute(name='value')
        if new_start_time != start_time_set_tomorrow:
            print('new_start_time', new_start_time, "- start_time_set_tomorrow", start_time_set_tomorrow)
            raise Exception('Date is incorrect')

        driver.find_element_by_id(CE.config_start_time_ok_button).click()
        time.sleep(2)
        sets_start_time = driver.find_element_by_id(CE.config_start_time).get_attribute(name='value')
        if sets_start_time != start_time_set_tomorrow:
            print('sets_start_time', sets_start_time, "- start_time_set_tomorrow", start_time_set_tomorrow)
            raise Exception('Date is incorrect')
        new_config = driver.find_element_by_id(CE.config_select_label).get_attribute('textContent')
        if new_config != CO.new_config:
            raise Exception('Wrong config name')

        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification_message = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
            if notification_message != CO.message_successfully_saved:
                raise Exception('Wrong notification message')
            if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
                raise Exception(CO.select_configuration, 'is missing')

    def test3_pc_delete_upcoming(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        if not Check.by_class_name_and_text(driver, CE.titlebar_panel, CO.provisioning_config_panel_title):
            raise Exception('Wrong title bar name')

        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
            Check.select_config(driver, wait, CO.upcoming_config)
            time.sleep(1)

            # Delete config
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(5)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            time.sleep(1)
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
                if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
                    raise Exception(CO.select_configuration, 'is missing')
        else:
            raise Exception('Less than two Config items')


class ProvisioningConfig02Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        pass

    def test1_pc_add_first_certificate(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        Check.start_create_config(driver, datetime, calendar, time)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(2)

        # Notification check 1
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.certificate_missing_name):
                raise Exception('Wrong notification message')
        # End

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        data_file_upload = 0
        while data_file_upload < 2:
            time.sleep(1)
            element = driver.find_element_by_id(CE.config_cert_select_file)
            element.send_keys(address)
            file_name = 'in_app_proxy_cert'
            upload_file_name = driver.find_element_by_css_selector(CE.config_cert_upload_file_name).\
                get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')
            file_size = '2.5 KB'
            upload_file_size = driver.find_element_by_css_selector(CE.config_cert_upload_file_size).\
                get_attribute('textContent')
            if upload_file_size != file_size:
                raise Exception('The selected file has wrong size')
            if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 1:
                raise Exception('Progress bar is missing')
            Check.by_class_name_and_text(driver, CE.config_buttons, CO.ui_button)
            driver.find_element_by_id(CE.config_cert_false_uploaded)
            cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
            if CO.ui_state_disabled not in cert_type_class:
                raise Exception(CO.ui_state_disabled, 'not found')
            cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
            if CO.ui_state_disabled not in cert_pass_class:
                raise Exception(CO.ui_state_disabled, 'not found')

            if data_file_upload == 0:
                data_file_upload += 1
                # Select Cancel
                driver.find_element_by_xpath(CE.config_cert_cancel_upload).click()
                driver.find_element_by_id(CE.config_cert_false_uploaded)
                cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
                if CO.ui_state_disabled not in cert_type_class:
                    raise Exception(CO.ui_state_disabled, 'not found')
                cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
                if CO.ui_state_disabled not in cert_pass_class:
                    raise Exception(CO.ui_state_disabled, 'not found')
            else:
                data_file_upload += 1
                # Select upload
                Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
                driver.find_element_by_id(CE.config_cert_true_uploaded)

        if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 0:
            raise Exception('Progress bar is exist')
        cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
        if CO.ui_state_disabled in cert_type_class:
            raise Exception(CO.ui_state_disabled, 'is found')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoTest_' + time_for_name)
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != CO.select_type:
            raise Exception('Certificate type contain wrong information')
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        driver.find_element_by_id(CE.config_cert_select_type_list)
        Check.by_id_and_text(driver, CE.config_cert_type_item_1, 'der').click()
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != 'der':
            raise Exception('Certificate type contain wrong information')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        driver.find_element_by_id(CE.config_cert_select_type_list)
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != 'p12':
            raise Exception('Certificate type contain wrong information')
        time.sleep(1)
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'is found')
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()

        # Verify Certificate Added
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != 'AutoTest_' + time_for_name:
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'p12':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 != 'cert_pass_' + time_for_name:
            raise Exception('Wrong password')

    def test2_pc_add_second_certificate(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        Check.start_create_config(driver, datetime, calendar, time)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        data_file_upload = 0
        while data_file_upload < 2:
            time.sleep(1)
            element = driver.find_element_by_id(CE.config_cert_select_file)
            element.send_keys(address)
            file_name = 'in_app_proxy_cert'
            upload_file_name = driver.find_element_by_css_selector(CE.config_cert_upload_file_name).\
                get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')
            file_size = '2.5 KB'
            upload_file_size = driver.find_element_by_css_selector(CE.config_cert_upload_file_size).\
                get_attribute('textContent')
            if upload_file_size != file_size:
                raise Exception('The selected file has wrong size')
            if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 1:
                raise Exception('Progress bar is missing')
            Check.by_class_name_and_text(driver, CE.config_buttons, CO.ui_button)
            driver.find_element_by_id(CE.config_cert_false_uploaded)
            cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
            if CO.ui_state_disabled not in cert_type_class:
                raise Exception(CO.ui_state_disabled, 'not found')
            cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
            if CO.ui_state_disabled not in cert_pass_class:
                raise Exception(CO.ui_state_disabled, 'not found')

            if data_file_upload == 0:
                data_file_upload += 1
                # Select Cancel
                driver.find_element_by_xpath(CE.config_cert_cancel_upload).click()
                driver.find_element_by_id(CE.config_cert_false_uploaded)
                cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
                if CO.ui_state_disabled not in cert_type_class:
                    raise Exception(CO.ui_state_disabled, 'not found')
                cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
                if CO.ui_state_disabled not in cert_pass_class:
                    raise Exception(CO.ui_state_disabled, 'not found')
            else:
                data_file_upload += 1
                # Select upload
                Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
                driver.find_element_by_id(CE.config_cert_true_uploaded)

        if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 0:
            raise Exception('Progress bar is exist')
        cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
        if CO.ui_state_disabled in cert_type_class:
            raise Exception(CO.ui_state_disabled, 'is found')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoTest_' + time_for_name)
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != CO.select_type:
            raise Exception('Certificate type contain wrong information')
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        driver.find_element_by_id(CE.config_cert_select_type_list)
        Check.by_id_and_text(driver, CE.config_cert_type_item_1, 'der').click()
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != 'der':
            raise Exception('Certificate type contain wrong information')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        time.sleep(1)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(3)
        # Verify Certificate Added
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != 'AutoTest_' + time_for_name:
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'der':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 is not '':
            print('table_password_0', table_password_0)
            raise Exception('Password field is not empty')

    def test3_pc_add_third_certificate(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        Check.start_create_config(driver, datetime, calendar, time)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 0:
            raise Exception('Progress bar is exist')
        cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_type_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoTest_' + time_for_name)
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != CO.select_type:
            raise Exception('Certificate type contain wrong information')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        time.sleep(1)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(3)
        # Verify Certificate Added
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != 'AutoTest_' + time_for_name:
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_x_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != '':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 is not '':
            print('table_password_0', table_password_0)
            raise Exception('Password field is not empty')

        # Add gateway

        # Add service

        time.sleep(1)

    def test4_pc_add_multiple_certificates(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        Check.start_create_config(driver, datetime, calendar, time)
        time.sleep(2)

        # Add certificates
        certs = 1
        while certs < 5:
            time.sleep(3)
            print(certs)
            driver.find_element_by_id(CE.config_add_certificate).click()
            time.sleep(2)

            address = files_path + "\in_app_proxy_cert"
            element = driver.find_element_by_id(CE.config_cert_select_file)
            element.send_keys(address)
            time.sleep(1)
            # Select upload
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
            wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
            driver.find_element_by_id(CE.config_cert_true_uploaded)
            driver.find_element_by_id(CE.config_cert_name).send_keys('AutoTest_cert_' + str(certs))

            if certs < 3:
                driver.find_element_by_id(CE.config_cert_type_drop_down).click()
                Check.by_id_and_text(driver, CE.config_cert_type_item_1, 'der').click()
                time.sleep(1)
                driver.find_element_by_id(CE.config_cert_save_changes).click()
                certs += 1
            elif certs < 5:
                driver.find_element_by_id(CE.config_cert_type_drop_down).click()
                Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
                time.sleep(1)
                driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + str(certs))
                driver.find_element_by_id(CE.config_cert_save_changes).click()
                certs += 1
        while 4 < certs < 7:
            time.sleep(3)
            print(certs)
            driver.find_element_by_id(CE.config_add_certificate).click()
            time.sleep(1)
            driver.find_element_by_id(CE.config_cert_name).send_keys('AutoTest_' + 'cert_' + str(certs))
            driver.find_element_by_id(CE.config_cert_save_changes).click()
            certs += 1

        # Verify Certificate Added
        cert_srting = 0
        while cert_srting <= 5:
            cert_table_data_name = 'form:certificatesTable:' + str(cert_srting) + ':certificateName'
            cert_table_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_srting + 1) + ') > td:nth-child(2) > img'
            cert_table_data_type = 'form:certificatesTable:' + str(cert_srting) + ':certificateType'
            cert_table_data_password = 'form:certificatesTable:' + str(cert_srting) + ':certificatePassword'
            table_name = 'AutoTest_cert_' + str(cert_srting + 1)
            if cert_srting < 2:
                time.sleep(1)
                cert_srting += 1
                table_name_n = driver.find_element_by_id(cert_table_data_name).get_attribute('textContent')
                if table_name_n != table_name:
                    raise Exception('Name is wrong or missing', table_name_n, '!=', table_name)
                table_uploaded_n = driver.find_element_by_css_selector(cert_table_data_img).get_attribute("outerHTML")
                if CO.table_ok_mark not in table_uploaded_n:
                    raise Exception('Wrong mark img')
                table_cert_type_n = driver.find_element_by_id(cert_table_data_type).get_attribute('textContent')
                if table_cert_type_n != 'der':
                    raise Exception('Wrong type')
                table_password_n = driver.find_element_by_id(cert_table_data_password).get_attribute('textContent')
                if table_password_n != '':
                    raise Exception('Wrong password')
            elif 1 < cert_srting < 4:
                cert_srting += 1
                table_name_n = driver.find_element_by_id(cert_table_data_name).get_attribute('textContent')
                if table_name_n != table_name:
                    raise Exception('Name is wrong or missing', table_name_n, '!=', table_name)
                table_uploaded_n = driver.find_element_by_css_selector(cert_table_data_img).get_attribute("outerHTML")
                if CO.table_ok_mark not in table_uploaded_n:
                    raise Exception('Wrong mark img')
                table_cert_type_n = driver.find_element_by_id(cert_table_data_type).get_attribute('textContent')
                if table_cert_type_n != 'p12':
                    raise Exception('Wrong type')
                table_password_n = driver.find_element_by_id(cert_table_data_password).get_attribute('textContent')
                if table_password_n != 'cert_pass_' + str(cert_srting):
                    raise Exception('Wrong password')

            elif 3 < cert_srting < 6:
                cert_srting += 1
                table_name_n = driver.find_element_by_id(cert_table_data_name).get_attribute('textContent')
                if table_name_n != table_name:
                    raise Exception('Name is wrong or missing', table_name_n, '!=', table_name)
                table_uploaded_n = driver.find_element_by_css_selector(cert_table_data_img).get_attribute("outerHTML")
                if CO.table_x_mark not in table_uploaded_n:
                    raise Exception('Wrong mark img')
                table_cert_type_n = driver.find_element_by_id(cert_table_data_type).get_attribute('textContent')
                if table_cert_type_n != '':
                    raise Exception('Wrong type')
                table_password_n = driver.find_element_by_id(cert_table_data_password).get_attribute('textContent')
                if table_password_n != '':
                    raise Exception('Wrong password')

        time.sleep(1)

    def test5_pc_add_certificate_and_gateway(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        Check.start_create_config(driver, datetime, calendar, time)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        # wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_select_file)))
        time.sleep(2)
        element = driver.find_element_by_id(CE.config_cert_select_file)
        element.send_keys(address)

        # Select upload
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
        driver.find_element_by_id(CE.config_cert_true_uploaded)

        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoCert_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_cert_password)))
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(1)

        # Add Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))

        # Notification check 1
        driver.find_element_by_id(CE.config_gateway_save).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_missing_name):
                raise Exception('Wrong notification message')
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_missing_client):
                raise Exception('Wrong notification message')
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_missing_trust):
                raise Exception('Wrong notification message')
        # End

        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('AutoGateway_' + time_for_name)
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != CO.gateway_select_type:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != CO.gateway_select_type:
            raise Exception('Wrong Trust dropdown')
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != 'AutoCert_' + time_for_name:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != 'AutoCert_' + time_for_name:
            raise Exception('Wrong Trust dropdown')

        # Notification check 2
        time.sleep(2)
        driver.find_element_by_id(CE.config_gateway_port).send_keys('wrong')
        driver.find_element_by_id(CE.config_gateway_save).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_invalid_format):
                print(driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent'))
                raise Exception('Wrong notification message')
        driver.find_element_by_id(CE.config_gateway_port).clear()
        # End

        driver.find_element_by_id(CE.config_gateway_port).send_keys('6666')
        driver.find_element_by_id(CE.config_gateway_host).send_keys('AutoHost_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_save).click()

        # Verify Gateway Added
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != 'AutoGateway_' + time_for_name:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != 'AutoCert_' + time_for_name:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != 'AutoCert_' + time_for_name:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '6666':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != 'AutoHost_' + time_for_name:
            raise Exception('Wrong gateway host', gateway_host)

        now = datetime.datetime.now()
        time_for_name_2 = now.strftime('D%d_H%H_M%M_S%S')

        # Add second Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))

        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('AutoGateway_' + time_for_name)
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != CO.gateway_select_type:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != CO.gateway_select_type:
            raise Exception('Wrong Trust dropdown')
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != 'AutoCert_' + time_for_name:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != 'AutoCert_' + time_for_name:
            raise Exception('Wrong Trust dropdown')

        driver.find_element_by_id(CE.config_gateway_port).send_keys('12388')
        driver.find_element_by_id(CE.config_gateway_host).send_keys('AutoHost_' + time_for_name_2)

        # Notification check 1
        driver.find_element_by_id(CE.config_gateway_save).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_already_exists):
                raise Exception('Wrong notification message')
        # End

        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).clear()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('AutoGateway_' + time_for_name_2)
        time.sleep(2)
        driver.find_element_by_id(CE.config_gateway_save).click()
        time.sleep(1)

        # Verify Gateway Added 2
        gateway_name = driver.find_element_by_id(CE.gateway_table_1_name).get_attribute('textContent')
        if gateway_name != 'AutoGateway_' + time_for_name_2:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_1_client).get_attribute('textContent')
        if gateway_client != 'AutoCert_' + time_for_name:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_1_trust).get_attribute('textContent')
        if gateway_trust != 'AutoCert_' + time_for_name:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_1_port).get_attribute('textContent')
        if gateway_port != '12388':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_1_host).get_attribute('textContent')
        if gateway_host != 'AutoHost_' + time_for_name_2:
            raise Exception('Wrong gateway host', gateway_host)

    def test6_pc_add_certificate_gateway_and_service(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        now = datetime.datetime.now()

        Check.start_create_config(driver, datetime, calendar, time)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        time.sleep(2)
        element = driver.find_element_by_id(CE.config_cert_select_file)
        element.send_keys(address)

        # Select upload
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
        driver.find_element_by_id(CE.config_cert_true_uploaded)
        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoCert_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_cert_password)))
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(1)

        # Add Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))
        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('AutoGateway_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_port).send_keys('1889')
        driver.find_element_by_id(CE.config_gateway_host).send_keys('AutoHost_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_save).click()

        service_count = 0
        while service_count <= 3:
            now = datetime.datetime.now()
            print('now time while', now)
            print('service_count', service_count)
            time_for_name = now.strftime('D%d_H%H_M%M_S%S')

            if service_count == 0:
                # Add Service 1 - empty
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                time.sleep(1)
                driver.find_element_by_id(CE.config_add_service).click()

                # Notification check 1
                time.sleep(3)
                driver.find_element_by_id(CE.config_service_save).click()
                if driver.find_elements_by_class_name(CE.main_notification_title):
                    if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.service_missing_name):
                        print(driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent'))
                        raise Exception('Wrong notification message')
                # End

                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('AutoService_' + time_for_name)
                driver.find_element_by_id(CE.config_service_save).click()
                time.sleep(1)

                # Verify Service Added 1
                service_name_1 = driver.find_element_by_css_selector(
                    Check.service_name(service_count)).get_attribute('textContent')
                service_value_1 = driver.find_element_by_css_selector(
                    Check.service_values(service_count)).get_attribute('textContent')
                if service_name_1 != 'AutoService_' + time_for_name:
                    raise Exception('Wrong Service name:', service_name_1)
                if service_value_1 != '':
                    print('service_value_1')
                    raise Exception('Wrong service values information:', service_value_1)

                # Add Service 2 - same name with error
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                time.sleep(1)
                driver.find_element_by_id(CE.config_add_service).click()
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('AutoService_' + time_for_name)
                driver.find_element_by_id(CE.config_service_save).click()

                # Notification check 2
                if driver.find_elements_by_class_name(CE.main_notification_title):
                    if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.service_name_already_exists):
                        raise Exception('Wrong notification message')
                # End

                driver.find_element_by_id(CE.config_service_cancel).click()

                service_count += 1
            elif service_count == 1:
                # Add Service 3 - gateway
                time.sleep(2)
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                driver.find_element_by_id(CE.config_add_service).click()
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('AutoService_' + time_for_name)

                driver.find_element_by_id(CE.config_service_select_gateway).click()
                driver.find_element_by_id(CE.config_service_select_gateway_list)
                driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
                time.sleep(1)
                service_client_dd = driver.find_element_by_id(
                    CE.config_service_select_gateway_list).get_attribute('textContent')
                if 'AutoGateway_' not in service_client_dd:
                    print('service_client_dd', service_client_dd)
                    raise Exception('Wrong Service dropdown')
                driver.find_element_by_id(CE.config_service_save).click()
                time.sleep(2)

                # Verify Service Added 2
                service_name_1 = driver.find_element_by_css_selector(
                    Check.service_name(service_count)).get_attribute('textContent')
                service_value_gate_1 = driver.find_element_by_css_selector(
                    Check.service_value_string_name(service_count)).get_attribute('textContent')
                service_value_gate_name_1 = driver.find_element_by_css_selector(
                    Check.service_value_string_value(service_count)).get_attribute('textContent')

                if service_name_1 != 'AutoService_' + time_for_name:
                    raise Exception('Wrong Service name:', service_name_1)
                if service_value_gate_1 != 'gate':
                    raise Exception('Wrong service value gate information')
                if 'AutoGateway_' not in service_value_gate_name_1:
                    raise Exception('Wrong service value gate name information')

                service_count += 1
            elif service_count == 2:
                # Add Service 4 - property
                time.sleep(2)
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                driver.find_element_by_id(CE.config_add_service).click()
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('AutoService_' + time_for_name)
                driver.find_element_by_id(CE.config_service_add_button).click()
                driver.find_element_by_id(CE.config_service_add_dialog)
                driver.find_element_by_id(CE.config_service_add_select).click()
                Check.by_class_name_and_text(driver, CE.menu_list_item, 'get').click()
                # driver.find_element_by_id('addServiceEntryDlgForm:j_idt125_4').click()
                add_select_label = driver.find_element_by_id(
                    CE.config_service_add_select_label).get_attribute('textContent')
                if add_select_label != 'get':
                    print('add_select_label', add_select_label)
                    raise Exception('Wrong select label')
                driver.find_element_by_css_selector(CE.config_service_add_value_close).click()
                time.sleep(1)
                detail_property_value = driver.find_element_by_id(
                    CE.config_service_property_values).get_attribute('textContent')
                if detail_property_value != CO.config_service_property_values_no_records:
                    print('detail_property_value', detail_property_value)
                    raise Exception('Wrong property values')
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_add_button).click()
                driver.find_element_by_id(CE.config_service_add_dialog)
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_add_select).click()
                Check.by_class_name_and_text(driver, CE.menu_list_item, 'get').click()
                add_select_label = driver.find_element_by_id(
                    CE.config_service_add_select_label).get_attribute('textContent')
                if add_select_label != 'get':
                    print('add_select_label', add_select_label)
                    raise Exception('Wrong select label')
                driver.find_element_by_id(CE.config_service_add_ok).click()
                time.sleep(1)
                detail_property_value = driver.find_element_by_css_selector(
                    CE.details_value_property_name).get_attribute('textContent')
                if detail_property_value != 'get':
                    print('detail_property_value', detail_property_value)
                    raise Exception('Wrong property value name')
                driver.find_element_by_css_selector(CE.config_service_detail_property_value).click()
                driver.find_element_by_css_selector(
                    CE.config_service_detail_property_value).send_keys('AutoProperty_' + str(service_count))
                driver.find_element_by_id(CE.config_service_detail_delete_action).click()

                # Notification check 1
                if driver.find_elements_by_class_name(CE.main_notification_title):
                    if not Check.by_class_name_and_text(driver, CE.main_notification_title,
                                                        CO.service_property_successfully_deleted):
                        raise Exception('Wrong notification message')
                # End

                driver.find_element_by_id(CE.config_service_add_button).click()
                driver.find_element_by_id(CE.config_service_add_dialog)
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_add_select).click()
                Check.by_class_name_and_text(driver, CE.menu_list_item, 'get').click()
                add_select_label = driver.find_element_by_id(
                    CE.config_service_add_select_label).get_attribute('textContent')
                if add_select_label != 'get':
                    print('add_select_label', add_select_label)
                    raise Exception('Wrong select label')
                driver.find_element_by_id(CE.config_service_add_ok).click()
                time.sleep(1)
                detail_property_value = driver.find_element_by_css_selector(
                    CE.details_value_property_name).get_attribute('textContent')
                if detail_property_value != 'get':
                    print('detail_property_value', detail_property_value)
                    raise Exception('Wrong property value name')
                driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
                driver.find_element_by_xpath(
                    CE.config_service_detail_property_value).send_keys('AutoProperty_' + str(service_count))
                driver.find_element_by_id(CE.config_service_save).click()
                time.sleep(1)

                # Verify Service Added 2
                service_name_1 = driver.find_element_by_css_selector(
                    Check.service_name(service_count)).get_attribute('textContent')
                service_value_property_name_1 = driver.find_element_by_css_selector(
                    Check.service_value_string_name(service_count)).get_attribute('textContent')
                service_value_property_value_1 = driver.find_element_by_css_selector(
                    Check.service_value_string_value(service_count)).get_attribute('textContent')

                if service_name_1 != 'AutoService_' + time_for_name:
                    raise Exception('Wrong Service name:', service_name_1)
                if service_value_property_name_1 != 'get':
                    raise Exception('Wrong service property name information')
                if service_value_property_value_1 != 'AutoProperty_' + str(service_count):
                    raise Exception('Wrong service property value information')
                service_count += 1
            elif service_count == 3:
                # Add Service 5 - gate and property
                time.sleep(2)
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                driver.find_element_by_id(CE.config_add_service).click()
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('AutoService_' + time_for_name)
                driver.find_element_by_id(CE.config_service_add_button).click()
                driver.find_element_by_id(CE.config_service_add_dialog)
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_add_select).click()
                Check.by_class_name_and_text(driver, CE.menu_list_item, 'path').click()
                add_select_label = driver.find_element_by_id(
                    CE.config_service_add_select_label).get_attribute('textContent')
                if add_select_label != 'path':
                    print('add_select_label', add_select_label)
                    raise Exception('Wrong select label')
                driver.find_element_by_id(CE.config_service_add_ok).click()
                time.sleep(1)
                detail_property_value = driver.find_element_by_css_selector(
                    CE.details_value_property_name).get_attribute('textContent')
                if detail_property_value != 'path':
                    print('detail_property_value', detail_property_value)
                    raise Exception('Wrong property value name')
                driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
                driver.find_element_by_xpath(
                    CE.config_service_detail_property_value).send_keys('AutoProperty_' + str(service_count))
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_select_gateway).click()
                driver.find_element_by_id(CE.config_service_select_gateway_list)
                driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
                time.sleep(1)
                service_client_dd = driver.find_element_by_id(
                    CE.config_service_select_gateway_list).get_attribute('textContent')
                if 'AutoGateway_' not in service_client_dd:
                    print('service_client_dd', service_client_dd)
                    raise Exception('Wrong Service dropdown')
                driver.find_element_by_id(CE.config_service_save).click()
                time.sleep(1)

                # Verify Service Added 1
                service_name_1 = driver.find_element_by_css_selector(
                    Check.service_name(service_count)).get_attribute('textContent')
                service_value_property = driver.find_element_by_css_selector(
                    Check.service_value_property_2(service_count)).get_attribute('textContent')
                service_value_property_value = driver.find_element_by_css_selector(
                    Check.service_value_property_value_2(service_count)).get_attribute('textContent')
                service_value_gate = driver.find_element_by_css_selector(
                    Check.service_value_property_1(service_count)).get_attribute('textContent')
                service_value_gate_name = driver.find_element_by_css_selector(
                    Check.service_value_property_value_1(service_count)).get_attribute('textContent')
                if service_name_1 != 'AutoService_' + time_for_name:
                    raise Exception('Wrong Service name:', service_name_1)
                if service_value_property != 'path':
                    raise Exception('Wrong service property name information:', service_value_property)
                if service_value_property_value != 'AutoProperty_' + str(service_count):
                    raise Exception('Wrong service property value information:', service_value_property_value)
                if service_value_gate != 'gate':
                    raise Exception('Wrong service value gate information:', service_value_gate)
                if 'AutoGateway_' not in service_value_gate_name:
                    raise Exception('Wrong service value gate name information:', service_value_gate_name)
                service_count += 1


class ProvisioningConfig03Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')

        driver = cls.driver
        config = driver.find_element_by_id(CE.config_select_label).get_attribute('textContent')

        print('Check.select_config(driver, wait, CO.upcoming_config)', Check.select_config(driver, wait, CO.upcoming_config))
        if Check.select_config(driver, wait, CO.upcoming_config):
            if config != CO.upcoming_config:
                # Select config
                wait = WebDriverWait(driver, 15)
                if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
                    driver.find_element_by_id(CE.config_select_label).click()
                if not driver.find_element_by_id(CE.config_select_list):
                    raise Exception('The list of configs is missing')
                Check.select_config(driver, wait, CO.upcoming_config)

            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)

            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            time.sleep(1)
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(
                    CE.main_notification_title).get_attribute('textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
                if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
                    raise Exception(CO.select_configuration, 'is missing')

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        driver = cls.driver
        wait = WebDriverWait(driver, 15)
        config = driver.find_element_by_id(CE.config_select_label).get_attribute('textContent')
        if Check.select_config(driver, wait, CO.upcoming_config):
            if config != CO.upcoming_config:
                # Select config
                if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
                    driver.find_element_by_id(CE.config_select_label).click()
                if not driver.find_element_by_id(CE.config_select_list):
                    raise Exception('The list of configs is missing')
                Check.select_config(driver, wait, CO.upcoming_config)

            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            time.sleep(1)
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(
                    CE.main_notification_title).get_attribute('textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
                if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
                    raise Exception(CO.select_configuration, 'is missing')
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        pass

    def test1_pc_add_upcoming_with_content(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        Check.start_create_config(driver, datetime, calendar, time)

        time_for_name = self.time_for_name

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        time.sleep(2)
        element = driver.find_element_by_id(CE.config_cert_select_file)
        element.send_keys(address)

        # Select upload
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
        driver.find_element_by_id(CE.config_cert_true_uploaded)
        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoCert_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_cert_password)))
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(1)

        # Add Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))
        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('AutoGateway_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_port).send_keys('1889')
        driver.find_element_by_id(CE.config_gateway_host).send_keys('AutoHost_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_save).click()

        # Add Service
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
        driver.find_element_by_id(CE.config_add_service).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).send_keys('AutoService_' + time_for_name)
        driver.find_element_by_id(CE.config_service_add_button).click()
        driver.find_element_by_id(CE.config_service_add_dialog)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_add_select).click()
        Check.by_class_name_and_text(driver, CE.menu_list_item, 'path').click()
        add_select_label = driver.find_element_by_id(
            CE.config_service_add_select_label).get_attribute('textContent')
        if add_select_label != 'path':
            print('add_select_label', add_select_label)
            raise Exception('Wrong select label')
        driver.find_element_by_id(CE.config_service_add_ok).click()
        time.sleep(1)
        detail_property_value = driver.find_element_by_css_selector(
            CE.details_value_property_name).get_attribute('textContent')
        if detail_property_value != 'path':
            print('detail_property_value', detail_property_value)
            raise Exception('Wrong property value name')
        driver.find_element_by_css_selector(CE.config_service_detail_property_value).click()
        driver.find_element_by_css_selector(
            CE.config_service_detail_property_value).send_keys('AutoProperty_' + time_for_name)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_select_gateway).click()
        driver.find_element_by_id(CE.config_service_select_gateway_list)
        driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
        time.sleep(1)
        service_client_dd = driver.find_element_by_id(
            CE.config_service_select_gateway_list).get_attribute('textContent')
        if 'AutoGateway_' not in service_client_dd:
            print('service_client_dd', service_client_dd)
            raise Exception('Wrong Service dropdown')
        driver.find_element_by_id(CE.config_service_save).click()
        time.sleep(1)

        # Save config
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification_message = driver.find_element_by_class_name(
                CE.main_notification_title).get_attribute('textContent')
            if notification_message != CO.message_successfully_saved:
                raise Exception('Wrong notification message')
            if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
                raise Exception(CO.select_configuration, 'is missing')
        time.sleep(1)

    def test2_pc_verify_upcoming(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        time_for_name = self.time_for_name

        # Select config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)
        time.sleep(2)

        # Verify config
        # Verify Certificate
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != 'AutoCert_' + time_for_name:
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'p12':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 != 'cert_pass_' + time_for_name:
            raise Exception('Wrong password')

        # Verify Gateway
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != 'AutoGateway_' + time_for_name:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != 'AutoCert_' + time_for_name:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != 'AutoCert_' + time_for_name:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '1889':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != 'AutoHost_' + time_for_name:
            raise Exception('Wrong gateway host', gateway_host)

        # Verify Service
        service_count = 0
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_count)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_count)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_count)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_count)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_count)).get_attribute('textContent')
        if service_name_1 != 'AutoService_' + time_for_name:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != 'path':
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != 'AutoProperty_' + time_for_name:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if 'AutoGateway_' not in service_value_gate_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

    def test3_pc_add_to_upcoming_and_revert(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)
        now = self.now - datetime.timedelta(days=1)
        time_for_name = now.strftime('D%d_H%H_M%M_S%S')
        print('time_for_name', time_for_name)
        time_for_name_2 = self.time_for_name
        print('time_for_name_2', time_for_name_2)
        auto_name = '0_Auto'
        auto_name_2 = 'Auto'

        # Select config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        time.sleep(2)
        element = driver.find_element_by_id(CE.config_cert_select_file)
        element.send_keys(address)

        # Select upload
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
        driver.find_element_by_id(CE.config_cert_true_uploaded)
        driver.find_element_by_id(CE.config_cert_name).send_keys(auto_name + 'Cert_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_cert_password)))
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(1)

        # Add Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))
        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys(auto_name + 'Gateway_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_port).send_keys('1984')
        driver.find_element_by_id(CE.config_gateway_host).send_keys(auto_name + 'Host_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_save).click()

        # Add Service
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
        driver.find_element_by_id(CE.config_add_service).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).send_keys(auto_name + 'Service_' + time_for_name)
        driver.find_element_by_id(CE.config_service_add_button).click()
        driver.find_element_by_id(CE.config_service_add_dialog)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_add_select).click()
        Check.by_class_name_and_text(driver, CE.menu_list_item, 'root').click()
        add_select_label = driver.find_element_by_id(
            CE.config_service_add_select_label).get_attribute('textContent')
        if add_select_label != 'root':
            print('add_select_label', add_select_label)
            raise Exception('Wrong select label')
        driver.find_element_by_id(CE.config_service_add_ok).click()
        time.sleep(1)
        detail_property_value = driver.find_element_by_css_selector(
            CE.details_value_property_name).get_attribute('textContent')
        if detail_property_value != 'root':
            print('detail_property_value', detail_property_value)
            raise Exception('Wrong property value name')
        driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
        driver.find_element_by_xpath(
            CE.config_service_detail_property_value).send_keys(auto_name +'Property_' + time_for_name)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_select_gateway).click()
        driver.find_element_by_id(CE.config_service_select_gateway_list)
        driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
        time.sleep(1)
        service_client_dd = driver.find_element_by_id(
            CE.config_service_select_gateway_list).get_attribute('textContent')
        if auto_name + 'Gateway_' not in service_client_dd:
            print('service_client_dd', service_client_dd)
            raise Exception('Wrong Service dropdown')
        driver.find_element_by_id(CE.config_service_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
        time.sleep(1)

        # Verify config
        # Verify Certificate 1
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != auto_name + 'Cert_' + time_for_name:
            print('table_name_0', table_name_0)
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'p12':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 != 'cert_pass_' + time_for_name:
            raise Exception('Wrong password')

        # Verify Gateway 1
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != auto_name + 'Gateway_' + time_for_name:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != auto_name + 'Cert_' + time_for_name:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != auto_name + 'Cert_' + time_for_name:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '1984':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != auto_name + 'Host_' + time_for_name:
            raise Exception('Wrong gateway host', gateway_host)

        # Verify Service 1
        service_count = 0
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_count)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_count)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_count)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_count)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_count)).get_attribute('textContent')
        if service_name_1 != auto_name + 'Service_' + time_for_name:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != 'root':
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != auto_name + 'Property_' + time_for_name:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if auto_name + 'Gateway_' not in service_value_gate_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Verify Certificate 2
        table_name_1 = driver.find_element_by_id(CE.cert_table_1_data_name).get_attribute('textContent')
        if table_name_1 != auto_name_2 + 'Cert_' + time_for_name_2:
            print('table_name_1', table_name_1)
            raise Exception('Name is wrong or missing')

        table_uploaded_1 = driver.find_element_by_css_selector(CE.cert_table_1_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_1:
            raise Exception('Wrong mark img')
        table_cert_type_1 = driver.find_element_by_id(CE.cert_table_1_data_type).get_attribute('textContent')
        if table_cert_type_1 != 'p12':
            raise Exception('Wrong type')

        table_password_1 = driver.find_element_by_id(CE.cert_table_1_data_password).get_attribute('textContent')
        if table_password_1 != 'cert_pass_' + time_for_name_2:
            raise Exception('Wrong password')

        # Verify Gateway 2
        gateway_name = driver.find_element_by_id(CE.gateway_table_1_name).get_attribute('textContent')
        if gateway_name != auto_name_2 + 'Gateway_' + time_for_name_2:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_1_client).get_attribute('textContent')
        if gateway_client != auto_name_2 + 'Cert_' + time_for_name_2:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_1_trust).get_attribute('textContent')
        if gateway_trust != auto_name_2 + 'Cert_' + time_for_name_2:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_1_port).get_attribute('textContent')
        if gateway_port != '1889':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_1_host).get_attribute('textContent')
        if gateway_host != auto_name_2 + 'Host_' + time_for_name_2:
            raise Exception('Wrong gateway host', gateway_host)

        # Verify Service 2
        service_count = 1
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_count)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_count)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_count)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_count)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_count)).get_attribute('textContent')
        if service_name_1 != auto_name_2 + 'Service_' + time_for_name_2:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != 'path':
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != auto_name_2 + 'Property_' + time_for_name_2:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if auto_name_2 + 'Gateway_' not in service_value_gate_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Revert changes
        driver.find_element_by_id(CE.config_revert).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        # Select config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)


        # Verify config 2
        # Verify Certificate 3
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != auto_name_2 + 'Cert_' + time_for_name_2:
            print('table_name_0', table_name_0)
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'p12':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 != 'cert_pass_' + time_for_name_2:
            raise Exception('Wrong password')

        # Verify Gateway 3
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != auto_name_2 + 'Gateway_' + time_for_name_2:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != auto_name_2 +'Cert_' + time_for_name_2:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != auto_name_2 + 'Cert_' + time_for_name_2:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '1889':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != auto_name_2 + 'Host_' + time_for_name_2:
            raise Exception('Wrong gateway host', gateway_host)

        # Verify Service 3
        service_count = 0
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_count)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_count)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_count)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_count)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_count)).get_attribute('textContent')
        if service_name_1 != auto_name_2 + 'Service_' + time_for_name_2:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != 'path':
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != auto_name_2 + 'Property_' + time_for_name_2:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if auto_name_2 + 'Gateway_' not in service_value_gate_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

    def test4_pc_add_to_upcoming_and_save(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)
        now = self.now - datetime.timedelta(days=1)
        time_for_name = now.strftime('D%d_H%H_M%M_S%S')
        print('time_for_name', time_for_name)
        time_for_name_2 = self.time_for_name
        print('time_for_name_2', time_for_name_2)
        auto_name = '0_Auto'
        auto_name_2 = 'Auto'

        # Select config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        time.sleep(2)
        element = driver.find_element_by_id(CE.config_cert_select_file)
        element.send_keys(address)

        # Select upload
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
        driver.find_element_by_id(CE.config_cert_true_uploaded)
        driver.find_element_by_id(CE.config_cert_name).send_keys(auto_name + 'Cert_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_cert_password)))
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(2)

        # Add Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))
        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys(auto_name + 'Gateway_' + time_for_name)
        time.sleep(1)
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_port).send_keys('1984')
        driver.find_element_by_id(CE.config_gateway_host).send_keys(auto_name + 'Host_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_save).click()

        # Add Service
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
        time.sleep(1)
        driver.find_element_by_id(CE.config_add_service).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).send_keys(auto_name + 'Service_' + time_for_name)
        driver.find_element_by_id(CE.config_service_add_button).click()
        driver.find_element_by_id(CE.config_service_add_dialog)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_add_select).click()
        Check.by_class_name_and_text(driver, CE.menu_list_item, 'root').click()
        add_select_label = driver.find_element_by_id(
            CE.config_service_add_select_label).get_attribute('textContent')
        if add_select_label != 'root':
            print('add_select_label', add_select_label)
            raise Exception('Wrong select label')
        driver.find_element_by_id(CE.config_service_add_ok).click()
        time.sleep(1)
        detail_property_value = driver.find_element_by_css_selector(
            CE.details_value_property_name).get_attribute('textContent')
        if detail_property_value != 'root':
            print('detail_property_value', detail_property_value)
            raise Exception('Wrong property value name')
        driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
        driver.find_element_by_xpath(
            CE.config_service_detail_property_value).send_keys(auto_name + 'Property_' + time_for_name)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_select_gateway).click()
        driver.find_element_by_id(CE.config_service_select_gateway_list)
        driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
        time.sleep(1)
        service_client_dd = driver.find_element_by_id(
            CE.config_service_select_gateway_list).get_attribute('textContent')
        if auto_name + 'Gateway_' not in service_client_dd:
            print('service_client_dd', service_client_dd)
            raise Exception('Wrong Service dropdown')
        driver.find_element_by_id(CE.config_service_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
        time.sleep(1)

        # Verify config
        # Verify Certificate 1
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != auto_name + 'Cert_' + time_for_name:
            print('table_name_0', table_name_0)
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'p12':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 != 'cert_pass_' + time_for_name:
            raise Exception('Wrong password')

        # Verify Gateway 1
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != auto_name + 'Gateway_' + time_for_name:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != auto_name + 'Cert_' + time_for_name:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != auto_name + 'Cert_' + time_for_name:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '1984':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != auto_name + 'Host_' + time_for_name:
            raise Exception('Wrong gateway host', gateway_host)

        # Verify Service 1
        service_count = 0
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_count)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_count)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_count)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_count)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_count)).get_attribute('textContent')
        if service_name_1 != auto_name + 'Service_' + time_for_name:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != 'root':
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != auto_name + 'Property_' + time_for_name:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if auto_name + 'Gateway_' not in service_value_gate_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Verify Certificate 2
        table_name_1 = driver.find_element_by_id(CE.cert_table_1_data_name).get_attribute('textContent')
        if table_name_1 != auto_name_2 + 'Cert_' + time_for_name_2:
            raise Exception('Name is wrong or missing')

        table_uploaded_1 = driver.find_element_by_css_selector(CE.cert_table_1_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_1:
            raise Exception('Wrong mark img')
        table_cert_type_1 = driver.find_element_by_id(CE.cert_table_1_data_type).get_attribute('textContent')
        if table_cert_type_1 != 'p12':
            raise Exception('Wrong type')

        table_password_1 = driver.find_element_by_id(CE.cert_table_1_data_password).get_attribute('textContent')
        if table_password_1 != 'cert_pass_' + time_for_name_2:
            raise Exception('Wrong password')

        # Verify Gateway 2
        gateway_name = driver.find_element_by_id(CE.gateway_table_1_name).get_attribute('textContent')
        if gateway_name != auto_name_2 + 'Gateway_' + time_for_name_2:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_1_client).get_attribute('textContent')
        if gateway_client != auto_name_2 + 'Cert_' + time_for_name_2:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_1_trust).get_attribute('textContent')
        if gateway_trust != auto_name_2 + 'Cert_' + time_for_name_2:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_1_port).get_attribute('textContent')
        if gateway_port != '1889':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_1_host).get_attribute('textContent')
        if gateway_host != auto_name_2 + 'Host_' + time_for_name_2:
            raise Exception('Wrong gateway host', gateway_host)

        # Verify Service 2
        service_count = 1
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_count)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_count)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_count)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_count)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_count)).get_attribute('textContent')
        if service_name_1 != auto_name_2 + 'Service_' + time_for_name_2:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != 'path':
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != auto_name_2 + 'Property_' + time_for_name_2:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if auto_name_2 + 'Gateway_' not in service_value_gate_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Apply changes
        driver.find_element_by_id(CE.config_apply).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        # Select config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)

        # Verify config 2
        # Verify Certificate 3
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != auto_name + 'Cert_' + time_for_name:
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'p12':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 != 'cert_pass_' + time_for_name:
            raise Exception('Wrong password')

        # Verify Gateway 3
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != auto_name + 'Gateway_' + time_for_name:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != auto_name + 'Cert_' + time_for_name:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != auto_name + 'Cert_' + time_for_name:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '1984':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != auto_name + 'Host_' + time_for_name:
            raise Exception('Wrong gateway host', gateway_host)

        # Verify Service 3
        service_count = 0
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_count)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_count)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_count)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_count)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_count)).get_attribute('textContent')
        if service_name_1 != auto_name + 'Service_' + time_for_name:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != 'root':
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != auto_name + 'Property_' + time_for_name:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if auto_name + 'Gateway_' not in service_value_gate_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Verify Certificate 4
        table_name_1 = driver.find_element_by_id(CE.cert_table_1_data_name).get_attribute('textContent')
        if table_name_1 != auto_name_2 + 'Cert_' + time_for_name_2:
            print('table_name_1', table_name_1)
            raise Exception('Name is wrong or missing')

        table_uploaded_1 = driver.find_element_by_css_selector(CE.cert_table_1_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_1:
            raise Exception('Wrong mark img')
        table_cert_type_1 = driver.find_element_by_id(CE.cert_table_1_data_type).get_attribute('textContent')
        if table_cert_type_1 != 'p12':
            raise Exception('Wrong type')

        table_password_1 = driver.find_element_by_id(CE.cert_table_1_data_password).get_attribute('textContent')
        if table_password_1 != 'cert_pass_' + time_for_name_2:
            raise Exception('Wrong password')

        # Verify Gateway 4
        gateway_name = driver.find_element_by_id(CE.gateway_table_1_name).get_attribute('textContent')
        if gateway_name != auto_name_2 + 'Gateway_' + time_for_name_2:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_1_client).get_attribute('textContent')
        if gateway_client != auto_name_2 + 'Cert_' + time_for_name_2:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_1_trust).get_attribute('textContent')
        if gateway_trust != auto_name_2 + 'Cert_' + time_for_name_2:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_1_port).get_attribute('textContent')
        if gateway_port != '1889':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_1_host).get_attribute('textContent')
        if gateway_host != auto_name_2 + 'Host_' + time_for_name_2:
            raise Exception('Wrong gateway host', gateway_host)

        # Verify Service 4
        service_count = 1
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_count)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_count)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_count)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_count)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_count)).get_attribute('textContent')
        if service_name_1 != auto_name_2 + 'Service_' + time_for_name_2:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != 'path':
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != auto_name_2 + 'Property_' + time_for_name_2:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if auto_name_2 + 'Gateway_' not in service_value_gate_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)


class ProvisioningConfig04Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')

        driver = cls.driver
        config = driver.find_element_by_id(CE.config_select_label).get_attribute('textContent')
        if Check.select_config(driver, wait, CO.upcoming_config):
            if config != CO.upcoming_config:
                # Select config
                wait = WebDriverWait(driver, 15)
                if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
                    driver.find_element_by_id(CE.config_select_label).click()
                if not driver.find_element_by_id(CE.config_select_list):
                    raise Exception('The list of configs is missing')
                Check.select_config(driver, wait, CO.upcoming_config)

            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            time.sleep(1)
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(
                    CE.main_notification_title).get_attribute('textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
                if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
                    raise Exception(CO.select_configuration, 'is missing')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        pass

    def test1_pc_upload_config_revert(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        address = files_path + r"\test_cert.json"
        print(address, address)
        time.sleep(1)
        element = driver.find_element_by_id(CE.config_select_file)
        element.send_keys(address)
        file_name = 'test_cert.json'
        upload_file_name = driver.find_element_by_class_name(CE.file_name_for_upload).\
            get_attribute('textContent')
        if upload_file_name != file_name:
            raise Exception('The selected file has wrong name')
        driver.find_element_by_id(CE.config_upload).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
            if CO.upload_config_do_not_forget not in notification:
                print('notification', notification)
                raise Exception('Wrong notification message')

        time.sleep(1)
        if not Check.by_id_and_value(driver, CE.config_start_time, '1/12/19'):
            raise Exception('Wrong date')

        # Verify Config
        cert_name_1 = 'in_app_proxy_cert'
        cert_name_2 = 'proxy_client_cert'
        cert_name_3 = 'trust_cert'
        cert_name_mod = [cert_name_1, cert_name_2, cert_name_3]
        cert_type_1 = 'p12'
        cert_type_2 = 'p12'
        cert_type_3 = 'der'
        cert_type_mod = [cert_type_1, cert_type_2, cert_type_3]
        cert_password_1 = 'ipad_1'
        cert_password_2 = 'ipad_2'
        cert_password_3 = ''
        cert_password_mod = [cert_password_1, cert_password_2, cert_password_3]
        gateway_name_1 = 'in_app_proxy'
        gateway_name_2 = 'login'
        gateway_name_3 = 'proxy'
        gateway_name_mod = [gateway_name_1, gateway_name_2, gateway_name_3]
        client_trust_mod = [cert_name_1, cert_name_3, cert_name_2]
        gateway_port_1 = '4440'
        gateway_port_2 = '4441'
        gateway_port_3 = '4442'
        gateway_port_mod = [gateway_port_1, gateway_port_2, gateway_port_3]
        gateway_host_1 = 'dev0.e-dapt.net'
        gateway_host_2 = 'dev1.e-dapt.net'
        gateway_host_3 = 'dev2.e-dapt.net'
        gateway_host_mod = [gateway_host_1, gateway_host_2, gateway_host_3]
        service_name_1 = 'AddAttachment'
        service_name_2 = 'Configuration'
        service_name_3 = 'ContextLog'
        service_name_mod = [service_name_1, service_name_2, service_name_3]
        service_value_1_1 = 'gate'
        service_value_1_2 = 'path'
        service_gate_value_mod = [gateway_name_3, gateway_name_2, gateway_name_1]
        service_value_2_1 = '/proxy/exchange/email/addAttachment'
        service_value_2_2 = '/proxy/config/getBinaryConfig'
        service_value_2_3 = '/proxy/log/changeContext/add'
        service_property_value_mod =[service_value_2_1, service_value_2_2, service_value_2_3]

        # Verify Certificates
        certificate_row = 0
        while certificate_row <= 2:
            print('certificate_row', certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            if table_name_n != cert_name_mod[certificate_row]:
                print('table_name_n:', table_name_n, 'cert_name_mod:', cert_name_mod[certificate_row])
                raise Exception('Name is wrong or missing')
            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            if CO.table_ok_mark not in table_uploaded_n:
                raise Exception('Wrong mark img')
            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            if table_cert_type_n != cert_type_mod[certificate_row]:
                print('table_cert_type_n:', table_cert_type_n, 'cert_type_mod:', cert_type_mod[certificate_row])
                raise Exception('Wrong type')

            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            if table_password_n != cert_password_mod[certificate_row]:
                print('table_password_n:', table_password_n, 'cert_password_mod:', cert_password_mod[certificate_row])
                raise Exception('Wrong password')
            print('certificate row %s Checked' % str(certificate_row + 1))
            certificate_row += 1

        # Verify Gateways
        gateway_row = 0
        while gateway_row <= 2:
            print('gateway_row', gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            if gateway_name_n != gateway_name_mod[gateway_row]:
                print('gateway_name_n:', gateway_name_n, 'gateway_name_mod:', gateway_name_mod[gateway_row])
                raise Exception('Wrong gateway name', gateway_name_n)
            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            if gateway_client_n != client_trust_mod[gateway_row]:
                print('gateway_client_n:', gateway_client_n, 'client_trust_mod:', client_trust_mod[gateway_row])
                raise Exception('Wrong gateway client')
            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            if gateway_trust_n != client_trust_mod[gateway_row]:
                print('gateway_trust_n:', gateway_trust_n, 'client_trust_mod:', client_trust_mod[gateway_row])
                raise Exception('Wrong gateway trust')
            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            if gateway_port_n != gateway_port_mod[gateway_row]:
                print('gateway_port_n:', gateway_port_n, 'gateway_port_mod:', gateway_port_mod[gateway_row])
                raise Exception('Wrong gateway port')
            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            if gateway_host_n != gateway_host_mod[gateway_row]:
                print('gateway_host_n:', gateway_host_n, 'gateway_host_mod:', gateway_host_mod[gateway_row])
                raise Exception('Wrong gateway host')
            print('gateway row %s Checked' % str(gateway_row + 1))
            gateway_row += 1

        # Verify Services
        service_count = 0
        while service_count <= 2:
            print('service_count', service_count)

            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(service_count)).get_attribute('textContent')
            service_value_property = driver.find_element_by_css_selector(

                Check.service_value_property_2(service_count)).get_attribute('textContent')
            service_value_property_value = driver.find_element_by_css_selector(
                Check.service_value_property_value_2(service_count)).get_attribute('textContent')
            service_value_gate = driver.find_element_by_css_selector(

                Check.service_value_property_1(service_count)).get_attribute('textContent')
            service_value_gate_name = driver.find_element_by_css_selector(
                Check.service_value_property_value_1(service_count)).get_attribute('textContent')

            if service_name_n != service_name_mod[service_count]:
                print('service_name_n:', service_name_n, 'service_name_mod:', service_name_mod[service_count])
                raise Exception('Wrong Service name')

            if service_value_property != service_value_1_2:
                print('service_value_property:', service_value_property, 'service_value_1_2:', service_value_1_2)
                raise Exception('Wrong service property name information')
            if service_value_property_value != service_property_value_mod[service_count]:
                print('service_value_property_value:', service_value_property_value, 'service_property_value_mod:',
                      service_property_value_mod[service_count])
                raise Exception('Wrong service property value information')

            if service_value_gate != service_value_1_1:
                print('service_value_gate:', service_value_gate, 'service_value_1_1:', service_value_1_1)
                raise Exception('Wrong service value gate information')
            if service_value_gate_name != service_gate_value_mod[service_count]:
                print('service_value_gate_name:', service_value_gate_name, 'service_gate_value_mod:',
                      service_gate_value_mod[service_count])
                raise Exception('Wrong service value gate name information')
            print('service row %s Checked' % str(service_count + 1))
            service_count += 1

        time.sleep(1)
        driver.find_element_by_id(CE.config_revert).click()

        time.sleep(1)
        if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
            raise Exception(CO.select_configuration, 'is missing')

    def test2_pc_upload_config_apply(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        address = files_path + r"\test_cert.json"
        print(address, address)
        time.sleep(1)
        element = driver.find_element_by_id(CE.config_select_file)
        element.send_keys(address)
        file_name = 'test_cert.json'
        upload_file_name = driver.find_element_by_class_name(CE.file_name_for_upload). \
            get_attribute('textContent')
        if upload_file_name != file_name:
            raise Exception('The selected file has wrong name')
        driver.find_element_by_id(CE.config_upload).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
            if CO.upload_config_do_not_forget not in notification:
                print('notification', notification)
                raise Exception('Wrong notification message')

        time.sleep(1)
        if not Check.by_id_and_value(driver, CE.config_start_time, '1/12/19'):
            raise Exception('Wrong date')

        # Verify Config
        cert_name_1 = 'in_app_proxy_cert'
        cert_name_2 = 'proxy_client_cert'
        cert_name_3 = 'trust_cert'
        cert_name_mod = [cert_name_1, cert_name_2, cert_name_3]
        cert_type_1 = 'p12'
        cert_type_2 = 'p12'
        cert_type_3 = 'der'
        cert_type_mod = [cert_type_1, cert_type_2, cert_type_3]
        cert_password_1 = 'ipad_1'
        cert_password_2 = 'ipad_2'
        cert_password_3 = ''
        cert_password_mod = [cert_password_1, cert_password_2, cert_password_3]
        gateway_name_1 = 'in_app_proxy'
        gateway_name_2 = 'login'
        gateway_name_3 = 'proxy'
        gateway_name_mod = [gateway_name_1, gateway_name_2, gateway_name_3]
        client_trust_mod = [cert_name_1, cert_name_3, cert_name_2]
        gateway_port_1 = '4440'
        gateway_port_2 = '4441'
        gateway_port_3 = '4442'
        gateway_port_mod = [gateway_port_1, gateway_port_2, gateway_port_3]
        gateway_host_1 = 'dev0.e-dapt.net'
        gateway_host_2 = 'dev1.e-dapt.net'
        gateway_host_3 = 'dev2.e-dapt.net'
        gateway_host_mod = [gateway_host_1, gateway_host_2, gateway_host_3]
        service_name_1 = 'AddAttachment'
        service_name_2 = 'Configuration'
        service_name_3 = 'ContextLog'
        service_name_mod = [service_name_1, service_name_2, service_name_3]
        service_value_1_1 = 'gate'
        service_value_1_2 = 'path'
        service_gate_value_mod = [gateway_name_3, gateway_name_2, gateway_name_1]
        service_value_2_1 = '/proxy/exchange/email/addAttachment'
        service_value_2_2 = '/proxy/config/getBinaryConfig'
        service_value_2_3 = '/proxy/log/changeContext/add'
        service_property_value_mod =[service_value_2_1, service_value_2_2, service_value_2_3]

        # Verify Certificates
        certificate_row = 0
        while certificate_row <= 2:
            print('certificate_row', certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            if table_name_n != cert_name_mod[certificate_row]:
                print('table_name_n:', table_name_n, 'cert_name_mod:', cert_name_mod[certificate_row])
                raise Exception('Name is wrong or missing')
            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            if CO.table_ok_mark not in table_uploaded_n:
                raise Exception('Wrong mark img')
            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            if table_cert_type_n != cert_type_mod[certificate_row]:
                print('table_cert_type_n:', table_cert_type_n, 'cert_type_mod:', cert_type_mod[certificate_row])
                raise Exception('Wrong type')

            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            if table_password_n != cert_password_mod[certificate_row]:
                print('table_password_n:', table_password_n, 'cert_password_mod:', cert_password_mod[certificate_row])
                raise Exception('Wrong password')
            print('certificate row %s Checked' % str(certificate_row + 1))
            certificate_row += 1

        # Verify Gateways
        gateway_row = 0
        while gateway_row <= 2:
            print('gateway_row', gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            if gateway_name_n != gateway_name_mod[gateway_row]:
                print('gateway_name_n:', gateway_name_n, 'gateway_name_mod:', gateway_name_mod[gateway_row])
                raise Exception('Wrong gateway name', gateway_name_n)
            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            if gateway_client_n != client_trust_mod[gateway_row]:
                print('gateway_client_n:', gateway_client_n, 'client_trust_mod:', client_trust_mod[gateway_row])
                raise Exception('Wrong gateway client')
            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            if gateway_trust_n != client_trust_mod[gateway_row]:
                print('gateway_trust_n:', gateway_trust_n, 'client_trust_mod:', client_trust_mod[gateway_row])
                raise Exception('Wrong gateway trust')
            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            if gateway_port_n != gateway_port_mod[gateway_row]:
                print('gateway_port_n:', gateway_port_n, 'gateway_port_mod:', gateway_port_mod[gateway_row])
                raise Exception('Wrong gateway port')
            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            if gateway_host_n != gateway_host_mod[gateway_row]:
                print('gateway_host_n:', gateway_host_n, 'gateway_host_mod:', gateway_host_mod[gateway_row])
                raise Exception('Wrong gateway host')
            print('gateway row %s Checked' % str(gateway_row + 1))
            gateway_row += 1

        # Verify Services
        service_count = 0
        while service_count <= 2:
            print('service_count', service_count)

            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(service_count)).get_attribute('textContent')
            service_value_property = driver.find_element_by_css_selector(

                Check.service_value_property_2(service_count)).get_attribute('textContent')
            service_value_property_value = driver.find_element_by_css_selector(
                Check.service_value_property_value_2(service_count)).get_attribute('textContent')
            service_value_gate = driver.find_element_by_css_selector(

                Check.service_value_property_1(service_count)).get_attribute('textContent')
            service_value_gate_name = driver.find_element_by_css_selector(
                Check.service_value_property_value_1(service_count)).get_attribute('textContent')

            if service_name_n != service_name_mod[service_count]:
                print('service_name_n:', service_name_n, 'service_name_mod:', service_name_mod[service_count])
                raise Exception('Wrong Service name')

            if service_value_property != service_value_1_2:
                print('service_value_property:', service_value_property, 'service_value_1_2:', service_value_1_2)
                raise Exception('Wrong service property name information')
            if service_value_property_value != service_property_value_mod[service_count]:
                print('service_value_property_value:', service_value_property_value, 'service_property_value_mod:',
                      service_property_value_mod[service_count])
                raise Exception('Wrong service property value information')

            if service_value_gate != service_value_1_1:
                print('service_value_gate:', service_value_gate, 'service_value_1_1:', service_value_1_1)
                raise Exception('Wrong service value gate information')
            if service_value_gate_name != service_gate_value_mod[service_count]:
                print('service_value_gate_name:', service_value_gate_name, 'service_gate_value_mod:',
                      service_gate_value_mod[service_count])
                raise Exception('Wrong service value gate name information')
            print('service row %s Checked' % str(service_count + 1))
            service_count += 1

        # Set date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        print('now_month', now_month)
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        if tomorrow_day[0] == '0':
            tomorrow_day = tomorrow_day[1]
            print('tomorrow_day', tomorrow_day)
        tomorrow_month_decimal = tomorrow.strftime('%m')
        if tomorrow_month_decimal[0] == '0':
            tomorrow_month_decimal = tomorrow_month_decimal[1]
            print('tomorrow_month_decimal', tomorrow_month_decimal)
        tomorrow_year = tomorrow.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_tomorrow = tomorrow_month_decimal + '/' + tomorrow_day + '/' + tomorrow_year[-2:]

        driver.find_element_by_id(CE.config_start_time).click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, CE.config_date_picker_day_highlight)))
        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')
        print('picker_month', picker_month)
        picker_day = ''

        while now_month.lower() != picker_month.lower():
            driver.find_element_by_class_name(CE.config_date_picker_next).click()
            time.sleep(1)
            picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')

        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
                picker_day = picker_elem.get_attribute('textContent')
                print('123')

        if now_day != picker_day:
            print('now_day', now_day, '- picker_day', picker_day)
            raise Exception('Day does not match')
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day, tomorrow_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification_message = driver.find_element_by_class_name(
                CE.main_notification_title).get_attribute('textContent')
            if notification_message != CO.start_time_changed:
                raise Exception('Wrong notification message')

        new_start_time = driver.find_element_by_id(CE.config_start_time).get_attribute(name='value')
        if new_start_time != start_time_set_tomorrow:
            print('new_start_time', new_start_time, "- start_time_set_tomorrow", start_time_set_tomorrow)
            raise Exception('Date is incorrect')
        time.sleep(1)

        # Save upcoming certificate
        driver.find_element_by_id(CE.config_apply).click()

        # Select upcoming
        time.sleep(1)
        if not Check.by_class_name_and_text(driver, CE.titlebar_panel, CO.provisioning_config_panel_title):
            raise Exception('Wrong title bar name')

        if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
            raise Exception(CO.select_configuration, 'is missing')
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)

        # Verify upcoming config
        # Verify Certificates 2
        certificate_row = 0
        while certificate_row <= 2:
            print('certificate_row', certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            if table_name_n != cert_name_mod[certificate_row]:
                print('table_name_n:', table_name_n, 'cert_name_mod:', cert_name_mod[certificate_row])
                raise Exception('Name is wrong or missing')
            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            if CO.table_ok_mark not in table_uploaded_n:
                raise Exception('Wrong mark img')
            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            if table_cert_type_n != cert_type_mod[certificate_row]:
                print('table_cert_type_n:', table_cert_type_n, 'cert_type_mod:', cert_type_mod[certificate_row])
                raise Exception('Wrong type')

            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            if table_password_n != cert_password_mod[certificate_row]:
                print('table_password_n:', table_password_n, 'cert_password_mod:', cert_password_mod[certificate_row])
                raise Exception('Wrong password')
            print('certificate row %s Checked' % str(certificate_row + 1))
            certificate_row += 1

        # Verify Gateways 2
        gateway_row = 0
        while gateway_row <= 2:
            print('gateway_row', gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            if gateway_name_n != gateway_name_mod[gateway_row]:
                print('gateway_name_n:', gateway_name_n, 'gateway_name_mod:', gateway_name_mod[gateway_row])
                raise Exception('Wrong gateway name', gateway_name_n)
            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            if gateway_client_n != client_trust_mod[gateway_row]:
                print('gateway_client_n:', gateway_client_n, 'client_trust_mod:', client_trust_mod[gateway_row])
                raise Exception('Wrong gateway client')
            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            if gateway_trust_n != client_trust_mod[gateway_row]:
                print('gateway_trust_n:', gateway_trust_n, 'client_trust_mod:', client_trust_mod[gateway_row])
                raise Exception('Wrong gateway trust')
            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            if gateway_port_n != gateway_port_mod[gateway_row]:
                print('gateway_port_n:', gateway_port_n, 'gateway_port_mod:', gateway_port_mod[gateway_row])
                raise Exception('Wrong gateway port')
            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            if gateway_host_n != gateway_host_mod[gateway_row]:
                print('gateway_host_n:', gateway_host_n, 'gateway_host_mod:', gateway_host_mod[gateway_row])
                raise Exception('Wrong gateway host')
            print('gateway row %s Checked' % str(gateway_row + 1))
            gateway_row += 1

        # Verify Services 2
        service_count = 0
        while service_count <= 2:
            print('service_count', service_count)

            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(service_count)).get_attribute('textContent')
            service_value_property = driver.find_element_by_css_selector(

                Check.service_value_property_2(service_count)).get_attribute('textContent')
            service_value_property_value = driver.find_element_by_css_selector(
                Check.service_value_property_value_2(service_count)).get_attribute('textContent')
            service_value_gate = driver.find_element_by_css_selector(

                Check.service_value_property_1(service_count)).get_attribute('textContent')
            service_value_gate_name = driver.find_element_by_css_selector(
                Check.service_value_property_value_1(service_count)).get_attribute('textContent')

            if service_name_n != service_name_mod[service_count]:
                print('service_name_n:', service_name_n, 'service_name_mod:', service_name_mod[service_count])
                raise Exception('Wrong Service name')

            if service_value_property != service_value_1_2:
                print('service_value_property:', service_value_property, 'service_value_1_2:', service_value_1_2)
                raise Exception('Wrong service property name information')
            if service_value_property_value != service_property_value_mod[service_count]:
                print('service_value_property_value:', service_value_property_value, 'service_property_value_mod:',
                      service_property_value_mod[service_count])
                raise Exception('Wrong service property value information')

            if service_value_gate != service_value_1_1:
                print('service_value_gate:', service_value_gate, 'service_value_1_1:', service_value_1_1)
                raise Exception('Wrong service value gate information')
            if service_value_gate_name != service_gate_value_mod[service_count]:
                print('service_value_gate_name:', service_value_gate_name, 'service_gate_value_mod:',
                      service_gate_value_mod[service_count])
                raise Exception('Wrong service value gate name information')
            print('service row %s Checked' % str(service_count + 1))
            service_count += 1


class ProvisioningConfig05Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        pass

    def test1_pc_copy_to_upcoming(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Delete config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
            Check.select_config(driver, wait, CO.upcoming_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            time.sleep(1)
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(CE.main_notification_title).get_attribute(
                    'textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
        # Delete end

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        # Find Certificates quantity
        cert_quantity = 0
        while cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(cert_quantity + 1), 'found')
                cert_quantity += 1
            else:
                print('cert_quantity = ', cert_quantity)
                break

        # Find Gateways quantity
        gateway_quantity = 0
        while gateway_quantity >= 0:
            # print(gateway_quantity)
            row = r'#form\3a gatewaysTable_data > tr:nth-child(' + str(gateway_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(gateway_quantity + 1), 'found')
                gateway_quantity += 1
            else:
                print('gateway_quantity = ', gateway_quantity)
                break

        # Find Services quantity
        services_quantity = 0
        while services_quantity >= 0:
            # print(services_quantity)
            row = r'#form\3a servicesTable_data > tr:nth-child(' + str(services_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(services_quantity + 1), 'found')
                services_quantity += 1
            else:
                print('services_quantity = ', services_quantity)
                break

        # Certificates
        cert_name_list = []
        cert_uploaded_list = []
        cert_type_list = []
        cert_password_list = []

        certificate_row = 0
        while certificate_row <= cert_quantity - 1:
            print('certificate_row', certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            cert_name_list.append(table_name_n)
            # if table_name_n != cert_name_mod[certificate_row]:
            #     print('table_name_n:', table_name_n, 'cert_name_mod:', cert_name_mod[certificate_row])
            #     raise Exception('Name is wrong or missing')
            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            cert_uploaded_list.append(table_uploaded_n)

            # if CO.table_ok_mark not in table_uploaded_n:
            #     raise Exception('Wrong mark img')
            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            cert_type_list.append(table_cert_type_n)

            # if table_cert_type_n != cert_type_mod[certificate_row]:
            #     print('table_cert_type_n:', table_cert_type_n, 'cert_type_mod:', cert_type_mod[certificate_row])
            #     raise Exception('Wrong type')

            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            cert_password_list.append(table_password_n)

            # if table_password_n != cert_password_mod[certificate_row]:
            #     print('table_password_n:', table_password_n, 'cert_password_mod:', cert_password_mod[certificate_row])
            #     raise Exception('Wrong password')
            print('certificate row %s Added' % str(certificate_row + 1))
            certificate_row += 1

        # Gateways
        # print('gateway_name_list', gateway_name_list)
        gateway_name_list = []
        gateway_client_list = []
        gateway_trust_list = []
        gateway_port_list = []
        gateway_host_list = []

        gateway_row = 0
        while gateway_row <= gateway_quantity - 1:
            print('gateway_row', gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            gateway_name_list.append(gateway_name_n)

            # if gateway_name_n != gateway_name_mod[gateway_row]:
            #     print('gateway_name_n:', gateway_name_n, 'gateway_name_mod:', gateway_name_mod[gateway_row])
            #     raise Exception('Wrong gateway name', gateway_name_n)
            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            gateway_client_list.append(gateway_client_n)

            # if gateway_client_n != client_trust_mod[gateway_row]:
            #     print('gateway_client_n:', gateway_client_n, 'client_trust_mod:', client_trust_mod[gateway_row])
            #     raise Exception('Wrong gateway client')
            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            gateway_trust_list.append(gateway_trust_n)

            # if gateway_trust_n != client_trust_mod[gateway_row]:
            #     print('gateway_trust_n:', gateway_trust_n, 'client_trust_mod:', client_trust_mod[gateway_row])
            #     raise Exception('Wrong gateway trust')
            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            gateway_port_list.append(gateway_port_n)

            # if gateway_port_n != gateway_port_mod[gateway_row]:
            #     print('gateway_port_n:', gateway_port_n, 'gateway_port_mod:', gateway_port_mod[gateway_row])
            #     raise Exception('Wrong gateway port')
            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            gateway_host_list.append(gateway_host_n)

            # if gateway_host_n != gateway_host_mod[gateway_row]:
            #     print('gateway_host_n:', gateway_host_n, 'gateway_host_mod:', gateway_host_mod[gateway_row])
            #     raise Exception('Wrong gateway host')
            print('gateway row %s Added' % str(gateway_row + 1))
            gateway_row += 1

        # Services
        service_name_list = []
        service_value_line2_list = []
        service_value_line2_value_list = []
        service_value_line1_list = []
        service_value_line1_value_list = []

        service_count = 0
        while service_count <= services_quantity - 1:
            print('service_count', service_count)

            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(service_count)).get_attribute('textContent')
            service_name_list.append(service_name_n)

            service_value_line2 = driver.find_elements_by_css_selector(Check.service_value_property_2(service_count))
            if service_value_line2:
                service_value_line2_list.append(service_value_line2[0].get_attribute('textContent'))
            else:
                service_value_line2_list.append(None)

            service_value_line2_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_2(service_count))
            if service_value_line2_value:
                service_value_line2_value_list.append(service_value_line2_value[0].get_attribute('textContent'))
            else:
                service_value_line2_value_list.append(None)

            service_value_line1 = driver.find_elements_by_css_selector(
                Check.service_value_property_1(service_count))
            if service_value_line1:
                service_value_line1_list.append(service_value_line1[0].get_attribute('textContent'))
            else:
                service_value_line1_list.append(None)

            service_value_line1_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_1(service_count))
            if service_value_line1_value:
                service_value_line1_value_list.append(service_value_line1_value[0].get_attribute('textContent'))
            else:
                service_value_line1_value_list.append(None)

            print('service row %s Added' % str(service_count + 1))
            service_count += 1

        driver.find_element_by_id(CE.config_copy).click()
        time.sleep(1)

        # Set date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        if tomorrow_day[0] == '0':
            tomorrow_day = tomorrow_day[1]
            print('tomorrow_day', tomorrow_day)
        tomorrow_month_decimal = tomorrow.strftime('%m')
        if tomorrow_month_decimal[0] == '0':
            tomorrow_month_decimal = tomorrow_month_decimal[1]
            print('tomorrow_month_decimal', tomorrow_month_decimal)
        tomorrow_year = tomorrow.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_tomorrow = tomorrow_month_decimal + '/' + tomorrow_day + '/' + tomorrow_year[-2:]

        # driver.find_element_by_id(CE.config_start_time).click()
        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')
        time.sleep(1)
        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
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
        if now_day == str(last_day_of_month[1]):
            driver.find_element_by_class_name(CE.config_date_picker_next).click()
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day, tomorrow_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_start_time_ok_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        new_start_time = driver.find_element_by_id(CE.config_start_time).get_attribute(name='value')
        if new_start_time != start_time_set_tomorrow:
            print('new_start_time', new_start_time, "- start_time_set_tomorrow", start_time_set_tomorrow)
            raise Exception('Date is incorrect')
        time.sleep(1)

        # Verify Certificates
        certificate_row = 0
        while certificate_row <= cert_quantity - 1:
            # print('certificate_row', certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            # cert_name_list.append(table_name_n)
            if table_name_n != cert_name_list[certificate_row]:
                print('table_name_n:', table_name_n, 'cert_name_mod:', cert_name_list[certificate_row])
                raise Exception('Name is wrong or missing')

            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            # cert_uploaded_list.append(table_uploaded_n)
            if table_uploaded_n != cert_uploaded_list[certificate_row]:
                raise Exception('Wrong mark img')

            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            # cert_type_list.append(table_cert_type_n)
            if table_cert_type_n != cert_type_list[certificate_row]:
                print('table_cert_type_n:', table_cert_type_n, 'cert_type_mod:', cert_type_list[certificate_row])
                raise Exception('Wrong type')

            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            # cert_password_list.append(table_password_n)
            if table_password_n != cert_password_list[certificate_row]:
                print('table_password_n:', table_password_n, 'cert_password_mod:', cert_password_list[certificate_row])
                raise Exception('Wrong password')
            print('certificate row %s Verify' % str(certificate_row + 1))
            certificate_row += 1

        # Verify Gateways
        gateway_row = 0
        while gateway_row <= gateway_quantity - 1:
            # print('gateway_row', gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            # gateway_name_list.append(gateway_name_n)

            if gateway_name_n != gateway_name_list[gateway_row]:
                print('gateway_name_n:', gateway_name_n, 'gateway_name_mod:', gateway_name_list[gateway_row])
                raise Exception('Wrong gateway name', gateway_name_n)
            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            # gateway_client_list.append(gateway_client_n)

            if gateway_client_n != gateway_client_list[gateway_row]:
                print('gateway_client_n:', gateway_client_n, 'client_trust_mod:', gateway_client_list[gateway_row])
                raise Exception('Wrong gateway client')
            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            # gateway_trust_list.append(gateway_trust_n)

            if gateway_trust_n != gateway_trust_list[gateway_row]:
                print('gateway_trust_n:', gateway_trust_n, 'client_trust_mod:', gateway_trust_list[gateway_row])
                raise Exception('Wrong gateway trust')
            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            # gateway_port_list.append(gateway_port_n)

            if gateway_port_n != gateway_port_list[gateway_row]:
                print('gateway_port_n:', gateway_port_n, 'gateway_port_mod:', gateway_port_list[gateway_row])
                raise Exception('Wrong gateway port')
            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            # gateway_host_list.append(gateway_host_n)

            if gateway_host_n != gateway_host_list[gateway_row]:
                print('gateway_host_n:', gateway_host_n, 'gateway_host_mod:', gateway_host_list[gateway_row])
                raise Exception('Wrong gateway host')
            print('gateway row %s Verify' % str(gateway_row + 1))
            gateway_row += 1

        # Verify Services
        service_count = 0
        while service_count <= services_quantity - 1:
            # print('service_count', service_count)

            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(service_count)).get_attribute('textContent')

            service_value_line2 = driver.find_elements_by_css_selector(
                Check.service_value_property_2(service_count))

            service_value_line2_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_2(service_count))

            service_value_line1 = driver.find_elements_by_css_selector(
                Check.service_value_property_1(service_count))

            service_value_line1_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_1(service_count))

            if service_name_n != service_name_list[service_count]:
                print('service_name_n:', service_name_n, 'service_name_mod:', service_name_list[service_count])
                raise Exception('Wrong Service name')

            if service_value_line2:
                if service_value_line2[0].get_attribute('textContent') != service_value_line2_list[service_count]:
                    print('service_value_line2:', service_value_line2,
                          'service_value_line2_list:', service_value_line2_list[service_count])
                    raise Exception('Wrong service information')

            if service_value_line2_value:
                if service_value_line2_value[0].get_attribute('textContent') != service_value_line2_value_list[service_count]:
                    print('service_value_line2_value:', service_value_line2_value,
                          'service_value_line2_list:', service_value_line2_list[service_count])
                    raise Exception('Wrong service information')

            if service_value_line1:
                if service_value_line1[0].get_attribute('textContent') != service_value_line1_list[service_count]:
                    print('service_value_line1:', service_value_line1,
                          'service_value_line1_list:', service_value_line1_list[service_count])
                    raise Exception('Wrong service information')

            if service_value_line1_value:
                if service_value_line1_value[0].get_attribute('textContent') != service_value_line1_value_list[service_count]:
                    print('service_value_line1_value:', service_value_line1_value,
                          'service_value_line1_value_list:', service_value_line1_value_list[service_count])
                    raise Exception('Wrong service information')

            print('service row %s Verify' % str(service_count + 1))
            service_count += 1

        # Save upcoming certificate
        driver.find_element_by_id(CE.config_apply).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        # Select upcoming
        time.sleep(2)
        if not Check.by_class_name_and_text(driver, CE.titlebar_panel, CO.provisioning_config_panel_title):
            raise Exception('Wrong title bar name')

        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)

        # Verify Certificates
        certificate_row = 0
        while certificate_row <= cert_quantity - 1:
            # print('certificate_row', certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            # cert_name_list.append(table_name_n)
            if table_name_n != cert_name_list[certificate_row]:
                print('table_name_n:', table_name_n, 'cert_name_mod:', cert_name_list[certificate_row])
                raise Exception('Name is wrong or missing')

            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            # cert_uploaded_list.append(table_uploaded_n)
            if table_uploaded_n != cert_uploaded_list[certificate_row]:
                raise Exception('Wrong mark img')

            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            # cert_type_list.append(table_cert_type_n)
            if table_cert_type_n != cert_type_list[certificate_row]:
                print('table_cert_type_n:', table_cert_type_n, 'cert_type_mod:', cert_type_list[certificate_row])
                raise Exception('Wrong type')

            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            # cert_password_list.append(table_password_n)
            if table_password_n != cert_password_list[certificate_row]:
                print('table_password_n:', table_password_n, 'cert_password_mod:', cert_password_list[certificate_row])
                raise Exception('Wrong password')
            print('certificate row %s Verify' % str(certificate_row + 1))
            certificate_row += 1

        # Verify Gateways
        gateway_row = 0
        while gateway_row <= gateway_quantity - 1:
            # print('gateway_row', gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            # gateway_name_list.append(gateway_name_n)

            if gateway_name_n != gateway_name_list[gateway_row]:
                print('gateway_name_n:', gateway_name_n, 'gateway_name_mod:', gateway_name_list[gateway_row])
                raise Exception('Wrong gateway name', gateway_name_n)
            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            # gateway_client_list.append(gateway_client_n)

            if gateway_client_n != gateway_client_list[gateway_row]:
                print('gateway_client_n:', gateway_client_n, 'client_trust_mod:', gateway_client_list[gateway_row])
                raise Exception('Wrong gateway client')
            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            # gateway_trust_list.append(gateway_trust_n)

            if gateway_trust_n != gateway_trust_list[gateway_row]:
                print('gateway_trust_n:', gateway_trust_n, 'client_trust_mod:', gateway_trust_list[gateway_row])
                raise Exception('Wrong gateway trust')
            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            # gateway_port_list.append(gateway_port_n)

            if gateway_port_n != gateway_port_list[gateway_row]:
                print('gateway_port_n:', gateway_port_n, 'gateway_port_mod:', gateway_port_list[gateway_row])
                raise Exception('Wrong gateway port')
            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            # gateway_host_list.append(gateway_host_n)

            if gateway_host_n != gateway_host_list[gateway_row]:
                print('gateway_host_n:', gateway_host_n, 'gateway_host_mod:', gateway_host_list[gateway_row])
                raise Exception('Wrong gateway host')
            print('gateway row %s Verify' % str(gateway_row + 1))
            gateway_row += 1

        # Verify Services
        service_count = 0
        while service_count <= services_quantity - 1:
            # print('service_count', service_count)

            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(service_count)).get_attribute('textContent')

            service_value_line2 = driver.find_elements_by_css_selector(
                Check.service_value_property_2(service_count))

            service_value_line2_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_2(service_count))

            service_value_line1 = driver.find_elements_by_css_selector(
                Check.service_value_property_1(service_count))

            service_value_line1_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_1(service_count))

            if service_name_n != service_name_list[service_count]:
                print('service_name_n:', service_name_n, 'service_name_mod:', service_name_list[service_count])
                raise Exception('Wrong Service name')

            if service_value_line2:
                if service_value_line2[0].get_attribute('textContent') != service_value_line2_list[service_count]:
                    print('service_value_line2:', service_value_line2,
                          'service_value_line2_list:', service_value_line2_list[service_count])
                    raise Exception('Wrong service information')

            if service_value_line2_value:
                if service_value_line2_value[0].get_attribute('textContent') != service_value_line2_value_list[service_count]:
                    print('service_value_line2_value:', service_value_line2_value,
                          'service_value_line2_list:', service_value_line2_list[service_count])
                    raise Exception('Wrong service information')

            if service_value_line1:
                if service_value_line1[0].get_attribute('textContent') != service_value_line1_list[service_count]:
                    print('service_value_line1:', service_value_line1,
                          'service_value_line1_list:', service_value_line1_list[service_count])
                    raise Exception('Wrong service information')

            if service_value_line1_value:
                if service_value_line1_value[0].get_attribute('textContent') != service_value_line1_value_list[service_count]:
                    print('service_value_line1_value:', service_value_line1_value,
                          'service_value_line1_value_list:', service_value_line1_value_list[service_count])
                    raise Exception('Wrong service information')

            print('service row %s Verify' % str(service_count + 1))
            service_count += 1


class ProvisioningConfig06Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')
        #
        driver = cls.driver

        # Delete config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
            Check.select_config(driver, wait, CO.upcoming_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(2)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
        # Delete end
        time.sleep(2)
        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        # Copy config
        driver.find_element_by_id(CE.config_copy).click()
        time.sleep(1)
        # Set date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        if tomorrow_day[0] == '0':
            tomorrow_day = tomorrow_day[1]
            print('tomorrow_day', tomorrow_day)
        tomorrow_month_decimal = tomorrow.strftime('%m')
        if tomorrow_month_decimal[0] == '0':
            tomorrow_month_decimal = tomorrow_month_decimal[1]
            print('tomorrow_month_decimal', tomorrow_month_decimal)
        tomorrow_year = tomorrow.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_tomorrow = tomorrow_month_decimal + '/' + tomorrow_day + '/' + tomorrow_year[-2:]

        # driver.find_element_by_id(CE.config_start_time).click()
        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')
        time.sleep(1)
        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
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
        if now_day == str(last_day_of_month[1]):
            driver.find_element_by_class_name(CE.config_date_picker_next).click()
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day, tomorrow_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_start_time_ok_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        new_start_time = driver.find_element_by_id(CE.config_start_time).get_attribute(name='value')
        if new_start_time != start_time_set_tomorrow:
            print('new_start_time', new_start_time, "- start_time_set_tomorrow", start_time_set_tomorrow)
            raise Exception('Date is incorrect')
        time.sleep(1)
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Select upcoming
        time.sleep(1)
        if not Check.by_class_name_and_text(driver, CE.titlebar_panel, CO.provisioning_config_panel_title):
            raise Exception('Wrong title bar name')

        if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
            raise Exception(CO.select_configuration, 'is missing')
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)

    def tearDown(self):
        pass

    def test1_pc_delete_certificate(self):
        driver = self.driver
        # driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        cert_quantity = 0
        while cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(cert_quantity + 1), 'found')
                cert_quantity += 1
            else:
                print('cert_quantity = ', cert_quantity)
                break

        # Certificates
        cert_name_list = []
        cert_uploaded_list = []
        cert_type_list = []
        cert_password_list = []

        certificate_row = 0
        while certificate_row <= cert_quantity - 1:
            # print('certificate_row', certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            cert_name_list.append(table_name_n)
            # if table_name_n != cert_name_mod[certificate_row]:
            #     print('table_name_n:', table_name_n, 'cert_name_mod:', cert_name_mod[certificate_row])
            #     raise Exception('Name is wrong or missing')
            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            cert_uploaded_list.append(table_uploaded_n)

            # if CO.table_ok_mark not in table_uploaded_n:
            #     raise Exception('Wrong mark img')
            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            cert_type_list.append(table_cert_type_n)

            # if table_cert_type_n != cert_type_mod[certificate_row]:
            #     print('table_cert_type_n:', table_cert_type_n, 'cert_type_mod:', cert_type_mod[certificate_row])
            #     raise Exception('Wrong type')

            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            cert_password_list.append(table_password_n)

            # if table_password_n != cert_password_mod[certificate_row]:
            #     print('table_password_n:', table_password_n, 'cert_password_mod:', cert_password_mod[certificate_row])
            #     raise Exception('Wrong password')
            print('certificate row %s Added' % str(certificate_row + 1))
            certificate_row += 1

        # Delete Certificate (cant deleted)
        rand_value = random.randint(1, cert_quantity - 1)
        print('rand_value', rand_value)
        delete_certificate = 'form:certificatesTable:' + str(rand_value) + ':removeCertificate'
        driver.find_element_by_id(delete_certificate).click()
        driver.find_element_by_class_name(CE.dialog_titlebar)
        time.sleep(2)
        driver.find_element_by_id(CE.config_delete_certificate_conform).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
            if notification != CO.unable_to_remove_certificate:
                print('notification', notification)
                raise Exception('Wrong notification message')

        # Find New Certificates quantity
        new_cert_quantity = 0
        while new_cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(new_cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(new_cert_quantity + 1), 'found')
                new_cert_quantity += 1
            else:
                print('new_cert_quantity = ', new_cert_quantity)
                break

        if cert_quantity != new_cert_quantity:
            raise Exception('Certificate was deleted')

        # Delete Certificate
        delete_certificate = 'form:certificatesTable:0:removeCertificate'
        driver.find_element_by_id(delete_certificate).click()
        driver.find_element_by_class_name(CE.dialog_titlebar)
        time.sleep(2)
        driver.find_element_by_id(CE.config_delete_certificate_conform).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
            if CO.message_successfully_deleted not in notification:
                print('notification:', notification)
                raise Exception('Wrong notification message')

        # Find New Certificates quantity
        new_cert_quantity = 0
        while new_cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(new_cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(new_cert_quantity + 1), 'found')
                new_cert_quantity += 1
            else:
                print('new_cert_quantity = ', new_cert_quantity)
                break

        # New Certificates
        new_cert_name_list = []
        new_cert_uploaded_list = []
        new_cert_type_list = []
        new_cert_password_list = []

        new_certificate_row = 0
        while new_certificate_row <= new_cert_quantity - 1:
            # print('new_certificate_row', new_certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(new_certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                new_certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(new_certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(new_certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            new_cert_name_list.append(table_name_n)
            # if table_name_n != cert_name_mod[certificate_row]:
            #     print('table_name_n:', table_name_n, 'cert_name_mod:', cert_name_mod[certificate_row])
            #     raise Exception('Name is wrong or missing')
            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            new_cert_uploaded_list.append(table_uploaded_n)

            # if CO.table_ok_mark not in table_uploaded_n:
            #     raise Exception('Wrong mark img')
            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            new_cert_type_list.append(table_cert_type_n)

            # if table_cert_type_n != cert_type_mod[certificate_row]:
            #     print('table_cert_type_n:', table_cert_type_n, 'cert_type_mod:', cert_type_mod[certificate_row])
            #     raise Exception('Wrong type')

            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            new_cert_password_list.append(table_password_n)

            # if table_password_n != cert_password_mod[certificate_row]:
            #     print('table_password_n:', table_password_n, 'cert_password_mod:', cert_password_mod[certificate_row])
            #     raise Exception('Wrong password')
            print('new_certificate row %s Added' % str(new_certificate_row + 1))
            new_certificate_row += 1

        if certificate_row == new_certificate_row:
            raise Exception('Certificate not deleted')
        cert_verify = 1
        while cert_verify != certificate_row - 1:
            print('cert_verify', cert_verify)
            # if cert_verify == 0:
            #     print('if')
            #     cert_verify += 1
            # else:
            #     print('else')
            if cert_name_list[cert_verify] != new_cert_name_list[cert_verify - 1]:
                print('cert_name:', cert_name_list[cert_verify], 'new_cert_name:', new_cert_name_list[cert_verify - 1])
                raise Exception('Name is incorrect')
            if cert_uploaded_list[cert_verify] != new_cert_uploaded_list[cert_verify - 1]:
                print('cert_uploaded:', cert_uploaded_list[cert_verify],
                      'new_cert_uploaded:', new_cert_uploaded_list[cert_verify - 1])
                raise Exception('Upload is incorrect')
            if cert_type_list[cert_verify] != new_cert_type_list[cert_verify - 1]:
                print('cert_type:', cert_type_list[cert_verify], 'new_cert_type:', new_cert_type_list[cert_verify - 1])
                raise Exception('Type is incorrect')
            if cert_password_list[cert_verify] != new_cert_password_list[cert_verify - 1]:
                print('cert_password:', cert_password_list[cert_verify],
                      'new_cert_password:', new_cert_password_list[cert_verify - 1])
                raise Exception('Password is incorrect')
            cert_verify += 1

        time.sleep(1)
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)

    def test2_pc_delete_gateway(self):
        driver = self.driver
        # driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Find Gateways quantity
        gateway_quantity = 0
        while gateway_quantity >= 0:
            # print(gateway_quantity)
            row = r'#form\3a gatewaysTable_data > tr:nth-child(' + str(gateway_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(gateway_quantity + 1), 'found')
                gateway_quantity += 1
            else:
                print('gateway_quantity = ', gateway_quantity)
                break

        # Gateways
        gateway_name_list = []
        gateway_client_list = []
        gateway_trust_list = []
        gateway_port_list = []
        gateway_host_list = []

        gateway_row = 0
        while gateway_row <= gateway_quantity - 1:
            print('gateway_row', gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            gateway_name_list.append(gateway_name_n)

            # if gateway_name_n != gateway_name_mod[gateway_row]:
            #     print('gateway_name_n:', gateway_name_n, 'gateway_name_mod:', gateway_name_mod[gateway_row])
            #     raise Exception('Wrong gateway name', gateway_name_n)
            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            gateway_client_list.append(gateway_client_n)

            # if gateway_client_n != client_trust_mod[gateway_row]:
            #     print('gateway_client_n:', gateway_client_n, 'client_trust_mod:', client_trust_mod[gateway_row])
            #     raise Exception('Wrong gateway client')
            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            gateway_trust_list.append(gateway_trust_n)

            # if gateway_trust_n != client_trust_mod[gateway_row]:
            #     print('gateway_trust_n:', gateway_trust_n, 'client_trust_mod:', client_trust_mod[gateway_row])
            #     raise Exception('Wrong gateway trust')
            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            gateway_port_list.append(gateway_port_n)

            # if gateway_port_n != gateway_port_mod[gateway_row]:
            #     print('gateway_port_n:', gateway_port_n, 'gateway_port_mod:', gateway_port_mod[gateway_row])
            #     raise Exception('Wrong gateway port')
            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            gateway_host_list.append(gateway_host_n)

            # if gateway_host_n != gateway_host_mod[gateway_row]:
            #     print('gateway_host_n:', gateway_host_n, 'gateway_host_mod:', gateway_host_mod[gateway_row])
            #     raise Exception('Wrong gateway host')
            print('gateway row %s Added' % str(gateway_row + 1))
            gateway_row += 1

        # Delete Gateway (cant deleted)
        rand_value = random.randint(1, gateway_quantity - 1)
        print('rand_value', rand_value)
        delete_gateway = 'form:gatewaysTable:' + str(rand_value) + ':removeGateway'
        driver.find_element_by_id(delete_gateway).click()
        driver.find_element_by_class_name(CE.dialog_titlebar)
        time.sleep(2)
        driver.find_element_by_id(CE.config_delete_gateway_conform).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
            if notification != CO.unable_to_remove_gateway:
                raise Exception('Wrong notification message')

        # Find New Gateways quantity
        new_gateway_quantity = 0
        while new_gateway_quantity >= 0:
            # print(new_gateway_quantity)
            row = r'#form\3a gatewaysTable_data > tr:nth-child(' + str(new_gateway_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(new_gateway_quantity + 1), 'found')
                new_gateway_quantity += 1
            else:
                print('new_gateway_quantity = ', new_gateway_quantity)
                break

        if gateway_quantity != new_gateway_quantity:
            raise Exception('Gateway was deleted')

        # Delete Gateway
        delete_gateway = 'form:gatewaysTable:0:removeGateway'
        driver.find_element_by_id(delete_gateway).click()
        driver.find_element_by_class_name(CE.dialog_titlebar)
        time.sleep(2)
        driver.find_element_by_id(CE.config_delete_gateway_conform).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
            if CO.message_successfully_deleted not in notification:
                print('notification:', notification)
                raise Exception('Wrong notification message')

        # Find New Gateways quantity
        new_gateway_quantity = 0
        while new_gateway_quantity >= 0:
            # print(new_gateway_quantity)
            row = r'#form\3a gatewaysTable_data > tr:nth-child(' + str(new_gateway_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(new_gateway_quantity + 1), 'found')
                new_gateway_quantity += 1
            else:
                print('new_gateway_quantity = ', new_gateway_quantity)
                break

        # New Gateways
        new_gateway_name_list = []
        new_gateway_client_list = []
        new_gateway_trust_list = []
        new_gateway_port_list = []
        new_gateway_host_list = []

        new_gateway_row = 0
        while new_gateway_row <= new_gateway_quantity - 1:
            # print('new_gateway_row', new_gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(new_gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(new_gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(new_gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(new_gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(new_gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            new_gateway_name_list.append(gateway_name_n)

            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            new_gateway_client_list.append(gateway_client_n)

            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            new_gateway_trust_list.append(gateway_trust_n)

            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            new_gateway_port_list.append(gateway_port_n)

            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            new_gateway_host_list.append(gateway_host_n)

            print('new_gateway row %s Added' % str(new_gateway_row + 1))
            new_gateway_row += 1

        if gateway_row == new_gateway_row:
            raise Exception('Gateway not deleted')
        gate_verify = 1
        while gate_verify != new_gateway_row:
            print('gate_verify', gate_verify)
            # if gate_verify == 0:
            #     print('if')
            #     gate_verify += 1
            # else:
            #     print('else')
            if gateway_name_list[gate_verify] != new_gateway_name_list[gate_verify - 1]:
                print('gate_name:', gateway_name_list[gate_verify],
                      'new_gate_name:', new_gateway_name_list[gate_verify - 1])
                raise Exception('Name is incorrect')
            if gateway_client_list[gate_verify] != new_gateway_client_list[gate_verify - 1]:
                print('gate_client:', gateway_client_list[gate_verify],
                      'new_gate_client:', new_gateway_client_list[gate_verify - 1])
                raise Exception('Client is incorrect')
            if gateway_trust_list[gate_verify] != new_gateway_trust_list[gate_verify - 1]:
                print('gate_trust:', gateway_trust_list[gate_verify],
                      'new_gate_trust:', new_gateway_trust_list[gate_verify - 1])
                raise Exception('Trust is incorrect')
            if gateway_port_list[gate_verify] != new_gateway_port_list[gate_verify - 1]:
                print('gate_port:', gateway_port_list[gate_verify],
                      'new_gate_port:', new_gateway_port_list[gate_verify - 1])
                raise Exception('Port is incorrect')
            if gateway_host_list[gate_verify] != new_gateway_host_list[gate_verify - 1]:
                print('gate_host:', gateway_host_list[gate_verify],
                      'new_gate_host:', new_gateway_host_list[gate_verify - 1])
                raise Exception('Host is incorrect')
            gate_verify += 1

        time.sleep(1)
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)

    def test3_pc_delete_service(self):
        driver = self.driver
        # driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Find Services quantity
        services_quantity = 0
        while services_quantity >= 0:
            # print(services_quantity)
            row = r'#form\3a servicesTable_data > tr:nth-child(' + str(services_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(services_quantity + 1), 'found')
                services_quantity += 1
            else:
                print('services_quantity = ', services_quantity)
                break

        # Services
        service_name_list = []
        service_value_line2_list = []
        service_value_line2_value_list = []
        service_value_line1_list = []
        service_value_line1_value_list = []

        service_count = 0
        while service_count <= services_quantity - 1:
            # print('service_count while start', service_count)

            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(service_count)).get_attribute('textContent')
            service_name_list.append(service_name_n)

            service_value_line2 = driver.find_elements_by_css_selector(Check.service_value_property_2(service_count))
            if service_value_line2:
                service_value_line2_list.append(service_value_line2[0].get_attribute('textContent'))
            else:
                service_value_line2_list.append(None)

            service_value_line2_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_2(service_count))
            if service_value_line2_value:
                service_value_line2_value_list.append(service_value_line2_value[0].get_attribute('textContent'))
            else:
                service_value_line2_value_list.append(None)

            service_value_line1 = driver.find_elements_by_css_selector(
                Check.service_value_property_1(service_count))
            if service_value_line1:
                service_value_line1_list.append(service_value_line1[0].get_attribute('textContent'))
            else:
                service_value_line1_list.append(None)

            service_value_line1_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_1(service_count))
            if service_value_line1_value:
                service_value_line1_value_list.append(service_value_line1_value[0].get_attribute('textContent'))
            else:
                service_value_line1_value_list.append(None)

            print('service row %s Added' % str(service_count + 1))
            service_count += 1
            print('service_count while end', service_count)

        # Delete Service
        rand_value = random.randint(0, services_quantity - 1)
        print('rand_value', rand_value)
        delete_service = 'form:servicesTable:' + str(rand_value) + ':removeService'
        driver.find_element_by_id(delete_service).click()
        driver.find_element_by_class_name(CE.dialog_titlebar)
        time.sleep(2)
        driver.find_element_by_id(CE.config_delete_service_conform).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
            if notification != CO.message_successfully_deleted:
                raise Exception('Wrong notification message')

        # Find New Services quantity
        new_services_quantity = 0
        while new_services_quantity >= 0:
            # print(new_services_quantity)
            row = r'#form\3a servicesTable_data > tr:nth-child(' + str(new_services_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(new_services_quantity + 1), 'found')
                new_services_quantity += 1
            else:
                print('new_services_quantity = ', new_services_quantity)
                break

        # New Services
        new_service_name_list = []
        new_service_value_line2_list = []
        new_service_value_line2_value_list = []
        new_service_value_line1_list = []
        new_service_value_line1_value_list = []

        new_service_count = 0
        while new_service_count <= new_services_quantity - 1:
            # print('new_service_count while start', new_service_count)
            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(new_service_count)).get_attribute('textContent')
            new_service_name_list.append(service_name_n)

            service_value_line2 = driver.find_elements_by_css_selector(
                Check.service_value_property_2(new_service_count))
            if service_value_line2:
                new_service_value_line2_list.append(service_value_line2[0].get_attribute('textContent'))
            else:
                new_service_value_line2_list.append(None)

            service_value_line2_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_2(new_service_count))
            if service_value_line2_value:
                new_service_value_line2_value_list.append(service_value_line2_value[0].get_attribute('textContent'))
            else:
                new_service_value_line2_value_list.append(None)

            service_value_line1 = driver.find_elements_by_css_selector(
                Check.service_value_property_1(new_service_count))
            if service_value_line1:
                new_service_value_line1_list.append(service_value_line1[0].get_attribute('textContent'))
            else:
                new_service_value_line1_list.append(None)

            service_value_line1_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_1(new_service_count))
            if service_value_line1_value:
                new_service_value_line1_value_list.append(service_value_line1_value[0].get_attribute('textContent'))
            else:
                new_service_value_line1_value_list.append(None)

            print('service row %s Added' % str(new_service_count + 1))
            new_service_count += 1
            print('new_service_count while end', new_service_count)

        # Verify Services
        if service_count == new_service_count:
            raise Exception('Service not deleted')

        # print('service_name_list:', service_name_list)
        # print('new_service_name_list:', new_service_name_list)
        service_verify = 0
        service_verify_rand = 0
        count = 0
        # print('rand_value', rand_value)
        while service_verify <= new_service_count:
            # print('service_verify', service_verify)
            if service_verify == rand_value:
                print('down in if')
                service_verify += 1
                if service_verify > new_service_count:
                    print('break -- service_verify > new_service_count')
                    break
            print('service_verify after if', service_verify)
            print('service_verify_rand after if', service_verify_rand)
            if service_name_list[service_verify] != new_service_name_list[service_verify_rand]:
                print('service_name:', service_name_list[service_verify],
                      'new_service_name:', new_service_name_list[service_verify_rand])
                raise Exception('Name is incorrect')
            if service_value_line2_list[service_verify] != new_service_value_line2_list[service_verify_rand]:
                print('service_value_line2:', service_value_line2_list[service_verify],
                      'new_service_value_line2:', new_service_value_line2_list[service_verify_rand])
                raise Exception('value_line2 is incorrect')
            if service_value_line2_value_list[service_verify] != new_service_value_line2_value_list[service_verify_rand]:
                print('service_value_line2_value:', service_value_line2_value_list[service_verify],
                      'new_service_value_line2_value:', new_service_value_line2_value_list[service_verify_rand])
                raise Exception('value_line2_value is incorrect')
            if service_value_line1_list[service_verify] != new_service_value_line1_list[service_verify_rand]:
                print('service_value_line1:', service_value_line1_list[service_verify],
                      'new_service_value_line1:', new_service_value_line1_list[service_verify_rand])
                raise Exception('value_line1 is incorrect')
            if service_value_line1_value_list[service_verify] != new_service_value_line1_value_list[service_verify_rand]:
                print('service_value_line1_value:', service_value_line1_value_list[service_verify],
                      'new_service_value_line1_value:', new_service_value_line1_value_list[service_verify_rand])
                raise Exception('value_line1_value is incorrect')
            service_verify += 1
            service_verify_rand += 1
            count += 1
            print('verify', count, 'string')

        time.sleep(1)
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)


class ProvisioningConfig07Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')
        #
        driver = cls.driver

        # Delete config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
            Check.select_config(driver, wait, CO.upcoming_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            time.sleep(5)
        # Delete end

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        # Copy config
        driver.find_element_by_id(CE.config_copy).click()
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.ID, CE.config_date_picker_div)))

        # Set date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        if tomorrow_day[0] == '0':
            tomorrow_day = tomorrow_day[1]
            print('tomorrow_day', tomorrow_day)
        tomorrow_month_decimal = tomorrow.strftime('%m')
        if tomorrow_month_decimal[0] == '0':
            tomorrow_month_decimal = tomorrow_month_decimal[1]
            print('tomorrow_month_decimal', tomorrow_month_decimal)
        tomorrow_year = tomorrow.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_tomorrow = tomorrow_month_decimal + '/' + tomorrow_day + '/' + tomorrow_year[-2:]

        # driver.find_element_by_id(CE.config_start_time).click()
        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')
        picker_day = ''
        time.sleep(1)
        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
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
        if now_day == str(last_day_of_month[1]):
            driver.find_element_by_class_name(CE.config_date_picker_next).click()
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day, tomorrow_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_start_time_ok_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        new_start_time = driver.find_element_by_id(CE.config_start_time).get_attribute(name='value')
        if new_start_time != start_time_set_tomorrow:
            print('new_start_time', new_start_time, "- start_time_set_tomorrow", start_time_set_tomorrow)
            raise Exception('Date is incorrect')
        time.sleep(1)
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Select upcoming
        time.sleep(1)
        if not Check.by_class_name_and_text(driver, CE.titlebar_panel, CO.provisioning_config_panel_title):
            raise Exception('Wrong title bar name')

        if not Check.by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
            raise Exception(CO.select_configuration, 'is missing')
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)

    def tearDown(self):
        pass

    def test3_pc_edit_certificate(self):
        driver = self.driver
        # driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        cert_quantity = 0
        while cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(cert_quantity + 1), 'found')
                cert_quantity += 1
            else:
                print('cert_quantity = ', cert_quantity)
                break

        # Certificates
        cert_name_list = []
        cert_uploaded_list = []
        cert_type_list = []
        cert_password_list = []

        certificate_row = 0
        while certificate_row <= cert_quantity - 1:
            # print('certificate_row', certificate_row)
            cert_table_n_data_name = 'form:certificatesTable:' + str(certificate_row) + ':certificateName'
            cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(
                certificate_row + 1) + ') > td:nth-child(2) > img'
            cert_table_n_data_type = 'form:certificatesTable:' + str(certificate_row) + ':certificateType'
            cert_table_n_data_password = 'form:certificatesTable:' + str(certificate_row) + ':certificatePassword'

            table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
            cert_name_list.append(table_name_n)
            table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
            cert_uploaded_list.append(table_uploaded_n)
            table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
            cert_type_list.append(table_cert_type_n)
            table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
            cert_password_list.append(table_password_n)
            print('certificate row %s Added' % str(certificate_row + 1))
            certificate_row += 1

        # Edit first Certificate
        cert_name_1 = '1_new_certificate_name'
        edit_certificate = 'form:certificatesTable:0:editCertificate'
        driver.find_element_by_id(edit_certificate).click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_cert_name).clear()
        driver.find_element_by_id(CE.config_cert_name).send_keys(cert_name_1)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(2)

        # Check for first Certificate
        cert_table_n_data_name = 'form:certificatesTable:0:certificateName'
        cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(1) > td:nth-child(2) > img'
        cert_table_n_data_type = 'form:certificatesTable:0:certificateType'
        cert_table_n_data_password = 'form:certificatesTable:0:certificatePassword'

        table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
        if cert_name_list[0] == table_name_n:
            raise Exception('Wrong certificate name')
        table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
        if cert_uploaded_list[0] != table_uploaded_n:
            raise Exception('Wrong certificate upload mark')
        table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
        if cert_type_list[0] != table_cert_type_n:
            raise Exception('Wrong certificate type')
        table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
        if cert_password_list[0] != table_password_n:
            raise Exception('Wrong certificate password')

        # Edit first Certificate again
        cert_name_2 = '1_certificate_with_upload'
        edit_certificate = 'form:certificatesTable:0:editCertificate'
        driver.find_element_by_id(edit_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        time.sleep(1)
        element = driver.find_element_by_id(CE.config_cert_select_file)
        element.send_keys(address)
        file_name = 'in_app_proxy_cert'
        upload_file_name = driver.find_element_by_css_selector(CE.config_cert_upload_file_name).\
            get_attribute('textContent')
        if upload_file_name != file_name:
            raise Exception('The selected file has wrong name')
        file_size = '2.5 KB'
        upload_file_size = driver.find_element_by_css_selector(CE.config_cert_upload_file_size).\
            get_attribute('textContent')
        if upload_file_size != file_size:
            raise Exception('The selected file has wrong size')
        if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 1:
            raise Exception('Progress bar is missing')
        Check.by_class_name_and_text(driver, CE.config_buttons, CO.ui_button)
        driver.find_element_by_id(CE.config_cert_false_uploaded)
        cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_type_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')

        # Select upload
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
        driver.find_element_by_id(CE.config_cert_true_uploaded)

        driver.find_element_by_id(CE.config_cert_name).clear()
        driver.find_element_by_id(CE.config_cert_name).send_keys(cert_name_2)

        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        driver.find_element_by_id(CE.config_cert_select_type_list)
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        time.sleep(1)
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'is found')
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_password_1')
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(3)

        # Check for first Certificate again
        cert_table_n_data_name = 'form:certificatesTable:0:certificateName'
        cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(1) > td:nth-child(2) > img'
        cert_table_n_data_type = 'form:certificatesTable:0:certificateType'
        cert_table_n_data_password = 'form:certificatesTable:0:certificatePassword'

        table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
        if cert_name_list[0] == table_name_n or table_name_n != cert_name_2:
            raise Exception('Wrong certificate name')
        table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
        if cert_uploaded_list[0] == table_uploaded_n:
            raise Exception('Wrong certificate upload mark')
        table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
        if cert_type_list[0] == table_cert_type_n or table_cert_type_n != 'p12':
            raise Exception('Wrong certificate type')
        table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
        if cert_password_list[0] == table_password_n or table_password_n != 'cert_password_1':
            raise Exception('Wrong certificate password')

        # Edit rnd Certificate
        # I think that there is a mistake
        rnd_cert_name = '2_rnd_certificate'
        rnd_cert_password = 'rnd_cert_pass'
        rand_value = random.randint(1, cert_quantity - 1)
        print('rand_value', rand_value)
        edit_certificate = 'form:certificatesTable:' + str(rand_value) + ':editCertificate'
        driver.find_element_by_id(edit_certificate).click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_cert_name).clear()
        driver.find_element_by_id(CE.config_cert_name).send_keys(rnd_cert_name)

        type_cert = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        select_type = ''
        if type_cert == 'p12':
            print('if type_cert', type_cert)
            select_type = 'der'
            return select_type
        elif type_cert == 'der':
            print('elif type_cert', type_cert)
            select_type = 'p12'
            return select_type

        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_cert_select_type_list)
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, select_type).click()
        time.sleep(1)
        if select_type == 'p12':
            driver.find_element_by_id(CE.config_cert_password).send_keys(rnd_cert_password)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(3)

        # Check for rnd Certificate again
        cert_table_n_data_name = 'form:certificatesTable:1:certificateName'
        cert_table_n_data_img = r'#form\3a certificatesTable_data > tr:nth-child(2) > td:nth-child(2) > img'
        cert_table_n_data_type = 'form:certificatesTable:1:certificateType'
        cert_table_n_data_password = 'form:certificatesTable:1:certificatePassword'

        table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')
        if cert_name_list[rand_value] == table_name_n or table_name_n != rnd_cert_name:
            raise Exception('Wrong certificate name')
        table_uploaded_n = driver.find_element_by_css_selector(cert_table_n_data_img).get_attribute("outerHTML")
        if cert_uploaded_list[rand_value] != table_uploaded_n:
            raise Exception('Wrong certificate upload mark')
        table_cert_type_n = driver.find_element_by_id(cert_table_n_data_type).get_attribute('textContent')
        if cert_type_list[rand_value] == table_cert_type_n or table_cert_type_n != select_type:
            raise Exception('Wrong certificate type')
        table_password_n = driver.find_element_by_id(cert_table_n_data_password).get_attribute('textContent')
        if cert_password_list[rand_value] == table_password_n or table_password_n != rnd_cert_password:
            raise Exception('Wrong certificate password')

        time.sleep(1)
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)

    def test2_pc_edit_gateway(self):
        driver = self.driver
        # driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        cert_table_n_data_name = 'form:certificatesTable:0:certificateName'
        table_name_n = driver.find_element_by_id(cert_table_n_data_name).get_attribute('textContent')

        cert_name = table_name_n

        # Find Gateways quantity
        gateway_quantity = 0
        while gateway_quantity >= 0:
            # print(gateway_quantity)
            row = r'#form\3a gatewaysTable_data > tr:nth-child(' + str(gateway_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(gateway_quantity + 1), 'found')
                gateway_quantity += 1
            else:
                print('gateway_quantity = ', gateway_quantity)
                break

        # Gateways
        gateway_name_list = []
        gateway_client_list = []
        gateway_trust_list = []
        gateway_port_list = []
        gateway_host_list = []

        gateway_row = 0
        while gateway_row <= gateway_quantity - 1:
            print('gateway_row', gateway_row)
            gateway_table_n_name = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayName'
            gateway_table_n_client = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayClient'
            gateway_table_n_trust = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayTrust'
            gateway_table_n_port = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayPort'
            gateway_table_n_host = 'form:gatewaysTable:' + str(gateway_row) + ':gatewayHost'

            gateway_name_n = driver.find_element_by_id(gateway_table_n_name).get_attribute('textContent')
            gateway_name_list.append(gateway_name_n)

            # if gateway_name_n != gateway_name_mod[gateway_row]:
            #     print('gateway_name_n:', gateway_name_n, 'gateway_name_mod:', gateway_name_mod[gateway_row])
            #     raise Exception('Wrong gateway name', gateway_name_n)
            gateway_client_n = driver.find_element_by_id(gateway_table_n_client).get_attribute('textContent')
            gateway_client_list.append(gateway_client_n)

            # if gateway_client_n != client_trust_mod[gateway_row]:
            #     print('gateway_client_n:', gateway_client_n, 'client_trust_mod:', client_trust_mod[gateway_row])
            #     raise Exception('Wrong gateway client')
            gateway_trust_n = driver.find_element_by_id(gateway_table_n_trust).get_attribute('textContent')
            gateway_trust_list.append(gateway_trust_n)

            # if gateway_trust_n != client_trust_mod[gateway_row]:
            #     print('gateway_trust_n:', gateway_trust_n, 'client_trust_mod:', client_trust_mod[gateway_row])
            #     raise Exception('Wrong gateway trust')
            gateway_port_n = driver.find_element_by_id(gateway_table_n_port).get_attribute('textContent')
            gateway_port_list.append(gateway_port_n)

            # if gateway_port_n != gateway_port_mod[gateway_row]:
            #     print('gateway_port_n:', gateway_port_n, 'gateway_port_mod:', gateway_port_mod[gateway_row])
            #     raise Exception('Wrong gateway port')
            gateway_host_n = driver.find_element_by_id(gateway_table_n_host).get_attribute('textContent')
            gateway_host_list.append(gateway_host_n)

            # if gateway_host_n != gateway_host_mod[gateway_row]:
            #     print('gateway_host_n:', gateway_host_n, 'gateway_host_mod:', gateway_host_mod[gateway_row])
            #     raise Exception('Wrong gateway host')
            print('gateway row %s Added' % str(gateway_row + 1))
            gateway_row += 1

        # Edit first Gateway
        gateway_name_1 = '1_new_gateway_name'
        edit_gateway = 'form:gatewaysTable:0:editGateway'
        driver.find_element_by_id(edit_gateway).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))
        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).clear()
        driver.find_element_by_id(CE.config_gateway_name).send_keys(gateway_name_1)
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != cert_name:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != cert_name:
            raise Exception('Wrong Trust dropdown')
        driver.find_element_by_id(CE.config_gateway_port).clear()
        driver.find_element_by_id(CE.config_gateway_port).send_keys('1856')
        driver.find_element_by_id(CE.config_gateway_host).click()
        driver.find_element_by_id(CE.config_gateway_host).clear()
        driver.find_element_by_id(CE.config_gateway_host).send_keys('New_gateway_host')
        driver.find_element_by_id(CE.config_gateway_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_gateway_save)))
        time.sleep(2)

        # Verify first Gateway
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != gateway_name_1 or gateway_name_list[0] == gateway_name:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != cert_name or gateway_client_list[0] == gateway_client:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != cert_name or gateway_trust_list[0] == gateway_trust:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '1856' or gateway_port_list[0] == gateway_port:
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != 'New_gateway_host' or gateway_host_list[0] == gateway_host:
            raise Exception('Wrong gateway host', gateway_host)

        # Edit rnd Gateway
        # I think that there is a mistake
        rand_value = random.randint(1, gateway_quantity - 1)
        print('rand_value', rand_value)
        gateway_name_2 = '2_rnd_gateway_name'
        edit_gateway = 'form:gatewaysTable:' + str(rand_value) + ':editGateway'
        driver.find_element_by_id(edit_gateway).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))
        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).clear()
        driver.find_element_by_id(CE.config_gateway_name).send_keys(gateway_name_2)
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != cert_name:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != cert_name:
            raise Exception('Wrong Trust dropdown')
        driver.find_element_by_id(CE.config_gateway_port).clear()
        driver.find_element_by_id(CE.config_gateway_port).send_keys('1963')
        driver.find_element_by_id(CE.config_gateway_host).clear()
        driver.find_element_by_id(CE.config_gateway_host).send_keys('New_gateway_host_2')
        driver.find_element_by_id(CE.config_gateway_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_gateway_save)))
        time.sleep(2)

        # Verify first Gateway
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != gateway_name_1 or gateway_name_list[rand_value] == gateway_name:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != cert_name or gateway_client_list[rand_value] == gateway_client:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != cert_name or gateway_trust_list[rand_value] == gateway_trust:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '1856' or gateway_port_list[rand_value] == gateway_port:
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != 'New_gateway_host' or gateway_host_list[rand_value] == gateway_host:
            raise Exception('Wrong gateway host', gateway_host)

        time.sleep(1)
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)

    def test1_pc_edit_service(self):
        driver = self.driver
        # driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        gateway_table_n_data_name = 'form:gatewaysTable:0:gatewayName'
        table_name_n = driver.find_element_by_id(gateway_table_n_data_name).get_attribute('textContent')

        gateway_name = table_name_n

        # Find Services quantity
        services_quantity = 0
        while services_quantity >= 0:
            # print(services_quantity)
            row = r'#form\3a servicesTable_data > tr:nth-child(' + str(services_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(services_quantity + 1), 'found')
                services_quantity += 1
            else:
                print('services_quantity = ', services_quantity)
                break

        # Services
        service_name_list = []
        service_value_line2_list = []
        service_value_line2_value_list = []
        service_value_line1_list = []
        service_value_line1_value_list = []

        service_count = 0
        while service_count <= services_quantity - 1:
            print('service_count', service_count)

            service_name_n = driver.find_element_by_css_selector(
                Check.service_name(service_count)).get_attribute('textContent')
            service_name_list.append(service_name_n)

            service_value_line2 = driver.find_elements_by_css_selector(Check.service_value_property_2(service_count))
            if service_value_line2:
                service_value_line2_list.append(service_value_line2[0].get_attribute('textContent'))
            else:
                service_value_line2_list.append(None)

            service_value_line2_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_2(service_count))
            if service_value_line2_value:
                service_value_line2_value_list.append(service_value_line2_value[0].get_attribute('textContent'))
            else:
                service_value_line2_value_list.append(None)

            service_value_line1 = driver.find_elements_by_css_selector(
                Check.service_value_property_1(service_count))
            if service_value_line1:
                service_value_line1_list.append(service_value_line1[0].get_attribute('textContent'))
            else:
                service_value_line1_list.append(None)

            service_value_line1_value = driver.find_elements_by_css_selector(
                Check.service_value_property_value_1(service_count))
            if service_value_line1_value:
                service_value_line1_value_list.append(service_value_line1_value[0].get_attribute('textContent'))
            else:
                service_value_line1_value_list.append(None)

            print('service row %s Added' % str(service_count + 1))
            service_count += 1

        # Edit Service 1
        new_service_name_1 = '1_new_service_name'
        new_property_value_1 = 'Some Property 1'
        new_value_property_1 = 'root'
        edit_service = 'form:servicesTable:0:editService'
        driver.find_element_by_id(edit_service).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).clear()
        driver.find_element_by_id(CE.config_service_name).send_keys(new_service_name_1)
        driver.find_element_by_id(CE.config_service_detail_delete_action).click()
        # Notification check
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification_message = driver.find_element_by_class_name(
                CE.main_notification_title).get_attribute('textContent')
            if notification_message != CO.message_successfully_deleted:
                raise Exception('Wrong notification message')
        # End
        driver.find_element_by_id(CE.config_service_add_button).click()
        driver.find_element_by_id(CE.config_service_add_dialog)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_add_select)))
        driver.find_element_by_id(CE.config_service_add_select).click()
        Check.by_class_name_and_text(driver, CE.menu_list_item, 'root').click()
        driver.find_element_by_id(CE.config_service_add_ok).click()
        time.sleep(1)
        driver.find_element_by_css_selector(CE.config_service_detail_property_value).click()
        driver.find_element_by_css_selector(CE.config_service_detail_property_value).send_keys(new_property_value_1)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_save)))
        driver.find_element_by_id(CE.config_service_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
        time.sleep(1)

        # Verify Service 1
        service_num = 0
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_num)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_num)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_num)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_num)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_num)).get_attribute('textContent')
        if service_name_1 != new_service_name_1 or service_name_list[service_num] == service_name_1:
            raise Exception('Wrong Service name:', service_name_1, 'new_service_name_1:', new_service_name_1,
                            'service_name_list:', service_name_list[service_num])
        if service_value_property != new_value_property_1 or service_value_line2_list[service_num] == service_value_property:
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != new_property_value_1 or service_value_line2_value_list[service_num] == service_value_property_value:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != service_value_line1_list[service_num]:
            raise Exception('Wrong service value gate information:', service_value_gate)
        if service_value_gate_name != service_value_line1_value_list[service_num]:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Edit Service 2
        new_service_name_2 = '2_new_service_name'
        edit_service = 'form:servicesTable:1:editService'
        driver.find_element_by_id(edit_service).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).clear()
        driver.find_element_by_id(CE.config_service_name).send_keys(new_service_name_2)
        driver.find_element_by_id(CE.config_service_select_gateway).click()
        driver.find_element_by_id(CE.config_service_select_gateway_list)
        driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_save)))
        driver.find_element_by_id(CE.config_service_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
        time.sleep(1)

        # Verify Service 2
        service_num = 1
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_num)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_num)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_num)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_num)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_num)).get_attribute('textContent')
        if service_name_1 != new_service_name_2 or service_name_list[service_num] == service_name_1:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property == new_value_property_1 or service_value_line2_list[service_num] != service_value_property:
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value == new_property_value_1 or service_value_line2_value_list[service_num] != service_value_property_value:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != service_value_line1_list[service_num]:
            raise Exception('Wrong service value gate information:', service_value_gate)
        if service_value_gate_name == service_value_line1_value_list[service_num] or service_value_gate_name != gateway_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Edit Service 3
        new_service_name_3 = '3_new_service_name'
        new_property_value_3 = 'Some Property 3'
        new_value_property_3 = 'root'
        edit_service = 'form:servicesTable:2:editService'
        driver.find_element_by_id(edit_service).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).clear()
        driver.find_element_by_id(CE.config_service_name).send_keys(new_service_name_3)
        driver.find_element_by_id(CE.config_service_detail_delete_action).click()
        # Notification check
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification_message = driver.find_element_by_class_name(
                CE.main_notification_title).get_attribute('textContent')
            if notification_message != CO.message_successfully_deleted:
                raise Exception('Wrong notification message')
        # End
        driver.find_element_by_id(CE.config_service_add_button).click()
        driver.find_element_by_id(CE.config_service_add_dialog)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_add_select)))
        driver.find_element_by_id(CE.config_service_add_select).click()
        Check.by_class_name_and_text(driver, CE.menu_list_item, 'root').click()
        driver.find_element_by_id(CE.config_service_add_ok).click()
        time.sleep(1)
        driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
        driver.find_element_by_xpath(CE.config_service_detail_property_value).send_keys(new_property_value_3)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_select_gateway).click()
        driver.find_element_by_id(CE.config_service_select_gateway_list)
        driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_save)))
        driver.find_element_by_id(CE.config_service_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
        time.sleep(1)

        # Verify Service 3
        service_num = 2
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_num)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_num)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_num)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_num)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_num)).get_attribute('textContent')
        if service_name_1 != new_service_name_3 or service_name_list[service_num] == service_name_1:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != new_value_property_3 or service_value_line2_list[service_num] == service_value_property:
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != new_property_value_3 or service_value_line2_value_list[service_num] == service_value_property_value:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != service_value_line1_list[service_num]:
            raise Exception('Wrong service value gate information:', service_value_gate)
        if service_value_gate_name == service_value_line1_value_list[service_num] or service_value_gate_name != gateway_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Edit Service 4
        new_service_name_4 = '4_new_service_name'
        new_property_value_4 = 'Some Property 4'
        new_value_property_4 = 'root'
        edit_service = 'form:servicesTable:3:editService'
        driver.find_element_by_id(edit_service).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).clear()
        driver.find_element_by_id(CE.config_service_name).send_keys(new_service_name_4)
        driver.find_element_by_id(CE.config_service_add_button).click()
        driver.find_element_by_id(CE.config_service_add_dialog)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_add_select)))
        driver.find_element_by_id(CE.config_service_add_select).click()
        Check.by_class_name_and_text(driver, CE.menu_list_item, 'root').click()
        driver.find_element_by_id(CE.config_service_add_ok).click()
        time.sleep(1)
        driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
        driver.find_element_by_xpath(CE.config_service_detail_property_value).send_keys(new_property_value_4)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_select_gateway).click()
        driver.find_element_by_id(CE.config_service_select_gateway_list)
        driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_save)))
        driver.find_element_by_id(CE.config_service_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
        time.sleep(1)

        # Verify Service 4
        service_num = 3
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_num)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_num)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_num)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_num)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_num)).get_attribute('textContent')
        if service_name_1 != new_service_name_4 or service_name_list[service_num] == service_name_1:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != new_value_property_4 or service_value_line2_list[service_num] == service_value_property:
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != new_property_value_4 or service_value_line2_value_list[service_num] == service_value_property_value:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate == service_value_line1_list[service_num]:
            raise Exception('Wrong service value gate information:', service_value_gate)
        if service_value_gate_name == service_value_line1_value_list[service_num] or service_value_gate_name != gateway_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Edit Service 5
        new_service_name_5 = '5_new_service_name'
        # new_property_value_5 = 'Some Property 5'
        # new_value_property_5 = 'get'
        edit_service = 'form:servicesTable:4:editService'
        driver.find_element_by_id(edit_service).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).clear()
        driver.find_element_by_id(CE.config_service_name).send_keys(new_service_name_5)
        time.sleep(1)
        driver.find_element_by_id(CE.config_service_select_gateway).click()
        driver.find_element_by_id(CE.config_service_select_gateway_list)
        driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_save)))
        driver.find_element_by_id(CE.config_service_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
        time.sleep(1)

        # Verify Service 5
        service_num = 4
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_num)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_num)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_num)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_num)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_num)).get_attribute('textContent')
        if service_name_1 != new_service_name_5 or service_name_list[service_num] == service_name_1:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_line1_list[service_num] != service_value_property:
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_line1_value_list[service_num] != service_value_property_value:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate == service_value_line2_list[service_num] or service_value_gate != 'gate':
            raise Exception('Wrong service value gate information:', service_value_gate)
        if service_value_gate_name == service_value_line2_value_list[service_num] or service_value_gate_name != gateway_name:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        # Edit Service 6
        new_service_name_6 = '6_new_service_name'
        new_property_value_6 = 'Some Property 6'
        new_value_property_6 = 'root'
        edit_service = 'form:servicesTable:5:editService'
        driver.find_element_by_id(edit_service).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
        driver.find_element_by_id(CE.config_service_name).click()
        driver.find_element_by_id(CE.config_service_name).clear()
        driver.find_element_by_id(CE.config_service_name).send_keys(new_service_name_6)
        driver.find_element_by_id(CE.config_service_add_button).click()
        driver.find_element_by_id(CE.config_service_add_dialog)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_add_select)))
        driver.find_element_by_id(CE.config_service_add_select).click()
        Check.by_class_name_and_text(driver, CE.menu_list_item, 'root').click()
        driver.find_element_by_id(CE.config_service_add_ok).click()
        time.sleep(1)
        driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
        driver.find_element_by_xpath(CE.config_service_detail_property_value).send_keys(new_property_value_6)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_save)))
        driver.find_element_by_id(CE.config_service_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
        time.sleep(1)

        # Verify Service 6
        service_num = 5
        service_name_1 = driver.find_element_by_css_selector(
            Check.service_name(service_num)).get_attribute('textContent')
        service_value_property = driver.find_element_by_css_selector(
            Check.service_value_property_2(service_num)).get_attribute('textContent')
        service_value_property_value = driver.find_element_by_css_selector(
            Check.service_value_property_value_2(service_num)).get_attribute('textContent')
        service_value_gate = driver.find_element_by_css_selector(
            Check.service_value_property_1(service_num)).get_attribute('textContent')
        service_value_gate_name = driver.find_element_by_css_selector(
            Check.service_value_property_value_1(service_num)).get_attribute('textContent')
        if service_name_1 != new_service_name_6 or service_name_list[service_num] == service_name_1:
            raise Exception('Wrong Service name:', service_name_1)
        if service_value_property != new_value_property_6 or service_value_line2_list[service_num] == service_value_property:
            raise Exception('Wrong service property name information:', service_value_property)
        if service_value_property_value != new_property_value_6 or service_value_line2_value_list[service_num] == service_value_property_value:
            raise Exception('Wrong service property value information:', service_value_property_value)
        if service_value_gate != service_value_line1_list[service_num]:
            raise Exception('Wrong service value gate information:', service_value_gate)
        if service_value_gate_name != service_value_line1_value_list[service_num]:
            raise Exception('Wrong service value gate name information:', service_value_gate_name)

        time.sleep(1)
        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(1)


class ProvisioningConfig08Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # downloads_folder = r'C:\Users\Guest-user\Downloads\\'
        downloads_folder = os.path.expanduser('~/Downloads')
        # print(downloads_folder)
        set_driver = driver_settings.driver_with_firefox_json_download(cls, downloads_folder)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("browser.download.manager.showWhenStarting", False)
        # profile.set_preference("browser.download.folderList", 2)
        # profile.set_preference("browser.download.dir", downloads_folder)
        # profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/json")
        # profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        # cls.driver = webdriver.Firefox(profile)

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        pass

    def test1_pc_download_config(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Select config
        Check.select_config(driver, wait, CO.current_config)

        # Download
        downloads_folder = os.path.expanduser('~/Downloads')
        driver.find_element_by_id(CE.config_download).click()
        time.sleep(1)
        file_path = str(downloads_folder) + '\edapt-demo(1).json'
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

        time.sleep(2)
        os.remove(file_path)
        print('Remove - OK')


class ProvisioningConfig09Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        downloads_folder = os.path.expanduser('~/Downloads')
        set_driver = driver_settings.driver_with_firefox_octet_download(cls, downloads_folder)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("browser.download.manager.showWhenStarting", False)
        # profile.set_preference("browser.download.folderList", 2)
        # profile.set_preference("browser.download.dir", downloads_folder)
        # profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        # cls.driver = webdriver.Firefox(profile)

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        pass

    def test1_pc_download_certificates(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Select config
        Check.select_config(driver, wait, CO.current_config)

        # Download
        downloads_folder = os.path.expanduser('~/Downloads')
        driver.find_element_by_id(CE.config_download_certificate_1).click()
        time.sleep(1)
        file_path = str(downloads_folder) + '\in_app_proxy_cert(1)'
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

        time.sleep(2)
        os.remove(file_path)
        print('Remove - OK')


class ProvisioningConfig10Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')
        driver = cls.driver

        # Delete config
        driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
            Check.select_config(driver, wait, CO.upcoming_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
        # Delete end

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        driver = cls.driver

        if len(driver.find_elements_by_id(CE.config_item_1)) == 0:
            # Upload config
            address = files_path + r"\main_test_env.json"
            print(address, address)
            time.sleep(1)
            element = driver.find_element_by_id(CE.config_select_file)
            element.send_keys(address)
            file_name = 'main_test_env.json'
            upload_file_name = driver.find_element_by_class_name(CE.file_name_for_upload).get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')
            driver.find_element_by_id(CE.config_upload).click()

            # Save config
            driver.find_element_by_id(CE.config_apply).click()
            Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)
        driver = self.driver

        wait = WebDriverWait(self.driver, 15)

        if len(driver.find_elements_by_id(CE.config_item_1)) == 0:
            # Upload config
            address = files_path + r"\main_test_env.json"
            print(address, address)
            time.sleep(1)
            element = driver.find_element_by_id(CE.config_select_file)
            element.send_keys(address)
            file_name = 'main_test_env.json'
            upload_file_name = driver.find_element_by_class_name(CE.file_name_for_upload).get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')
            driver.find_element_by_id(CE.config_upload).click()

            # Save config
            driver.find_element_by_id(CE.config_apply).click()
            Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        # Add config
        now_day = self.now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        wait.until(EC.invisibility_of_element_located((By.ID, 'configRemoveConfirmDlg_modal')))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add).click()
        time.sleep(1)
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day_highlight, now_day)
        picker_day_to_select.click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_start_time_ok_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(2)
        driver.find_element_by_id(CE.config_cert_name).click()
        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoTest_' + self.time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(1)
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_cert_modal)))

        # Apply
        driver.find_element_by_id(CE.config_apply).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

    def tearDown(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 15)
        driver = self.driver
        # wait.until(EC.invisibility_of_element_located((By.ID, CE.config_start_time_for_expired_config_modal)))
        driver.get(self.test_pc_url)
        time.sleep(1)

        # Delete config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
            if not driver.find_element_by_id(CE.config_select_list):
                raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
            Check.select_config(driver, wait, CO.upcoming_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(CE.main_notification_title).get_attribute(
                    'textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
            if not driver.find_element_by_id(CE.config_select_list):
                raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_1)) > 0:
            Check.select_config(driver, wait, CO.current_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(CE.main_notification_title).get_attribute(
                    'textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
        # Delete end

    def test1_pc_error_panel_delete_current(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Error panel
        driver.find_element_by_id(CE.config_error_panel)
        driver.find_element_by_id(CE.config_delete_expired_config)
        driver.find_element_by_id(CE.config_make_upcoming)

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        driver.find_element_by_id(CE.config_delete).click()
        time.sleep(1)
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        cert_quantity = 0
        while cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(cert_quantity + 1), 'found')
                cert_quantity += 1
            else:
                print('cert_quantity = ', cert_quantity)
                break

        if cert_quantity <= 1:
            raise Exception('Wrong certificate quantity:', cert_quantity)

    def test2_pc_error_panel_make_upcoming(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Error panel
        driver.find_element_by_id(CE.config_error_panel)
        driver.find_element_by_id(CE.config_delete_expired_config)
        driver.find_element_by_id(CE.config_make_upcoming)

        # Set today
        driver.find_element_by_id(CE.config_make_upcoming).click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_start_time_for_expired_config)

        now_day = self.now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day_highlight, now_day)
        picker_day_to_select.click()

        # Notification check 1
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = Check.by_class_name_and_text(driver, CE.main_notification_title,
                                                        CO.certificate_invalid_date_for_config)
            if not notification:
                raise Exception('Notification missing')

        # Set date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        if tomorrow_day[0] == '0':
            tomorrow_day = tomorrow_day[1]
            print('tomorrow_day', tomorrow_day)
        tomorrow_month_decimal = tomorrow.strftime('%m')
        if tomorrow_month_decimal[0] == '0':
            tomorrow_month_decimal = tomorrow_month_decimal[1]
            print('tomorrow_month_decimal', tomorrow_month_decimal)
        tomorrow_year = tomorrow.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_tomorrow = tomorrow_month_decimal + '/' + tomorrow_day + '/' + tomorrow_year[-2:]

        driver.find_element_by_id(CE.config_time_for_expired_input).click()

        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')
        time.sleep(1)
        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
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
        if now_day == str(last_day_of_month[1]):
            time.sleep(1)
            driver.find_element_by_class_name(CE.config_date_picker_next).click()
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day, tomorrow_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)
        time_input_field = driver.find_element_by_id(CE.config_time_for_expired_input).get_attribute(name='value')
        # if not time_input_field != start_time_set_tomorrow:
        #     raise Exception('Wrong field input:', time_input_field, 'start_time_set_tomorrow:', start_time_set_tomorrow)
        driver.find_element_by_id(CE.config_ok_for_expired_input).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        cert_quantity = 0
        while cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(cert_quantity + 1), 'found')
                cert_quantity += 1
            else:
                print('cert_quantity = ', cert_quantity)
                break

        if cert_quantity != 1:
            raise Exception('Wrong certificate quantity:', cert_quantity)

        # Select upcoming config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)
        time.sleep(1)

        cert_quantity = 0
        while cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(cert_quantity + 1), 'found')
                cert_quantity += 1
            else:
                print('cert_quantity = ', cert_quantity)
                break

        if cert_quantity != 4:
            raise Exception('Wrong certificate quantity:', cert_quantity)

    def test3_pc_error_panel_delete_expired(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Error panel
        driver.find_element_by_id(CE.config_error_panel)
        driver.find_element_by_id(CE.config_delete_expired_config)
        driver.find_element_by_id(CE.config_make_upcoming)

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        # Delete
        driver.find_element_by_id(CE.config_delete_expired_config).click()
        time.sleep(1)

        if driver.find_elements_by_id(CE.config_error_panel):
            raise Exception('Error panel exist')

        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
            if not driver.find_element_by_id(CE.config_select_list):
                raise Exception('The list of configs is missing')

        if driver.find_elements_by_id(CE.config_item_2):
            raise Exception('Config still exist')

        cert_quantity = 0
        while cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(cert_quantity + 1), 'found')
                cert_quantity += 1
            else:
                print('cert_quantity = ', cert_quantity)
                break

        if cert_quantity < 1:
            raise Exception('Wrong certificate quantity:', cert_quantity)


class ProvisioningConfig11Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        time.sleep(1)
        cls.now = datetime.datetime.now()
        cls.time_for_name = cls.now.strftime('D%d_H%H_M%M_S%S')
        driver = cls.driver

        # Delete config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_2)) > 0:
            Check.select_config(driver, wait, CO.upcoming_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
        if len(driver.find_elements_by_id(CE.config_item_1)) > 0:
            Check.select_config(driver, wait, CO.current_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(1)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()

        # Delete end

        # Upload config
        address = files_path + r"\main_test_env.json"
        print(address, address)
        time.sleep(1)
        element = driver.find_element_by_id(CE.config_select_file)
        element.send_keys(address)
        file_name = 'main_test_env.json'
        upload_file_name = driver.find_element_by_class_name(CE.file_name_for_upload).\
            get_attribute('textContent')
        if upload_file_name != file_name:
            raise Exception('The selected file has wrong name')
        driver.find_element_by_id(CE.config_upload).click()

        # Save config
        driver.find_element_by_id(CE.config_apply).click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)
        driver = self.driver

        wait = WebDriverWait(self.driver, 15)

        # Add config
        now_day = self.now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        driver.find_element_by_id(CE.config_add).click()
        wait.until(EC.presence_of_element_located((By.ID, CE.config_date_picker_div)))
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, CE.config_date_picker_day_highlight)))

        time.sleep(1)
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day_highlight, now_day)
        picker_day_to_select.click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_start_time_ok_button).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(2)
        driver.find_element_by_id(CE.config_cert_name).click()
        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoTest_' + self.time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(2)
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_cert_modal)))

        # Apply
        driver.find_element_by_id(CE.config_apply).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

    def tearDown(self):
        pass

    # @unittest.skip('skip')
    def test1_pc_error_panel_no_current_config(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)

        # Error panel
        driver.find_element_by_id(CE.config_error_panel)
        driver.find_element_by_id(CE.config_delete_expired_config)
        driver.find_element_by_id(CE.config_make_upcoming)

        # Make upcoming
        driver.find_element_by_id(CE.config_make_upcoming).click()
        time.sleep(1)

        # Set date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        if tomorrow_day[0] == '0':
            tomorrow_day = tomorrow_day[1]
            print('tomorrow_day', tomorrow_day)
        tomorrow_month_decimal = tomorrow.strftime('%m')
        if tomorrow_month_decimal[0] == '0':
            tomorrow_month_decimal = tomorrow_month_decimal[1]
            print('tomorrow_month_decimal', tomorrow_month_decimal)
        tomorrow_year = tomorrow.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        start_time_set_tomorrow = tomorrow_month_decimal + '/' + tomorrow_day + '/' + tomorrow_year[-2:]

        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')
        time.sleep(1)
        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
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
        if now_day == str(last_day_of_month[1]):
            driver.find_element_by_class_name(CE.config_date_picker_next).click()
        driver.find_element_by_id(CE.config_time_for_expired_input).click()
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day, tomorrow_day)
        time.sleep(1)
        picker_day_to_select.click()
        time.sleep(1)
        driver.find_element_by_id(CE.config_ok_for_expired_input).click()
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        # Delete current config
        driver.find_element_by_id(CE.config_delete).click()
        time.sleep(1)
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
        time.sleep(2)

        # Error panel
        error_message = driver.find_element_by_id(CE.config_error_panel).get_attribute('textContent')
        if CO.error_do_not_have_current_config not in error_message:
            raise Exception('Wrong error message:', error_message)

        # Select upcoming config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
        Check.select_config(driver, wait, CO.upcoming_config)

        # Open Start time dialog
        driver.find_element_by_id(CE.config_start_time).click()
        wait.until(EC.presence_of_element_located((By.ID, CE.config_date_picker_div)))

        # Set yesterday date
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_month_decimal = now.strftime('%m')
        if now_month_decimal[0] == '0':
            now_month_decimal = now_month_decimal[1]
            print('now_month_decimal', now_month_decimal)
        now_day = now.strftime('%d')
        if now_day[0] == '0':
            now_day = now_day[1]
            print('now_day', now_day)

        yesterday = now - datetime.timedelta(days=1)
        yesterday_day = yesterday.strftime('%d')
        if yesterday_day[0] == '0':
            yesterday_day = yesterday_day[1]
            print('yesterday_day', yesterday_day)
        yesterday_month_decimal = yesterday.strftime('%m')
        if yesterday_month_decimal[0] == '0':
            yesterday_month_decimal = yesterday_month_decimal[1]
            print('yesterday_month_decimal', yesterday_month_decimal)
        yesterday_year = yesterday.strftime('%Y')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        print('last_day_of_month[1]', last_day_of_month[1])
        # start_time_set_yesterday = yesterday_month_decimal + '/' + yesterday_day + '/' + yesterday_year[-2:]

        picker_year = driver.find_element_by_class_name(CE.config_date_picker_year).get_attribute('textContent')
        picker_month = driver.find_element_by_class_name(CE.config_date_picker_month).get_attribute('textContent')
        time.sleep(1)
        for picker_elem in driver.find_elements_by_class_name(CE.config_date_picker_day):
            if CE.config_date_picker_day_highlight in picker_elem.get_attribute(name='class'):
                picker_day = picker_elem.get_attribute('textContent')

        # if now_year != picker_year:
        #     print('now_year', now_year, '- picker_year', picker_year)
        #     raise Exception('Year does not match')
        # if now_month != picker_month:
        #     print('now_month', now_month, '- picker_month', picker_month)
        #     raise Exception('Month does not match')
        # if now_day != picker_day:
        #     print('now_day', now_day, '- picker_day', picker_day)
        #     raise Exception('Day does not match')
        if now_day == '31':
            driver.find_element_by_class_name(CE.config_date_picker_prev).click()
        print('yesterday_day', yesterday_day)
        picker_day_to_select = Check.by_class_name_and_text(driver, CE.config_date_picker_day, now_day)
        time.sleep(1)
        picker_day_to_select.click()

        # Notification check 1
        if driver.find_elements_by_class_name(CE.main_notification_title):
            notification = Check.by_class_name_and_text(driver, CE.main_notification_title, CO.start_time_changed)
            if not notification:
                raise Exception('Notification missing')

        driver.find_element_by_id(CE.config_apply).click()
        time.sleep(2)

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        cert_quantity = 0
        while cert_quantity >= 0:
            # print(cert_quantity)
            row = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_quantity + 1) + ')'
            if driver.find_elements_by_css_selector(row):
                print('Row', str(cert_quantity + 1), 'found')
                cert_quantity += 1
            else:
                print('cert_quantity = ', cert_quantity)
                break

        if cert_quantity != 4:
            raise Exception('Wrong certificate quantity:', cert_quantity)


class ProvisioningConfig12Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()

        cls.test_pc_url = server_address + '/page/provision-config.jsf'
        cls.driver.get(cls.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(cls.driver, 15)
        Check.login(cls.driver, wait, EC, By)
        cls.autotest_name = '0_AutoTest_'

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver

        config_item_1 = driver.find_elements_by_id(CE.config_item_1)
        if not config_item_1:

            # Upload config
            address = files_path + r"\main_test_env.json"
            print(address, address)
            time.sleep(1)
            element = driver.find_element_by_id(CE.config_select_file)
            element.send_keys(address)
            file_name = 'main_test_env.json'
            upload_file_name = driver.find_element_by_class_name(CE.file_name_for_upload).\
                get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')
            driver.find_element_by_id(CE.config_upload).click()
            if driver.find_elements_by_class_name(CE.main_notification_title):
                if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.upload_config_do_not_forget):
                    raise Exception('Wrong notification message')

            # Save config
            driver.find_element_by_id(CE.config_apply).click()
        cls.driver.quit()

    def setUp(self):
        print('\n', self._testMethodName)
        self.driver.implicitly_wait(10)
        driver = self.driver

        config_item_1 = driver.find_elements_by_id(CE.config_item_1)
        if not config_item_1:

            # Upload config
            address = files_path + r"\main_test_env.json"
            print(address, address)
            time.sleep(1)
            element = driver.find_element_by_id(CE.config_select_file)
            element.send_keys(address)
            file_name = 'main_test_env.json'
            upload_file_name = driver.find_element_by_class_name(CE.file_name_for_upload).\
                get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')
            driver.find_element_by_id(CE.config_upload).click()
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
                if CO.upload_config_do_not_forget not in notification:
                    raise Exception('Wrong notification message')

            # Save config
            driver.find_element_by_id(CE.config_apply).click()

    def tearDown(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        driver.get(self.test_pc_url)
        time.sleep(1)

        # Delete config
        if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
            driver.find_element_by_id(CE.config_select_label).click()
            if not driver.find_element_by_id(CE.config_select_list):
                raise Exception('The list of configs is missing')
        if len(driver.find_elements_by_id(CE.config_item_1)) > 0:
            time.sleep(2)
            Check.select_config(driver, wait, CO.current_config)
            time.sleep(1)
            driver.find_element_by_id(CE.config_delete).click()
            time.sleep(2)
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Yes').click()
            if driver.find_elements_by_class_name(CE.main_notification_title):
                notification_message = driver.find_element_by_class_name(CE.main_notification_title).get_attribute(
                    'textContent')
                if notification_message != CO.message_successfully_deleted:
                    print('notification_message', notification_message)
                    raise Exception('Wrong notification message')
        # Delete end

    def test1_pc_add_first_certificate(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)
        autotest_name = self.autotest_name

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(2)

        # Notification check 1
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.certificate_missing_name):
                raise Exception('Wrong notification message')
        # End

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        data_file_upload = 0
        while data_file_upload < 2:
            time.sleep(1)
            element = driver.find_element_by_id(CE.config_cert_select_file)
            element.send_keys(address)
            file_name = 'in_app_proxy_cert'
            upload_file_name = driver.find_element_by_css_selector(CE.config_cert_upload_file_name).\
                get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')
            file_size = '2.5 KB'
            upload_file_size = driver.find_element_by_css_selector(CE.config_cert_upload_file_size).\
                get_attribute('textContent')
            if upload_file_size != file_size:
                raise Exception('The selected file has wrong size')
            if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 1:
                raise Exception('Progress bar is missing')
            Check.by_class_name_and_text(driver, CE.config_buttons, CO.ui_button)
            driver.find_element_by_id(CE.config_cert_false_uploaded)
            cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
            if CO.ui_state_disabled not in cert_type_class:
                raise Exception(CO.ui_state_disabled, 'not found')
            cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
            if CO.ui_state_disabled not in cert_pass_class:
                raise Exception(CO.ui_state_disabled, 'not found')

            if data_file_upload == 0:
                data_file_upload += 1
                # Select Cancel
                driver.find_element_by_xpath(CE.config_cert_cancel_upload).click()
                driver.find_element_by_id(CE.config_cert_false_uploaded)
                cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
                if CO.ui_state_disabled not in cert_type_class:
                    raise Exception(CO.ui_state_disabled, 'not found')
                cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
                if CO.ui_state_disabled not in cert_pass_class:
                    raise Exception(CO.ui_state_disabled, 'not found')
            else:
                data_file_upload += 1
                # Select upload
                Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
                driver.find_element_by_id(CE.config_cert_true_uploaded)

        if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 0:
            raise Exception('Progress bar is exist')
        cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
        if CO.ui_state_disabled in cert_type_class:
            raise Exception(CO.ui_state_disabled, 'is found')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        driver.find_element_by_id(CE.config_cert_name).send_keys(autotest_name + time_for_name)
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != CO.select_type:
            raise Exception('Certificate type contain wrong information')
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        driver.find_element_by_id(CE.config_cert_select_type_list)
        Check.by_id_and_text(driver, CE.config_cert_type_item_1, 'der').click()
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != 'der':
            raise Exception('Certificate type contain wrong information')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        driver.find_element_by_id(CE.config_cert_select_type_list)
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != 'p12':
            raise Exception('Certificate type contain wrong information')
        time.sleep(2)
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'is found')
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_cert_save_changes)))

        # Save config
        driver.find_element_by_id(CE.config_apply).click()
        # Select current config
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        Check.select_config(driver, wait, CO.current_config)

        # Verify Certificate Added
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != autotest_name + time_for_name:
            print('table_name_0', table_name_0)
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'p12':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 != 'cert_pass_' + time_for_name:
            raise Exception('Wrong password')

    def test2_pc_add_second_certificate(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)
        autotest_name = self.autotest_name

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        data_file_upload = 0
        while data_file_upload < 2:
            time.sleep(1)
            element = driver.find_element_by_id(CE.config_cert_select_file)
            element.send_keys(address)
            file_name = 'in_app_proxy_cert'
            upload_file_name = driver.find_element_by_css_selector(CE.config_cert_upload_file_name).\
                get_attribute('textContent')
            if upload_file_name != file_name:
                raise Exception('The selected file has wrong name')
            file_size = '2.5 KB'
            upload_file_size = driver.find_element_by_css_selector(CE.config_cert_upload_file_size).\
                get_attribute('textContent')
            if upload_file_size != file_size:
                raise Exception('The selected file has wrong size')
            if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 1:
                raise Exception('Progress bar is missing')
            Check.by_class_name_and_text(driver, CE.config_buttons, CO.ui_button)
            driver.find_element_by_id(CE.config_cert_false_uploaded)
            cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
            if CO.ui_state_disabled not in cert_type_class:
                raise Exception(CO.ui_state_disabled, 'not found')
            cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
            if CO.ui_state_disabled not in cert_pass_class:
                raise Exception(CO.ui_state_disabled, 'not found')

            if data_file_upload == 0:
                data_file_upload += 1
                # Select Cancel
                driver.find_element_by_xpath(CE.config_cert_cancel_upload).click()
                driver.find_element_by_id(CE.config_cert_false_uploaded)
                cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
                if CO.ui_state_disabled not in cert_type_class:
                    raise Exception(CO.ui_state_disabled, 'not found')
                cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
                if CO.ui_state_disabled not in cert_pass_class:
                    raise Exception(CO.ui_state_disabled, 'not found')
            else:
                data_file_upload += 1
                # Select upload
                Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
                driver.find_element_by_id(CE.config_cert_true_uploaded)

        if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 0:
            raise Exception('Progress bar is exist')
        cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
        if CO.ui_state_disabled in cert_type_class:
            raise Exception(CO.ui_state_disabled, 'is found')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        driver.find_element_by_id(CE.config_cert_name).send_keys(autotest_name + time_for_name)
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != CO.select_type:
            raise Exception('Certificate type contain wrong information')
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        driver.find_element_by_id(CE.config_cert_select_type_list)
        Check.by_id_and_text(driver, CE.config_cert_type_item_1, 'der').click()
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != 'der':
            raise Exception('Certificate type contain wrong information')
        time.sleep(1)
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        time.sleep(1)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_cert_save_changes)))
        time.sleep(3)

        # Save config
        driver.find_element_by_id(CE.config_apply).click()
        # Select current config
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        Check.select_config(driver, wait, CO.current_config)

        # Verify Certificate Added
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != autotest_name + time_for_name:
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_ok_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != 'der':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 is not '':
            print('table_password_0', table_password_0)
            raise Exception('Password field is not empty')

    def test3_pc_add_third_certificate(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)
        autotest_name = self.autotest_name

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        if len(driver.find_elements_by_class_name(CE.config_cert_progress_bar)) != 0:
            raise Exception('Progress bar is exist')
        cert_type_class = driver.find_element_by_id(CE.config_cert_type).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_type_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        cert_pass_class = driver.find_element_by_id(CE.config_cert_password).get_attribute(name='class')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        driver.find_element_by_id(CE.config_cert_name).send_keys(autotest_name + time_for_name)
        cert_type_dd_text = driver.find_element_by_id(CE.config_cert_type_drop_down).get_attribute('textContent')
        if cert_type_dd_text != CO.select_type:
            raise Exception('Certificate type contain wrong information')
        if CO.ui_state_disabled not in cert_pass_class:
            raise Exception(CO.ui_state_disabled, 'not found')
        time.sleep(1)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(3)

        # Save config
        driver.find_element_by_id(CE.config_apply).click()
        # Select current config
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        Check.select_config(driver, wait, CO.current_config)

        # Verify Certificate Added
        table_name_0 = driver.find_element_by_id(CE.cert_table_0_data_name).get_attribute('textContent')
        if table_name_0 != autotest_name + time_for_name:
            print('table_name_0', table_name_0)
            raise Exception('Name is wrong or missing')

        table_uploaded_0 = driver.find_element_by_css_selector(CE.cert_table_0_data_img).get_attribute("outerHTML")
        if CO.table_x_mark not in table_uploaded_0:
            raise Exception('Wrong mark img')
        table_cert_type_0 = driver.find_element_by_id(CE.cert_table_0_data_type).get_attribute('textContent')
        if table_cert_type_0 != '':
            raise Exception('Wrong type')

        table_password_0 = driver.find_element_by_id(CE.cert_table_0_data_password).get_attribute('textContent')
        if table_password_0 is not '':
            print('table_password_0', table_password_0)
            raise Exception('Password field is not empty')

        # time.sleep(5)

    def test4_pc_add_multiple_certificates(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)
        autotest_name = self.autotest_name

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        # Select current config
        Check.select_config(driver, wait, CO.current_config)
        time.sleep(2)

        # Add certificates
        certs = 1
        while certs < 5:
            time.sleep(3)
            print(certs)
            driver.find_element_by_id(CE.config_add_certificate).click()
            time.sleep(2)

            address = files_path + "\in_app_proxy_cert"
            element = driver.find_element_by_id(CE.config_cert_select_file)
            element.send_keys(address)
            # Select upload
            Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
            wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
            driver.find_element_by_id(CE.config_cert_true_uploaded)
            driver.find_element_by_id(CE.config_cert_name).send_keys(autotest_name + 'cert_' + str(certs))

            if certs < 3:
                driver.find_element_by_id(CE.config_cert_type_drop_down).click()
                Check.by_id_and_text(driver, CE.config_cert_type_item_1, 'der').click()
                time.sleep(1)
                driver.find_element_by_id(CE.config_cert_save_changes).click()
                certs += 1
            elif certs < 5:
                driver.find_element_by_id(CE.config_cert_type_drop_down).click()
                Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
                time.sleep(2)
                driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + str(certs))
                driver.find_element_by_id(CE.config_cert_save_changes).click()
                certs += 1
        while 4 < certs < 7:
            time.sleep(3)
            print(certs)
            driver.find_element_by_id(CE.config_add_certificate).click()
            time.sleep(1)
            driver.find_element_by_id(CE.config_cert_name).send_keys(autotest_name + 'cert_' + str(certs))
            driver.find_element_by_id(CE.config_cert_save_changes).click()
            certs += 1

        # Save config
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_apply)))
        time.sleep(3)
        driver.find_element_by_id(CE.config_apply).click()
        # Select current config
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        Check.select_config(driver, wait, CO.current_config)

        # Verify Certificate Added
        cert_srting = 0
        while cert_srting <= 5:
            cert_table_data_name = 'form:certificatesTable:' + str(cert_srting) + ':certificateName'
            cert_table_data_img = r'#form\3a certificatesTable_data > tr:nth-child(' + str(cert_srting + 1) + ') > td:nth-child(2) > img'
            cert_table_data_type = 'form:certificatesTable:' + str(cert_srting) + ':certificateType'
            cert_table_data_password = 'form:certificatesTable:' + str(cert_srting) + ':certificatePassword'
            table_name = autotest_name + 'cert_' + str(cert_srting + 1)
            if cert_srting < 2:
                time.sleep(1)
                cert_srting += 1
                table_name_n = driver.find_element_by_id(cert_table_data_name).get_attribute('textContent')
                if table_name_n != table_name:
                    raise Exception('Name is wrong or missing', table_name_n, '!=', table_name)
                table_uploaded_n = driver.find_element_by_css_selector(cert_table_data_img).get_attribute("outerHTML")
                if CO.table_ok_mark not in table_uploaded_n:
                    raise Exception('Wrong mark img')
                table_cert_type_n = driver.find_element_by_id(cert_table_data_type).get_attribute('textContent')
                if table_cert_type_n != 'der':
                    raise Exception('Wrong type')
                table_password_n = driver.find_element_by_id(cert_table_data_password).get_attribute('textContent')
                if table_password_n != '':
                    raise Exception('Wrong password')
            elif 1 < cert_srting < 4:
                cert_srting += 1
                table_name_n = driver.find_element_by_id(cert_table_data_name).get_attribute('textContent')
                if table_name_n != table_name:
                    raise Exception('Name is wrong or missing', table_name_n, '!=', table_name)
                table_uploaded_n = driver.find_element_by_css_selector(cert_table_data_img).get_attribute("outerHTML")
                if CO.table_ok_mark not in table_uploaded_n:
                    raise Exception('Wrong mark img')
                table_cert_type_n = driver.find_element_by_id(cert_table_data_type).get_attribute('textContent')
                if table_cert_type_n != 'p12':
                    raise Exception('Wrong type')
                table_password_n = driver.find_element_by_id(cert_table_data_password).get_attribute('textContent')
                if table_password_n != 'cert_pass_' + str(cert_srting):
                    raise Exception('Wrong password')

            elif 3 < cert_srting < 6:
                cert_srting += 1
                table_name_n = driver.find_element_by_id(cert_table_data_name).get_attribute('textContent')
                if table_name_n != table_name:
                    raise Exception('Name is wrong or missing', table_name_n, '!=', table_name)
                table_uploaded_n = driver.find_element_by_css_selector(cert_table_data_img).get_attribute("outerHTML")
                if CO.table_x_mark not in table_uploaded_n:
                    raise Exception('Wrong mark img')
                table_cert_type_n = driver.find_element_by_id(cert_table_data_type).get_attribute('textContent')
                if table_cert_type_n != '':
                    raise Exception('Wrong type')
                table_password_n = driver.find_element_by_id(cert_table_data_password).get_attribute('textContent')
                if table_password_n != '':
                    raise Exception('Wrong password')

    def test5_pc_add_certificate_and_gateway(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)
        autotest_name = self.autotest_name

        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%B')
        now_day = now.strftime('%d')
        tomorrow = now + datetime.timedelta(days=1)
        tomorrow_day = tomorrow.strftime('%d')
        last_day_of_month = calendar.monthrange(int(now_year), int(now.strftime('%m')))
        # print('last_day_of_month[1]', last_day_of_month[1])

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        # wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_select_file)))
        time.sleep(2)
        element = driver.find_element_by_id(CE.config_cert_select_file)
        element.send_keys(address)

        # Select upload
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
        driver.find_element_by_id(CE.config_cert_true_uploaded)

        driver.find_element_by_id(CE.config_cert_name).send_keys('0_AutoCert_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_cert_password)))
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        time.sleep(1)

        # Add Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))

        # Notification check 1
        driver.find_element_by_id(CE.config_gateway_save).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_missing_name):
                raise Exception('Wrong notification message')
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_missing_client):
                raise Exception('Wrong notification message')
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_missing_trust):
                raise Exception('Wrong notification message')
        # End

        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('0_AutoGateway_' + time_for_name)
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != CO.gateway_select_type:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != CO.gateway_select_type:
            raise Exception('Wrong Trust dropdown')
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != '0_AutoCert_' + time_for_name:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != '0_AutoCert_' + time_for_name:
            raise Exception('Wrong Trust dropdown')

        # Notification check 2
        time.sleep(2)
        driver.find_element_by_id(CE.config_gateway_port).send_keys('wrong')
        driver.find_element_by_id(CE.config_gateway_save).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_invalid_format):
                print(driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent'))
                raise Exception('Wrong notification message')
        driver.find_element_by_id(CE.config_gateway_port).clear()
        # End

        driver.find_element_by_id(CE.config_gateway_port).send_keys('6666')
        driver.find_element_by_id(CE.config_gateway_host).send_keys('AutoHost_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_gateway_save)))

        # Save config
        driver.find_element_by_id(CE.config_apply).click()
        # Select current config
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        Check.select_config(driver, wait, CO.current_config)

        # Verify Gateway Added
        gateway_name = driver.find_element_by_id(CE.gateway_table_0_name).get_attribute('textContent')
        if gateway_name != '0_AutoGateway_' + time_for_name:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_0_client).get_attribute('textContent')
        if gateway_client != '0_AutoCert_' + time_for_name:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_0_trust).get_attribute('textContent')
        if gateway_trust != '0_AutoCert_' + time_for_name:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_0_port).get_attribute('textContent')
        if gateway_port != '6666':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_0_host).get_attribute('textContent')
        if gateway_host != 'AutoHost_' + time_for_name:
            raise Exception('Wrong gateway host', gateway_host)

        now = datetime.datetime.now()
        time_for_name_2 = now.strftime('D%d_H%H_M%M_S%S')

        # Add second Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))

        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('0_AutoGateway_' + time_for_name)
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != CO.gateway_select_type:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != CO.gateway_select_type:
            raise Exception('Wrong Trust dropdown')
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        gateway_client_dd = driver.find_element_by_id(CE.config_gateway_client_dd).get_attribute('textContent')
        if gateway_client_dd != '0_AutoCert_' + time_for_name:
            raise Exception('Wrong Client dropdown')
        gateway_trust_dd = driver.find_element_by_id(CE.config_gateway_trust_dd).get_attribute('textContent')
        if gateway_trust_dd != '0_AutoCert_' + time_for_name:
            raise Exception('Wrong Trust dropdown')

        driver.find_element_by_id(CE.config_gateway_port).send_keys('12388')
        driver.find_element_by_id(CE.config_gateway_host).send_keys('AutoHost_' + time_for_name_2)

        # Notification check 1
        driver.find_element_by_id(CE.config_gateway_save).click()
        if driver.find_elements_by_class_name(CE.main_notification_title):
            if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.gateway_already_exists):
                raise Exception('Wrong notification message')
        # End

        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).clear()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('0_AutoGateway_' + time_for_name_2)
        time.sleep(2)
        driver.find_element_by_id(CE.config_gateway_save).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_gateway_save)))
        time.sleep(1)

        # Save config
        driver.find_element_by_id(CE.config_apply).click()
        # Select current config
        Check.wait_until_invisibility(driver, wait, CE.loading_bar)
        Check.select_config(driver, wait, CO.current_config)

        # Verify Gateway Added
        gateway_name = driver.find_element_by_id(CE.gateway_table_1_name).get_attribute('textContent')
        if gateway_name != '0_AutoGateway_' + time_for_name_2:
            raise Exception('Wrong gateway name', gateway_name)
        gateway_client = driver.find_element_by_id(CE.gateway_table_1_client).get_attribute('textContent')
        if gateway_client != '0_AutoCert_' + time_for_name:
            raise Exception('Wrong gateway client', gateway_client)
        gateway_trust = driver.find_element_by_id(CE.gateway_table_1_trust).get_attribute('textContent')
        if gateway_trust != '0_AutoCert_' + time_for_name:
            raise Exception('Wrong gateway trust', gateway_trust)
        gateway_port = driver.find_element_by_id(CE.gateway_table_1_port).get_attribute('textContent')
        if gateway_port != '12388':
            raise Exception('Wrong gateway port', gateway_port)
        gateway_host = driver.find_element_by_id(CE.gateway_table_1_host).get_attribute('textContent')
        if gateway_host != 'AutoHost_' + time_for_name_2:
            raise Exception('Wrong gateway host', gateway_host)

    def test6_pc_add_certificate_gateway_and_service(self):
        driver = self.driver
        driver.get(self.test_pc_url)
        time.sleep(1)
        wait = WebDriverWait(driver, 15)
        autotest_name = self.autotest_name

        now = datetime.datetime.now()

        # Select current config
        Check.select_config(driver, wait, CO.current_config)

        time_for_name = now.strftime('D%d_H%H_M%M_S%S')

        # Add certificate
        driver.find_element_by_id(CE.config_add_certificate).click()
        time.sleep(1)

        address = files_path + "\in_app_proxy_cert"
        print(address, address)
        time.sleep(2)
        element = driver.find_element_by_id(CE.config_cert_select_file)
        element.send_keys(address)

        # Select upload
        Check.by_class_name_and_text(driver, CE.config_buttons, 'Upload').click()
        wait.until(EC.visibility_of_element_located((By.ID, CE.config_cert_true_uploaded)))
        driver.find_element_by_id(CE.config_cert_true_uploaded)
        driver.find_element_by_id(CE.config_cert_name).send_keys('AutoCert_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_type_drop_down).click()
        Check.by_id_and_text(driver, CE.config_cert_type_item_2, 'p12').click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_cert_password)))
        driver.find_element_by_id(CE.config_cert_password).send_keys('cert_pass_' + time_for_name)
        driver.find_element_by_id(CE.config_cert_save_changes).click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.config_cert_save_changes)))
        time.sleep(1)

        # Add Gateway
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_gateway)))
        time.sleep(2)
        driver.find_element_by_id(CE.config_add_gateway).click()
        wait.until(EC.element_to_be_clickable((By.ID, CE.config_gateway_name)))
        driver.find_element_by_id(CE.config_gateway_name).click()
        driver.find_element_by_id(CE.config_gateway_name).send_keys('0_AutoGateway_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_client_dd).click()
        driver.find_element_by_id(CE.config_gateway_client_list)
        driver.find_element_by_id(CE.config_gateway_client_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_trust_dd).click()
        driver.find_element_by_id(CE.config_gateway_trust_list)
        driver.find_element_by_id(CE.config_gateway_trust_items + str(1)).click()
        driver.find_element_by_id(CE.config_gateway_port).send_keys('1889')
        driver.find_element_by_id(CE.config_gateway_host).send_keys('AutoHost_' + time_for_name)
        driver.find_element_by_id(CE.config_gateway_save).click()

        service_count = 0
        while service_count <= 3:
            now = datetime.datetime.now()
            print('now time while', now)
            print('service_count', service_count)
            time_for_name = now.strftime('D%d_H%H_M%M_S%S')

            if service_count == 0:
                # Add Service 1 - empty
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                time.sleep(1)
                driver.find_element_by_id(CE.config_add_service).click()

                # Notification check 1
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_save).click()
                if driver.find_elements_by_class_name(CE.main_notification_title):
                    notif = driver.find_element_by_class_name(CE.main_notification_title).get_attribute('textContent')
                    if notif != CO.service_missing_name:
                        print('notif', notif)
                        raise Exception('Wrong notification message')
                # End

                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('0_AutoService_' + time_for_name)
                driver.find_element_by_id(CE.config_service_save).click()
                time.sleep(1)

                # Save config
                driver.find_element_by_id(CE.config_apply).click()
                # Select current config
                Check.wait_until_invisibility(driver, wait, CE.loading_bar)
                Check.select_config(driver, wait, CO.current_config)

                # Verify Service Added 1
                service_name_1 = driver.find_element_by_css_selector(
                    Check.service_name(service_count)).get_attribute('textContent')
                service_value_1 = driver.find_element_by_css_selector(
                    Check.service_values(service_count)).get_attribute('textContent')
                if service_name_1 != '0_AutoService_' + time_for_name:
                    raise Exception('Wrong Service name:', service_name_1)
                if service_value_1 != '':
                    print('service_value_1')
                    raise Exception('Wrong service values information:', service_value_1)

                # Add Service 2 - same name with error
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                time.sleep(1)
                driver.find_element_by_id(CE.config_add_service).click()
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('0_AutoService_' + time_for_name)
                driver.find_element_by_id(CE.config_service_save).click()

                # Notification check 2
                if driver.find_elements_by_class_name(CE.main_notification_title):
                    if not Check.by_class_name_and_text(driver, CE.main_notification_title, CO.service_name_already_exists):
                        raise Exception('Wrong notification message')
                # End

                driver.find_element_by_id(CE.config_service_cancel).click()

                service_count += 1
            elif service_count == 1:
                # Add Service 3 - gateway
                time.sleep(2)
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                driver.find_element_by_id(CE.config_add_service).click()
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('0_AutoService_' + time_for_name)

                driver.find_element_by_id(CE.config_service_select_gateway).click()
                driver.find_element_by_id(CE.config_service_select_gateway_list)
                driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
                time.sleep(1)
                service_client_dd = driver.find_element_by_id(
                    CE.config_service_select_gateway_list).get_attribute('textContent')
                if '0_AutoGateway_' not in service_client_dd:
                    print('service_client_dd', service_client_dd)
                    raise Exception('Wrong Service dropdown')
                driver.find_element_by_id(CE.config_service_save).click()
                time.sleep(1)
                Check.wait_until_invisibility(driver, wait, CE.loading_bar)
                time.sleep(1)

                # Check.select_config(driver, wait, CO.current_config)

                # Save config
                driver.find_element_by_id(CE.config_apply).click()
                # Select current config
                Check.wait_until_invisibility(driver, wait, CE.loading_bar)
                Check.select_config(driver, wait, CO.current_config)
                time.sleep(2)

                # Verify Service Added 2
                service_name_1 = driver.find_element_by_css_selector(
                    Check.service_name(service_count)).get_attribute('textContent')
                service_value_gate_1 = driver.find_element_by_css_selector(
                    Check.service_value_string_name(service_count)).get_attribute('textContent')
                service_value_gate_name_1 = driver.find_element_by_css_selector(
                    Check.service_value_string_value(service_count)).get_attribute('textContent')

                if service_name_1 != '0_AutoService_' + time_for_name:
                    raise Exception('Wrong Service name:', service_name_1)
                if service_value_gate_1 != 'gate':
                    raise Exception('Wrong service value gate information')
                if '0_AutoGateway_' not in service_value_gate_name_1:
                    raise Exception('Wrong service value gate name information')

                service_count += 1
            elif service_count == 2:
                # Add Service 4 - property
                time.sleep(2)
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                driver.find_element_by_id(CE.config_add_service).click()
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('0_AutoService_' + time_for_name)
                driver.find_element_by_id(CE.config_service_add_button).click()
                driver.find_element_by_id(CE.config_service_add_dialog)
                driver.find_element_by_id(CE.config_service_add_select).click()
                Check.by_class_name_and_text(driver, CE.menu_list_item, 'get').click()
                add_select_label = driver.find_element_by_id(
                    CE.config_service_add_select_label).get_attribute('textContent')
                if add_select_label != 'get':
                    print('add_select_label', add_select_label)
                    raise Exception('Wrong select label')
                driver.find_element_by_css_selector(CE.config_service_add_value_close).click()
                time.sleep(1)
                detail_property_value = driver.find_element_by_id(
                    CE.config_service_property_values).get_attribute('textContent')
                if detail_property_value != CO.config_service_property_values_no_records:
                    print('detail_property_value', detail_property_value)
                    raise Exception('Wrong property values')
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_add_button).click()
                driver.find_element_by_id(CE.config_service_add_dialog)
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_add_select).click()
                Check.by_class_name_and_text(driver, CE.menu_list_item, 'get').click()
                add_select_label = driver.find_element_by_id(
                    CE.config_service_add_select_label).get_attribute('textContent')
                if add_select_label != 'get':
                    print('add_select_label', add_select_label)
                    raise Exception('Wrong select label')
                driver.find_element_by_id(CE.config_service_add_ok).click()
                time.sleep(1)
                detail_property_value = driver.find_element_by_css_selector(
                    CE.details_value_property_name).get_attribute('textContent')
                if detail_property_value != 'get':
                    print('detail_property_value', detail_property_value)
                    raise Exception('Wrong property value name')
                driver.find_element_by_css_selector(CE.config_service_detail_property_value).click()
                driver.find_element_by_css_selector(
                    CE.config_service_detail_property_value).send_keys('AutoProperty_' + str(service_count))
                driver.find_element_by_id(CE.config_service_detail_delete_action).click()

                # Notification check 1
                if driver.find_elements_by_class_name(CE.main_notification_title):
                    if not Check.by_class_name_and_text(driver, CE.main_notification_title,
                                                        CO.service_property_successfully_deleted):
                        raise Exception('Wrong notification message')
                # End

                driver.find_element_by_id(CE.config_service_add_button).click()
                driver.find_element_by_id(CE.config_service_add_dialog)
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_add_select).click()
                Check.by_class_name_and_text(driver, CE.menu_list_item, 'get').click()
                add_select_label = driver.find_element_by_id(
                    CE.config_service_add_select_label).get_attribute('textContent')
                if add_select_label != 'get':
                    print('add_select_label', add_select_label)
                    raise Exception('Wrong select label')
                driver.find_element_by_id(CE.config_service_add_ok).click()
                time.sleep(1)
                detail_property_value = driver.find_element_by_css_selector(
                    CE.details_value_property_name).get_attribute('textContent')
                if detail_property_value != 'get':
                    print('detail_property_value', detail_property_value)
                    raise Exception('Wrong property value name')
                driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
                driver.find_element_by_xpath(
                    CE.config_service_detail_property_value).send_keys('AutoProperty_' + str(service_count))
                driver.find_element_by_id(CE.config_service_save).click()
                time.sleep(1)

                # Save config
                driver.find_element_by_id(CE.config_apply).click()
                # Select current config
                Check.wait_until_invisibility(driver, wait, CE.loading_bar)
                Check.select_config(driver, wait, CO.current_config)
                wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, CE.widget_overlay)))

                # Verify Service Added 2
                service_name_1 = driver.find_element_by_css_selector(
                    Check.service_name(service_count)).get_attribute('textContent')
                service_value_property_name_1 = driver.find_element_by_css_selector(
                    Check.service_value_string_name(service_count)).get_attribute('textContent')
                service_value_property_value_1 = driver.find_element_by_css_selector(
                    Check.service_value_string_value(service_count)).get_attribute('textContent')

                if service_name_1 != '0_AutoService_' + time_for_name:
                    raise Exception('Wrong Service name:', service_name_1)
                if service_value_property_name_1 != 'get':
                    raise Exception('Wrong service property name information')
                if service_value_property_value_1 != 'AutoProperty_' + str(service_count):
                    raise Exception('Wrong service property value information')
                service_count += 1
            elif service_count == 3:
                # Add Service 5 - gate and property
                time.sleep(2)
                wait.until(EC.visibility_of_element_located((By.ID, CE.config_add_service)))
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_add_service)))
                driver.find_element_by_id(CE.config_add_service).click()
                wait.until(EC.element_to_be_clickable((By.ID, CE.config_service_name)))
                driver.find_element_by_id(CE.config_service_name).click()
                driver.find_element_by_id(CE.config_service_name).send_keys('0_AutoService_' + time_for_name)
                driver.find_element_by_id(CE.config_service_add_button).click()
                driver.find_element_by_id(CE.config_service_add_dialog)
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_add_select).click()
                Check.by_class_name_and_text(driver, CE.menu_list_item, 'path').click()
                add_select_label = driver.find_element_by_id(
                    CE.config_service_add_select_label).get_attribute('textContent')
                if add_select_label != 'path':
                    print('add_select_label', add_select_label)
                    raise Exception('Wrong select label')
                driver.find_element_by_id(CE.config_service_add_ok).click()
                time.sleep(1)
                detail_property_value = driver.find_element_by_css_selector(
                    CE.details_value_property_name).get_attribute('textContent')
                if detail_property_value != 'path':
                    print('detail_property_value', detail_property_value)
                    raise Exception('Wrong property value name')
                driver.find_element_by_xpath(CE.config_service_detail_property_value).click()
                driver.find_element_by_xpath(
                    CE.config_service_detail_property_value).send_keys('AutoProperty_' + str(service_count))
                time.sleep(1)
                driver.find_element_by_id(CE.config_service_select_gateway).click()
                driver.find_element_by_id(CE.config_service_select_gateway_list)
                driver.find_element_by_id(CE.config_service_select_gateway_items + str(1)).click()
                time.sleep(1)
                service_client_dd = driver.find_element_by_id(
                    CE.config_service_select_gateway_list).get_attribute('textContent')
                if '0_AutoGateway_' not in service_client_dd:
                    print('service_client_dd', service_client_dd)
                    raise Exception('Wrong Service dropdown')
                driver.find_element_by_id(CE.config_service_save).click()
                wait.until(EC.invisibility_of_element_located((By.ID, CE.config_service_save)))
                time.sleep(1)

                # Save config
                driver.find_element_by_id(CE.config_apply).click()
                # Select current config
                Check.wait_until_invisibility(driver, wait, CE.loading_bar)
                Check.select_config(driver, wait, CO.current_config)

                # Verify Service Added 1
                service_name_1 = driver.find_element_by_css_selector(
                    Check.service_name(service_count)).get_attribute('textContent')
                service_value_property = driver.find_element_by_css_selector(
                    Check.service_value_property_2(service_count)).get_attribute('textContent')
                service_value_property_value = driver.find_element_by_css_selector(
                    Check.service_value_property_value_2(service_count)).get_attribute('textContent')
                service_value_gate = driver.find_element_by_css_selector(
                    Check.service_value_property_1(service_count)).get_attribute('textContent')
                service_value_gate_name = driver.find_element_by_css_selector(
                    Check.service_value_property_value_1(service_count)).get_attribute('textContent')
                if service_name_1 != '0_AutoService_' + time_for_name:
                    raise Exception('Wrong Service name:', service_name_1)
                if service_value_property != 'path':
                    raise Exception('Wrong service property name information:', service_value_property)
                if service_value_property_value != 'AutoProperty_' + str(service_count):
                    raise Exception('Wrong service property value information:', service_value_property_value)
                if service_value_gate != 'gate':
                    raise Exception('Wrong service value gate information:', service_value_gate)
                if '0_AutoGateway_' not in service_value_gate_name:
                    raise Exception('Wrong service value gate name information:', service_value_gate_name)
                service_count += 1
        time.sleep(1)
