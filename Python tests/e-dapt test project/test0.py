import time
from datetime import datetime
import unittest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import Check
import Config
from main_app_window import Maw, driver_instance

# config shortcut

mgd = Maw.get_devices()
ed = Config.Mail.email_details.Elements
mw = Config.Mail.main_window.Elements
ne = Config.Mail.new_email.Elements
driver_instance.implicitly_wait(5)
wait = WebDriverWait(mgd, 5)

words_for_search = 'test message for'

# time.sleep(1)
# driver_winium = winium.driver_winium
# window = driver_winium.find_element_by_name("AppBus")
# top_menu = window.find_element_by_id('TopMenuGroup')
# mail_folder = top_menu.find_element_by_name('Mail')
# calendar_folder = top_menu.find_element_by_name('Calendar')
# contacts_folder = top_menu.find_element_by_name('Contacts')
# action = ActionChains
# action.move_to_element(mail_folder)
# action.move_to_element(calendar_folder)
# action.move_to_element(contacts_folder)



# # @unittest.skip('Ok')
# class Test6Delete(unittest.TestCase):
#     def setUp(self):
#         main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
#         if main_checkbox == 'icon-icon_checked checkbox-custom':
#             mgd.find_element_by_xpath(mw.main_checkbox).click()
#
#         if 'display: none;' in mgd.find_element_by_class_name(mw.visibility_of_search).get_attribute(name="style"):
#             pass
#         else:
#             if mgd.find_element_by_id(mw.message_search_input).get_attribute(name="value") is '':
#                 mgd.find_element_by_id(mw.small_search_button).click()
#             else:
#                 mgd.find_element_by_class_name(mw.close_icon).click()
#                 time.sleep(1)
#                 mgd.find_element_by_id(mw.small_search_button).click()
#
#     def tearDown(self):
#         pass

    # # @unittest.skip('Ok')
    # def test1_mass_delete_from_inbox(self):
    #     mgd.find_element_by_xpath(mw.inbox_folder).click()
    #     time.sleep(1)
    #
    #     Check.assert_in_xpath_class(
    #         self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
    #         'Check - Selected folder is inbox -')
    #     time.sleep(1)
    #
    #     mgd.find_element_by_id(mw.small_search_button).click()
    #
    #     search_word = words_for_search
    #
    #     Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
    #     mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
    #     Check.assert_in_id_value(
    #         self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
    #     time.sleep(1)
    #
    #     main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
    #     if main_checkbox == 'icon-icon_checked checkbox-custom':
    #         pass
    #     else:
    #         mgd.find_element_by_xpath(mw.main_checkbox).click()
    #     print('Check - Main checkbox clicked')
    #     #######################
    #     topic_elements = mgd.find_elements_by_class_name(mw.topic)
    #     choose_elements = []
    #     for elem in topic_elements:
    #         if elem.get_attribute('innerText') == delete_name_1:
    #             choose_elements.append(topic_elements.index(elem) + 1)
    #         if elem.get_attribute('innerText') == flag_name_1:
    #             choose_elements.append(topic_elements.index(elem) + 1)
    #         if elem.get_attribute('innerText') == move_to_name_1:
    #             choose_elements.append(topic_elements.index(elem) + 1)
    #
    #     for index in choose_elements:
    #         if 'Today at 'in mgd.find_element_by_xpath(
    #                                 '//*[@id="list"]/li[' + str(index) + ']/div[4]').get_attribute('innerText'):
    #             Check.checkbox_in_n_message_click(index)
    #             Check.assert_not_in_class_attr_message_in_n_row(
    #                 self, index, 'checked-message', 'Message is checked', 'Check - message is not checked - ')
    #     time.sleep(2)
    #
    #     main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
    #     if main_checkbox == 'icon-icon_checked checkbox-custom':
    #
    #         mgd.find_element_by_id(mw.small_delete_button).click()
    #         time.sleep(1)
    #         Check.check_exists_by_class_name(mw.block_wrapper)
    #         print('Check - block wrapper exist')
    #         Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
    #         print('Check - Cancel button')
    #         time.sleep(1)
    #         mgd.find_element_by_id(mw.small_delete_button).click()
    #         time.sleep(1)
    #         Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
    #         print('Check - Ok button')
    #
    # # @unittest.skip('Ok')
    # def test1_mass_delete_from_sent_items(self):
    #     mgd.find_element_by_xpath(mw.sent_items_folder).click()
    #     time.sleep(1)
    #
    #     Check.assert_in_xpath_class(
    #         self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
    #         'Check - Selected folder is sent items -')
    #     time.sleep(1)
    #
    #     mgd.find_element_by_id(mw.small_search_button).click()
    #
    #     search_word = words_for_search
    #
    #     Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
    #     mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
    #     Check.assert_in_id_value(
    #         self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
    #     time.sleep(2)
    #
    #     #######################
    #     len_of_list = len(mgd.find_elements_by_class_name(mw.row))
    #     print(len_of_list)
    #     when_stop = 1
    #     while when_stop < 4:
    #         index_row = 1
    #         while index_row < 9:
    #             len_of_list = len(mgd.find_elements_by_class_name(mw.row))
    #             print(len_of_list)
    #
    #             if index_row > len_of_list:
    #                 break
    #             message_in_row = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute('innerText')
    #             # for elem in save_message:
    #             if delete_name_2 in message_in_row:
    #                 a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
    #                 b = a.get_attribute('innerText')
    #                 if 'Today at ' in b:
    #                     pass
    #                 else:
    #                     Check.checkbox_in_n_message_click(index_row)
    #
    #             elif flag_name_2 in message_in_row:
    #                 a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
    #                 b = a.get_attribute('innerText')
    #                 if 'Today at ' in b:
    #                     if 'unread-message' in mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(name="class"):
    #                         pass
    #                     else:
    #                         Check.checkbox_in_n_message_click(index_row)
    #                 else:
    #                     Check.checkbox_in_n_message_click(index_row)
    #
    #             elif move_to_name_2 in message_in_row:
    #                 a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
    #                 b = a.get_attribute('innerText')
    #                 if 'Today at ' in b:
    #                     if 'unread-message' in mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']').get_attribute(name="class"):
    #                         pass
    #                     else:
    #                         Check.checkbox_in_n_message_click(index_row)
    #                 else:
    #                     Check.checkbox_in_n_message_click(index_row)
    #
    #             else:
    #                 Check.checkbox_in_n_message_click(index_row)
    #             index_row += 1
    #
    #         if mgd.find_element_by_id(mw.small_delete_button).is_displayed():
    #             mgd.find_element_by_id(mw.small_delete_button).click()
    #             print('Check - small delete button')
    #             time.sleep(1)
    #             Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
    #             print('Check - Ok button')
    #         time.sleep(2)
    #         if len(mgd.find_elements_by_class_name(mw.row)) <= 3:
    #             when_stop = 5
    #
    #     #######################
    #     # topic_elements = mgd.find_elements_by_class_name(mw.topic)
    #     # choose_elements = []
    #     # for elem in topic_elements:
    #     #     if elem.get_attribute('innerText') == delete_name_2:
    #     #         choose_elements.append(topic_elements.index(elem) + 1)
    #     #     if elem.get_attribute('innerText') == flag_name_2:
    #     #         choose_elements.append(topic_elements.index(elem) + 1)
    #     #     if elem.get_attribute('innerText') == move_to_name_2:
    #     #         choose_elements.append(topic_elements.index(elem) + 1)
    #     #
    #     # for index in choose_elements:
    #     #     if 'Today at 'in mgd.find_element_by_xpath(
    #     #                             '//*[@id="list"]/li[' + str(index) + ']/div[4]').get_attribute('innerText'):
    #     #         Check.checkbox_in_n_message_click(index)
    #     #         Check.assert_not_in_class_attr_message_in_n_row(
    #     #             self, index, 'checked-message', 'Message is checked', 'Check - message is not checked - ')
    #     #         time.sleep(1)
    #     # time.sleep(2)
    #     #
    #     # mgd.find_element_by_id(mw.small_delete_button).click()
    #     # time.sleep(1)
    #     # Check.check_exists_by_class_name(mw.block_wrapper)
    #     # print('Check - block wrapper exist')
    #     # Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
    #     # print('Check - Cancel button')
    #     # time.sleep(1)
    #     # while len(mgd.find_elements_by_class_name(mw.row)) >= 11:
    #     #     mgd.find_element_by_id(mw.small_delete_button).click()
    #     #     time.sleep(1)
    #     #     Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
    #     #     print('Check - Ok button')
    #     #     time.sleep(1)
    #
    # # @unittest.skip('Ok')
    # def test1_mass_delete_from_junk_emails(self):
    #     mgd.find_element_by_xpath(mw.junk_email_folder).click()
    #     time.sleep(1)
    #
    #     Check.assert_in_xpath_class(
    #         self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk e-mail)',
    #         'Check - Selected folder is junk e-mail -')
    #     time.sleep(1)
    #
    #     mgd.find_element_by_id(mw.small_search_button).click()
    #
    #     search_word = words_for_search
    #
    #     Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
    #     mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
    #     Check.assert_in_id_value(
    #         self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
    #     time.sleep(1)
    #
    #     main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
    #     if main_checkbox == 'icon-icon_checked checkbox-custom':
    #         pass
    #     else:
    #         mgd.find_element_by_xpath(mw.main_checkbox).click()
    #     print('Check - Main checkbox clicked')
    #     #######################
    #     topic_elements = mgd.find_elements_by_class_name(mw.topic)
    #     choose_elements = []
    #     for elem in topic_elements:
    #         if elem.get_attribute('innerText') == delete_name_3:
    #             choose_elements.append(topic_elements.index(elem) + 1)
    #         if elem.get_attribute('innerText') == flag_name_4:
    #             choose_elements.append(topic_elements.index(elem) + 1)
    #         if elem.get_attribute('innerText') == move_to_name_4:
    #             choose_elements.append(topic_elements.index(elem) + 1)
    #
    #     for index in choose_elements:
    #         if 'Today at ' in mgd.find_element_by_xpath(
    #                                 '//*[@id="list"]/li[' + str(index) + ']/div[4]').get_attribute('innerText'):
    #             Check.checkbox_in_n_message_click(index)
    #             Check.assert_not_in_class_attr_message_in_n_row(
    #                 self, index, 'checked-message', 'Message is checked', 'Check - message is not checked - ')
    #     time.sleep(2)
    #
    #     main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
    #     if main_checkbox == 'icon-icon_checked checkbox-custom':
    #
    #         mgd.find_element_by_id(mw.small_delete_button).click()
    #         time.sleep(1)
    #         Check.check_exists_by_class_name(mw.block_wrapper)
    #         print('Check - block wrapper exist')
    #         Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
    #         print('Check - Cancel button')
    #         time.sleep(1)
    #         mgd.find_element_by_id(mw.small_delete_button).click()
    #         time.sleep(1)
    #         Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
    #         print('Check - Ok button')
    #
    # # @unittest.skip('Ok')
    # def test1_mass_delete_from_drafts(self):
    #     mgd.find_element_by_xpath(mw.drafts_folder).click()
    #     time.sleep(1)
    #
    #     Check.assert_in_xpath_class(
    #         self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
    #         'Check - Selected folder is drafts -')
    #     time.sleep(1)
    #
    #     mgd.find_element_by_id(mw.small_search_button).click()
    #
    #     search_word = words_for_search
    #
    #     Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
    #     mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
    #     Check.assert_in_id_value(
    #         self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
    #     time.sleep(1)
    #
    #     main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
    #     if main_checkbox == 'icon-icon_checked checkbox-custom':
    #         pass
    #     else:
    #         mgd.find_element_by_xpath(mw.main_checkbox).click()
    #     print('Check - Main checkbox clicked')
    #     #######################
    #     topic_elements = mgd.find_elements_by_class_name(mw.topic)
    #     choose_elements = []
    #     for elem in topic_elements:
    #         if elem.get_attribute('innerText') == draft_name_1:
    #             choose_elements.append(topic_elements.index(elem) + 1)
    #         if elem.get_attribute('innerText') == draft_name_2:
    #             choose_elements.append(topic_elements.index(elem) + 1)
    #
    #     for index in choose_elements:
    #         if 'Today at ' in mgd.find_element_by_xpath(
    #                                 '//*[@id="list"]/li[' + str(index) + ']/div[4]').get_attribute('innerText'):
    #             Check.checkbox_in_n_message_click(index)
    #             Check.assert_not_in_class_attr_message_in_n_row(
    #                 self, index, 'checked-message', 'Message is checked', 'Check - message is not checked - ')
    #     time.sleep(2)
    #
    #     main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
    #     if main_checkbox == 'icon-icon_checked checkbox-custom':
    #
    #         mgd.find_element_by_id(mw.small_delete_button).click()
    #         time.sleep(1)
    #         Check.check_exists_by_class_name(mw.block_wrapper_header)
    #         print('Check - block wrapper exist')
    #         Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Cancel').click()
    #         print('Check - Cancel button')
    #         time.sleep(1)
    #         mgd.find_element_by_id(mw.small_delete_button).click()
    #         time.sleep(1)
    #         Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
    #         print('Check - Ok button')
    #
    # # @unittest.skip('Ok')
    # def test2_mass_delete_from_deleted_items(self):
    #     mgd.find_element_by_xpath(mw.deleted_items_folder).click()
    #     time.sleep(1)
    #
    #     Check.assert_in_xpath_class(
    #         self, mw.deleted_items_selected_folder, 'selected-folder', 'Wrong selected folder (not deleted items)',
    #         'Check - Selected folder is deleted items -')
    #     time.sleep(1)
    #
    #     mgd.find_element_by_id(mw.small_search_button).click()
    #
    #     search_word = words_for_search
    #
    #     Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
    #     mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
    #     Check.assert_in_id_value(
    #         self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
    #     time.sleep(1)
    #
    #     #######################

    # def test2_mass_delete(self):
    #     mgd.find_element_by_id(mw.small_search_button).click()
    #
    #     search_word = words_for_search
    #
    #     Check.assert_equal_id(self, mw.message_search_input, 1, 'Search input not found', 'Check - Search input')
    #     mgd.find_element_by_id(mw.message_search_input).send_keys(search_word)
    #     Check.assert_in_id_value(
    #         self, mw.message_search_input, search_word, 'input is different', 'Check - input is correct')
    #     time.sleep(1)
    #
    #     folder_index = 1
    #     while folder_index < 6:
    #         if folder_index == 1:
    #             mgd.find_element_by_xpath(mw.inbox_folder).click()
    #             time.sleep(1)
    #             Check.assert_in_xpath_class(
    #                 self, mw.inbox_selected_folder, 'selected-folder', 'Wrong selected folder (not inbox)',
    #                 'Check - Selected folder is inbox -')
    #             time.sleep(1)
    #             if Check.check_exists_by_class_name(mw.norecords) > 0:
    #                 folder_index += 1
    #                 continue
    #         elif folder_index == 2:
    #             mgd.find_element_by_xpath(mw.sent_items_folder).click()
    #             time.sleep(1)
    #             Check.assert_in_xpath_class(
    #                 self, mw.sent_items_selected_folder, 'selected-folder', 'Wrong selected folder (not sent items)',
    #                 'Check - Selected folder is sent items -')
    #             time.sleep(1)
    #             if Check.check_exists_by_class_name(mw.norecords) > 0:
    #                 folder_index += 1
    #                 continue
    #
    #         elif folder_index == 3:
    #             mgd.find_element_by_xpath(mw.junk_email_folder).click()
    #             time.sleep(1)
    #             Check.assert_in_xpath_class(
    #                 self, mw.junk_email_selected_folder, 'selected-folder', 'Wrong selected folder (not junk e-mail)',
    #                 'Check - Selected folder is junk e-mail -')
    #             time.sleep(1)
    #             if Check.check_exists_by_class_name(mw.norecords) > 0:
    #                 folder_index += 1
    #                 continue
    #
    #         elif folder_index == 4:
    #             mgd.find_element_by_xpath(mw.drafts_folder).click()
    #             time.sleep(1)
    #             Check.assert_in_xpath_class(
    #                 self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
    #                 'Check - Selected folder is drafts -')
    #             time.sleep(1)
    #             if Check.check_exists_by_class_name(mw.norecords) > 0:
    #                 folder_index += 1
    #                 continue
    #
    #         elif folder_index == 5:
    #             mgd.find_element_by_xpath(mw.deleted_items_folder).click()
    #             time.sleep(1)
    #             Check.assert_in_xpath_class(
    #                 self, mw.deleted_items_selected_folder, 'selected-folder',
    #                 'Wrong selected folder (not deleted items)',
    #                 'Check - Selected folder is deleted items -')
    #             time.sleep(1)
    #             if Check.check_exists_by_class_name(mw.norecords) > 0:
    #                 folder_index += 1
    #                 continue
    #
    #         len_of_list = len(mgd.find_elements_by_class_name(mw.row))
    #         print(len_of_list)
    #         when_stop = 1
    #         while when_stop < 5:
    #             index_row = 1
    #             while index_row < 9:
    #                 time.sleep(1)
    #                 len_of_list = len(mgd.find_elements_by_class_name(mw.row))
    #                 print(len_of_list)
    #
    #                 if index_row > len_of_list:
    #                     break
    #
    #                 a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(index_row) + ']/div[4]')
    #                 b = a.get_attribute('innerText')
    #                 if 'Today at ' in b:
    #                     Check.checkbox_in_n_message_click(index_row)
    #                 else:
    #                     print('9876543')
    #                 # else:
    #                 #     print('12345678')
    #                 index_row += 1
    #             main_checkbox = mgd.find_element_by_xpath(mw.main_checkbox).get_attribute(name='class')
    #             if main_checkbox == 'icon-icon_checked checkbox-custom':
    #                 mgd.find_element_by_id(mw.small_delete_button).click()
    #                 time.sleep(1)
    #                 Check.find_element_by_class_name_and_text(ne.wrapper_close, 'OK').click()
    #                 print('Check - Ok button')
    #             time.sleep(4)
    #             print(len(mgd.find_elements_by_class_name(mw.row)))
    #             if len(mgd.find_elements_by_class_name(mw.row)) == 0:
    #                 when_stop = 5
    #             else:
    #                 when_stop += 1
    #         folder_index += 1
