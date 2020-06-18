import time
import unittest
from selenium import webdriver
import Check
import Config.Contacts
from Config.Contacts import main_contacts
from main_app_window import Maw, driver_instance
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

mgd = Maw.get_devices()
cm = Config.Contacts.main_contacts.Elements
driver_instance.implicitly_wait(5)
contacts_folder = 'Contacts'
suggested_contacts_folder = 'Suggested Contacts'
deleted_items_folder = 'Deleted Items'


def setUpModule():
    print('Start: basics_contacts_tests.py\n')


def tearDownModule():
    Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
    folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
    if 'folder-selected' not in folder_status:
        raise Exception(contacts_folder + ' folder in not selected')
    elif 'folder-selected' in folder_status:
        print('Check - ' + contacts_folder + ' folder is selected')

    if Check.find_element_by_class_name_and_text(cm.contact_title, 'abr.test'):
        Check.find_element_by_class_name_and_text(cm.contact_title, 'abr.test').click()
        mgd.find_element_by_xpath(cm.delete_option).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
    if Check.find_element_by_class_name_and_text(cm.contact_title, 'Allison'):
        Check.find_element_by_class_name_and_text(cm.contact_title, 'Allison').click()
        mgd.find_element_by_xpath(cm.delete_option).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
    if Check.find_element_by_class_name_and_text(cm.contact_title, 'A Eddie Dean'):
        Check.find_element_by_class_name_and_text(cm.contact_title, 'A Eddie Dean').click()
        mgd.find_element_by_xpath(cm.delete_option).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
    if Check.find_element_by_class_name_and_text(cm.contact_title, 'Chambers Jake'):
        Check.find_element_by_class_name_and_text(cm.contact_title, 'Chambers Jake').click()
        mgd.find_element_by_xpath(cm.delete_option).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
    if Check.find_element_by_class_name_and_text(cm.contact_title, 'A Test'):
        Check.find_element_by_class_name_and_text(cm.contact_title, 'A Test').click()
        mgd.find_element_by_xpath(cm.delete_option).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)

    if Check.check_exists_by_class_name(cm.folders_list_wrapper):
        print('View mode is list of folders')
    else:
        print('View mode is list of contacts')
        mgd.find_element_by_xpath(cm.view_change).click()

    Check.find_element_by_class_name_and_text(cm.folder_name, 'Deleted Items').click()
    folder_status = mgd.find_element_by_xpath(cm.folder_deleted_items_select).get_attribute(name='class')
    if 'folder-selected' not in folder_status:
        raise Exception(deleted_items_folder + ' folder in not selected')
    elif 'folder-selected' in folder_status:
        print('Check - ' + deleted_items_folder + ' folder is selected')
    if Check.check_exists_by_class_name(cm.folders_list_wrapper):
        print('View mode is list of folders')
        # Check.assert_equal_xpath(
        # self, cm.view_change, 1, 'View change button not found', 'Check - View change button')
        # Check.assert_in_xpath_class(self, cm.view_change, 'clickable', 'View change button not clickable',
        #     'Check - View change button is clickable :')
        mgd.find_element_by_xpath(cm.view_change).click()
        time.sleep(1)

        main_len_of_list = len(mgd.find_elements_by_class_name(cm.name_in_abc))
        print('Len of list = ' + str(main_len_of_list))
        while main_len_of_list >= 2:
            name = mgd.find_element_by_class_name(cm.contact_title).get_attribute('innerText')
            print('Check - Contact ' + name + ' is open')
            # Check.assert_equal_xpath(self, cm.delete_option_abc, 1, 'Delete options unavailable',
            #                          'Check - Delete options')
            # Check.assert_in_xpath_class(
            #     self, cm.delete_option_abc,
            #     'clickable', 'Delete options not clickable', 'Check - Delete options is clickable :')
            mgd.find_element_by_xpath(cm.delete_option_abc).click()
            Check.element_is_visible_class_name(
                cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
            Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
            print('Check - Delete button')
            time.sleep(1)
            new_list = len(mgd.find_elements_by_class_name(cm.name_in_abc))
            if new_list >= main_len_of_list:
                raise Exception('Contact are not deleted')
            print('Check - ' + name + ' contact is deleted')
            main_len_of_list -= 1

    print('End: basics_contacts_tests.py\n')
    driver_instance.quit()


# @unittest.skip("Ok")
class Test1(unittest.TestCase):

    def setUp(self):
        mgd.find_element_by_xpath(cm.new_contact).click()
        print('Check - Add Contact button')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact card')

    def tearDown(self):
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()

        driver_instance.implicitly_wait(5)

    @unittest.skip("Ok")
    def test_1_open_close_new_contacts(self):
        Check.assert_equal_id(self, cm.close_button, 1, 'Close button is missing', 'Check - Close button')
        mgd.find_element_by_id(cm.close_button).click()
        Check.check_exists_by_class_name(cm.contact_info)
        print('Check - Contact card is closed')

    def test_2_yes_option(self):
        name = 'abr.test'
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')
        Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option).click()
        time.sleep(3)
        mgd.find_element_by_xpath("//*[@class='title' and contains(text(),'"+name+"')]")
        print('Check - ' + name + ' contact card')
        time.sleep(3)


# @unittest.skip("Ok")
class Test1Folders(unittest.TestCase):
    def setUp(self):
        Check.find_element_by_class_name_and_text(cm.folder_name, contacts_folder).click()

    def tearDown(self):
        Check.find_element_by_class_name_and_text(cm.folder_name, contacts_folder).click()

    def test1_folders(self):
        mgd.find_element_by_class_name(cm.folders_list_wrapper)
        print('Check - folder list wrapper')
        folders = [contacts_folder, suggested_contacts_folder, deleted_items_folder]
        folders_path = [cm.folder_contacts_select, cm.folder_suggestet_contacts_select, cm.folder_deleted_items_select]
        elem = 0
        for path in folders_path:
            mgd.find_element_by_xpath(path).click()
            a = mgd.find_element_by_xpath(path)
            folder_status = a.get_attribute(name='class')
            if 'folder-selected' not in folder_status:
                raise Exception(folders[elem] + ' folder in not selected')
            elif 'folder-selected' in folder_status:
                print('Check - ' + folders[elem] + ' folder is selected')
            elem += 1
        time.sleep(1)


# @unittest.skip("Ok")
class Test1ApplyUnsavedChanges(unittest.TestCase):

    def setUp(self):
        mgd.find_element_by_xpath(cm.new_contact).click()
        print('Check - Add Contact button')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact card')

    def tearDown(self):
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()

        driver_instance.implicitly_wait(5)

    # def test_1_open_close_new_contacts(self):
    #     Check.assert_equal_id(self, cm.close_button, 1, 'Close button is missing', 'Check - Close button')
    #     mgd.find_element_by_id(cm.close_button).click()
    #     Check.check_exists_by_class_name(cm.contact_info)
    #     print('Check - Contact card is closed')

    def test_for_no_wrapper(self):
        name = "Magneto"
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')
        Check.assert_equal_id(self, cm.close_button, 1, 'Close button is missing', 'Check - Close button')
        mgd.find_element_by_id(cm.close_button).click()
        Check.assert_in_class_name_text(
            self, cm.apply_unsaved_changes,
            'Apply unsaved changes?', 'Close editor confirmation did not exist', 'Check - ')
        Check.assert_equal_xpath(self, cm.no_apply_unsaved_changes, 1, '"No" button not found', 'Check - "No" button')
        mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()

    def test_for_yes_wrapper(self):
        name = "Allison"
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')
        department = "Testers"
        mgd.find_element_by_id(cm.department_input).send_keys(department)
        Check.assert_in_id_value(
            self, cm.department_input, department, 'Department input contain wrong data',
            'Check - Department input contain ')
        Check.assert_in_xpath_text(
            self, cm.department_info, department, 'Department info contain wrong data',
            'Check - Department title contain ')
        job_title = 'Bug'
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title contain wrong data', 'Check - Job title contain ')
        Check.assert_equal_xpath(self, cm.undo_option, 1, 'Undo options unavailable', 'Check - Undo options')

        Check.assert_equal_id(self, cm.close_button, 1, 'Close button is missing', 'Check - Close button')
        mgd.find_element_by_id(cm.close_button).click()
        Check.assert_in_class_name_text(
            self, cm.apply_unsaved_changes,
            'Apply unsaved changes?', 'Close editor confirmation did not exist', 'Check - ')
        Check.assert_equal_xpath(
            self, cm.yes_apply_unsaved_changes, 1, '"Yes" button not found', 'Check - "Yes" button')
        mgd.find_element_by_xpath(cm.yes_apply_unsaved_changes).click()
        time.sleep(2)

    def test_for_cancel_wrapper(self):
        name = "Abaddon"
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')
        Check.assert_equal_id(self, cm.close_button, 1, 'Close button is missing', 'Check - Close button')
        mgd.find_element_by_id(cm.close_button).click()
        Check.assert_in_class_name_text(
            self, cm.apply_unsaved_changes,
            'Apply unsaved changes?', 'Close editor confirmation did not exist', 'Check - ')
        Check.assert_equal_xpath(
            self, cm.cancel_apply_unsaved_changes, 1, '"Cancel" button not found', 'Check - "Cancel" button')
        mgd.find_element_by_xpath(cm.cancel_apply_unsaved_changes).click()
        time.sleep(2)


# @unittest.skip("Ok")
class Test2Options(unittest.TestCase):

    def setUp(self):
        print('setUp Test2Options')
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')

    def tearDown(self):
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        time.sleep(1)
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')
            time.sleep(1)
        driver_instance.implicitly_wait(5)

    # @unittest.skip("Ok")
    def test1_for_yes_option(self):
        name = "Armitage"
        name2 = 'AAAppolo'
        repeat = 1
        while repeat < 2:
            mgd.find_element_by_xpath(cm.new_contact).click()
            print('Check - Add Contact button')
            mgd.find_element_by_class_name(cm.contact_info)
            print('Check - Contact card')
            if repeat == 1:
                mgd.find_element_by_id(cm.name_input).send_keys(name)
            elif repeat == 2:
                mgd.find_element_by_id(cm.name_input).send_keys(name2)
            Check.assert_in_id_value(
                self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
            Check.assert_in_xpath_text(
                self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')
            Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
            Check.assert_in_xpath_class(
                self, cm.yes_option, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
            mgd.find_element_by_xpath(cm.yes_option).click()
            time.sleep(1)
            mgd.find_element_by_xpath("//*[@class='title' and contains(text(),'"+name+"')]")
            print('Check - ' + name + ' contact card')
            time.sleep(1)
            repeat += 1

    # @unittest.skip("Fall - Ok")
    def test_for_undo_option_create(self):
        name = "Armitage"
        mgd.find_element_by_xpath(cm.new_contact).click()
        print('Check - Add Contact button')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact card')
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')
        job_title = 'Policeman'
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title contain wrong data', 'Check - Job title contain ')
        Check.assert_equal_xpath(self, cm.undo_option, 1, 'Undo options unavailable', 'Check - Undo options')
        time.sleep(1)
        Check.assert_in_xpath_class(
            self, cm.undo_option, 'clickable', 'Undo options not clickable', 'Check - Undo options is clickable :')
        mgd.find_element_by_xpath(cm.undo_option).click()
        time.sleep(1)
        Check.assert_not_in_id_value(
            self, cm.name_input, name, 'Name input contain ' + name, 'Check - Name input clear')
        Check.assert_not_in_xpath_text(
            self, cm.name_title, name, 'Name title contain ' + name, 'Check - Name title clear')
        Check.assert_not_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title contain ' + job_title, 'Check - Job title clear')
        time.sleep(3)

    # @unittest.skip("Ok")
    def test2_for_undo_option_exist(self):
        name = 'Armitage'
        name2 = 'Azazel'
        print(Check.find_element_by_class_name_and_text(cm.contact_title, name))
        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        print('Check - Contact card')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact ' + name + ' is open')
        time.sleep(1)
        mgd.find_element_by_id(cm.name_input).clear()
        mgd.find_element_by_id(cm.name_input).send_keys(name2)
        Check.assert_in_id_value(
            self, cm.name_input, name2, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name2, 'Name title contain wrong data', 'Check - Name title contain ')
        job_title = 'Policeman'
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title contain wrong data', 'Check - Job title contain ')
        Check.assert_equal_xpath(self, cm.undo_option, 1, 'Undo options unavailable', 'Check - Undo options')
        Check.assert_in_xpath_class(
            self, cm.undo_option, 'clickable', 'Undo options not clickable', 'Check - Undo options is clickable :')
        mgd.find_element_by_xpath(cm.undo_option).click()
        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title')
        Check.assert_not_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title contain ' + job_title, 'Check - Job title clear')
        time.sleep(3)

    # @unittest.skip("Ok")
    def test_for_delete_option(self):
        name = 'Armitage'
        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        print('Check - Contact card')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact ' + name + ' is open')
        time.sleep(1)
        Check.assert_equal_xpath(self, cm.delete_option, 1, 'Delete options unavailable', 'Check - Delete options')
        Check.assert_in_xpath_class(
            self, cm.delete_option,
            'clickable', 'Delete options not clickable', 'Check - Delete options is clickable :')
        mgd.find_element_by_xpath(cm.delete_option).click()
        time.sleep(1)
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
        Check.assert_equal_class_name(
            self, cm.block_wrapper, 0, 'Delete wrapper exist', 'Check - Delete wrapper does not exist')

        Check.find_element_by_class_name_and_text(cm.folder_name, 'Deleted Items').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_deleted_items_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(deleted_items_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + deleted_items_folder + ' folder is selected')

        # if Check.find_element_by_class_name_and_text(cm.contact_title, name) is not None:
        #     print('Check - ' + name + ' is found')
        # elif Check.find_element_by_class_name_and_text(cm.contact_title, name) is None:
        #     raise Exception(name + ' not found')

    # @unittest.skip("")
    def test_for_move_to1(self):
        name = 'AAAppolo'

        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        print('Check - Contact card')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact ' + name + ' is open')
        time.sleep(1)
        Check.assert_equal_xpath(self, cm.move_to_option, 1, 'Move to options unavailable', 'Check - Move to options')
        Check.assert_in_xpath_class(
            self, cm.move_to_option,
            'clickable', 'Move to options not clickable', 'Check - Move to options is clickable :')
        mgd.find_element_by_xpath(cm.move_to_option).click()
        time.sleep(1)
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Move to wrapper', 'Move to wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Suggested Contacts').click()
        print('Check - Suggested Contacts button')

        Check.find_element_by_class_name_and_text(cm.folder_name, 'Suggested Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_suggestet_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(suggested_contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + suggested_contacts_folder + ' folder is selected')

        if Check.find_element_by_class_name_and_text(cm.contact_title, name) is not None:
            print('Check - ' + name + ' is found')
        elif Check.find_element_by_class_name_and_text(cm.contact_title, name) is None:
            raise Exception(name + ' not found')

    # @unittest.skip("")
    def test_for_move_to2(self):
        name = 'AAAppolo'

        Check.find_element_by_class_name_and_text(cm.folder_name, 'Suggested Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_suggestet_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(suggested_contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + suggested_contacts_folder + ' folder is selected')

        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        print('Check - Contact card')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact ' + name + ' is open')
        time.sleep(2)
        #########
        #########
        Check.assert_equal_xpath(self, cm.move_to_option, 1, 'Move to options unavailable', 'Check - Move to options')
        Check.assert_in_xpath_class(
            self, cm.move_to_option,
            'clickable', 'Move to options not clickable', 'Check - Move to options is clickable :')
        mgd.find_element_by_xpath(cm.move_to_option).click()
        time.sleep(1)
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Move to wrapper', 'Move to wrapper does not exist')
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Contacts').click()
        print('Check - Contacts button')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        time.sleep(1)
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')
            time.sleep(1)
        if Check.find_element_by_class_name_and_text(cm.contact_title, name) is not None:
            print('Check - ' + name + ' is found')
        elif Check.find_element_by_class_name_and_text(cm.contact_title, name) is None:
            raise Exception(name + ' not found')

    # @unittest.skip("Ok")
    def test_for_move_to3_with_apply_unsaved_changes_yes(self):
        name = 'AAAppolo'
        job_edit = 'Musician'

        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        print('Check - Contact card')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact ' + name + ' is open')
        time.sleep(1)

        #########

        mgd.find_element_by_id(cm.job_title_input).clear()
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_edit)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_edit, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_edit, 'Job title info contain wrong data',
            'Check - Job title title contain ')

        Check.assert_equal_xpath(self, cm.move_to_option, 1, 'Move to options unavailable',
                                 'Check - Move to options')
        Check.assert_in_xpath_class(
            self, cm.move_to_option,
            'clickable', 'Move to options not clickable', 'Check - Move to options is clickable :')
        mgd.find_element_by_xpath(cm.move_to_option).click()
        time.sleep(1)

        #########

        Check.assert_in_class_name_text(
            self, cm.apply_unsaved_changes,
            'Apply unsaved changes before contact moving?', 'Close editor confirmation did not exist', 'Check - ')
        Check.assert_equal_xpath(self, cm.yes_apply_unsaved_changes, 1, '"Yes" button not found', 'Check - "Yes" button')
        mgd.find_element_by_xpath(cm.yes_apply_unsaved_changes).click()

        #########

        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Move to wrapper', 'Move to wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Suggested Contacts').click()
        print('Check - Suggested Contacts button')



        ##################

        Check.find_element_by_class_name_and_text(cm.folder_name, 'Suggested Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_suggestet_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(suggested_contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + suggested_contacts_folder + ' folder is selected')
        if Check.find_element_by_class_name_and_text(cm.contact_title, name) is not None:
            print('Check - ' + name + ' is found')
        elif Check.find_element_by_class_name_and_text(cm.contact_title, name) is None:
            raise Exception(name + ' not found')
        ##########
        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        Check.assert_in_id_value(
            self, cm.job_title_input, job_edit, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_edit, 'Job title info contain wrong data',
            'Check - Job title title contain ')

    # @unittest.skip("Ok")
    def test_for_move_to4_with_apply_unsaved_changes_no(self):
        name = 'AAAppolo'
        job_edit = 'Elder god'

        Check.find_element_by_class_name_and_text(cm.folder_name, 'Suggested Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_suggestet_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(suggested_contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + suggested_contacts_folder + ' folder is selected')

        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        print('Check - Contact card')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact ' + name + ' is open')
        time.sleep(2)

        mgd.find_element_by_id(cm.job_title_input).clear()
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_edit)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_edit, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_edit, 'Job title info contain wrong data',
            'Check - Job title title contain ')

        Check.assert_equal_xpath(self, cm.move_to_option, 1, 'Move to options unavailable',
                                 'Check - Move to options')
        Check.assert_in_xpath_class(
            self, cm.move_to_option,
            'clickable', 'Move to options not clickable', 'Check - Move to options is clickable :')
        mgd.find_element_by_xpath(cm.move_to_option).click()
        time.sleep(1)

        #########

        Check.assert_in_class_name_text(
            self, cm.apply_unsaved_changes,
            'Apply unsaved changes before contact moving?', 'Close editor confirmation did not exist', 'Check - ')
        Check.assert_equal_xpath(self, cm.no_apply_unsaved_changes, 1, '"No" button not found', 'Check - "No" button')
        mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()

        #########

        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Move to wrapper', 'Move to wrapper does not exist')
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Contacts').click()
        print('Check - Contacts button')

        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        time.sleep(1)
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')
            time.sleep(1)
        if Check.find_element_by_class_name_and_text(cm.contact_title, name) is not None:
            print('Check - ' + name + ' is found')
        elif Check.find_element_by_class_name_and_text(cm.contact_title, name) is None:
            raise Exception(name + ' not found')

        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        Check.assert_not_in_id_value(
            self, cm.job_title_input, job_edit, 'Job title input contain wrong data',
            'Check - Job title input')
        Check.assert_not_in_xpath_text(
            self, cm.job_title_info, job_edit, 'Job title info contain wrong data',
            'Check - Job title title')

    # @unittest.skip("Ok")
    def test_for_move_to5_with_apply_unsaved_changes_cancel(self):
        name = 'AAAppolo'
        job_edit1 = 'Musician'
        job_edit2 = 'Unknown'
        job_edit3 = 'Archer'

        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        print('Check - Contact card')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact ' + name + ' is open')
        time.sleep(1)

        mgd.find_element_by_id(cm.job_title_input).clear()
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_edit2)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_edit2, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_edit2, 'Job title info contain wrong data',
            'Check - Job title title contain ')

        Check.assert_equal_xpath(self, cm.move_to_option, 1, 'Move to options unavailable',
                                 'Check - Move to options')
        Check.assert_in_xpath_class(
            self, cm.move_to_option,
            'clickable', 'Move to options not clickable', 'Check - Move to options is clickable :')
        mgd.find_element_by_xpath(cm.move_to_option).click()
        time.sleep(1)

        #########

        Check.assert_in_class_name_text(
            self, cm.apply_unsaved_changes,
            'Apply unsaved changes before contact moving?', 'Close editor confirmation did not exist', 'Check - ')
        Check.assert_equal_xpath(
            self, cm.cancel_apply_unsaved_changes, 1, '"Cancel" button not found', 'Check - "Cancel" button')
        mgd.find_element_by_xpath(cm.cancel_apply_unsaved_changes).click()

        #########
        mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()

        time.sleep(1)
        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        print('Check - ' + name + ' is found')
        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_edit1, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_edit1, 'Job title info contain wrong data',
            'Check - Job title title contain ')
        Check.assert_not_in_id_value(
            self, cm.job_title_input, job_edit2, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_not_in_xpath_text(
            self, cm.job_title_info, job_edit2, 'Job title info contain wrong data',
            'Check - Job title title contain ')
        time.sleep(1)
        mgd.find_element_by_id(cm.job_title_input).clear()
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_edit3)
        time.sleep(1)
        Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option).click()


# @unittest.skip("Ok")
class Test3EditContact(unittest.TestCase):
        def setUp(self):
            Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
            folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
            if 'folder-selected' not in folder_status:
                raise Exception(contacts_folder + ' folder in not selected')
            elif 'folder-selected' in folder_status:
                print('Check - ' + contacts_folder + ' folder is selected')

            mgd.find_element_by_xpath(cm.new_contact).click()
            name = "A Test"
            mgd.find_element_by_id(cm.name_input).send_keys(name)
            Check.assert_in_id_value(
                self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
            Check.assert_in_xpath_text(
                self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')
            Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
            Check.assert_in_xpath_class(
                self, cm.yes_option, 'option-item active clickable', 'Yes options not clickable',
                'Check - Yes options is clickable :')
            mgd.find_element_by_xpath(cm.yes_option).click()

        def tearDown(self):
            driver_instance.implicitly_wait(1)
            if Check.check_exists_by_xpath(cm.contact_modal_window):
                print('Contact card - exist')
                mgd.find_element_by_id(cm.close_button).click()
            if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
                print('Block wrapper "Apply unsaved changes" - exist')
                mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
            driver_instance.implicitly_wait(5)

        def test_edit_contact(self):
            time.sleep(3)
            Check.find_element_by_class_name_and_text(cm.contact_title, 'A Test').click()
            Check.assert_equal_class_name(self, cm.contact_info, 1, 'Contact info - not exist', 'Check - Contact info')
            name = "A Eddie Dean"
            mgd.find_element_by_id(cm.name_input).clear()
            mgd.find_element_by_id(cm.name_input).send_keys(name)
            Check.assert_in_id_value(
                self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
            Check.assert_in_xpath_text(
                self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')

            job_title = "Traveler"
            mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
            Check.assert_in_id_value(
                self, cm.job_title_input, job_title, 'Job title input contain wrong data',
                'Check - Job title input contain ')
            Check.assert_in_xpath_text(
                self, cm.job_title_info, job_title, 'Job title info contain wrong data',
                'Check - Job title title contain ')

            company = "Ka-tet"
            mgd.find_element_by_id(cm.company_input).send_keys(company)
            Check.assert_in_id_value(
                self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
            Check.assert_in_xpath_text(
                self, cm.company_info, company, 'Company info contain wrong data', 'Check - Company title contain ')

            department = "Department of the Mid-world"
            mgd.find_element_by_id(cm.department_input).send_keys(department)
            Check.assert_in_id_value(
                self, cm.department_input, department, 'Department input contain wrong data',
                'Check - Department input contain ')
            Check.assert_in_xpath_text(
                self, cm.department_info, department, 'Department info contain wrong data',
                'Check - Department title contain ')

            mgd.find_element_by_id(cm.birthday_input).click()
            mgd.find_element_by_id(cm.birthday_input).send_keys("881987")
            Check.assert_in_id_value(
                self, cm.birthday_input, '1987-08-08', 'Birthday input contain wrong data',
                'Check - Birthday input contain ')

            contacts_tab = mgd.find_element_by_id(cm.contact_tab)
            contacts_tab.click()

            business_phone = '8012129070'
            mgd.find_element_by_name(cm.business_phone_input).send_keys(business_phone)
            Check.assert_in_name_value(
                self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
                'Check - Business phone input contain ')
            Check.assert_in_xpath_text(
                self, cm.work_phone_info, business_phone, 'Business phone info contain wrong data',
                'Check - Business phone title contain ')

            mobile_phone = '8012127090'
            mgd.find_element_by_name(cm.mobile_phone_input).send_keys(mobile_phone)
            Check.assert_in_name_value(
                self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
                'Check - Mobile phone input contain ')

            home_phone = '8012125060'
            mgd.find_element_by_name(cm.home_phone_input).send_keys(home_phone)
            Check.assert_in_name_value(
                self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
                'Check - Home phone input contain ')

            website = 'big_black_house.com'
            mgd.find_element_by_id(cm.website_input).send_keys(website)
            Check.assert_in_id_value(
                self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input contain ')

            email_1 = 'twenty-three-year-old@ka-tet.turtle'
            mgd.find_element_by_id(cm.email_input).send_keys(email_1)
            Check.assert_in_id_value(
                self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input contain ')

            email_2 = '1987_new_york@ka-tet.turtle'
            mgd.find_element_by_id(cm.email_input_2).send_keys(email_2)
            Check.assert_in_id_value(
                self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 contain ')

            email_3 = 'keflex_mid-world@ka-tet.turtle'
            mgd.find_element_by_id(cm.email_input_3).send_keys(email_3)
            Check.assert_in_id_value(
                self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 contain ')

            im_id = 'None'
            mgd.find_element_by_id(cm.im_id_input).send_keys(im_id)
            time.sleep(1)
            Check.assert_in_id_value(
                self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input contain ')

            address_tab = mgd.find_element_by_id(cm.address_tab)
            address_tab.click()

            work_street = '2264 Walton st'
            mgd.find_element_by_name(cm.work_street_input).send_keys(work_street)
            Check.assert_in_name_value(
                self, cm.work_street_input, work_street, 'Work street input contain wrong data',
                'Check - Work street input contain ')

            work_city = 'Portland'
            mgd.find_element_by_name(cm.work_city_input).send_keys(work_city)
            Check.assert_in_name_value(
                self, cm.work_city_input, work_city, 'Work city input contain wrong data',
                'Check - Work city input contain ')

            work_state = 'Maine'
            mgd.find_element_by_name(cm.work_state_input).send_keys(work_state)
            Check.assert_in_name_value(
                self, cm.work_state_input, work_state, 'Work state input contain wrong data',
                'Check - Work state input contain ')

            work_postal_code = 'ME 04103'
            mgd.find_element_by_name(cm.work_postal_code_input).send_keys(work_postal_code)
            Check.assert_in_name_value(
                self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
                'Check - Work postal code input contain ')

            work_country = 'USA'
            mgd.find_element_by_name(cm.work_country_input).send_keys(work_country)
            Check.assert_in_name_value(
                self, cm.work_country_input, work_country, 'Work country input contain wrong data',
                'Check - Work country input contain ')
            work_address = work_street + ' ' + work_city + ' ' + work_state + ' ' + work_postal_code + ' ' + work_country
            Check.assert_in_xpath_text(
                self, cm.address_info, work_address, 'Address info contain wrong data',
                'Check - Address title contain ')

            home_street = '51 Florida Ave'
            mgd.find_element_by_name(cm.home_street_input).send_keys(home_street)
            Check.assert_in_name_value(
                self, cm.home_street_input, home_street, 'Home street input contain wrong data',
                'Check - Home street input contain ')

            home_city = 'Bangor'
            mgd.find_element_by_name(cm.home_city_input).send_keys(home_city)
            Check.assert_in_name_value(
                self, cm.home_city_input, home_city, 'Home city input contain wrong data',
                'Check - Home city input contain ')

            home_state = 'Maine'
            mgd.find_element_by_name(cm.home_state_input).send_keys(home_state)
            Check.assert_in_name_value(
                self, cm.home_state_input, home_state, 'Home state input contain wrong data',
                'Check - Home state input contain ')

            home_postal_code = 'ME 04401-3005'
            mgd.find_element_by_name(cm.home_postal_code_input).send_keys(home_postal_code)
            Check.assert_in_name_value(
                self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',
                'Check - Home postal code input contain ')

            home_country = 'USA'
            mgd.find_element_by_name(cm.home_country_input).send_keys(home_country)
            Check.assert_in_name_value(
                self, cm.home_country_input, home_country, 'Home country input contain wrong data',
                'Check - Home country input contain ')

            more_tab = mgd.find_element_by_id(cm.more_tab)
            more_tab.click()

            language = 'English, Spanish'
            mgd.find_element_by_id(cm.language_input).send_keys(language)
            Check.assert_in_id_value(
                self, cm.language_input, language, 'Language input contain wrong data',
                'Check - Language input contain ')

            hobbies = 'Music, Shooting'
            mgd.find_element_by_id(cm.hobbies_input).send_keys(hobbies)
            Check.assert_in_id_value(
                self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input contain ')
            # mgd.find_element_by_name(cm.gender).click()
            # Check.assert_equal_xpath(
            #     self, cm.gender_wrapper, 1, 'Gender wrapper is not exist', 'Check - Gender wrapper exist')
            # mgd.find_element_by_xpath(cm.male).click()
            # Check.assert_in_id_value(self, cm.gender, 'male', 'Gender contain wrong data', 'Check - Gender is')
            Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
            Check.assert_in_xpath_class(
                self, cm.yes_option, 'option-item active clickable', 'Yes options not clickable',
                'Check - Yes options is clickable :')
            mgd.find_element_by_xpath(cm.yes_option).click()
            time.sleep(2)
            a = Check.find_element_by_class_name_and_text(cm.contact_title, name)
            a.click()
            time.sleep(2)

            Check.assert_in_id_value(
                self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
            Check.assert_in_xpath_text(
                self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')

            Check.assert_in_id_value(
                self, cm.job_title_input, job_title, 'Job title input contain wrong data',
                'Check - Job title input contain ')
            Check.assert_in_xpath_text(
                self, cm.job_title_info, job_title, 'Job title info contain wrong data',
                'Check - Job title title contain ')

            Check.assert_in_id_value(
                self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
            Check.assert_in_xpath_text(
                self, cm.company_info, company, 'Company info contain wrong data', 'Check - Company title contain ')

            Check.assert_in_id_value(
                self, cm.department_input, department, 'Department input contain wrong data',
                'Check - Department input contain ')
            Check.assert_in_xpath_text(
                self, cm.department_info, department, 'Department info contain wrong data',
                'Check - Department title contain ')

            Check.assert_in_id_value(
                self, cm.birthday_input, '1987-08-08', 'Birthday input contain wrong data',
                'Check - Birthday input contain ')

            contacts_tab = mgd.find_element_by_id(cm.contact_tab)
            contacts_tab.click()

            Check.assert_in_name_value(
                self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
                'Check - Business phone input contain ')
            Check.assert_in_xpath_text(
                self, cm.work_phone_info, business_phone, 'Business phone info contain wrong data',
                'Check - Business phone title contain ')

            Check.assert_in_name_value(
                self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
                'Check - Mobile phone input contain ')

            Check.assert_in_name_value(
                self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
                'Check - Home phone input contain ')

            Check.assert_in_id_value(
                self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input contain ')

            Check.assert_in_id_value(
                self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input contain ')

            Check.assert_in_id_value(
                self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 contain ')

            Check.assert_in_id_value(
                self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 contain ')

            time.sleep(1)
            Check.assert_in_id_value(
                self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input contain ')

            address_tab = mgd.find_element_by_id(cm.address_tab)
            address_tab.click()

            Check.assert_in_name_value(
                self, cm.work_street_input, work_street, 'Work street input contain wrong data',
                'Check - Work street input contain ')

            Check.assert_in_name_value(
                self, cm.work_city_input, work_city, 'Work city input contain wrong data',
                'Check - Work city input contain ')

            Check.assert_in_name_value(
                self, cm.work_state_input, work_state, 'Work state input contain wrong data',
                'Check - Work state input contain ')

            Check.assert_in_name_value(
                self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
                'Check - Work postal code input contain ')

            Check.assert_in_name_value(
                self, cm.work_country_input, work_country, 'Work country input contain wrong data',
                'Check - Work country input contain ')
            work_address = work_street + ' ' + work_city + ' ' + work_state + ' ' + work_postal_code + ' ' + work_country
            Check.assert_in_xpath_text(
                self, cm.address_info, work_address, 'Address info contain wrong data',
                'Check - Address title contain ')

            Check.assert_in_name_value(
                self, cm.home_street_input, home_street, 'Home street input contain wrong data',
                'Check - Home street input contain ')

            Check.assert_in_name_value(
                self, cm.home_city_input, home_city, 'Home city input contain wrong data',
                'Check - Home city input contain ')

            Check.assert_in_name_value(
                self, cm.home_state_input, home_state, 'Home state input contain wrong data',
                'Check - Home state input contain ')

            Check.assert_in_name_value(
                self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',
                'Check - Home postal code input contain ')

            Check.assert_in_name_value(
                self, cm.home_country_input, home_country, 'Home country input contain wrong data',
                'Check - Home country input contain ')

            more_tab = mgd.find_element_by_id(cm.more_tab)
            more_tab.click()

            Check.assert_in_id_value(
                self, cm.language_input, language, 'Language input contain wrong data',
                'Check - Language input contain ')

            Check.assert_in_id_value(
                self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input contain ')
            # Check.assert_in_id_value(self, cm.gender, 'male', 'Gender contain wrong data', 'Check - Gender is')

            print('Check - Contact card is edited')


# @unittest.skip("Ok")
class Test4Fill(unittest.TestCase):

    def setUp(self):
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')

        mgd.find_element_by_xpath(cm.new_contact).click()
        print('Check - Add Contact button')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact card')

    def tearDown(self):
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        driver_instance.implicitly_wait(5)

    # @unittest.skip('Fall - Ok')
    def test_fill_and_undo(self):
        name = "Jake Chambers"
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')

        job_title = "Traveler"
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title info contain wrong data', 'Check - Job title title contain ')

        company = "Ka-tet"
        mgd.find_element_by_id(cm.company_input).send_keys(company)
        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info, company, 'Company info contain wrong data', 'Check - Company title contain ')

        department = "Department of the Mid-world"
        mgd.find_element_by_id(cm.department_input).send_keys(department)
        Check.assert_in_id_value(
            self, cm.department_input, department, 'Department input contain wrong data',
            'Check - Department input contain ')
        Check.assert_in_xpath_text(
            self, cm.department_info, department, 'Department info contain wrong data',
            'Check - Department title contain ')

        mgd.find_element_by_id(cm.birthday_input).click()
        mgd.find_element_by_id(cm.birthday_input).send_keys("881966")
        Check.assert_in_id_value(
            self, cm.birthday_input, '1966-08-08', 'Birthday input contain wrong data',
            'Check - Birthday input contain ')

        contacts_tab = mgd.find_element_by_id(cm.contact_tab)
        contacts_tab.click()

        business_phone = '8080809070'
        mgd.find_element_by_name(cm.business_phone_input).send_keys(business_phone)
        Check.assert_in_name_value(
            self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
            'Check - Business phone input contain ')
        Check.assert_in_xpath_text(
            self, cm.work_phone_info, business_phone, 'Business phone info contain wrong data',
            'Check - Business phone title contain ')

        mobile_phone = '8080807090'
        mgd.find_element_by_name(cm.mobile_phone_input).send_keys(mobile_phone)
        Check.assert_in_name_value(
            self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
            'Check - Mobile phone input contain ')

        home_phone = '8080805060'
        mgd.find_element_by_name(cm.home_phone_input).send_keys(home_phone)
        Check.assert_in_name_value(
            self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
            'Check - Home phone input contain ')

        website = 'haunted_house.com '
        mgd.find_element_by_id(cm.website_input).send_keys(website)
        Check.assert_in_id_value(
            self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input contain ')

        email_1 = 'eleven-year-old@ka-tet.turtle'
        mgd.find_element_by_id(cm.email_input).send_keys(email_1)
        Check.assert_in_id_value(
            self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input contain ')

        email_2 = 'new_york@ka-tet.turtle'
        mgd.find_element_by_id(cm.email_input_2).send_keys(email_2)
        Check.assert_in_id_value(
            self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 contain ')

        email_3 = 'mid-world@ka-tet.turtle'
        mgd.find_element_by_id(cm.email_input_3).send_keys(email_3)
        Check.assert_in_id_value(
            self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 contain ')

        im_id = 'None'
        mgd.find_element_by_id(cm.im_id_input).send_keys(im_id)
        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input contain ')

        address_tab = mgd.find_element_by_id(cm.address_tab)
        address_tab.click()

        work_street = '2264 Walton st'
        mgd.find_element_by_name(cm.work_street_input).send_keys(work_street)
        Check.assert_in_name_value(
            self, cm.work_street_input, work_street, 'Work street input contain wrong data',
            'Check - Work street input contain ')

        work_city = 'Portland'
        mgd.find_element_by_name(cm.work_city_input).send_keys(work_city)
        Check.assert_in_name_value(
            self, cm.work_city_input, work_city, 'Work city input contain wrong data',
            'Check - Work city input contain ')

        work_state = 'Maine'
        mgd.find_element_by_name(cm.work_state_input).send_keys(work_state)
        Check.assert_in_name_value(
            self, cm.work_state_input, work_state, 'Work state input contain wrong data',
            'Check - Work state input contain ')

        work_postal_code = 'ME 04103'
        mgd.find_element_by_name(cm.work_postal_code_input).send_keys(work_postal_code)
        Check.assert_in_name_value(
            self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
            'Check - Work postal code input contain ')

        work_country = 'USA'
        mgd.find_element_by_name(cm.work_country_input).send_keys(work_country)
        Check.assert_in_name_value(
            self, cm.work_country_input, work_country, 'Work country input contain wrong data',
            'Check - Work country input contain ')
        work_address = work_street + ' ' + work_city + ' ' + work_state + ' ' + work_postal_code + ' ' + work_country
        Check.assert_in_xpath_text(
            self, cm.address_info, work_address, 'Address info contain wrong data', 'Check - Address title contain ')

        home_street = '49 Florida Ave'
        mgd.find_element_by_name(cm.home_street_input).send_keys(home_street)
        Check.assert_in_name_value(
            self, cm.home_street_input, home_street, 'Home street input contain wrong data',
            'Check - Home street input contain ')

        home_city = 'Bangor'
        mgd.find_element_by_name(cm.home_city_input).send_keys(home_city)
        Check.assert_in_name_value(
            self, cm.home_city_input, home_city, 'Home city input contain wrong data',
            'Check - Home city input contain ')

        home_state = 'Maine'
        mgd.find_element_by_name(cm.home_state_input).send_keys(home_state)
        Check.assert_in_name_value(
            self, cm.home_state_input, home_state, 'Home state input contain wrong data',
            'Check - Home state input contain ')

        home_postal_code = 'ME 04401-3005'
        mgd.find_element_by_name(cm.home_postal_code_input).send_keys(home_postal_code)
        Check.assert_in_name_value(
            self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',
            'Check - Home postal code input contain ')

        home_country = 'USA'
        mgd.find_element_by_name(cm.home_country_input).send_keys(home_country)
        Check.assert_in_name_value(
            self, cm.home_country_input, home_country, 'Home country input contain wrong data',
            'Check - Home country input contain ')

        more_tab = mgd.find_element_by_id(cm.more_tab)
        more_tab.click()

        language = 'English, Spanish'
        mgd.find_element_by_id(cm.language_input).send_keys(language)
        Check.assert_in_id_value(
            self, cm.language_input, language, 'Language input contain wrong data', 'Check - Language input contain ')

        hobbies = 'Cooking, Shooting'
        mgd.find_element_by_id(cm.hobbies_input).send_keys(hobbies)
        Check.assert_in_id_value(
            self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input contain ')

        # mgd.find_element_by_id(cm.gender).click()
        # Check.assert_equal_xpath(
        #     self, cm.gender_wrapper, 1, 'Gender wrapper is not exist', 'Check - Gender wrapper exist')
        # mgd.find_element_by_xpath(cm.female).click()
        # Check.assert_in_id_value(self, cm.gender, 'female', 'Gender contain wrong data', 'Check - Gender is')
        # mgd.find_element_by_id(cm.gender).click()
        # Check.assert_equal_xpath(
        #     self, cm.gender_wrapper, 1, 'Gender wrapper is not exist', 'Check - Gender wrapper exist')
        # mgd.find_element_by_xpath(cm.male).click()
        # Check.assert_in_id_value(self, cm.gender, 'male', 'Gender contain wrong data', 'Check - Gender is')

        Check.assert_equal_xpath(self, cm.undo_option, 1, 'Undo options unavailable', 'Check - Undo options')
        Check.assert_in_xpath_class(
            self, cm.undo_option, 'clickable can', 'Undo options not clickable', 'Check - Undo options is clickable :')
        mgd.find_element_by_xpath(cm.undo_option).click()
        Check.assert_not_in_xpath_class(
            self, cm.undo_option, 'clickable can', 'Undo options is clickable', 'Check - Undo options not clickable')

        #
        # verification after rollback of changes
        #
        #

        time.sleep(2)
        mgd.find_element_by_id(cm.profile_tab).click()
        Check.assert_not_in_id_value(
            self, cm.name_input, name, 'Name input not empty', 'Check - Name input is empty')
        Check.assert_not_in_xpath_text(
            self, cm.name_title, name, 'Name title not empty', 'Check - Name title is empty')

        Check.assert_not_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input not empty', 'Check - Job title is empty')
        Check.assert_not_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title info not empty', 'Check - Job title is empty')

        Check.assert_not_in_id_value(
            self, cm.company_input, company, 'Company input not empty', 'Check - Company input is empty')
        Check.assert_not_in_xpath_text(
            self, cm.company_info, company, 'Company info not empty', 'Check - Company title is empty')

        Check.assert_not_in_id_value(
            self, cm.department_input, department, 'Department input not empty', 'Check - Department input is empty')
        Check.assert_not_in_xpath_text(
            self, cm.department_info, department, 'Department info not empty', 'Check - Department title is empty')

        Check.assert_not_in_id_value(
            self, cm.birthday_input, '1966-08-08', 'Birthday input not empty', 'Check - Birthday input is empty')

        contacts_tab = mgd.find_element_by_id(cm.contact_tab)
        contacts_tab.click()

        Check.assert_not_in_name_value(
            self, cm.business_phone_input, business_phone, 'Business phone input not empty',
            'Check - Business phone input is empty')

        Check.assert_not_in_xpath_text(
            self, cm.work_phone_info, business_phone, 'Business phone info not empty',
            'Check - Business phone title is empty')

        Check.assert_not_in_name_value(
            self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input not empty',
            'Check - Mobile phone input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_phone_input, home_phone, 'Home phone input not empty', 'Check - Home phone input is empty')

        Check.assert_not_in_id_value(
            self, cm.website_input, website, 'Website input not empty', 'Check - Website input is empty')

        Check.assert_not_in_id_value(
            self, cm.email_input, email_1, 'Email input not empty', 'Check - Email input is empty')

        Check.assert_not_in_id_value(
            self, cm.email_input_2, email_2, 'Email input 2 not empty', 'Check - Email input 2 is empty')

        Check.assert_not_in_id_value(
            self, cm.email_input_3, email_3, 'Email input 3 not empty', 'Check - Email input 3 is empty')

        time.sleep(1)
        Check.assert_not_in_id_value(
            self, cm.im_id_input, im_id, 'Im_id input not empty', 'Check - Im_id input is empty')

        address_tab = mgd.find_element_by_id(cm.address_tab)
        address_tab.click()

        Check.assert_not_in_name_value(
            self, cm.work_street_input, work_street, 'Work street input not empty',
            'Check - Work street input is empty')

        Check.assert_not_in_name_value(
            self, cm.work_city_input, work_city, 'Work city input not empty', 'Check - Work city input is empty')

        Check.assert_not_in_name_value(
            self, cm.work_state_input, work_state, 'Work state input not empty', 'Check - Work state input is empty')

        Check.assert_not_in_name_value(
            self, cm.work_postal_code_input, work_postal_code, 'Work postal code input not empty',
            'Check - Work postal code input is empty')

        Check.assert_not_in_name_value(
            self, cm.work_country_input, work_country, 'Work country input not empty',
            'Check - Work country input is empty')
        Check.assert_not_in_xpath_text(
            self, cm.address_info, work_address, 'Address info not empty', 'Check - Address title is empty')

        Check.assert_not_in_name_value(
            self, cm.home_street_input, home_street, 'Home street input not empty',
            'Check - Home street input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_city_input, home_city, 'Home city input not empty', 'Check - Home city input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_state_input,  home_state, 'Home state input not empty', 'Check - Home state input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_postal_code_input, home_postal_code, 'Home postal code input not empty',

            'Check - Home postal code input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_country_input, home_country, 'Home country input not empty',
            'Check - Home country input is empty')

        more_tab = mgd.find_element_by_id(cm.more_tab)
        more_tab.click()

        Check.assert_not_in_id_value(
            self, cm.language_input, language, 'Language input not empty', 'Check - Language input is empty')

        Check.assert_not_in_id_value(
            self, cm.hobbies_input, hobbies, 'Hobbies input not empty', 'Check - Hobbies input is empty')
        # Check.assert_not_in_id_value(self, cm.gender, 'male', 'Gender not empty', 'Check - Gender is empty')

    # @unittest.skip("")
    def test_fill_and_yes(self):
        name = "Chambers Jake"
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain ')

        job_title = "Traveler"
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title info contain wrong data', 'Check - Job title title contain ')

        company = "Ka-tet"
        mgd.find_element_by_id(cm.company_input).send_keys(company)
        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info, company, 'Company info contain wrong data', 'Check - Company title contain ')

        department = "Department of the Mid-world"
        mgd.find_element_by_id(cm.department_input).send_keys(department)
        Check.assert_in_id_value(
            self, cm.department_input, department, 'Department input contain wrong data',
            'Check - Department input contain ')
        Check.assert_in_xpath_text(
            self, cm.department_info, department, 'Department info contain wrong data',
            'Check - Department title contain ')

        mgd.find_element_by_id(cm.birthday_input).click()
        mgd.find_element_by_id(cm.birthday_input).send_keys("881966")
        Check.assert_in_id_value(
            self, cm.birthday_input, '1966-08-08', 'Birthday input contain wrong data',
            'Check - Birthday input contain ')

        contacts_tab = mgd.find_element_by_id(cm.contact_tab)
        contacts_tab.click()

        business_phone = '8080809070'
        mgd.find_element_by_name(cm.business_phone_input).send_keys(business_phone)
        Check.assert_in_name_value(
            self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
            'Check - Business phone input contain ')
        Check.assert_in_xpath_text(
            self, cm.work_phone_info, business_phone, 'Business phone info contain wrong data',
            'Check - Business phone title contain ')

        mobile_phone = '8080807090'
        mgd.find_element_by_name(cm.mobile_phone_input).send_keys(mobile_phone)
        Check.assert_in_name_value(
            self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
            'Check - Mobile phone input contain ')

        home_phone = '8080805060'
        mgd.find_element_by_name(cm.home_phone_input).send_keys(home_phone)
        Check.assert_in_name_value(
            self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
            'Check - Home phone input contain ')

        website = 'haunted_house.com'
        mgd.find_element_by_id(cm.website_input).send_keys(website)
        Check.assert_in_id_value(
            self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input contain ')

        email_1 = 'eleven-year-old@ka-tet.turtle'
        mgd.find_element_by_id(cm.email_input).send_keys(email_1)
        Check.assert_in_id_value(
            self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input contain ')

        email_2 = 'new_york@ka-tet.turtle'
        mgd.find_element_by_id(cm.email_input_2).send_keys(email_2)
        Check.assert_in_id_value(
            self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 contain ')

        email_3 = 'mid-world@ka-tet.turtle'
        mgd.find_element_by_id(cm.email_input_3).send_keys(email_3)
        Check.assert_in_id_value(
            self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 contain ')

        im_id = 'None'
        mgd.find_element_by_id(cm.im_id_input).send_keys(im_id)
        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input contain ')

        address_tab = mgd.find_element_by_id(cm.address_tab)
        address_tab.click()

        work_street = '2264 Walton st'
        mgd.find_element_by_name(cm.work_street_input).send_keys(work_street)
        Check.assert_in_name_value(
            self, cm.work_street_input, work_street, 'Work street input contain wrong data',
            'Check - Work street input contain ')

        work_city = 'Portland'
        mgd.find_element_by_name(cm.work_city_input).send_keys(work_city)
        Check.assert_in_name_value(
            self, cm.work_city_input, work_city, 'Work city input contain wrong data',
            'Check - Work city input contain ')

        work_state = 'Maine'
        mgd.find_element_by_name(cm.work_state_input).send_keys(work_state)
        Check.assert_in_name_value(
            self, cm.work_state_input, work_state, 'Work state input contain wrong data',
            'Check - Work state input contain ')

        work_postal_code = 'ME 04103'
        mgd.find_element_by_name(cm.work_postal_code_input).send_keys(work_postal_code)
        Check.assert_in_name_value(
            self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
            'Check - Work postal code input contain ')

        work_country = 'USA'
        mgd.find_element_by_name(cm.work_country_input).send_keys(work_country)
        Check.assert_in_name_value(
            self, cm.work_country_input, work_country, 'Work country input contain wrong data',
            'Check - Work country input contain ')
        work_address = work_street + ' ' + work_city + ' ' + work_state + ' ' + work_postal_code + ' ' + work_country
        Check.assert_in_xpath_text(
            self, cm.address_info, work_address, 'Address info contain wrong data', 'Check - Address title contain ')

        home_street = '49 Florida Ave'
        mgd.find_element_by_name(cm.home_street_input).send_keys(home_street)
        Check.assert_in_name_value(
            self, cm.home_street_input, home_street, 'Home street input contain wrong data',
            'Check - Home street input contain ')

        home_city = 'Bangor'
        mgd.find_element_by_name(cm.home_city_input).send_keys(home_city)
        Check.assert_in_name_value(
            self, cm.home_city_input, home_city, 'Home city input contain wrong data',
            'Check - Home city input contain ')

        home_state = 'Maine'
        mgd.find_element_by_name(cm.home_state_input).send_keys(home_state)
        Check.assert_in_name_value(
            self, cm.home_state_input, home_state, 'Home state input contain wrong data',
            'Check - Home state input contain ')

        home_postal_code = 'ME 04401-3005'
        mgd.find_element_by_name(cm.home_postal_code_input).send_keys(home_postal_code)
        Check.assert_in_name_value(
            self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',
            'Check - Home postal code input contain ')

        home_country = 'USA'
        mgd.find_element_by_name(cm.home_country_input).send_keys(home_country)
        Check.assert_in_name_value(
            self, cm.home_country_input, home_country, 'Home country input contain wrong data',
            'Check - Home country input contain ')

        more_tab = mgd.find_element_by_id(cm.more_tab)
        more_tab.click()

        language = 'English, Spanish'
        mgd.find_element_by_id(cm.language_input).send_keys(language)
        Check.assert_in_id_value(
            self, cm.language_input, language, 'Language input contain wrong data', 'Check - Language input contain ')

        hobbies = 'Cooking, Shooting'
        mgd.find_element_by_id(cm.hobbies_input).send_keys(hobbies)
        Check.assert_in_id_value(
            self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input contain ')

        # mgd.find_element_by_id(cm.gender).click()
        # Check.assert_equal_xpath(
        #     self, cm.gender_wrapper, 1, 'Gender wrapper is not exist', 'Check - Gender wrapper exist')
        # mgd.find_element_by_xpath(cm.male).click()
        # Check.assert_in_id_value(self, cm.gender, 'male', 'Gender contain wrong data', 'Check - Gender is')

        Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option).click()
        time.sleep(2)
        #
        #
        print(Check.find_element_by_class_name_and_text(cm.contact_title, name))
        time.sleep(3)
        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        # card_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), '" + name + "')]")
        # card_found.click()

        print('Check - Contact card')
        mgd.find_element_by_class_name(cm.contact_info)
        print('Check - Contact ' + name + ' is open')
        time.sleep(1)

        #
        #

        time.sleep(2)
        mgd.find_element_by_id(cm.profile_tab).click()
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain')
        Check.assert_in_xpath_text(
            self, cm.name_title, name, 'Name title contain wrong data', 'Check - Name title contain')

        Check.assert_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data', 'Check - Job title contain')
        Check.assert_in_xpath_text(
            self, cm.job_title_info, job_title, 'Job title info contain wrong data', 'Check - Job title contain')

        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain')
        Check.assert_in_xpath_text(
            self, cm.company_info, company, 'Company info contain wrong data', 'Check - Company title contain')

        Check.assert_in_id_value(
            self, cm.department_input, department, 'Department input contain wrong data',
            'Check - Department input contain')
        Check.assert_in_xpath_text(
            self, cm.department_info, department, 'Department info contain wrong data',
            'Check - Department title contain')

        Check.assert_in_id_value(
            self, cm.birthday_input, '1966-08-08', 'Birthday input contain wrong data',
            'Check - Birthday input contain')

        contacts_tab = mgd.find_element_by_id(cm.contact_tab)
        contacts_tab.click()

        Check.assert_in_name_value(
            self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
            'Check - Business phone input contain')

        Check.assert_in_xpath_text(
            self, cm.work_phone_info, business_phone, 'Business phone info contain wrong data',
            'Check - Business phone title contain')

        Check.assert_in_name_value(
            self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
            'Check - Mobile phone input contain')

        Check.assert_in_name_value(
            self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
            'Check - Home phone input contain')

        Check.assert_in_id_value(
            self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input contain')

        Check.assert_in_id_value(
            self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input contain')

        Check.assert_in_id_value(
            self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 contain')

        Check.assert_in_id_value(
            self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 contain')

        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input contain')

        address_tab = mgd.find_element_by_id(cm.address_tab)
        address_tab.click()

        Check.assert_in_name_value(
            self, cm.work_street_input, work_street, 'Work street input contain wrong data',
            'Check - Work street input contain')

        Check.assert_in_name_value(
            self, cm.work_city_input, work_city, 'Work city input contain wrong data',
            'Check - Work city input contain')

        Check.assert_in_name_value(
            self, cm.work_state_input, work_state, 'Work state input contain wrong data',
            'Check - Work state input contain')

        Check.assert_in_name_value(
            self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
            'Check - Work postal code input contain')

        Check.assert_in_name_value(
            self, cm.work_country_input, work_country, 'Work country input contain wrong data',
            'Check - Work country input contain')
        Check.assert_in_xpath_text(
            self, cm.address_info, work_address, 'Address info contain wrong data', 'Check - Address title contain')

        Check.assert_in_name_value(
            self, cm.home_street_input, home_street, 'Home street input contain wrong data',
            'Check - Home street input contain')

        Check.assert_in_name_value(
            self, cm.home_city_input, home_city, 'Home city input contain wrong data',
            'Check - Home city input contain')

        Check.assert_in_name_value(
            self, cm.home_state_input,  home_state, 'Home state input contain wrong data',
            'Check - Home state input contain')

        Check.assert_in_name_value(
            self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',

            'Check - Home postal code input contain')

        Check.assert_in_name_value(
            self, cm.home_country_input, home_country, 'Home country input contain wrong data',
            'Check - Home country input contain')

        more_tab = mgd.find_element_by_id(cm.more_tab)
        more_tab.click()

        Check.assert_in_id_value(
            self, cm.language_input, language, 'Language input contain wrong data', 'Check - Language input contain')

        Check.assert_in_id_value(
            self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input contain')
        # Check.assert_in_id_value(self, cm.gender, 'male', 'Gender contain wrong data', 'Check - Gender contain')


# @unittest.skip("Ok")
class Test5Search(unittest.TestCase):

    def setUp(self):
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')

        time.sleep(2)
        mgd.find_element_by_xpath(cm.clear_search).click()
        Check.assert_empty_xpath_value(
            cm.clear_search, 'Search field did not empty', '')
        time.sleep(2)

    def tearDown(self):
        time.sleep(2)
        mgd.find_element_by_xpath(cm.clear_search).click()
        Check.assert_empty_xpath_value(
            cm.clear_search, 'Search field did not empty', 'Check - Search field is empty')
        time.sleep(2)

    def test_search_name(self):
        print('Search name')
        search = 'Contact for autotest'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.contact_title, 14, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_company(self):
        print('Search company')
        search = 'Test inc.'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.contact_title, 8, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_department(self):
        print('Search department')
        search = 'Department of truth'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.contact_title, 3, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_job_title(self):
        print('Search job title')
        search = 'High lvl tester'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.contact_title, 8, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_work_phone(self):
        print('Search work phone')
        search = '8965569855'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.contact_title, 5, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_email(self):
        print('Search email')
        search = 'cont@autotest.ab'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.contact_title, 14, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_address(self):
        print('Search address')
        search = 'City 17'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.contact_title, 5, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')


# @unittest.skip("Ok")
class Test6ABCApplyUnsavedChanges(unittest.TestCase):
    def setUp(self):
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')

        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
            Check.assert_equal_xpath(
                self, cm.view_change, 1, 'View change button not found', 'Check - View change button')
            Check.assert_in_xpath_class(
                self, cm.view_change, 'clickable', 'View change button not clickable',
                'Check - View change button is clickable :')
            time.sleep(1)
            mgd.find_element_by_xpath(cm.view_change).click()
            time.sleep(1)
        Check.assert_equal_xpath(
            self, cm.contact_cards_list_xpath, 1, 'Contact card list not found', 'Check - Contact card list')
        time.sleep(1)

    def tearDown(self):
        print('/////')
        time.sleep(2)
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
        else:
            print('View mode is list of contacts')
            mgd.find_element_by_xpath(cm.view_change).click()
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        driver_instance.implicitly_wait(5)

        print("/////")

    # @unittest.skip('')
    def test_abc_no_wrapper(self):
        name = 'Allison'
        name2 = 'abr.test'
        allison_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), '" + name + "')]")
        allison_found.click()
        print('Check - ' + name + ' contact card is found')
        Check.check_exists_by_xpath(cm.contact_modal_window)
        print('Check - Contact card exist')
        mgd.find_element_by_xpath("//*[@class='title' and contains(text(), '" + name + "')]")
        print('Check - Contact name is ' + name)
        company = 'Big Brother Airlines'
        mgd.find_element_by_id(cm.company_input).send_keys(company)
        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title contain ')
        abrtest_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), '" + name2 + "')]")
        abrtest_found.click()
        Check.assert_equal_class_name(
            self, cm.apply_unsaved_changes, 1, 'Block wrapper "Apply unsaved changes" did not exist',
            'Check - Block wrapper "Apply unsaved changes"')
        mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        print('Check - No button')
        mgd.find_element_by_xpath("//*[@class='title' and contains(text(), '" + name2 + "')]")
        print('Check - Contact name is ' + name2)

    # @unittest.skip('')
    def test_abc_yes_wrapper(self):
        name = 'Allison'
        name2 = 'abr.test'
        allison_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), '" + name + "')]")
        allison_found.click()
        print('Check - ' + name + ' contact card is found')
        Check.check_exists_by_xpath(cm.contact_modal_window)
        print('Check - Contact card exist')
        mgd.find_element_by_xpath("//*[@class='title' and contains(text(), '" + name + "')]")
        print('Check - Contact name is ' + name)
        company = 'Grey Wolf Airlines'
        mgd.find_element_by_id(cm.company_input).clear()
        time.sleep(1)
        mgd.find_element_by_id(cm.company_input).send_keys(company)
        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title contain ')
        abrtest_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), '" + name2 + "')]")
        abrtest_found.click()
        time.sleep(2)
        Check.assert_equal_class_name(
            self, cm.apply_unsaved_changes, 1, 'Block wrapper "Apply unsaved changes" did not exist',
            'Check - Block wrapper "Apply unsaved changes"')
        mgd.find_element_by_xpath(cm.yes_apply_unsaved_changes).click()
        print('Check - Yes button')
        mgd.find_element_by_xpath("//*[@class='title' and contains(text(), '" + name2 + "')]")
        print('Check - Contact name is ' + name2)
        allison_found.click()
        print('Check - ' + name + ' contact card is found')
        Check.check_exists_by_xpath(cm.contact_modal_window)
        print('Check - Contact card exist')
        mgd.find_element_by_xpath("//*[@class='title' and contains(text(), '" + name + "')]")
        print('Check - Contact name is ' + name)
        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title contain ')
        company_text = len(mgd.find_element_by_xpath(cm.company_info_abc).text)
        print('Company field contain ' + str(company_text) + ' letters')
        while company_text > 0:
            mgd.find_element_by_id(cm.company_input).send_keys(Keys.BACKSPACE)
            company_text -= 1
        time.sleep(1)
        Check.assert_in_xpath_class(
            self, cm.yes_option_abc, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option_abc).click()

    # @unittest.skip('')
    def test_abc_cancel_wrapper(self):
        name = 'Allison'
        name2 = 'abr.test'
        allison_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), '" + name + "')]")
        allison_found.click()
        print('Check - ' + name + ' contact card is found')
        Check.check_exists_by_xpath(cm.contact_modal_window)
        print('Check - Contact card exist')
        mgd.find_element_by_xpath("//*[@class='title' and contains(text(), '" + name + "')]")
        print('Check - Contact name is ' + name)
        company = 'Big World Airlines'
        mgd.find_element_by_id(cm.company_input).clear()
        time.sleep(1)
        mgd.find_element_by_id(cm.company_input).send_keys(company)
        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title contain ')
        abrtest_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), '" + name2 + "')]")
        abrtest_found.click()
        Check.assert_equal_class_name(
            self, cm.apply_unsaved_changes, 1, 'Block wrapper "Apply unsaved changes" did not exist',
            'Check - Block wrapper "Apply unsaved changes"')
        mgd.find_element_by_xpath(cm.cancel_apply_unsaved_changes).click()
        print('Check - Cancel button')
        mgd.find_element_by_xpath("//*[@class='title' and contains(text(), '" + name + "')]")
        print('Check - Contact name is ' + name)

        # mgd.find_element_by_id(cm.company_input).clear()
        # mgd.find_element_by_id(cm.company_input).send_keys(Keys.BACKSPACE)
        # Check.assert_in_id_value(
        #     self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        # Check.assert_in_xpath_text(
        #     self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title contain ')
        #


# @unittest.skip("Ok")
class Test7ABCOptions(unittest.TestCase):

    def setUp(self):
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')

        print(Check.check_exists_by_class_name(cm.folders_list_wrapper))
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
            Check.assert_equal_xpath(
                self, cm.view_change, 1, 'View change button not found', 'Check - View change button')
            Check.assert_in_xpath_class(
                self, cm.view_change, 'clickable', 'View change button not clickable',
                'Check - View change button is clickable :')
            time.sleep(1)
            mgd.find_element_by_xpath(cm.view_change).click()
            time.sleep(1)
        Check.assert_equal_xpath(
            self, cm.contact_cards_list_xpath, 1, 'Contact card list not found', 'Check - Contact card list')
        time.sleep(2)
        name2 = "BBC_edit"
        abc_found = mgd.find_elements_by_xpath("//*[@class='name' and contains(text(), 'BBC_edit')]")
        if abc_found == []:
            mgd.find_element_by_xpath(cm.new_contact).click()
            mgd.find_element_by_id(cm.name_input).send_keys(name2)
            mgd.find_element_by_xpath(cm.yes_option).click()

    def tearDown(self):
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
        else:
            print('View mode is list of contacts')
            mgd.find_element_by_xpath(cm.view_change).click()
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        driver_instance.implicitly_wait(5)

        print("/////")

    def test_for_delete_options_in_abc_view(self):
        mgd.find_element_by_xpath(cm.new_contact).click()
        Check.assert_equal_xpath(
            self, cm.contact_modal_window, 1, 'New Contact window not found', 'Check - New Contact window')
        name2 = "BBC_edit"
        mgd.find_element_by_id(cm.name_input).send_keys(name2)
        Check.assert_in_id_value(
            self, cm.name_input, name2, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name2, 'Name title contain wrong data', 'Check - Name title contain ')
        Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option).click()

        abc_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), 'BBC_edit')]")
        abc_found.click()
        Check.assert_equal_class_name(self, cm.contact_info, 1, 'Contact info does not exist', 'Check - Contact info')
        Check.find_element_by_class_name_and_text(cm.contact_title, name2)

        mgd.find_element_by_xpath(cm.delete_option_abc).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Delete wrapper exist', 'Check - Delete wrapper not exist')

        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
        else:
            print('View mode is list of contacts')
            mgd.find_element_by_xpath(cm.view_change).click()

        Check.find_element_by_class_name_and_text(cm.folder_name, 'Deleted Items').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_deleted_items_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(deleted_items_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + deleted_items_folder + ' folder is selected')

        # if Check.find_element_by_class_name_and_text(cm.contact_title, name2) is not None:
        #     print('Check - ' + name2 + ' is found')
        # elif Check.find_element_by_class_name_and_text(cm.contact_title, name2) is None:
        #     raise Exception(name2 + ' not found')

    def test_for_undo_options_in_abc_view(self):
        mgd.find_element_by_xpath(cm.new_contact).click()
        Check.assert_equal_xpath(
            self, cm.contact_modal_window, 1, 'New Contact window not found', 'Check - New Contact window')
        name2 = "BBC_edit"
        mgd.find_element_by_id(cm.name_input).send_keys(name2)
        Check.assert_in_id_value(
            self, cm.name_input, name2, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name2, 'Name title contain wrong data', 'Check - Name title contain ')
        Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option).click()

        abc_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), 'BBC_edit')]")
        abc_found.click()
        Check.assert_equal_class_name(self, cm.contact_info, 1, 'Contact info does not exist', 'Check - Contact info')
        Check.find_element_by_class_name_and_text(cm.name_in_abc, 'BBC_edit')
        time.sleep(1)
        job_title = 'undo'
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info_abc, job_title, 'Job title contain wrong data', 'Check - Job title contain ')
        Check.assert_equal_xpath(self, cm.undo_option_abc, 1, 'Undo options unavailable', 'Check - Undo options')
        Check.assert_in_xpath_class(
            self, cm.undo_option_abc, 'clickable', 'Undo options not clickable', 'Check - Undo options is clickable :')
        mgd.find_element_by_xpath(cm.undo_option_abc).click()
        Check.assert_not_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input is clear ')
        Check.assert_not_in_xpath_text(
            self, cm.job_title_info_abc, job_title, 'Job title contain wrong data', 'Check - Job title is clear')

        # mgd.find_element_by_xpath(cm.delete_option_abc).click()
        # Check.element_is_visible_class_name(
        #     cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        # time.sleep(2)
        # Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        # print('Check - Delete button')
        # time.sleep(2)
        # Check.element_is_visible_class_name(
        #     cm.block_wrapper, 'Delete wrapper exist', 'Check - Delete wrapper not exist')

    def test_for_yes_options_in_abc_view(self):
        time.sleep(2)
        abc_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), 'BBC_edit')]")
        abc_found.click()
        Check.assert_equal_class_name(self, cm.contact_info, 1, 'Contact info does not exist', 'Check - Contact info')
        Check.find_element_by_class_name_and_text(cm.contact_title, 'BBC_edit')

        job_title = 'Trata-ta-ta-ta'
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info_abc, job_title, 'Job title contain wrong data', 'Check - Job title contain ')

        Check.assert_equal_xpath(self, cm.yes_option_abc, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option_abc, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option_abc).click()

        print('add check')

        mgd.find_element_by_xpath(cm.delete_option_abc).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Delete wrapper exist', 'Check - Delete wrapper not exist')


# @unittest.skip("Ok")
class Test8ABCFill(unittest.TestCase):

    def setUp(self):
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')

        print(Check.check_exists_by_class_name(cm.folders_list_wrapper))
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
            Check.assert_equal_xpath(
                self, cm.view_change, 1, 'View change button not found', 'Check - View change button')
            Check.assert_in_xpath_class(
                self, cm.view_change, 'clickable', 'View change button not clickable',
                'Check - View change button is clickable :')
            time.sleep(1)
            mgd.find_element_by_xpath(cm.view_change).click()
            time.sleep(1)
        Check.assert_equal_xpath(
            self, cm.contact_cards_list_xpath, 1, 'Contact card list not found', 'Check - Contact card list')
        time.sleep(2)

    def tearDown(self):
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
        else:
            print('View mode is list of contacts')
            mgd.find_element_by_xpath(cm.view_change).click()
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        if Check.find_element_by_class_name_and_text(cm.contact_title, 'BBC_edit'):
            Check.find_element_by_class_name_and_text(cm.contact_title, 'BBC_edit').click()
            mgd.find_element_by_xpath(cm.delete_option).click()
            Check.element_is_visible_class_name(
                cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
            time.sleep(2)
            Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
            print('Check - Delete button')
            time.sleep(2)

        driver_instance.implicitly_wait(5)

        print("/////")

    # @unittest.skip(' Ok ')
    def test_fill_and_yes_abc_view(self):
        mgd.find_element_by_xpath(cm.new_contact).click()
        Check.assert_equal_xpath(
            self, cm.contact_modal_window, 1, 'New Contact window not found', 'Check - New Contact window')
        name2 = "BBC_edit"
        mgd.find_element_by_id(cm.name_input).send_keys(name2)
        Check.assert_in_id_value(
            self, cm.name_input, name2, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name2, 'Name title contain wrong data', 'Check - Name title contain ')
        Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option).click()

        bbc_edit_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), 'BBC_edit')]")
        bbc_edit_found.click()
        Check.assert_equal_class_name(self, cm.contact_info, 1, 'Contact info does not exist', 'Check - Contact info')
        Check.find_element_by_class_name_and_text(cm.contact_title, name2)
        time.sleep(1)

        name = "A Susan Delgado"
        mgd.find_element_by_id(cm.name_input).clear()
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name, 'Name title contain wrong data', 'Check - Name title contain ')

        job_title = "Bride"
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info_abc, job_title, 'Job title info contain wrong data',
            'Check - Job title title contain ')

        company = "Ka-tet"
        mgd.find_element_by_id(cm.company_input).send_keys(company)
        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title contain ')

        department = "Department of the Mid-world"
        mgd.find_element_by_id(cm.department_input).send_keys(department)
        Check.assert_in_id_value(
            self, cm.department_input, department, 'Department input contain wrong data',
            'Check - Department input contain ')
        Check.assert_in_xpath_text(
            self, cm.department_info_abc, department, 'Department info contain wrong data',
            'Check - Department title contain ')

        mgd.find_element_by_id(cm.birthday_input).click()
        mgd.find_element_by_id(cm.birthday_input).send_keys("662000")
        Check.assert_in_id_value(
            self, cm.birthday_input, '2000-06-06', 'Birthday input contain wrong data',
            'Check - Birthday input contain ')

        contacts_tab = mgd.find_element_by_id(cm.contact_tab)
        contacts_tab.click()

        business_phone = '1212809070'
        mgd.find_element_by_name(cm.business_phone_input).send_keys(business_phone)
        Check.assert_in_name_value(
            self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
            'Check - Business phone input contain ')
        Check.assert_in_xpath_text(
            self, cm.work_phone_info_abc, business_phone, 'Business phone info contain wrong data',
            'Check - Business phone title contain ')

        mobile_phone = '1212807090'
        mgd.find_element_by_name(cm.mobile_phone_input).send_keys(mobile_phone)
        Check.assert_in_name_value(
            self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
            'Check - Mobile phone input contain ')

        home_phone = '1212805060'
        mgd.find_element_by_name(cm.home_phone_input).send_keys(home_phone)
        Check.assert_in_name_value(
            self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
            'Check - Home phone input contain ')

        website = 'charyou_tree.com'
        mgd.find_element_by_id(cm.website_input).send_keys(website)
        Check.assert_in_id_value(
            self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input contain ')

        email_1 = 'sixteen-year-old@ka-tet.bear'
        mgd.find_element_by_id(cm.email_input).send_keys(email_1)
        Check.assert_in_id_value(
            self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input contain ')

        email_2 = 'old_world@ka-tet.bear'
        mgd.find_element_by_id(cm.email_input_2).send_keys(email_2)
        Check.assert_in_id_value(
            self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 contain ')

        email_3 = 'burn_with_fire@ka-tet.bear'
        mgd.find_element_by_id(cm.email_input_3).send_keys(email_3)
        Check.assert_in_id_value(
            self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 contain ')

        im_id = '12prop8989555'
        mgd.find_element_by_id(cm.im_id_input).send_keys(im_id)
        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input contain ')

        address_tab = mgd.find_element_by_id(cm.address_tab)
        address_tab.click()

        work_street = 'Castle'
        mgd.find_element_by_name(cm.work_street_input).send_keys(work_street)
        Check.assert_in_name_value(
            self, cm.work_street_input, work_street, 'Work street input contain wrong data',
            'Check - Work street input contain ')

        work_city = 'Hambry'
        mgd.find_element_by_name(cm.work_city_input).send_keys(work_city)
        Check.assert_in_name_value(
            self, cm.work_city_input, work_city, 'Work city input contain wrong data',
            'Check - Work city input contain ')

        work_state = 'Majise'
        mgd.find_element_by_name(cm.work_state_input).send_keys(work_state)
        time.sleep(1)
        Check.assert_in_name_value(
            self, cm.work_state_input, work_state, 'Work state input contain wrong data',
            'Check - Work state input contain ')

        work_postal_code = 'CSMJH 001'
        mgd.find_element_by_name(cm.work_postal_code_input).send_keys(work_postal_code)
        Check.assert_in_name_value(
            self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
            'Check - Work postal code input contain ')

        work_country = 'Clean Sea'
        mgd.find_element_by_name(cm.work_country_input).send_keys(work_country)
        Check.assert_in_name_value(
            self, cm.work_country_input, work_country, 'Work country input contain wrong data',
            'Check - Work country input contain ')
        work_address = work_street + ' ' + work_city + ' ' + work_state + ' ' + work_postal_code + ' ' + work_country
        Check.assert_in_xpath_text(
            self, cm.address_info_abc, work_address, 'Address info contain wrong data',
            'Check - Address title contain ')

        home_street = '36 Wrong st'
        mgd.find_element_by_name(cm.home_street_input).send_keys(home_street)
        Check.assert_in_name_value(
            self, cm.home_street_input, home_street, 'Home street input contain wrong data',
            'Check - Home street input contain ')

        home_city = 'Hambry'
        mgd.find_element_by_name(cm.home_city_input).send_keys(home_city)
        Check.assert_in_name_value(
            self, cm.home_city_input, home_city, 'Home city input contain wrong data',
            'Check - Home city input contain ')

        home_state = 'Majise'
        mgd.find_element_by_name(cm.home_state_input).send_keys(home_state)
        Check.assert_in_name_value(
            self, cm.home_state_input, home_state, 'Home state input contain wrong data',
            'Check - Home state input contain ')

        home_postal_code = 'CSMJH 009-25'
        mgd.find_element_by_name(cm.home_postal_code_input).send_keys(home_postal_code)
        Check.assert_in_name_value(
            self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',
            'Check - Home postal code input contain ')

        home_country = 'Clean Sea'
        mgd.find_element_by_name(cm.home_country_input).send_keys(home_country)
        Check.assert_in_name_value(
            self, cm.home_country_input, home_country, 'Home country input contain wrong data',
            'Check - Home country input contain ')

        more_tab = mgd.find_element_by_id(cm.more_tab)
        more_tab.click()

        language = 'Old old old English'
        mgd.find_element_by_id(cm.language_input).send_keys(language)
        Check.assert_in_id_value(
            self, cm.language_input, language, 'Language input contain wrong data', 'Check - Language input contain ')

        hobbies = 'Cleaning, Cooking, Trouble maker'
        mgd.find_element_by_id(cm.hobbies_input).send_keys(hobbies)
        Check.assert_in_id_value(
            self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input contain ')

        # mgd.find_element_by_id(cm.gender).click()
        # time.sleep(2)
        # Check.assert_equal_xpath(
        #     self, cm.gender_wrapper_abc, 1, 'Gender wrapper is not exist', 'Check - Gender wrapper exist')
        # mgd.find_element_by_xpath(cm.male_abc).click()
        # Check.assert_in_id_value(self, cm.gender, 'male', 'Gender contain wrong data', 'Check - Gender is')
        # mgd.find_element_by_id(cm.gender).click()
        # Check.assert_equal_xpath(
        #     self, cm.gender_wrapper_abc, 1, 'Gender wrapper is not exist', 'Check - Gender wrapper exist')
        # mgd.find_element_by_xpath(cm.female_abc).click()
        # Check.assert_in_id_value(self, cm.gender, 'female', 'Gender contain wrong data', 'Check - Gender is')

        Check.assert_equal_xpath(self, cm.yes_option_abc, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option_abc, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        time.sleep(1)
        mgd.find_element_by_xpath(cm.yes_option_abc).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(cm.name_in_abc, name).click()

        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name, 'Name title contain wrong data', 'Check - Name title contain ')

        Check.assert_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info_abc, job_title, 'Job title info contain wrong data',
            'Check - Job title title contain ')

        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title contain ')

        Check.assert_in_id_value(
            self, cm.department_input, department, 'Department input contain wrong data',
            'Check - Department input contain ')
        Check.assert_in_xpath_text(
            self, cm.department_info_abc, department, 'Department info contain wrong data',
            'Check - Department title contain ')

        Check.assert_in_id_value(
            self, cm.birthday_input, '2000-06-06', 'Birthday input contain wrong data',
            'Check - Birthday input contain ')

        contacts_tab = mgd.find_element_by_id(cm.contact_tab)
        contacts_tab.click()

        Check.assert_in_name_value(
            self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
            'Check - Business phone input contain ')
        Check.assert_in_xpath_text(
            self, cm.work_phone_info_abc, business_phone, 'Business phone info contain wrong data',
            'Check - Business phone title contain ')

        Check.assert_in_name_value(
            self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
            'Check - Mobile phone input contain ')

        Check.assert_in_name_value(
            self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
            'Check - Home phone input contain ')

        Check.assert_in_id_value(
            self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input contain ')

        Check.assert_in_id_value(
            self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input contain ')

        Check.assert_in_id_value(
            self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 contain ')

        Check.assert_in_id_value(
            self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 contain ')

        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input contain ')

        address_tab = mgd.find_element_by_id(cm.address_tab)
        address_tab.click()

        Check.assert_in_name_value(
            self, cm.work_street_input, work_street, 'Work street input contain wrong data',
            'Check - Work street input contain ')

        Check.assert_in_name_value(
            self, cm.work_city_input, work_city, 'Work city input contain wrong data',
            'Check - Work city input contain ')

        Check.assert_in_name_value(
            self, cm.work_state_input, work_state, 'Work state input contain wrong data',
            'Check - Work state input contain ')

        Check.assert_in_name_value(
            self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
            'Check - Work postal code input contain ')

        Check.assert_in_name_value(
            self, cm.work_country_input, work_country, 'Work country input contain wrong data',
            'Check - Work country input contain ')
        work_address = work_street + ' ' + work_city + ' ' + work_state + ' ' + work_postal_code + ' ' + work_country
        Check.assert_in_xpath_text(
            self, cm.address_info_abc, work_address, 'Address info contain wrong data',
            'Check - Address title contain ')

        Check.assert_in_name_value(
            self, cm.home_street_input, home_street, 'Home street input contain wrong data',
            'Check - Home street input contain ')

        Check.assert_in_name_value(
            self, cm.home_city_input, home_city, 'Home city input contain wrong data',
            'Check - Home city input contain ')

        Check.assert_in_name_value(
            self, cm.home_state_input, home_state, 'Home state input contain wrong data',
            'Check - Home state input contain ')

        Check.assert_in_name_value(
            self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',
            'Check - Home postal code input contain ')

        Check.assert_in_name_value(
            self, cm.home_country_input, home_country, 'Home country input contain wrong data',
            'Check - Home country input contain ')

        more_tab = mgd.find_element_by_id(cm.more_tab)
        more_tab.click()

        Check.assert_in_id_value(
            self, cm.language_input, language, 'Language input contain wrong data', 'Check - Language input contain ')

        Check.assert_in_id_value(
            self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input contain ')

        # Check.assert_in_id_value(self, cm.gender, 'female', 'Gender contain wrong data', 'Check - Gender is')

        mgd.find_element_by_xpath(cm.delete_option_abc).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Delete wrapper exist', 'Check - Delete wrapper not exist')

    # @unittest.skip(' Ok ')
    def test_fill_and_undo_abc_view(self):
        mgd.find_element_by_xpath(cm.new_contact).click()
        Check.assert_equal_xpath(
            self, cm.contact_modal_window, 1, 'New Contact window not found', 'Check - New Contact window')
        name2 = "BBC_edit"
        mgd.find_element_by_id(cm.name_input).send_keys(name2)
        Check.assert_in_id_value(
            self, cm.name_input, name2, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title, name2, 'Name title contain wrong data', 'Check - Name title contain ')
        Check.assert_equal_xpath(self, cm.yes_option, 1, 'Yes options unavailable', 'Check - Yes options')
        Check.assert_in_xpath_class(
            self, cm.yes_option, 'clickable', 'Yes options not clickable', 'Check - Yes options is clickable :')
        mgd.find_element_by_xpath(cm.yes_option).click()

        bbc_edit_found = mgd.find_element_by_xpath("//*[@class='name' and contains(text(), 'BBC_edit')]")
        bbc_edit_found.click()
        Check.assert_equal_class_name(self, cm.contact_info, 1, 'Contact info does not exist', 'Check - Contact info')
        Check.find_element_by_class_name_and_text(cm.contact_title, name2)
        time.sleep(1)

        name = "A Susan Delgado undo"
        mgd.find_element_by_id(cm.name_input).clear()
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        Check.assert_in_id_value(
            self, cm.name_input, name, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name, 'Name title contain wrong data', 'Check - Name title contain ')

        job_title = "Bride"
        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title)
        Check.assert_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input contain ')
        Check.assert_in_xpath_text(
            self, cm.job_title_info_abc, job_title, 'Job title info contain wrong data',
            'Check - Job title title contain ')

        company = "Ka-tet"
        mgd.find_element_by_id(cm.company_input).send_keys(company)
        Check.assert_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input contain ')
        Check.assert_in_xpath_text(
            self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title contain ')

        department = "Department of the Mid-world"
        mgd.find_element_by_id(cm.department_input).send_keys(department)
        Check.assert_in_id_value(
            self, cm.department_input, department, 'Department input contain wrong data',
            'Check - Department input contain ')
        Check.assert_in_xpath_text(
            self, cm.department_info_abc, department, 'Department info contain wrong data',
            'Check - Department title contain ')

        mgd.find_element_by_id(cm.birthday_input).click()
        mgd.find_element_by_id(cm.birthday_input).send_keys("662000")
        Check.assert_in_id_value(
            self, cm.birthday_input, '2000-06-06', 'Birthday input contain wrong data',
            'Check - Birthday input contain ')

        contacts_tab = mgd.find_element_by_id(cm.contact_tab)
        contacts_tab.click()

        business_phone = '1212809070'
        mgd.find_element_by_name(cm.business_phone_input).send_keys(business_phone)
        Check.assert_in_name_value(
            self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
            'Check - Business phone input contain ')
        Check.assert_in_xpath_text(
            self, cm.work_phone_info_abc, business_phone, 'Business phone info contain wrong data',
            'Check - Business phone title contain ')

        mobile_phone = '1212807090'
        mgd.find_element_by_name(cm.mobile_phone_input).send_keys(mobile_phone)
        Check.assert_in_name_value(
            self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
            'Check - Mobile phone input contain ')

        home_phone = '1212805060'
        mgd.find_element_by_name(cm.home_phone_input).send_keys(home_phone)
        Check.assert_in_name_value(
            self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
            'Check - Home phone input contain ')

        website = 'charyou_tree.com'
        mgd.find_element_by_id(cm.website_input).send_keys(website)
        Check.assert_in_id_value(
            self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input contain ')

        email_1 = 'sixteen-year-old@ka-tet.bear'
        mgd.find_element_by_id(cm.email_input).send_keys(email_1)
        Check.assert_in_id_value(
            self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input contain ')

        email_2 = 'old_world@ka-tet.bear'
        mgd.find_element_by_id(cm.email_input_2).send_keys(email_2)
        Check.assert_in_id_value(
            self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 contain ')

        email_3 = 'burn_with_fire@ka-tet.bear'
        mgd.find_element_by_id(cm.email_input_3).send_keys(email_3)
        Check.assert_in_id_value(
            self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 contain ')

        im_id = '12prop8989555'
        mgd.find_element_by_id(cm.im_id_input).send_keys(im_id)
        time.sleep(1)
        Check.assert_in_id_value(
            self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input contain ')

        address_tab = mgd.find_element_by_id(cm.address_tab)
        address_tab.click()

        work_street = 'Castle'
        mgd.find_element_by_name(cm.work_street_input).send_keys(work_street)
        Check.assert_in_name_value(
            self, cm.work_street_input, work_street, 'Work street input contain wrong data',
            'Check - Work street input contain ')

        work_city = 'Hambry'
        mgd.find_element_by_name(cm.work_city_input).send_keys(work_city)
        Check.assert_in_name_value(
            self, cm.work_city_input, work_city, 'Work city input contain wrong data',
            'Check - Work city input contain ')

        work_state = 'Majise'
        mgd.find_element_by_name(cm.work_state_input).send_keys(work_state)
        Check.assert_in_name_value(
            self, cm.work_state_input, work_state, 'Work state input contain wrong data',
            'Check - Work state input contain ')

        work_postal_code = 'CSMJH 001'
        mgd.find_element_by_name(cm.work_postal_code_input).send_keys(work_postal_code)
        Check.assert_in_name_value(
            self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
            'Check - Work postal code input contain ')

        work_country = 'Clean Sea'
        mgd.find_element_by_name(cm.work_country_input).send_keys(work_country)
        Check.assert_in_name_value(
            self, cm.work_country_input, work_country, 'Work country input contain wrong data',
            'Check - Work country input contain ')
        work_address = work_street + ' ' + work_city + ' ' + work_state + ' ' + work_postal_code + ' ' + work_country
        Check.assert_in_xpath_text(
            self, cm.address_info_abc, work_address, 'Address info contain wrong data',
            'Check - Address title contain ')

        home_street = '36 Wrong st'
        mgd.find_element_by_name(cm.home_street_input).send_keys(home_street)
        Check.assert_in_name_value(
            self, cm.home_street_input, home_street, 'Home street input contain wrong data',
            'Check - Home street input contain ')

        home_city = 'Hambry'
        mgd.find_element_by_name(cm.home_city_input).send_keys(home_city)
        Check.assert_in_name_value(
            self, cm.home_city_input, home_city, 'Home city input contain wrong data',
            'Check - Home city input contain ')

        home_state = 'Majise'
        mgd.find_element_by_name(cm.home_state_input).send_keys(home_state)
        Check.assert_in_name_value(
            self, cm.home_state_input, home_state, 'Home state input contain wrong data',
            'Check - Home state input contain ')

        home_postal_code = 'CSMJH 009-25'
        mgd.find_element_by_name(cm.home_postal_code_input).send_keys(home_postal_code)
        Check.assert_in_name_value(
            self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',
            'Check - Home postal code input contain ')

        home_country = 'Clean Sea'
        mgd.find_element_by_name(cm.home_country_input).send_keys(home_country)
        Check.assert_in_name_value(
            self, cm.home_country_input, home_country, 'Home country input contain wrong data',
            'Check - Home country input contain ')

        more_tab = mgd.find_element_by_id(cm.more_tab)
        more_tab.click()

        language = 'Old old old English'
        mgd.find_element_by_id(cm.language_input).send_keys(language)
        Check.assert_in_id_value(
            self, cm.language_input, language, 'Language input contain wrong data', 'Check - Language input contain ')

        hobbies = 'Cleaning, Cooking, Trouble maker'
        mgd.find_element_by_id(cm.hobbies_input).send_keys(hobbies)
        time.sleep(2)
        Check.assert_in_id_value(
            self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input contain ')

        # mgd.find_element_by_id(cm.gender).click()
        # Check.assert_equal_xpath(
        #     self, cm.gender_wrapper_abc, 1, 'Gender wrapper is not exist', 'Check - Gender wrapper exist')
        # mgd.find_element_by_xpath(cm.male_abc).click()
        # Check.assert_in_id_value(self, cm.gender, 'male', 'Gender contain wrong data', 'Check - Gender is')
        # mgd.find_element_by_id(cm.gender).click()
        # Check.assert_equal_xpath(
        #     self, cm.gender_wrapper_abc, 1, 'Gender wrapper is not exist', 'Check - Gender wrapper exist')
        # mgd.find_element_by_xpath(cm.female_abc).click()
        # Check.assert_in_id_value(self, cm.gender, 'female', 'Gender contain wrong data', 'Check - Gender is')

        Check.assert_equal_xpath(self, cm.undo_option_abc, 1, 'Undo options unavailable', 'Check - Undo options')
        Check.assert_in_xpath_class(
            self, cm.undo_option_abc, 'clickable', 'Undo options not clickable', 'Check - Undo options is clickable :')
        mgd.find_element_by_xpath(cm.undo_option_abc).click()

        time.sleep(2)
        profile_tab = mgd.find_element_by_id(cm.profile_tab)
        profile_tab.click()

        Check.assert_in_id_value(
            self, cm.name_input, name2, 'Name input contain wrong data', 'Check - Name input contain ')
        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name2, 'Name title contain wrong data', 'Check - Name title contain ')

        Check.assert_not_in_id_value(
            self, cm.job_title_input, job_title, 'Job title input contain wrong data',
            'Check - Job title input is empty')
        Check.assert_not_in_xpath_text(
            self, cm.job_title_info_abc, job_title, 'Job title info contain wrong data',
            'Check - Job title title is empty')

        Check.assert_not_in_id_value(
            self, cm.company_input, company, 'Company input contain wrong data', 'Check - Company input is empty')
        Check.assert_not_in_xpath_text(
            self, cm.company_info_abc, company, 'Company info contain wrong data', 'Check - Company title is empty')

        Check.assert_not_in_id_value(
            self, cm.department_input, department, 'Department input contain wrong data',
            'Check - Department input is empty')
        Check.assert_not_in_xpath_text(
            self, cm.department_info_abc, department, 'Department info contain wrong data',
            'Check - Department title is empty')

        Check.assert_not_in_id_value(
            self, cm.birthday_input, '2000-06-06', 'Birthday input contain wrong data',
            'Check - Birthday input is empty')

        contacts_tab.click()

        Check.assert_not_in_name_value(
            self, cm.business_phone_input, business_phone, 'Business phone input contain wrong data',
            'Check - Business phone input is empty')
        Check.assert_not_in_xpath_text(
            self, cm.work_phone_info_abc, business_phone, 'Business phone info contain wrong data',
            'Check - Business phone title is empty')

        Check.assert_not_in_name_value(
            self, cm.mobile_phone_input, mobile_phone, 'Mobile phone input contain wrong data',
            'Check - Mobile phone input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_phone_input, home_phone, 'Home phone input contain wrong data',
            'Check - Home phone input is empty')

        Check.assert_not_in_id_value(
            self, cm.website_input, website, 'Website input contain wrong data', 'Check - Website input is empty')

        Check.assert_not_in_id_value(
            self, cm.email_input, email_1, 'Email input contain wrong data', 'Check - Email input is empty')

        Check.assert_not_in_id_value(
            self, cm.email_input_2, email_2, 'Email input 2 contain wrong data', 'Check - Email input 2 is empty')

        Check.assert_not_in_id_value(
            self, cm.email_input_3, email_3, 'Email input 3 contain wrong data', 'Check - Email input 3 is empty')

        time.sleep(1)
        Check.assert_not_in_id_value(
            self, cm.im_id_input, im_id, 'Im_id input contain wrong data', 'Check - Im_id input is empty')

        address_tab.click()

        Check.assert_not_in_name_value(
            self, cm.work_street_input, work_street, 'Work street input contain wrong data',
            'Check - Work street input is empty')

        Check.assert_not_in_name_value(
            self, cm.work_city_input, work_city, 'Work city input contain wrong data',
            'Check - Work city input is empty')

        Check.assert_not_in_name_value(
            self, cm.work_state_input, work_state, 'Work state input contain wrong data',
            'Check - Work state input is empty')

        Check.assert_not_in_name_value(
            self, cm.work_postal_code_input, work_postal_code, 'Work postal code input contain wrong data',
            'Check - Work postal code input is empty')

        Check.assert_not_in_name_value(
            self, cm.work_country_input, work_country, 'Work country input contain wrong data',
            'Check - Work country input is empty')
        work_address = work_street + ' ' + work_city + ' ' + work_state + ' ' + work_postal_code + ' ' + work_country
        Check.assert_not_in_xpath_text(
            self, cm.address_info_abc, work_address, 'Address info contain wrong data',
            'Check - Address title is empty')

        Check.assert_not_in_name_value(
            self, cm.home_street_input, home_street, 'Home street input contain wrong data',
            'Check - Home street input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_city_input, home_city, 'Home city input contain wrong data',
            'Check - Home city input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_state_input, home_state, 'Home state input contain wrong data',
            'Check - Home state input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_postal_code_input, home_postal_code, 'Home postal code input contain wrong data',
            'Check - Home postal code input is empty')

        Check.assert_not_in_name_value(
            self, cm.home_country_input, home_country, 'Home country input contain wrong data',
            'Check - Home country input is empty')

        more_tab.click()

        Check.assert_not_in_id_value(
            self, cm.language_input, language, 'Language input contain wrong data', 'Check - Language input is empty')

        Check.assert_not_in_id_value(
            self, cm.hobbies_input, hobbies, 'Hobbies input contain wrong data', 'Check - Hobbies input is empty')

        # Check.assert_not_in_id_value(self, cm.gender, 'female', 'Gender contain wrong data', 'Check - Gender is empty')

        Check.find_element_by_class_name_and_text(cm.contact_title, name2)
        mgd.find_element_by_xpath(cm.delete_option_abc).click()
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
        print('Check - Delete button')
        time.sleep(2)
        Check.element_is_visible_class_name(
            cm.block_wrapper, 'Delete wrapper exist', 'Check - Delete wrapper not exist')


# @unittest.skip("Ok")
class Test9ABCSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Test9ABCSearch\n')
        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')


    @classmethod
    def tearDownClass(cls):
        print('/////')
        time.sleep(2)
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
        else:
            print('View mode is list of contacts')
            mgd.find_element_by_xpath(cm.view_change).click()
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        driver_instance.implicitly_wait(5)
        print("/////")

    def setUp(self):
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
            Check.assert_equal_xpath(
                self, cm.view_change, 1, 'View change button not found', 'Check - View change button')
            Check.assert_in_xpath_class(
                self, cm.view_change, 'clickable', 'View change button not clickable',
                'Check - View change button is clickable :')
            time.sleep(1)
            mgd.find_element_by_xpath(cm.view_change).click()
            time.sleep(1)
        Check.assert_equal_xpath(
            self, cm.contact_cards_list_xpath, 1, 'Contact card list not found', 'Check - Contact card list')
        time.sleep(4)
        mgd.find_element_by_xpath(cm.clear_search).click()
        Check.assert_empty_xpath_value(
            cm.clear_search, 'Search field did not empty', '')
        time.sleep(2)

    def tearDown(self):
        time.sleep(2)
        mgd.find_element_by_xpath(cm.clear_search).click()
        Check.assert_empty_xpath_value(
            cm.clear_search, 'Search field did not empty', 'Check - Search field is empty')
        time.sleep(2)
        print('/////')

    def test_search_name(self):
        print('Search name')
        search = 'Contact for autotest'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.name_in_abc, 14, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_company(self):
        print('Search company')
        search = 'Test inc.'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.name_in_abc, 8, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_department(self):
        print('Search department')
        search = 'Department of truth'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.name_in_abc, 3, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_job_title(self):
        print('Search job title')
        search = 'High lvl tester'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.name_in_abc, 8, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_work_phone(self):
        print('Search work phone')
        search = '8965569855'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.name_in_abc, 5, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_email(self):
        print('Search email')
        search = 'cont@autotest.ab'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.name_in_abc, 14, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')

    def test_search_address(self):
        print('Search address')
        search = 'City 17'
        mgd.find_element_by_xpath(cm.search_contact).send_keys(search)
        time.sleep(3)
        Check.check_exists_contacts_by_class_name(
            cm.name_in_abc, 5, 'Contacts list contains more elements',
            'Contacts list contains less elements', 'Contacts list contains the right amount elements')


# @unittest.skip("")
class TestDeleteFromDeletedItems(unittest.TestCase):
    def setUp(self):
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
        else:
            print('View mode is list of contacts')
            mgd.find_element_by_xpath(cm.view_change).click()

        Check.find_element_by_class_name_and_text(cm.folder_name, 'Deleted Items').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_deleted_items_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(deleted_items_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + deleted_items_folder + ' folder is selected')

    def tearDown(self):
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
        else:
            print('View mode is list of contacts')
            mgd.find_element_by_xpath(cm.view_change).click()

        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        driver_instance.implicitly_wait(5)

        Check.find_element_by_class_name_and_text(cm.folder_name, 'Contacts').click()
        folder_status = mgd.find_element_by_xpath(cm.folder_contacts_select).get_attribute(name='class')
        if 'folder-selected' not in folder_status:
            raise Exception(contacts_folder + ' folder in not selected')
        elif 'folder-selected' in folder_status:
            print('Check - ' + contacts_folder + ' folder is selected')

    # @unittest.skip("Ok")
    def test_deleted_items(self):
        main_len_of_list = len(mgd.find_elements_by_class_name(cm.contact_title))
        print('Len of list = ' + str(main_len_of_list))
        while main_len_of_list >= 6:
            mgd.find_element_by_class_name(cm.contact_title).click()
            print('Check - Contact card')
            time.sleep(1)
            mgd.find_element_by_class_name(cm.contact_info)
            name = mgd.find_element_by_class_name(cm.contact_title).get_attribute('innerText')
            print('Check - Contact ' + name + ' is open')
            # time.sleep(1)
            Check.assert_equal_xpath(self, cm.delete_option, 1, 'Delete options unavailable', 'Check - Delete options')
            Check.assert_in_xpath_class(
                self, cm.delete_option,
                'clickable', 'Delete options not clickable', 'Check - Delete options is clickable :')
            mgd.find_element_by_xpath(cm.delete_option).click()
            # time.sleep(1)
            Check.element_is_visible_class_name(
                cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
            # time.sleep(2)
            Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
            print('Check - Delete button')
            # time.sleep(2)
            Check.assert_equal_class_name(
                self, cm.block_wrapper, 0, 'Delete wrapper exist', 'Check - Delete wrapper does not exist')
            # time.sleep(1)
            new_list = len(mgd.find_elements_by_class_name(cm.contact_title))
            if new_list >= main_len_of_list:
                raise Exception('Contact are not deleted')
            print('Check - ' + name + ' contact is deleted')
            main_len_of_list -= 1

    # @unittest.skip("Ok")
    def test_deleted_items_ABC(self):
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
            Check.assert_equal_xpath(
                self, cm.view_change, 1, 'View change button not found', 'Check - View change button')
            Check.assert_in_xpath_class(
                self, cm.view_change, 'clickable', 'View change button not clickable',
                'Check - View change button is clickable :')
            mgd.find_element_by_xpath(cm.view_change).click()
            time.sleep(1)

            main_len_of_list = len(mgd.find_elements_by_class_name(cm.name_in_abc))
            print('Len of list = ' + str(main_len_of_list))
            while main_len_of_list >= 2:
                name = mgd.find_element_by_class_name(cm.contact_title).get_attribute('innerText')
                print('Check - Contact ' + name + ' is open')
                Check.assert_equal_xpath(self, cm.delete_option_abc, 1, 'Delete options unavailable',
                                         'Check - Delete options')
                Check.assert_in_xpath_class(
                    self, cm.delete_option_abc,
                    'clickable', 'Delete options not clickable', 'Check - Delete options is clickable :')
                mgd.find_element_by_xpath(cm.delete_option_abc).click()
                Check.element_is_visible_class_name(
                    cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
                Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
                print('Check - Delete button')
                time.sleep(1)
                new_list = len(mgd.find_elements_by_class_name(cm.name_in_abc))
                if new_list >= main_len_of_list:
                    raise Exception('Contact are not deleted')
                print('Check - ' + name + ' contact is deleted')
                main_len_of_list -= 1


@unittest.skip("skip. need add scrolling")
class Test11SelectContacts(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_scroll(self):
        mgd.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@unittest.skip("skip. need add scrolling")
class Test11ABCSelectContacts(unittest.TestCase):
    def setUp(self):
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
            Check.assert_equal_xpath(
                self, cm.view_change, 1, 'View change button not found', 'Check - View change button')
            Check.assert_in_xpath_class(
                self, cm.view_change, 'clickable', 'View change button not clickable',
                'Check - View change button is clickable :')
            time.sleep(1)
            mgd.find_element_by_xpath(cm.view_change).click()
            time.sleep(1)
        Check.assert_equal_xpath(
            self, cm.contact_cards_list_xpath, 1, 'Contact card list not found', 'Check - Contact card list')
        time.sleep(4)
        mgd.find_element_by_xpath(cm.clear_search).click()
        Check.assert_empty_xpath_value(
            cm.clear_search, 'Search field did not empty', '')
        time.sleep(2)

    def tearDown(self):
        if Check.check_exists_by_class_name(cm.folders_list_wrapper):
            print('View mode is list of folders')
        else:
            print('View mode is list of contacts')
            mgd.find_element_by_xpath(cm.view_change).click()
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_xpath(cm.contact_modal_window):
            print('Contact card - exist')
            mgd.find_element_by_id(cm.close_button).click()
        if Check.check_exists_by_class_name(cm.apply_unsaved_changes):
            print('Block wrapper "Apply unsaved changes" - exist')
            mgd.find_element_by_xpath(cm.no_apply_unsaved_changes).click()
        if Check.find_element_by_class_name_and_text(cm.contact_title, 'BBC_edit'):
            Check.find_element_by_class_name_and_text(cm.contact_title, 'BBC_edit').click()
            mgd.find_element_by_xpath(cm.delete_option).click()
            Check.element_is_visible_class_name(
                cm.block_wrapper, 'Check - Delete wrapper', 'Delete wrapper does not exist')
            time.sleep(2)
            Check.find_element_by_class_name_and_text(cm.confirm_button, 'Delete').click()
            print('Check - Delete button')
            time.sleep(2)

        driver_instance.implicitly_wait(5)

        print("/////")

    def test_select_contacts(self):
        name1 = 'Crag Barbarian'
        name2 = 'Crag21'
        name3 = 'Test auto contact 11'
        name4 = 'Von Fon'
        name5 = 'Werty As We'

        # actionsChains = ActionChains(Maw)

        contact1 = Check.find_element_by_class_name_and_text(cm.name_in_abc, name1)
        # actionsChains.move_to_element(contact1)
        # actionsChains.perform()
        contact1.click()

        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name1, 'Contact is not a ' + name1, 'Check - contact ' + name1)
        time.sleep(2)
        contact2 = Check.find_element_by_class_name_and_text(cm.name_in_abc, name2)
        # actionsChains.move_to_element(contact2)
        # actionsChains.perform()
        contact2.click()

        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name2, 'Contact is not a ' + name2, 'Check - contact ' + name2)
        time.sleep(2)
        contact3 = Check.find_element_by_class_name_and_text(cm.name_in_abc, name3)
        # actionsChains.move_to_element(contact3).perform()
        contact3.click()
        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name3, 'Contact is not a ' + name3, 'Check - contact ' + name3)
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.name_in_abc, name4).click()
        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name4, 'Contact is not a ' + name4, 'Check - contact ' + name4)
        time.sleep(2)
        Check.find_element_by_class_name_and_text(cm.name_in_abc, name5).click()
        Check.assert_in_xpath_text(
            self, cm.name_title_abc, name5, 'Contact is not a ' + name5, 'Check - contact ' + name5)
        time.sleep(2)
