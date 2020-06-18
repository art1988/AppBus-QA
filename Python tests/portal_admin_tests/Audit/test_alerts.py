import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import AlertsElements, Other, Elements
import driver_settings
import time
import datetime
from selenium.webdriver import ActionChains
import calendar
import os

CE = AlertsElements
CElem = Elements
CO = Other

# QA Server
# server_address = 'https://dev-msa-qa.botf03.net:9613/edapt-admin'

# QA Stag Server
server_address = 'https://dev-msa-qa-stag.botf03.net:9613/edapt-admin'


class Alerts01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_a_url = server_address + '/page/logevent.jsf'
        cls.driver.get(cls.test_a_url)
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
        driver.get(self.test_a_url)
        wait = WebDriverWait(self.driver, 15)

        content_list = [CE.add_new_button, CE.delete_button, CE.refresh_button, CE.edit_alert_0_button]
        # count_123 = 0
        for elem in content_list:
            # print('len(content_list)', len(content_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

    def test2_add_alert_required_fields(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_a_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for subject
        now = datetime.datetime.now()
        time_for_alert = now.strftime('%H%M%S')

        # data
        alert_action = '{"operation":"VALUE","alertType":"USERNAME", "time":"' + time_for_alert + '"},'
        alert_email_group = '1_test_email_group'
        alert_subject = 'Test_alert' + time_for_alert

        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.alert_details)
        driver.find_element_by_id(CE.ad_actions).send_keys(alert_action)
        driver.find_element_by_id(CE.ad_subject).send_keys(alert_subject)
        driver.find_element_by_id(CE.ad_email_group_dd).click()

        # Select Email Group
        email_group_count = 0
        driver.implicitly_wait(2)
        while email_group_count < 20:
            # print('email_group_count', email_group_count)
            id_elem = 'entity:dialogsForm:log-event-email-name_' + str(email_group_count)
            if driver.find_element_by_id(id_elem):
                txt_cont = driver.find_element_by_id(id_elem).get_attribute('textContent')
                if alert_email_group in txt_cont:
                    driver.find_element_by_id(id_elem).click()
                    break
                else:
                    email_group_count += 1
            else:
                raise Exception('Email group not found')
        driver.implicitly_wait(15)

        driver.find_element_by_id(CE.ad_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    css_email_group = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_email_group = driver.find_elements_by_css_selector(css_email_group)
                    if find_email_group[0].get_attribute('textContent') != alert_email_group:
                        raise Exception('Wrong Email Group')
                    css_action = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
                    find_action = driver.find_elements_by_css_selector(css_action)
                    if find_action[0].get_attribute('textContent') != alert_action:
                        raise Exception('Wrong Action')
                    print('Alert - added')
                    break
                count_items += 1
            else:
                raise Exception('The Alert', alert_subject, ' not found')

    def test3_add_alert_all_fields(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_a_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for subject
        now = datetime.datetime.now()
        time_for_alert = now.strftime('%H%M%S')

        # data
        alert_action = '{"operation":"VALUE","alertType":"USERNAME", "time":"' + time_for_alert + '"},'
        alert_email_group = '1_test_email_group'
        alert_subject = 'Test_alert' + time_for_alert
        alert_body = 'Body for ' + alert_subject
        alert_description = 'Description for ' + alert_subject

        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.alert_details)
        driver.find_element_by_id(CE.ad_actions).send_keys(alert_action)
        driver.find_element_by_id(CE.ad_subject).send_keys(alert_subject)
        driver.find_element_by_id(CE.ad_body).send_keys(alert_body)
        driver.find_element_by_id(CE.ad_description).send_keys(alert_description)
        driver.find_element_by_id(CE.ad_email_group_dd).click()

        # Select Email Group
        email_group_count = 0
        driver.implicitly_wait(2)
        while email_group_count < 20:
            # print('email_group_count', email_group_count)
            id_elem = 'entity:dialogsForm:log-event-email-name_' + str(email_group_count)
            if driver.find_element_by_id(id_elem):
                txt_cont = driver.find_element_by_id(id_elem).get_attribute('textContent')
                if alert_email_group in txt_cont:
                    driver.find_element_by_id(id_elem).click()
                    break
                else:
                    email_group_count += 1
            else:
                raise Exception('Email group not found')
        driver.implicitly_wait(15)

        driver.find_element_by_id(CE.ad_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    css_email_group = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_email_group = driver.find_elements_by_css_selector(css_email_group)
                    if find_email_group[0].get_attribute('textContent') != alert_email_group:
                        raise Exception('Wrong Email Group')
                    css_action = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
                    find_action = driver.find_elements_by_css_selector(css_action)
                    if find_action[0].get_attribute('textContent') != alert_action:
                        raise Exception('Wrong Action')
                    css_body = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(5)'
                    find_body = driver.find_elements_by_css_selector(css_body)
                    if find_body[0].get_attribute('textContent') != alert_body:
                        print('find_body', find_body[0].get_attribute('textContent'))
                        print('alert_body', alert_body)
                        raise Exception('Wrong Body')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(6)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != alert_description:
                        raise Exception('Wrong Description')
                    print('Alert - added')
                    break
                count_items += 1
            else:
                raise Exception('The Alert', alert_subject, ' not found')

    def test4_edit_alert(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_a_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for subject
        now = datetime.datetime.now()
        time_for_alert = now.strftime('%H%M%S')

        # data
        alert_action = '{"operation":"VALUE","alertType":"USERNAME", "time":"' + time_for_alert + '"},'
        alert_email_group = '1_test_email_group'
        alert_subject = 'Test_alert for edit' + time_for_alert
        alert_body = 'Body_' + alert_subject
        alert_description = 'Description_' + alert_subject

        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.alert_details)
        driver.find_element_by_id(CE.ad_actions).send_keys(alert_action)
        driver.find_element_by_id(CE.ad_subject).send_keys(alert_subject)
        driver.find_element_by_id(CE.ad_body).send_keys(alert_body)
        driver.find_element_by_id(CE.ad_description).send_keys(alert_description)
        driver.find_element_by_id(CE.ad_email_group_dd).click()

        # Select Email Group
        email_group_count = 0
        driver.implicitly_wait(2)
        while email_group_count < 20:
            # print('email_group_count', email_group_count)
            id_elem = 'entity:dialogsForm:log-event-email-name_' + str(email_group_count)
            if driver.find_element_by_id(id_elem):
                txt_cont = driver.find_element_by_id(id_elem).get_attribute('textContent')
                if alert_email_group in txt_cont:
                    driver.find_element_by_id(id_elem).click()
                    break
                else:
                    email_group_count += 1
            else:
                raise Exception('Email group not found')
        driver.implicitly_wait(15)

        driver.find_element_by_id(CE.ad_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    css_email_group = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_email_group = driver.find_elements_by_css_selector(css_email_group)
                    if find_email_group[0].get_attribute('textContent') != alert_email_group:
                        raise Exception('Wrong Email Group')
                    css_action = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
                    find_action = driver.find_elements_by_css_selector(css_action)
                    if find_action[0].get_attribute('textContent') != alert_action:
                        raise Exception('Wrong Action')
                    css_body = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(5)'
                    find_body = driver.find_elements_by_css_selector(css_body)
                    if find_body[0].get_attribute('textContent') != alert_body:
                        print('find_body', find_body[0].get_attribute('textContent'))
                        print('alert_body', alert_body)
                        raise Exception('Wrong Body')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(6)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != alert_description:
                        raise Exception('Wrong Description')
                    print('Alert - added')
                    break
                count_items += 1
            else:
                raise Exception('The Alert', alert_subject, ' not found')

        # New data
        new_alert_action = '{"operation":"SUPERVALUE","alertType":"MEGAUSERNAME", "time":"' + time_for_alert + '"},'
        new_alert_email_group = '0_test_email_group'
        new_alert_subject = 'Test_alert edited' + time_for_alert
        new_alert_body = 'Body_' + new_alert_subject
        new_alert_description = 'Description_' + new_alert_subject

        # Edit Alert
        edit_alert_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':edit'
        driver.find_element_by_id(edit_alert_id).click()
        time.sleep(1)
        edit_action_field_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':actionField'
        edit_email_group_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':emailGroupField_label'
        edit_subject_field_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':subjectField'
        edit_body_field_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':bodyField'
        edit_description_field_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':descriptionField'
        edit_save_button_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':save'
        edit_cancel_button_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':cancel'

        driver.find_element_by_id(edit_action_field_id).clear()
        driver.find_element_by_id(edit_subject_field_id).clear()
        driver.find_element_by_id(edit_body_field_id).clear()
        driver.find_element_by_id(edit_description_field_id).clear()
        driver.find_element_by_id(edit_action_field_id).send_keys(new_alert_action)
        driver.find_element_by_id(edit_subject_field_id).send_keys(new_alert_subject)
        driver.find_element_by_id(edit_body_field_id).send_keys(new_alert_body)
        driver.find_element_by_id(edit_description_field_id).send_keys(new_alert_description)

        # Select Email Group
        driver.find_element_by_id(edit_email_group_id).click()
        email_group_count = 0
        driver.implicitly_wait(2)
        while email_group_count < 20:
            # print('email_group_count', email_group_count)
            id_elem = 'table:tableForm:entityTable:' + str(count_items - 1) + ':emailGroupField_' + str(email_group_count)
            if driver.find_element_by_id(id_elem):
                txt_cont = driver.find_element_by_id(id_elem).get_attribute('textContent')
                if new_alert_email_group in txt_cont:
                    driver.find_element_by_id(id_elem).click()
                    break
                else:
                    email_group_count += 1
            else:
                raise Exception('Email group not found')
        driver.implicitly_wait(15)

        # Cancel edit
        driver.find_element_by_id(edit_cancel_button_id).click()
        time.sleep(2)

        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    css_email_group = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_email_group = driver.find_elements_by_css_selector(css_email_group)
                    if find_email_group[0].get_attribute('textContent') != alert_email_group:
                        raise Exception('Wrong Email Group')
                    css_action = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
                    find_action = driver.find_elements_by_css_selector(css_action)
                    if find_action[0].get_attribute('textContent') != alert_action:
                        raise Exception('Wrong Action')
                    css_body = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(5)'
                    find_body = driver.find_elements_by_css_selector(css_body)
                    if find_body[0].get_attribute('textContent') != alert_body:
                        print('find_body', find_body[0].get_attribute('textContent'))
                        print('alert_body', alert_body)
                        raise Exception('Wrong Body')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(6)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != alert_description:
                        raise Exception('Wrong Description')
                    print('Alert - added')
                    break
                count_items += 1
            else:
                raise Exception('The Alert', alert_subject, ' not found')

        # Edit Alert
        edit_alert_id = 'table:tableForm:entityTable:' + str(count_items - 1) + ':edit'
        driver.find_element_by_id(edit_alert_id).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, edit_action_field_id)))
        driver.find_element_by_id(edit_action_field_id).clear()
        driver.find_element_by_id(edit_subject_field_id).clear()
        driver.find_element_by_id(edit_body_field_id).clear()
        driver.find_element_by_id(edit_description_field_id).clear()
        driver.find_element_by_id(edit_action_field_id).send_keys(new_alert_action)
        driver.find_element_by_id(edit_subject_field_id).send_keys(new_alert_subject)
        driver.find_element_by_id(edit_body_field_id).send_keys(new_alert_body)
        driver.find_element_by_id(edit_description_field_id).send_keys(new_alert_description)

        # Select Email Group
        driver.find_element_by_id(edit_email_group_id).click()
        email_group_count = 0
        driver.implicitly_wait(2)
        while email_group_count < 20:
            # print('email_group_count', email_group_count)
            id_elem = 'table:tableForm:entityTable:' + str(count_items - 1) + ':emailGroupField_' + str(email_group_count)
            if driver.find_element_by_id(id_elem):
                txt_cont = driver.find_element_by_id(id_elem).get_attribute('textContent')
                if new_alert_email_group in txt_cont:
                    driver.find_element_by_id(id_elem).click()
                    break
                else:
                    email_group_count += 1
            else:
                raise Exception('Email group not found')
        driver.implicitly_wait(15)

        # Save edit
        driver.find_element_by_id(edit_save_button_id).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        # find alert edited
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == new_alert_subject:
                    css_email_group = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_email_group = driver.find_elements_by_css_selector(css_email_group)
                    if find_email_group[0].get_attribute('textContent') != new_alert_email_group:
                        raise Exception('Wrong Email Group')
                    css_action = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
                    find_action = driver.find_elements_by_css_selector(css_action)
                    if find_action[0].get_attribute('textContent') != new_alert_action:
                        raise Exception('Wrong Action')
                    css_body = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(5)'
                    find_body = driver.find_elements_by_css_selector(css_body)
                    if find_body[0].get_attribute('textContent') != new_alert_body:
                        print('find_body', find_body[0].get_attribute('textContent'))
                        print('alert_body', alert_body)
                        raise Exception('Wrong Body')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(6)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != new_alert_description:
                        raise Exception('Wrong Description')
                    print('Alert - edited')
                    break
                count_items += 1
            else:
                raise Exception('The Alert', alert_subject, ' not found')

    def test5_refresh(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_a_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for subject
        now = datetime.datetime.now()
        time_for_alert = now.strftime('%H%M%S')

        # data
        alert_action = '{"operation":"VALUE","alertType":"USERNAME", "time":"' + time_for_alert + '"},'
        alert_email_group = '1_test_email_group'
        alert_subject = 'Test_alert for refresh' + time_for_alert
        alert_body = 'Body_' + alert_subject
        alert_description = 'Description_' + alert_subject

        # Find group before create
        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    raise Exception('The Alert', alert_subject, ' is found')
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

        # New tab & switch
        exe_script = "window.open('" + server_address + "/page/logevent.jsf','_blank');"
        driver.execute_script(exe_script)

        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.alert_details)
        driver.find_element_by_id(CE.ad_actions).send_keys(alert_action)
        driver.find_element_by_id(CE.ad_subject).send_keys(alert_subject)
        driver.find_element_by_id(CE.ad_body).send_keys(alert_body)
        driver.find_element_by_id(CE.ad_description).send_keys(alert_description)
        driver.find_element_by_id(CE.ad_email_group_dd).click()

        # Select Email Group
        email_group_count = 0
        driver.implicitly_wait(2)
        while email_group_count < 20:
            # print('email_group_count', email_group_count)
            id_elem = 'entity:dialogsForm:log-event-email-name_' + str(email_group_count)
            if driver.find_element_by_id(id_elem):
                txt_cont = driver.find_element_by_id(id_elem).get_attribute('textContent')
                if alert_email_group in txt_cont:
                    driver.find_element_by_id(id_elem).click()
                    break
                else:
                    email_group_count += 1
            else:
                raise Exception('Email group not found')
        driver.implicitly_wait(15)

        driver.find_element_by_id(CE.ad_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Switch and refresh
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_id(CE.refresh_button).click()
        time.sleep(1)

        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    css_email_group = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_email_group = driver.find_elements_by_css_selector(css_email_group)
                    if find_email_group[0].get_attribute('textContent') != alert_email_group:
                        raise Exception('Wrong Email Group')
                    css_action = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
                    find_action = driver.find_elements_by_css_selector(css_action)
                    if find_action[0].get_attribute('textContent') != alert_action:
                        raise Exception('Wrong Action')
                    css_body = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(5)'
                    find_body = driver.find_elements_by_css_selector(css_body)
                    if find_body[0].get_attribute('textContent') != alert_body:
                        print('find_body', find_body[0].get_attribute('textContent'))
                        print('alert_body', alert_body)
                        raise Exception('Wrong Body')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(6)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != alert_description:
                        raise Exception('Wrong Description')
                    print('Alert - added')
                    break
                count_items += 1
            else:
                raise Exception('The Alert', alert_subject, ' not found')

    def test6_delete_one_alert(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_a_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for subject
        now = datetime.datetime.now()
        time_for_alert = now.strftime('%H%M%S')

        # data
        alert_action = '{"operation":"VALUE","alertType":"USERNAME", "time":"' + time_for_alert + '"},'
        alert_email_group = '1_test_email_group'
        alert_subject = 'Test_alert delete' + time_for_alert
        alert_body = 'Body_' + alert_subject
        alert_description = 'Description_' + alert_subject

        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.alert_details)
        driver.find_element_by_id(CE.ad_actions).send_keys(alert_action)
        driver.find_element_by_id(CE.ad_subject).send_keys(alert_subject)
        driver.find_element_by_id(CE.ad_body).send_keys(alert_body)
        driver.find_element_by_id(CE.ad_description).send_keys(alert_description)
        driver.find_element_by_id(CE.ad_email_group_dd).click()

        # Select Email Group
        email_group_count = 0
        driver.implicitly_wait(2)
        while email_group_count < 20:
            # print('email_group_count', email_group_count)
            id_elem = 'entity:dialogsForm:log-event-email-name_' + str(email_group_count)
            if driver.find_element_by_id(id_elem):
                txt_cont = driver.find_element_by_id(id_elem).get_attribute('textContent')
                if alert_email_group in txt_cont:
                    driver.find_element_by_id(id_elem).click()
                    break
                else:
                    email_group_count += 1
            else:
                raise Exception('Email group not found')
        driver.implicitly_wait(15)

        driver.find_element_by_id(CE.ad_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    css_email_group = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_email_group = driver.find_elements_by_css_selector(css_email_group)
                    if find_email_group[0].get_attribute('textContent') != alert_email_group:
                        raise Exception('Wrong Email Group')
                    css_action = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
                    find_action = driver.find_elements_by_css_selector(css_action)
                    if find_action[0].get_attribute('textContent') != alert_action:
                        raise Exception('Wrong Action')
                    css_body = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(5)'
                    find_body = driver.find_elements_by_css_selector(css_body)
                    if find_body[0].get_attribute('textContent') != alert_body:
                        print('find_body', find_body[0].get_attribute('textContent'))
                        print('alert_body', alert_body)
                        raise Exception('Wrong Body')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(6)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != alert_description:
                        raise Exception('Wrong Description')
                    print('Alert - added')
                    break
                count_items += 1
            else:
                raise Exception('The Alert', alert_subject, ' not found')
        driver.implicitly_wait(15)

        # Delete > Cancel
        css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
        time.sleep(2)
        find_row = driver.find_elements_by_css_selector(css_selector)
        find_row[0].click()

        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_cancel)))
        driver.find_element_by_id(CE.delete_cancel).click()

        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    css_email_group = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_email_group = driver.find_elements_by_css_selector(css_email_group)
                    if find_email_group[0].get_attribute('textContent') != alert_email_group:
                        raise Exception('Wrong Email Group')
                    css_action = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
                    find_action = driver.find_elements_by_css_selector(css_action)
                    if find_action[0].get_attribute('textContent') != alert_action:
                        raise Exception('Wrong Action')
                    css_body = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(5)'
                    find_body = driver.find_elements_by_css_selector(css_body)
                    if find_body[0].get_attribute('textContent') != alert_body:
                        print('find_body', find_body[0].get_attribute('textContent'))
                        print('alert_body', alert_body)
                        raise Exception('Wrong Body')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(6)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != alert_description:
                        raise Exception('Wrong Description')
                    print('Alert - added')
                    break
                count_items += 1
            else:
                raise Exception('The Alert', alert_subject, ' not found')
        driver.implicitly_wait(15)

        # Delete > Delete
        css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
        time.sleep(2)
        find_row = driver.find_elements_by_css_selector(css_selector)
        find_row[0].click()

        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_confirm)))
        driver.find_element_by_id(CE.delete_confirm).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find alert
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == alert_subject:
                    raise Exception('The Alert', alert_subject, ' is found')
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

    def test7_mass_delete_alert(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_a_url)
        wait = WebDriverWait(self.driver, 15)

        alert_name = 'Test_alert'

        # find alert
        items_value = 0
        count_items = 1
        driver.implicitly_wait(1)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if alert_name in find_row[0].get_attribute('textContent'):
                    items_value += 1
                    css_checkbox = 'tr.ui-widget-content:nth-child(' + str(
                        count_items) + ') > td:nth-child(1) > div:nth-child(1)'
                    driver.find_element_by_css_selector(css_checkbox).click()
                    print('Alert selected')
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

        # Delete > Cancel
        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_cancel)))
        driver.find_element_by_id(CE.delete_cancel).click()

        # find alert
        items_value_2 = 0
        count_items = 1
        driver.implicitly_wait(1)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if alert_name in find_row[0].get_attribute('textContent'):
                    items_value_2 += 1
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

        if items_value != items_value_2:
            raise Exception('Wrong value of items')

        # Delete > Delete
        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_confirm)))
        driver.find_element_by_id(CE.delete_confirm).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check notify
        driver.implicitly_wait(0)
        if driver.find_elements_by_class_name(CElem.main_notification_title):
            notification_message = driver.find_element_by_class_name(CElem.main_notification_title).get_attribute(
                'textContent')
            if notification_message != CO.message_successfully_deleted:
                print('notification_message', notification_message)
                raise Exception('Wrong notification message')

        # find alert
        items_value_3 = 0
        count_items = 1
        driver.implicitly_wait(1)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if alert_name in find_row[0].get_attribute('textContent'):
                    items_value_3 += 1
                    css_checkbox = 'tr.ui-widget-content:nth-child(' + str(
                        count_items) + ') > td:nth-child(1) > div:nth-child(1)'
                    driver.find_element_by_css_selector(css_checkbox).click()
                    print('Alert selected')
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

        if items_value_3 != 0:
            raise Exception('Not all items deleted')
