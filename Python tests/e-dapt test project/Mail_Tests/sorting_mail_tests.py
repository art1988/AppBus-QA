import time
from datetime import datetime
import unittest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import Check
import Config
from main_app_window import Maw, driver_instance
# from selenium.webdriver.common.action_chains import ActionChains
# from slic import winium


# config shortcut

mgd = Maw.get_devices()
ed = Config.Mail.email_details.Elements
mw = Config.Mail.main_window.Elements
ne = Config.Mail.new_email.Elements
driver_instance.implicitly_wait(5)
wait = WebDriverWait(mgd, 20)

today = datetime.now()
today_format = today.strftime("%Y %d %b ")

# Names for presets
delete_name_1 = 'Autotest message for Delete Inbox'
delete_name_2 = 'Autotest message for Delete Sent Items'
delete_name_3 = 'Autotest message for Delete Junk E-mail'
flag_name_1 = 'Autotest message for Importance Inbox'
flag_name_2 = 'Autotest message for Importance Sent Items'
flag_name_3 = 'Autotest message for Importance Deleted Items'
flag_name_4 = 'Autotest message for Importance Junk E-mail'
draft_name_1 = 'Autotest message for Delete draft'
draft_name_2 = 'Autotest message for Importance draft'
move_to_name_1 = 'Autotest message for Move To Inbox'
move_to_name_2 = 'Autotest message for Move To Sent Items'
move_to_name_3 = 'Autotest message for Move To Deleted Items'
move_to_name_4 = 'Autotest message for Move To Junk E-mail'
checkboxes_name_1 = 'Autotest message for Inbox 1'
checkboxes_name_2 = 'Autotest message for Inbox 2'
search_name = 'Test message for search '
words_for_search = 'test message for'

autotest_messages_list = [delete_name_1, delete_name_2, delete_name_3, flag_name_1, flag_name_2, flag_name_3,
                          flag_name_4, draft_name_1, draft_name_2, move_to_name_1, move_to_name_2, move_to_name_3,
                          move_to_name_4, checkboxes_name_1, checkboxes_name_2]


def setUpModule():
    print('Start: sorting_mail_tests.py\n')
    # mail_folder = winium.top_menu.find_element_by_name('Mail')
    # calendar_folder = winium.top_menu.find_element_by_name('Calendar')
    # actions = ActionChains(driver_instance)
    # actions.move_to_element(calendar_folder).move_to_element(mail_folder).click().perform()

def tearDownModule():
    print('End: sorting_mail_tests.py\n')
    # driver_instance.quit()


# @unittest.skip('Ok')
class Test4Presets(unittest.TestCase):
    def setUp(self):
        driver_instance.implicitly_wait(2)
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

        if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
            pass
        else:
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()

        time.sleep(1)
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        date_arrow_exist = len(mgd.find_elements_by_xpath(mw.sorting_date_arrow_icon))
        if date_arrow_exist == 0:
            mgd.find_element_by_xpath(mw.date_sorting).click()
            mgd.find_element_by_id(mw.small_sorting_button).click()
        # time.sleep(1)
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        # time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon_f:
            mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()
        if 'opened' in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        driver_instance.implicitly_wait(5)

    def tearDown(self):
        time.sleep(3)

    # @unittest.skip('Ok')
    def test1_search_presets(self):
        number = 1
        while number < 7:
            time.sleep(1)
            mgd.find_element_by_id(mw.new_email_button).click()
            time.sleep(1)
            mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
            time.sleep(2)
            name = search_name + today_format + str(number)
            mgd.find_element_by_id(ne.subject_field_input).send_keys(name)
            time.sleep(1)
            mgd.find_element_by_xpath(ne.send_email_button).click()
            print('Check - Send button' + name)
            time.sleep(3)
            number += 1

        number_draft = 7
        while number_draft < 10:
            mgd.find_element_by_id(mw.new_email_button).click()
            time.sleep(1)
            mgd.find_element_by_id(ne.subject_field_input).send_keys(search_name + today_format + str(number_draft))
            time.sleep(2)
            mgd.find_element_by_id(ne.close_email_button).click()
            Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper)
            time.sleep(1)
            Check.find_element_by_class_name_and_text(ne.close_editor_confirmation_button, 'Save').click()
            time.sleep(1)
            number_draft += 1

        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(2)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(2)
        number_sorting = 4
        while number_sorting < 7:

            name_for_sorting = search_name + today_format + str(number_sorting)
            row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
            if row_number is None:
                mgd.find_element_by_id(mw.spinner).click()
                # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
                time.sleep(1)
            row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
            time.sleep(1)
            if row_number is None:
                raise Exception('Message not found')
            time.sleep(1)
            Check.checkbox_in_n_message_click(row_number)
            Check.assert_in_class_attr_message_in_n_row(
                self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
                'Check - ' + str(row_number) + 'st message is checked - ')
            number_sorting += 1

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(1)
        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        #############################################

        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        time.sleep(2)
        #############################################

        number_sorting = 4
        while number_sorting < 7:
            name_for_sorting = search_name + today_format + str(number_sorting)
            row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
            if row_number is None:
                raise Exception('Message not found')

            Check.checkbox_in_n_message_click(row_number)
            Check.assert_in_class_attr_message_in_n_row(
                self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
                'Check - ' + str(row_number) + 'st message is checked - ')
            number_sorting += 1

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)

    # @unittest.skip('Ok')
    def test2_create_main_presets(self):
        time.sleep(1)
        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(delete_name_1)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(delete_name_2)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(delete_name_3)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        time.sleep(1)
        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(flag_name_1)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(flag_name_2)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(flag_name_3)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")

        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(flag_name_4)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(draft_name_1)
        time.sleep(2)
        mgd.find_element_by_id(ne.close_email_button).click()
        Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper)
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.close_editor_confirmation_button, 'Save').click()
        time.sleep(1)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(draft_name_2)
        time.sleep(2)
        mgd.find_element_by_id(ne.close_email_button).click()
        Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper)
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.close_editor_confirmation_button, 'Save').click()
        time.sleep(1)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(move_to_name_1)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(move_to_name_2)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(move_to_name_3)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(move_to_name_4)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        time.sleep(1)
        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(checkboxes_name_1)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

        time.sleep(1)
        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        mgd.find_element_by_id(ne.subject_field_input).send_keys(checkboxes_name_2)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(3)

    # @unittest.skip('Ok')
    def test3_move_to_presets(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        name_for_sorting = move_to_name_2
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            mgd.find_element_by_id(mw.spinner).click()
            # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
            time.sleep(1)
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        time.sleep(1)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Sent Items').click()
        print('Check - Sent Items')
        time.sleep(1)

        name_for_sorting = move_to_name_3
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')
        time.sleep(1)
        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)

        name_for_sorting = move_to_name_4
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)

    # @unittest.skip('Ok')
    def test4_flag_presets(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')

        #############################################


        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()

        #############################################

        name_for_sorting = flag_name_2
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')
        time.sleep(1)
        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Sent Items').click()
        print('Check - Sent Items')
        time.sleep(1)

        name_for_sorting = flag_name_3
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)

        #############################################


        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()

        #############################################

        name_for_sorting = flag_name_4
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        time.sleep(1)
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)

    # @unittest.skip('Ok')
    def test5_delete_presets(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')

        #############################################


        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()

        #############################################

        name_for_sorting = delete_name_3
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')
        time.sleep(1)
        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)


# @unittest.skip('Ok')
class Test5Checkboxes(unittest.TestCase):
    def setUp(self):
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

    def tearDown(self):
        pass

    def test_checkbox_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        time.sleep(1)

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')

    def test_checkbox_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        time.sleep(1)

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')

    def test_checkbox_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        time.sleep(1)

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')

    def test_checkbox_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
            'Check - Selected folder is drafts -')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        time.sleep(1)

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')

    def test_checkbox_junk(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)
        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk e-mail)',
            'Check - Selected folder is junk e-mail -')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        time.sleep(1)

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked')
        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked')

        Check.assert_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is not checked', 'Check - 4st message is checked')
        Check.checkbox_in_n_message_click(4)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, '4', 'checked-message', '4st message is checked', 'Check - 4st message is not checked')


# @unittest.skip('Ok')
class Test5MoreOption(unittest.TestCase):
    def setUp(self):
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

    def tearDown(self):
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

    # @unittest.skip('ok')
    def test1_more_read_unread_options_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'unread-message', '1st message is not unread', 'Check - 1st message is unread - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')

        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'unread-message', ' message is not unread', 'Check - 2st message is unread - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')
        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist - ')
        Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as read').click()
        print('Check - Mark as read')
        time.sleep(2)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is not read', 'Check - 1st message is read - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', '2st message is not read', 'Check - 2st message is read - ')
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is not unread', 'Check - 1st message is read - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', ' message is not unread', 'Check - 2st message is read - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as unread').click()
        time.sleep(2)
        print('Check - Mark as unread')

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'unread-message', '1st message is not read', 'Check - 1st message is unread - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'unread-message', '2st message is not read', 'Check - 2st message is unread - ')
        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

    # @unittest.skip('ok')
    def test1_more_read_unread_options_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is unread', 'Check - 1st message is read - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', ' message is unread', 'Check - 2st message is read - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')
        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist - ')
        Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as unread').click()
        print('Check - Mark as unread')
        time.sleep(2)

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'unread-message', '1st message is not unread', 'Check - 1st message is unread - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'unread-message', '2st message is not unread', 'Check - 2st message is unread - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')
        time.sleep(1)

        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as read').click()
        time.sleep(2)
        print('Check - Mark as read')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is not read', 'Check - 1st message is read - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', '2st message is not read', 'Check - 2st message is read - ')
        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is not checked', 'Check - 1st message is unchecked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is not checked', 'Check - 2st message is unchecked - ')

    # @unittest.skip('ok')
    def test1_more_read_unread_options_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'unread-message', '1st message is not unread', 'Check - 1st message is unread - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')

        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'unread-message', ' message is not unread', 'Check - 2st message is unread - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')
        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist - ')
        Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as read').click()
        print('Check - Mark as read')
        time.sleep(2)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is not read', 'Check - 1st message is read - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', '2st message is not read', 'Check - 2st message is read - ')
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is not unread', 'Check - 1st message is read - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', ' message is not unread', 'Check - 2st message is read - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as unread').click()
        time.sleep(2)
        print('Check - Mark as unread')

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'unread-message', '1st message is not read', 'Check - 1st message is unread - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'unread-message', '2st message is not read', 'Check - 2st message is unread - ')
        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

    # @unittest.skip('ok')
    def test1_more_read_unread_options_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
            'Check - Selected folder is drafts -')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is unread', 'Check - 1st message is read - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', ' message is unread', 'Check - 2st message is read - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist - ')

        first_flag_attr = mgd.find_element_by_xpath('//*[@id="list"]/li[1]/div[2]/i').get_attribute(name="class")
        second_flag_attr = mgd.find_element_by_xpath('//*[@id="list"]/li[2]/div[2]/i').get_attribute(name="class")

        if first_flag_attr == 'icon-icon_flag flag-red' or second_flag_attr == 'icon-icon_flag flag-red':
            if first_flag_attr == 'icon-icon_flag flag-red' and second_flag_attr == 'icon-icon_flag flag-red':
                # print('both')
                more_dd_element = len(mgd.find_elements_by_class_name(mw.more_dropdown_item))
                self.assertEqual(more_dd_element, 1, 'The number of dropdown items in "More" is not correct')
                print('Check - Dropdawn list contain 1 elements')
            else:
                # print('one')
                more_dd_element = len(mgd.find_elements_by_class_name(mw.more_dropdown_item))
                self.assertEqual(more_dd_element, 2, 'The number of dropdown items in "More" is not correct')
                print('Check - Dropdawn list contain 2 elements')
        else:
            # print('no one')
            more_dd_element = len(mgd.find_elements_by_class_name(mw.more_dropdown_item))
            self.assertEqual(more_dd_element, 1, 'The number of dropdown items in "More" is not correct')
            print('Check - Dropdawn list contain 1 elements')

        time.sleep(2)

        Check.checkbox_in_n_message_click(1)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')

    # @unittest.skip('ok')
    def test1_more_read_unread_options_junk(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk e-mail)',
            'Check - Selected folder is junk e-mail -')

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'unread-message', '1st message is not unread', 'Check - 1st message is unread - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.checkbox_in_n_message_click(1)
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')

        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'unread-message', ' message is not unread', 'Check - 2st message is unread - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')
        Check.checkbox_in_n_message_click(2)
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')
        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist - ')
        Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as read').click()
        print('Check - Mark as read')
        time.sleep(2)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is not read', 'Check - 1st message is read - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', '2st message is not read', 'Check - 2st message is read - ')
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'unread-message', '1st message is not unread', 'Check - 1st message is read - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'unread-message', ' message is not unread', 'Check - 2st message is read - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

        mgd.find_element_by_id(mw.small_more_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as unread').click()
        time.sleep(2)
        print('Check - Mark as unread')

        Check.assert_in_class_attr_message_in_n_row(
            self, '1', 'unread-message', '1st message is not read', 'Check - 1st message is unread - ')
        Check.assert_in_class_attr_message_in_n_row(
            self, '2', 'unread-message', '2st message is not read', 'Check - 2st message is unread - ')
        Check.checkbox_in_n_message_click(1)
        Check.checkbox_in_n_message_click(2)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

    # @unittest.skip('ok')
    def test1_more_important_options_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')

        first_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(1):
            first_flag = 1
            print('1st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(1):
            first_flag = 2
            print('1st message is not important')

        second_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(2):
            second_flag = 1
            print('2st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(2):
            second_flag = 2
            print('2st message is not important')

        if first_flag == 0 or second_flag == 0:
            raise Exception('One or both of this messages not contain flags')

        elif first_flag and second_flag == 1:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

        else:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

    # @unittest.skip('ok')
    def test1_more_important_options_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')

        first_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(1):
            first_flag = 1
            print('1st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(1):
            first_flag = 2
            print('1st message is not important')

        second_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(2):
            second_flag = 1
            print('2st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(2):
            second_flag = 2
            print('2st message is not important')

        if first_flag == 0 or second_flag == 0:
            raise Exception('One or both of this messages not contain flags')

        elif first_flag and second_flag == 1:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

        else:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

    # @unittest.skip('ok')
    def test1_more_important_options_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')

        first_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(1):
            first_flag = 1
            print('1st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(1):
            first_flag = 2
            print('1st message is not important')

        second_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(2):
            second_flag = 1
            print('2st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(2):
            second_flag = 2
            print('2st message is not important')

        if first_flag == 0 or second_flag == 0:
            print(first_flag)
            print(second_flag)
            raise Exception('One or both of this messages not contain flags')

        elif first_flag and second_flag == 1:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

        else:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

    # @unittest.skip('ok')
    def test1_more_important_options_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
            'Check - Selected folder is drafts -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')

        first_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(1):
            first_flag = 1
            print('1st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(1):
            first_flag = 2
            print('1st message is not important')

        second_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(2):
            second_flag = 1
            print('2st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(2):
            second_flag = 2
            print('2st message is not important')

        if first_flag == 0 or second_flag == 0:
            raise Exception('One or both of this messages not contain flags')

        elif first_flag and second_flag == 1:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

        else:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

    # @unittest.skip('ok')
    def test1_more_important_options_junk(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk e-mail)',
            'Check - Selected folder is junk e-mail -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        Check.assert_not_in_class_attr_message_in_n_row(
            self, 1, 'checked-message', '1st message is checked', 'Check - 1st message is not checked - ')
        Check.assert_not_in_class_attr_message_in_n_row(
            self, 2, 'checked-message', '2st message is checked', 'Check - 2st message is not checked - ')

        first_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(1):
            first_flag = 1
            print('1st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(1):
            first_flag = 2
            print('1st message is not important')

        second_flag = 0
        if 'flag_red' in Check.flag_in_n_message_attr(2):
            second_flag = 1
            print('2st message is important')
        elif 'flag_red' not in Check.flag_in_n_message_attr(2):
            second_flag = 2
            print('2st message is not important')

        if first_flag == 0 or second_flag == 0:
            raise Exception('One or both of this messages not contain flags')

        elif first_flag and second_flag == 1:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

        else:
            Check.checkbox_in_n_message_click(1)
            Check.checkbox_in_n_message_click(2)

            Check.assert_in_class_attr_message_in_n_row(
                self, '1', 'checked-message', '1st message is not checked', 'Check - 1st message is checked - ')
            Check.assert_in_class_attr_message_in_n_row(
                self, '2', 'checked-message', '2st message is not checked', 'Check - 2st message is checked - ')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as important').click()
            print('Check - Mark as important')
            time.sleep(2)

            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is not important',
                'Check - 1st message is important')
            Check.assert_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is not important',
                'Check - 2st message is important')

            mgd.find_element_by_id(mw.small_more_button).click()

            Check.assert_equal_class_name(
                self, mw.dropdown_list, 1, 'More dropdown list not exist', 'Check - More dropdown list exist')
            Check.find_element_by_class_name_and_text(mw.more_dropdown_item, 'Mark as not important').click()
            print('Check - Mark as not important')
            time.sleep(2)

            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('1'), 'flag-red', '1st message is important',
                'Check - 1st message is not important')
            Check.assert_not_in_xpath_class(
                self, Check.flag_in_n_message('2'), 'flag-red', '2st message is important',
                'Check - 2st message is not important')

    # @unittest.skip('ok')
    def test_importance_for_sorting_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        importance_row = str(Check.find_number_of_row_class_name_text(mw.topic, flag_name_1))

        element = mgd.find_element_by_xpath('//*[@id="list"]/li[' + importance_row + ']/div[4]')
        text_element = element.get_attribute('innerText')
        if 'Today at ' in text_element:
            Check.flag_in_n_message_click(importance_row)
            print('Check - Importance message is flagged')
        else:
            raise Exception('Importance message not flagged')

    # @unittest.skip('ok')
    def test_importance_for_sorting_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        importance_row = str(Check.find_number_of_row_class_name_text(mw.topic, flag_name_2))

        element = mgd.find_element_by_xpath('//*[@id="list"]/li[' + importance_row + ']/div[4]')
        text_element = element.get_attribute('innerText')
        if 'Today at ' in text_element:
            Check.flag_in_n_message_click(importance_row)
            print('Check - Importance message is flagged')
        else:
            raise Exception('Importance message not flagged')

    # @unittest.skip('ok')
    def test_importance_for_sorting_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        importance_row = str(Check.find_number_of_row_class_name_text(mw.topic, flag_name_3))
        print(importance_row)

        element = mgd.find_element_by_xpath('//*[@id="list"]/li[' + importance_row + ']/div[4]')
        text_element = element.get_attribute('innerText')
        if 'Today at ' in text_element:
            Check.flag_in_n_message_click(importance_row)
            print('Check - Importance message is flagged')
        else:
            raise Exception('Importance message not flagged')

    # @unittest.skip('ok')
    def test_importance_for_sorting_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
            'Check - Selected folder is drafts -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        importance_row = str(Check.find_number_of_row_class_name_text(mw.topic, draft_name_2))

        element = mgd.find_element_by_xpath('//*[@id="list"]/li[' + importance_row + ']/div[4]')
        text_element = element.get_attribute('innerText')
        if 'Today at ' in text_element:
            Check.flag_in_n_message_click(importance_row)
            print('Check - Importance message is flagged')
        else:
            raise Exception('Importance message not flagged')

    # @unittest.skip('ok')
    def test_importance_for_sorting_junk(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk e-mail)',
            'Check - Selected folder is junk e-mail -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        importance_row = str(Check.find_number_of_row_class_name_text(mw.topic, flag_name_4))

        element = mgd.find_element_by_xpath('//*[@id="list"]/li[' + importance_row + ']/div[4]')
        text_element = element.get_attribute('innerText')
        if 'Today at ' in text_element:
            Check.flag_in_n_message_click(importance_row)
            print('Check - Importance message is flagged')
        else:
            raise Exception('Importance message not flagged')


# @unittest.skip('Ok')
class Test5MoveTo(unittest.TestCase):
    def setUp(self):
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

    def tearDown(self):
        pass

    # @unittest.skip('Ok')
    def test2_inbox_move_to_sent_items(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')

        name_for_sorting = move_to_name_1
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Sent Items').click()
        print('Check - Sent Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Inbox').click()
        print('Check - Inbox')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test2_inbox_move_to_deleted_items(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')

        name_for_sorting = move_to_name_1
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Inbox').click()
        print('Check - Inbox')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test2_inbox_move_to_junk_email(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')

        name_for_sorting = move_to_name_1
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk emails)',
            'Check - Selected folder is junk emails -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Inbox').click()
        print('Check - Inbox')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test3_sent_items_move_to_inbox(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')

        name_for_sorting = move_to_name_2
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Inbox').click()
        print('Check - Inbox')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Sent Items').click()
        print('Check - Sent Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test3_sent_items_move_to_deleted_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')

        name_for_sorting = move_to_name_2
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Sent Items').click()
        print('Check - Sent Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test3_sent_items_move_to_junk_email(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')

        name_for_sorting = move_to_name_2
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not Junk E-mail)',
            'Check - Selected folder is Junk E-mail -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Sent Items').click()
        print('Check - Sent Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test4_deleted_items_move_to_inbox(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')

        name_for_sorting = move_to_name_3
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)
        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Inbox').click()
        print('Check - Inbox')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')

        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test4_deleted_items_move_to_sent_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')

        name_for_sorting = move_to_name_3
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Sent Items').click()
        print('Check - Sent Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')

        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test4_deleted_items_move_to_junk_email(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')

        name_for_sorting = move_to_name_3
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not Junk E-mail)',
            'Check - Selected folder is Junk E-mail -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')

        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')
        print(row_number)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test5_junk_email_move_to_inbox(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not Junk E-mail)',
            'Check - Selected folder is Junk E-mail -')
        time.sleep(3)

        name_for_sorting = move_to_name_4
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Inbox').click()
        print('Check - Inbox')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')

        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not Junk E-mail)',
            'Check - Selected folder is Junk E-mail -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')

        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test5_junk_emails_move_to_sent_items(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not Junk E-mail)',
            'Check - Selected folder is Junk E-mail -')
        time.sleep(3)

        name_for_sorting = move_to_name_4
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Sent Items').click()
        print('Check - Sent Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')

        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not Junk E-mail)',
            'Check - Selected folder is Junk E-mail -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')

        print('Check - ' + name_for_sorting + ' message is found')

    # @unittest.skip('Ok')
    def test5_junk_emails_move_to_delete_items(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not Junk E-mail)',
            'Check - Selected folder is Junk E-mail -')
        time.sleep(3)

        name_for_sorting = move_to_name_4
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Deleted Items').click()
        print('Check - Deleted Items')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')
        print('Check - ' + name_for_sorting + ' message is found')

        # New move to

        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_sorting)
        if row_number is None:
            raise Exception('Message not found')

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')

        mgd.find_element_by_id(mw.small_move_to_button).click()
        Check.assert_equal_class_name(
            self, mw.dropdown_list, 1, 'Move to dropdown list not exist', 'Check - Move to dropdown list exist')
        Check.find_element_by_class_name_and_text(mw.move_to_folder_name, 'Junk E-mail').click()
        print('Check - Junk E-mail')
        time.sleep(1)
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not Junk E-mail)',
            'Check - Selected folder is Junk E-mail -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_sorting) is None:
            raise Exception(name_for_sorting + ' message is not found')

        print('Check - ' + name_for_sorting + ' message is found')


# @unittest.skip('Ok')
class Test5Search(unittest.TestCase):
    def setUp(self):
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

        if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
            pass
        else:
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()

    def tearDown(self):
        if mgd.find_element_by_id(mw.message_search_input):
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()

    def test_search_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        search_word = search_name
        mgd.find_element_by_id(mw.small_search_button).click()
        print('Check - Search button')
        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word + today_format)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(2)
        len_of_row = len(mgd.find_elements_by_class_name(mw.row))

        if len_of_row == 3:
            print('Check - Find 3 messages')
        elif len_of_row > 3:
            print('len_of_row', len_of_row)
            raise Exception('More than 3 messages is found')
        elif len_of_row < 3:
            print('len_of_row', len_of_row)
            raise Exception('Less than 3 messages is found')

        mgd.find_element_by_class_name(mw.close_icon).click()
        print('Check - the close icon is clicked')
        time.sleep(2)

        if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
            print('Check - input is clear')
        else:
            raise Exception('Search input is not clear')

    def test_search_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        search_word = search_name
        mgd.find_element_by_id(mw.small_search_button).click()
        print('Check - Search button')
        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word + today_format)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(2)
        len_of_row = len(mgd.find_elements_by_class_name(mw.row))
        if len_of_row == 3:
            print('Check - Find 3 messages', len_of_row)
        elif len_of_row > 3:
            print('len_of_row', len_of_row)
            raise Exception('More than 3 messages is found', len_of_row)
        elif len_of_row < 3:
            print('len_of_row', len_of_row)
            raise Exception('Less than 3 messages is found', len_of_row)

        mgd.find_element_by_class_name(mw.close_icon).click()
        print('Check - the close icon is clicked')
        time.sleep(2)

        if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
            print('Check - input is clear')
        else:
            raise Exception('Search input is not clear')

    def test_search_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        search_word = search_name
        mgd.find_element_by_id(mw.small_search_button).click()
        print('Check - Search button')
        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word + today_format)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(2)
        len_of_row = len(mgd.find_elements_by_class_name(mw.row))
        if len_of_row == 3:
            print('Check - Find 3 messages', len_of_row)
        elif len_of_row > 3:
            print('len_of_row', len_of_row)
            raise Exception('More than 3 messages is found', len_of_row)
        elif len_of_row < 3:
            print('len_of_row', len_of_row)
            raise Exception('Less than 3 messages is found', len_of_row)

        mgd.find_element_by_class_name(mw.close_icon).click()
        print('Check - the close icon is clicked')
        time.sleep(2)

        if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
            print('Check - input is clear')
        else:
            raise Exception('Search input is not clear')

    def test_search_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
            'Check - Selected folder is drafts -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        search_word = search_name
        mgd.find_element_by_id(mw.small_search_button).click()
        print('Check - Search button')
        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word + today_format)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(4)

        len_of_row = len(mgd.find_elements_by_class_name(mw.row))
        if len_of_row == 3:
            print('Check - Find 3 messages', len_of_row)
        elif len_of_row > 3:
            print('len_of_row', len_of_row)
            raise Exception('More than 3 messages is found', len_of_row)
        elif len_of_row < 3:
            print('len_of_row', len_of_row)
            raise Exception('Less than 3 messages is found', len_of_row)
        mgd.find_element_by_class_name(mw.close_icon).click()
        print('Check - the close icon is clicked')
        time.sleep(2)

        if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
            print('Check - input is clear')
        else:
            raise Exception('Search input is not clear')

    def test_search_junk_email(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk emails)',
            'Check - Selected folder is junk emails -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        search_word = search_name
        mgd.find_element_by_id(mw.small_search_button).click()
        print('Check - Search button')
        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word + today_format)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(2)

        len_of_row = len(mgd.find_elements_by_class_name(mw.row))
        if len_of_row == 3:
            print('Check - Find 3 messages', len_of_row)
        elif len_of_row > 3:
            print('len_of_row', len_of_row)
            raise Exception('More than 3 messages is found', len_of_row)
        elif len_of_row < 3:
            print('len_of_row', len_of_row)
            raise Exception('Less than 3 messages is found', len_of_row)
        mgd.find_element_by_class_name(mw.close_icon).click()
        print('Check - the close icon is clicked')
        time.sleep(2)

        if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
            print('Check - input is clear')
        else:
            raise Exception('Search input is not clear')


# @unittest.skip('ERRORS')
class Test6Delete(unittest.TestCase):
    def setUp(self):
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

        if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
            pass
        else:
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()

    def tearDown(self):
        if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
            pass
        else:
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()
        time.sleep(10)

    # @unittest.skip('NOT Ok')
    def test1_mass_delete_from_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        mgd.find_element_by_id(mw.small_search_button).click()

        search_word = words_for_search

        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            pass
        else:
            mgd.find_element_by_xpath(mw.main_checkbox).click()
        print('Check - Main checkbox clicked')
        #######################
        topic_elements = mgd.find_elements_by_class_name(mw.topic)
        choose_elements = []
        for elem in topic_elements:
            if elem.get_attribute('innerText') == delete_name_1:
                choose_elements.append(topic_elements.index(elem) + 1)
            if elem.get_attribute('innerText') == flag_name_1:
                choose_elements.append(topic_elements.index(elem) + 1)
            if elem.get_attribute('innerText') == move_to_name_1:
                choose_elements.append(topic_elements.index(elem) + 1)
        ''' Если этот тест будет проходить следует удалиь закоментированный код. Изменение выше append на remove'''
        for index in choose_elements:
            if 'Today at 'in mgd.find_element_by_xpath(
                                    '//*[@id="list"]/li[' + str(index) + ']/div[4]').get_attribute('innerText'):
                Check.checkbox_in_n_message_click(index)
                Check.assert_not_in_class_attr_message_in_n_row(
                    self, index, 'checked-message', 'Message is checked', 'Check - message is not checked - ')
        time.sleep(2)

        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':

            mgd.find_element_by_id(mw.small_delete_button).click()
            time.sleep(1)
            Check.check_exists_by_class_name(mw.block_wrapper)
            print('Check - block wrapper exist')
            Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
            print('Check - Cancel button')
            time.sleep(1)
            mgd.find_element_by_id(mw.small_delete_button).click()
            time.sleep(1)
            Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
            print('Check - Ok button')

    # @unittest.skip('NOT Ok')
    def test1_mass_delete_from_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        mgd.find_element_by_id(mw.small_search_button).click()

        search_word = words_for_search

        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        #######################
        len_of_list = len(mgd.find_elements_by_class_name(mw.row))
        print(len_of_list)
        when_stop = 1
        while when_stop < 4:
            index_row = 1
            while index_row < 9:
                main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
                if main_checkbox == 'icon-icon_checked checkbox-custom':
                    pass
                else:
                    mgd.find_element_by_xpath(mw.main_checkbox).click()
                print('Check - Main checkbox clicked')
                len_of_list = len(mgd.find_elements_by_class_name(mw.row))
                print(len_of_list)

                if index_row > len_of_list:
                    break
                message_in_row = mgd.find_element_by_xpath(
                    '//*[@id="list"]/li[' + str(index_row) + ']').get_attribute('innerText')
                # for elem in save_message:
                if delete_name_2 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    print('delete_name_2', delete_name_2, '- find')
                    if 'Today at ' in b:
                        Check.checkbox_in_n_message_click(index_row)
                        print('delete_name_2', delete_name_2, '- uncheck')
                    else:
                        pass

                elif flag_name_2 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    print('flag_name_2', flag_name_2, '- find')
                    if 'Today at ' in b:
                        print('flag_name_2', flag_name_2, '- contain: "Today at"')
                        elem = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(
                            name="class")
                        if 'unread-message' in elem:
                            print('flag_name_2', flag_name_2, '- contain: "unread-message"')
                            Check.checkbox_in_n_message_click(index_row)
                        else:
                            pass
                    else:
                        print('flag_name_2', flag_name_2, '- uncheck (else)')
                        Check.checkbox_in_n_message_click(index_row)

                elif move_to_name_2 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    print('move_to_name_2', move_to_name_2, '- find')
                    if 'Today at ' in b:
                        print('move_to_name_2', move_to_name_2, '- contain: "Today at"')
                        elem = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(
                            name="class")
                        if 'unread-message' in elem:
                            print('move_to_name_2', move_to_name_2, '- contain: "unread-message"')
                            Check.checkbox_in_n_message_click(index_row)
                        else:
                            pass
                    else:
                        print('move_to_name_2', move_to_name_2, '- uncheck (else)')
                        Check.checkbox_in_n_message_click(index_row)

                else:
                    print('123123') # Check.checkbox_in_n_message_click(index_row)
                index_row += 1

            if mgd.find_element_by_id(mw.small_delete_button).is_displayed():
                mgd.find_element_by_id(mw.small_delete_button).click()
                print('Check - small delete button')
                time.sleep(1)
                Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
                print('Check - Ok button')
            time.sleep(2)
            if len(mgd.find_elements_by_class_name(mw.row)) <= 3:
                when_stop = 5

        #######################
        # topic_elements = mgd.find_elements_by_class_name(mw.topic)
        # choose_elements = []
        # for elem in topic_elements:
        #     if elem.get_attribute('innerText') == delete_name_2:
        #         choose_elements.append(topic_elements.index(elem) + 1)
        #     if elem.get_attribute('innerText') == flag_name_2:
        #         choose_elements.append(topic_elements.index(elem) + 1)
        #     if elem.get_attribute('innerText') == move_to_name_2:
        #         choose_elements.append(topic_elements.index(elem) + 1)
        #
        # for index in choose_elements:
        #     if 'Today at 'in mgd.find_element_by_xpath(
        #                             '//*[@id="list"]/li[' + str(index) + ']/div[4]').get_attribute('innerText'):
        #         Check.checkbox_in_n_message_click(index)
        #         Check.assert_not_in_class_attr_message_in_n_row(
        #             self, index, 'checked-message', 'Message is checked', 'Check - message is not checked - ')
        #         time.sleep(1)
        # time.sleep(2)
        #
        # mgd.find_element_by_id(mw.small_delete_button).click()
        # time.sleep(1)
        # Check.check_exists_by_class_name(mw.block_wrapper)
        # print('Check - block wrapper exist')
        # Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
        # print('Check - Cancel button')
        # time.sleep(1)
        # while len(mgd.find_elements_by_class_name(mw.row)) >= 11:
        #     mgd.find_element_by_id(mw.small_delete_button).click()
        #     time.sleep(1)
        #     Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
        #     print('Check - Ok button')
        #     time.sleep(1)

    # @unittest.skip('Ok')
    def test1_mass_delete_from_junk_emails(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk e-mail)',
            'Check - Selected folder is junk e-mail -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        mgd.find_element_by_id(mw.small_search_button).click()

        search_word = words_for_search

        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            pass
        else:
            mgd.find_element_by_xpath(mw.main_checkbox).click()
        print('Check - Main checkbox clicked')

        #######################
        topic_elements = mgd.find_elements_by_class_name(mw.topic)
        choose_elements = []
        for elem in topic_elements:
            if elem.get_attribute('innerText') == delete_name_3:
                choose_elements.append(topic_elements.index(elem) + 1)
            if elem.get_attribute('innerText') == flag_name_4:
                choose_elements.append(topic_elements.index(elem) + 1)
            if elem.get_attribute('innerText') == move_to_name_4:
                choose_elements.append(topic_elements.index(elem) + 1)

        for index in choose_elements:
            if 'Today at ' in mgd.find_element_by_xpath(
                                    '//*[@id="list"]/li[' + str(index) + ']/div[4]').get_attribute('innerText'):
                Check.checkbox_in_n_message_click(index)
                Check.assert_not_in_class_attr_message_in_n_row(
                    self, index, 'checked-message', 'Message is checked', 'Check - message is not checked - ')
        time.sleep(2)

        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':

            mgd.find_element_by_id(mw.small_delete_button).click()
            time.sleep(1)
            Check.check_exists_by_class_name(mw.block_wrapper)
            print('Check - block wrapper exist')
            Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
            print('Check - Cancel button')
            time.sleep(1)
            mgd.find_element_by_id(mw.small_delete_button).click()
            time.sleep(1)
            Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
            print('Check - Ok button')

    # @unittest.skip('Ok')
    def test1_mass_delete_from_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
            'Check - Selected folder is drafts -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        mgd.find_element_by_id(mw.small_search_button).click()

        search_word = words_for_search

        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            pass
        else:
            mgd.find_element_by_xpath(mw.main_checkbox).click()
        print('Check - Main checkbox clicked')

        #######################
        topic_elements = mgd.find_elements_by_class_name(mw.topic)
        choose_elements = []
        for elem in topic_elements:
            if elem.get_attribute('innerText') == draft_name_1:
                choose_elements.append(topic_elements.index(elem) + 1)
            if elem.get_attribute('innerText') == draft_name_2:
                choose_elements.append(topic_elements.index(elem) + 1)

        for index in choose_elements:
            if 'Today at ' in mgd.find_element_by_xpath(
                                    '//*[@id="list"]/li[' + str(index) + ']/div[4]').get_attribute('innerText'):
                Check.checkbox_in_n_message_click(index)
                Check.assert_not_in_class_attr_message_in_n_row(
                    self, index, 'checked-message', 'Message is checked', 'Check - message is not checked - ')
        time.sleep(2)

        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':

            mgd.find_element_by_id(mw.small_delete_button).click()
            time.sleep(1)
            Check.check_exists_by_class_name(mw.block_wrapper_header)
            print('Check - block wrapper exist')
            Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
            print('Check - Cancel button')
            time.sleep(1)
            mgd.find_element_by_id(mw.small_delete_button).click()
            time.sleep(1)
            Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
            print('Check - Ok button')

    # @unittest.skip('Ok')
    def test2_mass_delete_from_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(2)

        mgd.find_element_by_id(mw.small_search_button).click()

        search_word = words_for_search

        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(1)
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            pass
        else:
            mgd.find_element_by_xpath(mw.main_checkbox).click()
        print('Check - Main checkbox clicked')

        #######################

        len_of_list = len(mgd.find_elements_by_class_name(mw.row))
        print('len_of_list', len_of_list)
        when_stop = 1
        while when_stop < 4:
            index_row = 1
            while index_row < 9:
                len_of_list = len(mgd.find_elements_by_class_name(mw.row))
                print('len_of_list', len_of_list)

                if index_row > len_of_list:
                    break

                message_in_row = mgd.find_element_by_xpath(
                    '//*[@id="list"]/li[' + str(index_row) + ']').get_attribute('innerText')

                if delete_name_1 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    if 'Today at ' in b:
                        elem = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(
                            name="class")
                        if 'unread-message' in elem:
                            pass
                        else:
                            Check.checkbox_in_n_message_click(index_row)
                    else:
                        Check.checkbox_in_n_message_click(index_row)

                elif delete_name_2 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    if 'Today at ' in b:
                        elem = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(
                            name="class")
                        if 'unread-message' in elem:
                            pass
                        else:
                            Check.checkbox_in_n_message_click(index_row)
                    else:
                        Check.checkbox_in_n_message_click(index_row)

                elif delete_name_3 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    if 'Today at ' in b:
                        elem = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(
                            name="class")
                        if 'unread-message' in elem:
                            pass
                        else:
                            Check.checkbox_in_n_message_click(index_row)
                    else:
                        Check.checkbox_in_n_message_click(index_row)

                elif draft_name_1 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    if 'Today at ' in b:
                        pass
                    else:
                        Check.checkbox_in_n_message_click(index_row)

                elif flag_name_3 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    if 'Today at ' in b:
                        elem = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(
                            name="class")
                        if 'unread-message' in elem:
                            pass
                        else:
                            Check.checkbox_in_n_message_click(index_row)
                    else:
                        Check.checkbox_in_n_message_click(index_row)

                elif move_to_name_3 in message_in_row:
                    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
                    b = a.get_attribute('innerText')
                    if 'Today at ' in b:
                        elem = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(
                            name="class")
                        if 'unread-message' in elem:
                            pass
                        else:
                            Check.checkbox_in_n_message_click(index_row)
                            print('03')
                    else:
                        Check.checkbox_in_n_message_click(index_row)

                else:
                    Check.checkbox_in_n_message_click(index_row)
                index_row += 1

            if Check.check_exists_by_id(mw.small_delete_button) > 0:
                mgd.find_element_by_id(mw.small_delete_button).click()
                time.sleep(1)
                Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
                print('Check - Ok button')
            time.sleep(4)
            print(len(mgd.find_elements_by_class_name(mw.row)))
            if len(mgd.find_elements_by_class_name(mw.row)) <= 5:
                when_stop = 5

    # @unittest.skip('Ok')
    def test3_delete_from_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        name_for_delete = delete_name_1
        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')
        time.sleep(1)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        mgd.find_element_by_id(mw.small_delete_button).click()
        time.sleep(1)

        Check.check_exists_by_class_name(mw.block_wrapper)
        print('Check - block wrapper exist')

        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
        print('Check - Cancel button')
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        mgd.find_element_by_id(mw.small_delete_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
        print('Check - Ok button')

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete):
            raise Exception(name_for_delete + ' message is not deleted')
        print('Check - message is deleted')

        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            count_of_element = 0
            while count_of_element < 20:
                mgd.find_element_by_id(mw.spinner).click()
                # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
                count_of_element += 1
                if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete):
                    break
        time.sleep(1)
        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

    # @unittest.skip('Ok')
    def test3_delete_from_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
            'Check - Selected folder is sent items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        name_for_delete = delete_name_2
        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')
        time.sleep(2)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        mgd.find_element_by_id(mw.small_delete_button).click()
        time.sleep(1)

        Check.check_exists_by_class_name(mw.block_wrapper)
        print('Check - block wrapper exist')

        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
        print('Check - Cancel button')
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        mgd.find_element_by_id(mw.small_delete_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
        print('Check - Ok button')

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete):
            raise Exception(name_for_delete + ' message is not deleted')
        print('Check - message is deleted')

        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            count_of_element = 0
            while count_of_element < 20:
                mgd.find_element_by_id(mw.spinner).click()
                # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
                count_of_element += 1
                if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete):
                    break

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

    # @unittest.skip('Ok')
    def test3_delete_from_junk_emails(self):
        mgd.find_element_by_xpath(mw.junk_email_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk e-mail)',
            'Check - Selected folder is junk e-mail -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        name_for_delete = delete_name_3
        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        time.sleep(1)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        mgd.find_element_by_id(mw.small_delete_button).click()
        time.sleep(1)

        Check.check_exists_by_class_name(mw.block_wrapper)
        print('Check - block wrapper exist')

        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
        print('Check - Cancel button')
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        mgd.find_element_by_id(mw.small_delete_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
        print('Check - Ok button')

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete):
            raise Exception(name_for_delete + ' message is not deleted')
        print('Check - message is deleted')

        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            count_of_element = 0
            while count_of_element < 20:
                mgd.find_element_by_id(mw.spinner).click()
                # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
                count_of_element += 1
                if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete):
                    break

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

    # @unittest.skip('Ok')
    def test3_delete_from_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
            'Check - Selected folder is drafts -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        name_for_delete = draft_name_1
        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')
        time.sleep(1)

        Check.checkbox_in_n_message_click(row_number)
        Check.assert_in_class_attr_message_in_n_row(
            self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
            'Check - ' + str(row_number) + 'st message is checked - ')
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        mgd.find_element_by_id(mw.small_delete_button).click()
        time.sleep(1)

        Check.check_exists_by_class_name(mw.block_wrapper)
        print('Check - block wrapper exist')

        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
        print('Check - Cancel button')
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

        mgd.find_element_by_id(mw.small_delete_button).click()
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
        print('Check - Ok button')

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete):
            raise Exception(name_for_delete + ' message is not deleted')
        print('Check - message is deleted')

        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(1)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            count_of_element = 0
            while count_of_element < 20:
                mgd.find_element_by_id(mw.spinner).click()
                # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
                time.sleep(1)
                count_of_element += 1
                if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete):
                    break
        time.sleep(1)
        if Check.find_element_by_class_name_and_text(mw.topic, name_for_delete) is None:
            raise Exception(name_for_delete + ' message is not found')
        print('Check - message is found')
        row_number = Check.find_number_of_row_class_name_text(mw.topic, name_for_delete)
        Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

    # @unittest.skip('Ok')
    def test4_delete_from_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)

        #############################################
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.date_sorting).click()
        #############################################

        Check.assert_in_xpath_class(
            self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
            'Check - Selected folder is deleted items -')
        time.sleep(2)

        mgd.find_element_by_id(mw.spinner).click()
        # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)

        ############################
        mgd.find_element_by_id(mw.small_search_button).click()
        search_word = words_for_search
        Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
        mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
        Check.assert_in_id_value(
            self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
        time.sleep(1)

        list_for_delete = [delete_name_1, delete_name_2, delete_name_3, draft_name_1]

        for each_elem in list_for_delete:
            print(each_elem)
            if Check.find_number_of_row_class_name_text(mw.topic, each_elem):
                row_number = Check.find_number_of_row_class_name_text(mw.topic, each_elem)
                time.sleep(1)

                Check.checkbox_in_n_message_click(row_number)
                Check.assert_in_class_attr_message_in_n_row(
                    self, row_number, 'checked-message', str(row_number) + 'st message is not checked',
                    'Check - ' + str(row_number) + 'st message is checked - ')
                Check.date_in_n_message(self, row_number, 'Today at ', 'Message is not today', 'Check - today message')

                mgd.find_element_by_id(mw.small_delete_button).click()
                time.sleep(1)
                Check.check_exists_by_class_name(mw.block_wrapper)
                print('Check - delete block wrapper exist')
                Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
                print('Check - Ok button')
                time.sleep(3)

        ############################


@unittest.skip('ERRORS')
class Test7SortingInboxMail(unittest.TestCase):
    def setUp(self):
        driver_instance.implicitly_wait(2)
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

        if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
            pass
        else:
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()

        time.sleep(1)
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        if len(Maw.get_devices().find_elements_by_xpath(mw.sorting_date_arrow_icon)) <= 0:
            mgd.find_element_by_xpath(mw.date_sorting).click()
            mgd.find_element_by_id(mw.small_sorting_button).click()
            time.sleep(1)
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon_f:
            mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()

    def tearDown(self):
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        if len(Maw.get_devices().find_elements_by_xpath(mw.sorting_date_arrow_icon)) <= 0:
            mgd.find_element_by_xpath(mw.date_sorting).click()
            mgd.find_element_by_id(mw.small_sorting_button).click()
            time.sleep(1)
        sorting_arrow_icon = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon:
            mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()

    # @unittest.skip('ok')
    def test_sort_date_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox')

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_in_xpath_class(
            self, mw.sorting_dropdawn_list, 'opened', 'Sorting drop down list not found',
            'Check - Sorting drop down list')

        Check.assert_equal_xpath(
            self, mw.sorting_date_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')

        Check.assert_in_xpath_class(
            self, mw.sorting_date_arrow_icon, 'awesome-icon_long_arrow_down', 'Sorting icon arrow not down',
            'Check - Sorting icon arrow is down')

        Check.assert_in_xpath_text(
            self, mw.date_in_first_message, 'Today at', 'First message have wrong date', 'Check - Date is correct:')

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, move_to_name_1, 'First message have wrong subject',
            'Check - Subject is correct')

        mgd.find_element_by_xpath(mw.date_sorting).click()
        time.sleep(2)

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_date_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')

        Check.assert_in_xpath_text(
            self, mw.date_in_first_message, 'Apr 11 2014', 'First message have wrong date', 'Check - Date is correct:')

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, 'More Parts Deals!', 'First message have wrong subject',
            'Check - Subject is correct')

    # @unittest.skip('ok')
    def test_sort_from_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox')

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_in_xpath_class(
            self, mw.sorting_dropdawn_list, 'opened', 'Sorting drop down list not found',
            'Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.from_sorting).click()
        time.sleep(1)

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_equal_xpath(
            self, mw.sorting_from_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        Check.assert_in_xpath_class(
            self, mw.sorting_from_arrow_icon, 'awesome-icon_long_arrow_down', 'Sorting icon arrow not down',
            'Check - Sorting icon arrow is down')

        Check.assert_in_class_name_text(
            self, mw.sender, 'Exadel Account 1', 'First message have wrong sender', 'Check - Sender is correct:')

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, move_to_name_1, 'First message have wrong subject',
            'Check - Subject is correct')

        Check.assert_in_xpath_text(
            self, mw.date_in_first_message, 'Today at', 'First message have wrong date', 'Check - Date is correct:')

        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")

        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)

        mgd.find_element_by_xpath(mw.from_sorting).click()
        time.sleep(2)

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_from_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')

        Check.assert_in_xpath_class(
            self, mw.sorting_from_arrow_icon, 'awesome-icon_long_arrow_up', 'Sorting icon arrow not up',
            'Check - Sorting icon arrow is up')

        Check.assert_in_class_name_text(
            self, mw.sender, 'User Zero', 'First message have wrong sender', 'Check - Sender is correct:')

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, 'RE: test 4', 'First message have wrong subject',
            'Check - Subject is correct')

        Check.assert_in_xpath_text(
            self, mw.date_in_first_message, 'Apr 22 2016', 'First message have wrong date', 'Check - Date is correct:')

    # @unittest.skip('ok')
    def test_sort_importance_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox')

        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_in_xpath_class(
            self, mw.sorting_dropdawn_list, 'opened', 'Sorting drop down list not found',
            'Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.importance_sorting).click()
        time.sleep(1)

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_importance_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, Check.flag_in_n_message('1'), 'flag-red', 'The first message does not have an important flag',
            'Check - The first message have an important flag')

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, flag_name_1, 'First message have wrong subject',
            'Check - Subject is correct')

        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')

        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.importance_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_in_xpath_class(
            self, mw.sorting_importance_arrow_icon, 'awesome-icon_long_arrow_up', 'Sorting icon arrow not up',
            'Check - Sorting icon arrow is up')
        time.sleep(2)

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, move_to_name_1, 'First message have wrong subject',
            'Check - Subject is correct')

        Check.assert_not_in_xpath_class(
            self, mw.flag_in_1th_message, 'flag-red', 'The first message have an important flag',
            'Check - The first message does not have an important flag')

    # @unittest.skip('ok')
    def test_sort_subject_inbox(self):
        mgd.find_element_by_xpath(mw.inbox_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
            'Check - Selected folder is inbox')

        mgd.find_element_by_id(mw.small_sorting_button).click()

        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.subject_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_subject_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')

        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_subject_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')

        sorting_subject_f = mgd.find_element_by_xpath(mw.subject_with_no_subject).text
        self.assertIn("(no subject)", sorting_subject_f, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_f)

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')

        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.subject_sorting).click()
        time.sleep(1)

        mgd.find_element_by_id(mw.small_sorting_button).click()

        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_subject_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        time.sleep(1)

        sorting_subject_s = mgd.find_element_by_xpath(mw.subject_in_1th_message).text
        self.assertIn("Laptop Week Price Alert:", sorting_subject_s, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_s)


@unittest.skip('ERRORS')
class Test7SortingSentItemsMail(unittest.TestCase):
    def setUp(self):
        driver_instance.implicitly_wait(2)
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

        if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
            pass
        else:
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()

        time.sleep(1)
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        if len(Maw.get_devices().find_elements_by_xpath(mw.sorting_date_arrow_icon)) <= 0:
            mgd.find_element_by_xpath(mw.date_sorting).click()
            mgd.find_element_by_id(mw.small_sorting_button).click()
            time.sleep(1)
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon_f:
            mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()

    def tearDown(self):
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        if len(Maw.get_devices().find_elements_by_xpath(mw.sorting_date_arrow_icon)) <= 0:
            mgd.find_element_by_xpath(mw.date_sorting).click()
            mgd.find_element_by_id(mw.small_sorting_button).click()
            time.sleep(1)
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon_f:
            mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()

    # @unittest.skip('ok')
    def test_sort_date_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)
        sent_items_selected_folder = mgd.find_element_by_xpath(
            mw.sent_items_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', sent_items_selected_folder, 'Wrong selected folder (not sent items)')
        print('Check - Selected folder is sent items')

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_in_xpath_class(
            self, mw.sorting_dropdawn_list, 'opened', 'Sorting drop down list not found',
            'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_date_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        Check.assert_in_xpath_class(
            self, mw.sorting_date_arrow_icon, 'awesome-icon_long_arrow_down', 'Sorting icon arrow not down',
            'Check - Sorting icon arrow is down')
        Check.assert_in_xpath_text(
            self, mw.date_in_first_message, 'Today at', 'First message have wrong date', 'Check - Date is correct:')

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, move_to_name_2, 'First message have wrong subject',
            'Check - Subject is correct')

        mgd.find_element_by_xpath(mw.date_sorting).click()
        time.sleep(2)

        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_date_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        time.sleep(1)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Feb 19 2016', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)
        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, 'Test s', 'First message have wrong subject',
            'Check - Subject is correct')

    # @unittest.skip('ok')
    def test_sort_from_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)
        sent_items_selected_folder = mgd.find_element_by_xpath(
            mw.sent_items_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', sent_items_selected_folder, 'Wrong selected folder (not sent items)')
        print('Check - Selected folder is sent items')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.from_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_from_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_from_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')
        sender_in_first_message_f = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Exadel Account 1', sender_in_first_message_f, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_f)
        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)
        sorting_subject_f = mgd.find_element_by_xpath(mw.subject_in_1th_message).text
        self.assertIn(move_to_name_2, sorting_subject_f, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_f)
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        mgd.find_element_by_xpath(mw.from_sorting).click()
        time.sleep(2)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_from_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_from_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        sender_in_first_message_s = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Exadel Account 1', sender_in_first_message_s, 'First message have wrong date')
        print('Check - Sender is correct: ', sender_in_first_message_s)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Aug 09', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct:', date_in_first_message_s)
        sorting_subject_s = mgd.find_element_by_xpath(mw.subject_in_1th_message).text
        self.assertIn("Declined: New Event", sorting_subject_s, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_s)

    # @unittest.skip('ok')
    def test_sort_importance_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)
        sent_items_selected_folder = mgd.find_element_by_xpath(
            mw.sent_items_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', sent_items_selected_folder, 'Wrong selected folder (not sent items)')
        print('Check - Selected folder is sent items')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.importance_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_importance_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_importance_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')
        time.sleep(1)
        sorting_flag_f = mgd.find_element_by_xpath(mw.flag_in_1th_message).get_attribute(name="class")
        self.assertIn('flag-red', sorting_flag_f, 'The first message does not have an important flag')
        print('Check - The first message have an important flag')
        sender_in_first_message_f = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Exadel Account 1', sender_in_first_message_f, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_f)
        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)
        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, flag_name_2, 'First message have wrong subject',
            'Check - Subject is correct')
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.importance_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_importance_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        sorting_flag_s = mgd.find_element_by_xpath(mw.flag_in_1th_message).get_attribute(name="class")
        self.assertNotIn('flag-red', sorting_flag_s, 'The first message have an important flag')
        print('Check - The first message does not have an important flag')
        sender_in_first_message_s = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Exadel Account 1', sender_in_first_message_s, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_s)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)
        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, move_to_name_2, 'First message have wrong subject',
            'Check - Subject is correct')

    # @unittest.skip('ok')
    def test_sort_subject_sent_items(self):
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)
        sent_items_selected_folder = mgd.find_element_by_xpath(
            mw.sent_items_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', sent_items_selected_folder, 'Wrong selected folder (not sent items)')
        print('Check - Selected folder is sent items')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.subject_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_subject_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_subject_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')
        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Apr 24 at', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)
        sorting_subject_f = mgd.find_element_by_xpath(mw.subject_with_no_subject).text
        self.assertIn("(no subject)", sorting_subject_f, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_f)
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.subject_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_subject_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        time.sleep(1)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Jul 19 ', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)
        sorting_subject_s = mgd.find_element_by_xpath(mw.subject_in_1th_message).text
        self.assertIn("yy", sorting_subject_s, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_s)


@unittest.skip('NEED FIX')
class Test7SortingDeletedItemsMail(unittest.TestCase):
    def setUp(self):
        driver_instance.implicitly_wait(2)
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

        if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
            pass
        else:
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()

        time.sleep(1)
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        if len(Maw.get_devices().find_elements_by_xpath(mw.sorting_date_arrow_icon)) <= 0:
            mgd.find_element_by_xpath(mw.date_sorting).click()
            mgd.find_element_by_id(mw.small_sorting_button).click()
            time.sleep(1)
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon_f:
            mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()

    def tearDown(self):
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        if len(Maw.get_devices().find_elements_by_xpath(mw.sorting_date_arrow_icon)) <= 0:
            mgd.find_element_by_xpath(mw.date_sorting).click()
            mgd.find_element_by_id(mw.small_sorting_button).click()
            time.sleep(1)
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon_f:
            mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()

    # @unittest.skip('ok')
    def test_sort_date_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)
        deleted_items_selected_folder = mgd.find_element_by_xpath(
            mw.deleted_items_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', deleted_items_selected_folder, 'Wrong selected folder (not deleted items)')
        print('Check - Selected folder is deleted items')
        time.sleep(2)

        mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(2)

        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')

        Check.assert_equal_xpath(
            self, mw.sorting_date_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')

        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)
        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, move_to_name_3, 'First message have wrong subject',
            'Check - Subject is correct')

        mgd.find_element_by_xpath(mw.date_sorting).click()
        time.sleep(2)
        mgd.find_element_by_id(mw.small_sorting_button).click()

        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_date_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')

        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, move_to_name_2, 'First message have wrong subject',
            'Check - Subject is correct')

        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Apr 09 2014', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)

    # @unittest.skip('ok')
    def test_sort_from_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)
        deleted_items_selected_folder = mgd.find_element_by_xpath(
            mw.deleted_items_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', deleted_items_selected_folder, 'Wrong selected folder (not deleted items)')
        print('Check - Selected folder is deleted items')

        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.from_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_from_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_from_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')
        time.sleep(1)

        sender_in_first_message_f = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Draft', sender_in_first_message_f, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_f)

        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at ', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)

        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        mgd.find_element_by_xpath(mw.from_sorting).click()
        time.sleep(2)

        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_from_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_from_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        time.sleep(2)

        sender_in_first_message_s = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('provision@e-dapt.net', sender_in_first_message_s, 'First message have wrong date')
        print('Check - Sender is correct: ', sender_in_first_message_s)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('May 05 2016', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct:', date_in_first_message_s)

    # @unittest.skip('ok')
    def test_sort_importance_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)
        deleted_items_selected_folder = mgd.find_element_by_xpath(
            mw.deleted_items_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', deleted_items_selected_folder, 'Wrong selected folder (not deleted items)')
        print('Check - Selected folder is deleted items')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.importance_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_importance_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')

        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_importance_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')

        sorting_flag_f = mgd.find_element_by_xpath(mw.flag_in_1th_message).get_attribute(name="class")
        self.assertIn('flag-red', sorting_flag_f, 'The first message does not have an important flag')
        print('Check - The first message have an important flag')

        sender_in_first_message_f = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Exadel Account 1', sender_in_first_message_f, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_f)

        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at ', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, flag_name_3, 'First message have wrong subject',
            'Check - Subject is correct')

        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')

        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.importance_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_importance_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')

        sorting_flag_s = mgd.find_element_by_xpath(mw.flag_in_1th_message).get_attribute(name="class")
        self.assertNotIn('flag-red', sorting_flag_s, 'The first message have an important flag')
        print('Check - The first message does not have an important flag')

        sender_in_first_message_s = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Exadel Account 1', sender_in_first_message_s, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_s)

        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)

        Check.assert_in_xpath_text(
            self, mw.subject_in_1th_message, move_to_name_3, 'First message have wrong subject',
            'Check - Subject is correct')

    # @unittest.skip('ok')
    def test_sort_subject_deleted_items(self):
        mgd.find_element_by_xpath(mw.deleted_items_folder).click()
        time.sleep(1)
        deleted_items_selected_folder = mgd.find_element_by_xpath(
            mw.deleted_items_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', deleted_items_selected_folder, 'Wrong selected folder (not deleted items)')
        print('Check - Selected folder is deleted items')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.subject_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_subject_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_subject_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')

        sorting_subject_f = mgd.find_element_by_xpath(mw.subject_with_no_subject).text
        self.assertIn("(no subject)", sorting_subject_f, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_f)

        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)

        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.subject_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_subject_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        time.sleep(1)

        sorting_subject_s = mgd.find_element_by_xpath(mw.subject_in_1th_message).text
        self.assertIn("Zse", sorting_subject_s, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_s)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Dec 07', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)


@unittest.skip('NEED FIX ALL')
class Test7SortingDraftsMail(unittest.TestCase):
    def setUp(self):
        driver_instance.implicitly_wait(2)
        main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
        if main_checkbox == 'icon-icon_checked checkbox-custom':
            mgd.find_element_by_xpath(mw.main_checkbox).click()

        if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
            pass
        else:
            if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
                mgd.find_element_by_id(mw.small_search_button).click()
            else:
                mgd.find_element_by_class_name(mw.close_icon).click()
                time.sleep(1)
                mgd.find_element_by_id(mw.small_search_button).click()

        time.sleep(2)
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon_f:
            mgd.find_element_by_xpath(mw.date_sorting).click()

    def tearDown(self):
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(2)
        mgd.find_element_by_xpath(mw.date_sorting).click()
        mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        time.sleep(1)
        if 'awesome-icon_long_arrow_down' not in sorting_arrow_icon_f:
            mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()

    # @unittest.skip('ok')
    def test_sort_date_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)
        drafts_selected_folder = mgd.find_element_by_xpath(mw.drafts_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', drafts_selected_folder, 'Wrong selected folder (not drafts)')
        print('Check - Selected folder is drafts')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_date_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')
        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)
        mgd.find_element_by_xpath(mw.date_sorting).click()
        time.sleep(2)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_date_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Nov 27', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)

    # @unittest.skip('ok')
    def test_sort_from_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)
        drafts_selected_folder = mgd.find_element_by_xpath(mw.drafts_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', drafts_selected_folder, 'Wrong selected folder (not drafts)')
        print('Check - Selected folder is drafts')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.from_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_from_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_from_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')
        sender_in_first_message_f = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Draft', sender_in_first_message_f, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_f)
        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        if 'opened' not in sorting_dropdawn_list:
            mgd.find_element_by_id(mw.small_sorting_button).click()
        time.sleep(1)
        mgd.find_element_by_xpath(mw.from_sorting).click()
        time.sleep(2)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_from_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_from_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        sender_in_first_message_s = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Exadel Account 1', sender_in_first_message_s, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_s)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at ', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct:', date_in_first_message_s)

    # @unittest.skip('ok')
    def test_sort_importance_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)
        drafts_selected_folder = mgd.find_element_by_xpath(mw.drafts_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', drafts_selected_folder, 'Wrong selected folder (not drafts)')
        print('Check - Selected folder is drafts')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.importance_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_importance_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_importance_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')
        sorting_flag_f = mgd.find_element_by_xpath(mw.flag_in_1th_message).get_attribute(name="class")
        self.assertIn('flag-red', sorting_flag_f, 'The first message does not have an important flag')
        print('Check - The first message have an important flag')
        sender_in_first_message_f = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Draft', sender_in_first_message_f, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_f)
        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Dec 22', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.importance_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_importance_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        time.sleep(1)
        sorting_flag_s = mgd.find_element_by_xpath(mw.flag_in_1th_message).get_attribute(name="class")
        self.assertNotIn('flag-red', sorting_flag_s, 'The first message have an important flag')
        print('Check - The first message does not have an important flag')
        sender_in_first_message_s = mgd.find_element_by_class_name(mw.sender).text
        self.assertIn('Draft', sender_in_first_message_s, 'First message have wrong sender')
        print('Check - Sender is correct: ', sender_in_first_message_s)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)

    # @unittest.skip('ok')
    def test_sort_subject_drafts(self):
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)
        drafts_selected_folder = mgd.find_element_by_xpath(mw.drafts_selected_folder).get_attribute(name="class")
        self.assertIn('selected-folder', drafts_selected_folder, 'Wrong selected folder (not drafts)')
        print('Check - Selected folder is drafts')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_dropdawn_list = mgd.find_element_by_xpath(mw.sorting_dropdawn_list).get_attribute(name="class")
        self.assertIn('opened', sorting_dropdawn_list, 'Sorting drop down list not found')
        print('Check - Sorting drop down list')
        time.sleep(1)

        mgd.find_element_by_xpath(mw.subject_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        Check.assert_equal_xpath(
            self, mw.sorting_subject_arrow_icon, 1, 'Sorting icon arrow not exist', 'Check - Sorting icon arrow')
        sorting_arrow_icon_f = mgd.find_element_by_xpath(mw.sorting_subject_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_down', sorting_arrow_icon_f, 'Sorting icon arrow not down')
        print('Check - Sorting icon arrow is down')
        sorting_subject_f = mgd.find_element_by_xpath(mw.subject_with_no_subject).text
        self.assertIn("(no subject)", sorting_subject_f, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_f)
        date_in_first_message_f = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Today at', date_in_first_message_f, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_f)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        Check.assert_equal_xpath(
            self, mw.sorting_dropdawn_list, 1, 'Sorting drop down list not found', 'Check - Sorting drop down list')
        mgd.find_element_by_id(mw.small_sorting_button).click()
        mgd.find_element_by_xpath(mw.subject_sorting).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.small_sorting_button).click()
        sorting_arrow_icon_s = mgd.find_element_by_xpath(mw.sorting_subject_arrow_icon).get_attribute(name="class")
        self.assertIn('awesome-icon_long_arrow_up', sorting_arrow_icon_s, 'Sorting icon arrow not up')
        print('Check - Sorting icon arrow is up')
        time.sleep(1)
        sorting_subject_s = mgd.find_element_by_xpath(mw.subject_in_1th_message).text
        self.assertIn("Zse", sorting_subject_s, 'The first message contains an incorrect topic')
        print('Check - Subject is correct: ', sorting_subject_s)
        date_in_first_message_s = mgd.find_element_by_xpath(mw.date_in_first_message).text
        self.assertIn('Dec 07', date_in_first_message_s, 'First message have wrong date')
        print('Check - Date is correct: ', date_in_first_message_s)
