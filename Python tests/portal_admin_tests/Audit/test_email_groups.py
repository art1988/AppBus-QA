import unittest
import Check
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from content import EmailGroupsElements, Other, Elements
import driver_settings
import time
import datetime
from selenium.webdriver import ActionChains
import calendar
import os

CE = EmailGroupsElements
CElem = Elements
CO = Other

# QA Server
# server_address = 'https://dev-msa-qa.botf03.net:9613/edapt-admin'

# QA Stag Server
server_address = 'https://dev-msa-qa-stag.botf03.net:9613/edapt-admin'

project_path = os.path.dirname(os.path.dirname(__file__))
files_path = os.path.join(project_path, 'files')


class EmailGroups01Tests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        set_driver = driver_settings.driver(cls)
        cls.driver = set_driver
        # cls.driver = webdriver.Firefox()
        cls.test_eg_url = server_address + '/page/emailgroup.jsf'
        cls.driver.get(cls.test_eg_url)
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
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        content_list = [CE.add_new_button, CE.delete_button, CE.refresh_button, CE.edit_group_0_button]
        # count_123 = 0
        for elem in content_list:
            # print('len(content_list)', len(content_list))
            # print(driver.find_elements_by_id(elem))
            if not driver.find_elements_by_id(elem):
                raise Exception(elem, 'not found')
            # else:
            #     count_123 += 1
            # print(count_123)

    def test2_add_new_group_full(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for name
        now = datetime.datetime.now()
        time_for_group = now.strftime('%H%M%S')
        time.sleep(1)
        group_name = 'Test_Group' + time_for_group
        group_content = 'test_email' + time_for_group + '@test.ves'
        group_description = 'Description for ' + group_name

        # Create Group
        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.email_groups_detail)
        driver.find_element_by_id(CE.egd_name).send_keys(group_name)
        driver.find_element_by_id(CE.egd_content).send_keys(group_content)
        driver.find_element_by_id(CE.egd_description).send_keys(group_description)
        driver.find_element_by_id(CE.egd_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    if find_content[0].get_attribute('textContent') != group_content:
                        raise Exception('Wrong group Content')
                    css_decsr = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_decsr = driver.find_elements_by_css_selector(css_decsr)
                    if find_decsr[0].get_attribute('textContent') != group_description:
                        raise Exception('Wrong group Description')
                    print('Email Group - added')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')

    def test3_add_new_group_without_description(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for name
        now = datetime.datetime.now()
        time_for_group = now.strftime('%H%M%S')
        time.sleep(1)
        group_name = 'Test_Group' + time_for_group
        group_content = 'test_email' + time_for_group + '@test.ves'

        # Create Group
        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.email_groups_detail)
        driver.find_element_by_id(CE.egd_name).send_keys(group_name)
        driver.find_element_by_id(CE.egd_content).send_keys(group_content)
        driver.find_element_by_id(CE.egd_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    if find_content[0].get_attribute('textContent') != group_content:
                        raise Exception('Wrong group Content')
                    css_decsr = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_decsr = driver.find_elements_by_css_selector(css_decsr)
                    if find_decsr[0].get_attribute('textContent') != '':
                        raise Exception('Wrong group Description')
                    print('Email Group - added')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')

    def test4_add_new_group_multiple_content(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for name
        now = datetime.datetime.now()
        time_for_group = now.strftime('%H%M%S')
        time.sleep(1)
        group_name = 'Test_Group_multiple' + time_for_group
        group_description = 'Description for ' + group_name
        group_content_multiple_list = []
        for x in range(100):
            group_content_multiple_list.append(str(x) + '_test_email' + time_for_group + '@test.ves,')
        # print('group_content_multiple_list', group_content_multiple_list)

        # Create Group
        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.email_groups_detail)
        driver.find_element_by_id(CE.egd_name).send_keys(group_name)
        for elem in group_content_multiple_list:
            driver.find_element_by_id(CE.egd_content).send_keys(elem + ' ')
        time.sleep(1)
        driver.find_element_by_id(CE.egd_description).send_keys(group_description)
        driver.find_element_by_id(CE.egd_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    # print('if find_row[0] == group_name')
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    content_list = find_content[0].get_attribute('textContent').split(' ')
                    # print('content_list', content_list)
                    if content_list != group_content_multiple_list:
                        raise Exception('Wrong group Content')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != group_description:
                        raise Exception('Wrong group Description')
                    print('Email Group - added')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')

    def test5_add_new_group_with_upload(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for name
        now = datetime.datetime.now()
        time_for_group = now.strftime('%H%M%S')
        time.sleep(1)
        group_name = 'Test_Group_upload' + time_for_group
        # group_content = 'test_email' + time_for_group + '@test.ves'
        group_description = 'Description for ' + group_name

        # File cred
        file_name = 'email_groups_content.txt'
        address = files_path + "\email_groups_content.txt"
        file_size = os.path.getsize(address)
        print('file_size', file_size)
        email_groups_content_file = open(address, "rt")
        contents = email_groups_content_file.read()
        email_groups_content_file.close()
        print('contents:', contents)
        group_content_multiple_list = contents.split(' ')

        # Create Group
        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.email_groups_detail)
        driver.find_element_by_id(CE.egd_name).send_keys(group_name)
        driver.find_element_by_id(CE.egd_description).send_keys(group_description)
        # Use file
        element = driver.find_element_by_id(CE.file_upload_choose)
        element.send_keys(address)
        loaded_name = driver.find_element_by_css_selector(CE.loaded_name).get_attribute('textContent')
        loaded_size = driver.find_element_by_css_selector(CE.loaded_size).get_attribute('textContent')
        driver.find_element_by_class_name(CE.file_upload_progress)
        driver.find_element_by_css_selector(CE.loaded_cancel_upload)
        if loaded_name != file_name:
            raise Exception('Wrong file name')
        if str(file_size) not in str(loaded_size):
            raise Exception('Wrong file size')
        driver.find_element_by_class_name(CE.file_upload_upload).click()
        driver.find_element_by_class_name(CE.file_upload_content)
        driver.find_element_by_id(CE.egd_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)
        time.sleep(2)

        # find group
        count_items = 1
        driver.implicitly_wait(1)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    # print('if find_row[0] == group_name')
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    content_list = find_content[0].get_attribute('textContent').split(' ')
                    # print('content_list', content_list)
                    if content_list != group_content_multiple_list:
                        raise Exception('Wrong group Content')
                    css_description = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_description = driver.find_elements_by_css_selector(css_description)
                    if find_description[0].get_attribute('textContent') != group_description:
                        raise Exception('Wrong group Description')
                    print('Email Group - added')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')

    def test6_edit_group(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for name
        now = datetime.datetime.now()
        time_for_group = now.strftime('%H%M%S')
        time.sleep(1)

        group_name = 'Test_Group_for_edit' + time_for_group
        group_content = 'test_email_for_edit' + time_for_group + '@test.ves'
        group_description = 'Description for ' + group_name
        group_name_edited = 'Test_Group_edited' + time_for_group
        group_content_edited = 'test_email_edited' + time_for_group + '@test.ves'
        group_description_edited = 'Description for ' + group_name_edited

        # Create Group
        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.email_groups_detail)
        driver.find_element_by_id(CE.egd_name).send_keys(group_name)
        driver.find_element_by_id(CE.egd_content).send_keys(group_content)
        driver.find_element_by_id(CE.egd_description).send_keys(group_description)
        driver.find_element_by_id(CE.egd_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    id_edit = 'table:tableForm:entityTable:' + str(count_items - 1) + ':edit'
                    driver.find_element_by_id(id_edit).click()
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')
        driver.implicitly_wait(15)

        id_edit = 'table:tableForm:entityTable:' + str(count_items - 1) + ':edit'
        id_name_edit_field = 'table:tableForm:entityTable:' + str(count_items - 1) + ':nameField'
        id_content_edit_field = 'table:tableForm:entityTable:' + str(count_items - 1) + ':contentField'
        id_description_edit_field = 'table:tableForm:entityTable:' + str(count_items - 1) + ':descriptionField'
        id_edit_cancel = 'table:tableForm:entityTable:' + str(count_items - 1) + ':cancel'
        id_edit_save = 'table:tableForm:entityTable:' + str(count_items - 1) + ':save'

        driver.find_element_by_id(id_name_edit_field).clear()
        driver.find_element_by_id(id_name_edit_field).send_keys(group_name_edited)
        driver.find_element_by_id(id_content_edit_field).clear()
        driver.find_element_by_id(id_content_edit_field).send_keys(group_content_edited)
        driver.find_element_by_id(id_description_edit_field).clear()
        driver.find_element_by_id(id_description_edit_field).send_keys(group_description_edited)

        # Edit > Cancel
        driver.find_element_by_id(id_edit_cancel).click()

        # find group
        count_items_new = 1
        driver.implicitly_wait(2)
        while count_items_new <= 20:
            print('count_items', count_items_new)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items_new) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name_edited:
                    raise Exception('Group has been edited')
                count_items_new += 1
            else:
                break
        driver.implicitly_wait(15)

        driver.find_element_by_id(id_edit).click()
        driver.find_element_by_id(id_name_edit_field).clear()
        driver.find_element_by_id(id_name_edit_field).send_keys(group_name_edited)
        driver.find_element_by_id(id_content_edit_field).clear()
        driver.find_element_by_id(id_content_edit_field).send_keys(group_content_edited)
        driver.find_element_by_id(id_description_edit_field).clear()
        driver.find_element_by_id(id_description_edit_field).send_keys(group_description_edited)

        # Edit > Save
        driver.find_element_by_id(id_edit_save).click()

        # find group
        count_items_edited = 1
        driver.implicitly_wait(2)
        while count_items_edited <= 20:
            print('count_items', count_items_edited)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items_edited) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name_edited:
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items_edited) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    if find_content[0].get_attribute('textContent') != group_content_edited:
                        raise Exception('Wrong group Content')
                    css_decsr = 'tr.ui-widget-content:nth-child(' + str(count_items_edited) + ') > td:nth-child(4)'
                    find_decsr = driver.find_elements_by_css_selector(css_decsr)
                    if find_decsr[0].get_attribute('textContent') != group_description_edited:
                        raise Exception('Wrong group Description')
                    print('Email Group - edited')
                    break
                count_items_edited += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')

    def test7_refresh(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for name
        now = datetime.datetime.now()
        time_for_group = now.strftime('%H%M%S')
        time.sleep(1)
        group_name = 'Test_Group refresh' + time_for_group
        group_content = 'test_email' + time_for_group + '@test.ves'
        group_description = 'Description for ' + time_for_group

        # Find group before create
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    raise Exception('Group found')
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

        # New tab & switch
        # driver.execute_script(
        #     "window.open('https://dev-msa-qa.botf03.net:9613/edapt-admin/page/emailgroup.jsf','_blank');")
        exe_script = "window.open('" + server_address + "/page/emailgroup.jsf','_blank');"
        driver.execute_script(exe_script)
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)

        # Create Group
        driver.find_element_by_id(CE.add_new_button).click()
        time.sleep(2)
        driver.find_element_by_id(CE.email_groups_detail)
        driver.find_element_by_id(CE.egd_name).send_keys(group_name)
        driver.find_element_by_id(CE.egd_content).send_keys(group_content)
        driver.find_element_by_id(CE.egd_description).send_keys(group_description)
        driver.find_element_by_id(CE.egd_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Switch and refresh
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_id(CE.refresh_button).click()
        time.sleep(1)

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    if find_content[0].get_attribute('textContent') != group_content:
                        raise Exception('Wrong group Content')
                    css_decsr = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_decsr = driver.find_elements_by_css_selector(css_decsr)
                    if find_decsr[0].get_attribute('textContent') != group_description:
                        raise Exception('Wrong group Description')
                    print('Email Group - added')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')

    def test8_delete(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        # Time for name
        now = datetime.datetime.now()
        time_for_group = now.strftime('%H%M%S')
        time.sleep(1)
        group_name = 'Test_Group_Delete' + time_for_group
        group_content = 'test_email' + time_for_group + '@test.ves'
        group_description = 'Description for ' + group_name

        # Create Group
        driver.find_element_by_id(CE.add_new_button).click()
        driver.find_element_by_id(CE.email_groups_detail)
        driver.find_element_by_id(CE.egd_name).send_keys(group_name)
        driver.find_element_by_id(CE.egd_content).send_keys(group_content)
        driver.find_element_by_id(CE.egd_description).send_keys(group_description)
        driver.find_element_by_id(CE.egd_add_button).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    if find_content[0].get_attribute('textContent') != group_content:
                        raise Exception('Wrong group Content')
                    css_decsr = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_decsr = driver.find_elements_by_css_selector(css_decsr)
                    if find_decsr[0].get_attribute('textContent') != group_description:
                        raise Exception('Wrong group Description')
                    print('Email Group - added')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')
        driver.implicitly_wait(15)

        # Delete > cancel
        css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
        driver.find_elements_by_css_selector(css_selector)[0].click()
        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_cancel)))
        driver.find_element_by_id(CE.delete_cancel).click()

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    if find_content[0].get_attribute('textContent') != group_content:
                        raise Exception('Wrong group Content')
                    css_decsr = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_decsr = driver.find_elements_by_css_selector(css_decsr)
                    if find_decsr[0].get_attribute('textContent') != group_description:
                        raise Exception('Wrong group Description')
                    print('Email Group - added')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')
        driver.implicitly_wait(15)

        # Delete > comfirm
        css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
        driver.find_elements_by_css_selector(css_selector)[0].click()
        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_confirm)))
        driver.find_element_by_id(CE.delete_confirm).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check notify
        if driver.find_elements_by_class_name(CElem.main_notification_title):
            notification_message = driver.find_element_by_class_name(CElem.main_notification_title).get_attribute(
                'textContent')
            if notification_message != CO.message_successfully_deleted:
                print('notification_message', notification_message)
                raise Exception('Wrong notification message')

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    raise Exception('Group found')
                count_items += 1
            else:
                break

    def test8_delete_fail(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        # exist group
        group_name = '1_test_email_group'
        group_content = 'exadel1@botf03.net'
        group_description = 'Do not delete this group. This test email group is assignment in ' \
                            'the alert and used in the Alert tests'

        # find group
        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    if find_content[0].get_attribute('textContent') != group_content:
                        raise Exception('Wrong group Content')
                    css_decsr = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_decsr = driver.find_elements_by_css_selector(css_decsr)
                    if find_decsr[0].get_attribute('textContent') != group_description:
                        raise Exception('Wrong group Description')
                    print('Email Group - exist')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')
        driver.implicitly_wait(15)

        # Delete > comfirm
        css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
        driver.find_elements_by_css_selector(css_selector)[0].click()
        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_confirm)))
        driver.find_element_by_id(CE.delete_confirm).click()
        driver.find_element_by_id(CE.error_dialog)
        error_message = driver.find_element_by_id(CE.error_form_list).get_attribute('textContent')
        if CO.reassign_error not in error_message:
            print('error_message', error_message)
            raise Exception('Wrong error message')
        driver.find_element_by_id(CE.error_close).click()
        time.sleep(5)

        count_items = 1
        driver.implicitly_wait(2)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if find_row[0].get_attribute('textContent') == group_name:
                    css_content = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(3)'
                    find_content = driver.find_elements_by_css_selector(css_content)
                    if find_content[0].get_attribute('textContent') != group_content:
                        raise Exception('Wrong group Content')
                    css_decsr = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(4)'
                    find_decsr = driver.find_elements_by_css_selector(css_decsr)
                    if find_decsr[0].get_attribute('textContent') != group_description:
                        raise Exception('Wrong group Description')
                    print('Email Group - exist')
                    break
                count_items += 1
            else:
                raise Exception('The Email Group', group_name, ' not found')

    def test9_mass_delete(self):
        print('\n', self._testMethodName)
        driver = self.driver
        driver.get(self.test_eg_url)
        wait = WebDriverWait(self.driver, 15)

        group_name = 'Test_Group'

        # find group
        items_value = 0
        count_items = 1
        driver.implicitly_wait(1)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if group_name in find_row[0].get_attribute('textContent'):
                    items_value += 1
                    css_checkbox = 'tr.ui-widget-content:nth-child(' + str(
                        count_items) + ') > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)'
                    driver.find_element_by_css_selector(css_checkbox).click()
                    print('Email Group selected')
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

        # Delete > cancel
        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_cancel)))
        driver.find_element_by_id(CE.delete_cancel).click()

        # find group
        items_value_2 = 0
        count_items = 1
        driver.implicitly_wait(1)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if group_name in find_row[0].get_attribute('textContent'):
                    items_value_2 += 1
                    print('Email Group selected')
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

        if items_value != items_value_2:
            raise Exception('Wrong value of items')

        # Delete > comfirm
        driver.find_element_by_id(CE.delete_button).click()
        driver.find_element_by_id(CE.delete_dialog)
        wait.until(EC.element_to_be_clickable((By.ID, CE.delete_confirm)))
        driver.find_element_by_id(CE.delete_confirm).click()
        Check.wait_until_invisibility(driver, wait, CElem.loading_bar)

        # Check notify
        driver.implicitly_wait(1)
        if driver.find_elements_by_class_name(CElem.main_notification_title):
            notification_message = driver.find_element_by_class_name(CElem.main_notification_title).get_attribute(
                'textContent')
            if notification_message != CO.message_successfully_deleted:
                print('notification_message', notification_message)
                raise Exception('Wrong notification message')

        # find group
        items_value_3 = 0
        count_items = 1
        driver.implicitly_wait(1)
        while count_items <= 20:
            print('count_items', count_items)
            css_selector = 'tr.ui-widget-content:nth-child(' + str(count_items) + ') > td:nth-child(2)'
            time.sleep(2)
            find_row = driver.find_elements_by_css_selector(css_selector)
            if find_row:
                if group_name in find_row[0].get_attribute('textContent'):
                    items_value_3 += 1
                count_items += 1
            else:
                break
        driver.implicitly_wait(15)

        if items_value_3 != 0:
            raise Exception('Not all items deleted')
