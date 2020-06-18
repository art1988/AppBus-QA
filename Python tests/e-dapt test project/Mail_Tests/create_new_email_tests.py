import time
import unittest
from datetime import datetime
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
wait = WebDriverWait(mgd, 10)


def setUpModule():
    print('Start: create_new_email_tests.py\n')


def tearDownModule():
    print('End: create_new_email_tests.py\n')
    # driver_instance.quit()


# @unittest.skip('ok')
class Test3CreateNewEmail(unittest.TestCase):
    def setUp(self):
        time.sleep(1)
        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)

    def tearDown(self):
        time.sleep(2)
        if Check.check_exists_by_class_name(ed.email_message_show):
            print('Details of the email are open (TestCreateNewEmail)')
            mgd.find_element_by_class_name(ed.back_button).click()
        if Check.check_exists_by_id(ne.block_wrapper_header):
            block_wrapper = mgd.find_element_by_id(ne.block_wrapper_header)
            if block_wrapper.is_displayed():
                print('Alert block - exist (TestCreateNewEmail)')
                mgd.find_element_by_class_name(ne.wrapper_close).click()
        if Check.check_exists_by_id(ne.new_email):
            print("New email window - exist (TestCreateNewEmail)")
            mgd.find_element_by_id(ne.close_email_button).click()
            time.sleep(1)
            if Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper):
                print("Block wrapper - exist (TestCreateNewEmail)")
                Check.find_element_by_class_name_and_text(ne.close_editor_confirmation_button, 'Delete Draft').click()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        driver = Maw.get_driver()
        driver.switch_to.default_content()
        time.sleep(2)
        if Check.check_exists_by_class_name(ed.email_message_show):
            print('Details of the email are open (TestCreateNewEmail)')
            mgd.find_element_by_class_name(ed.back_button).click()
        if Check.check_exists_by_id(ne.block_wrapper_header):
            block_wrapper = mgd.find_element_by_id(ne.block_wrapper_header)
            if block_wrapper.is_displayed():
                print('Alert block - exist (TestCreateNewEmail)')
                mgd.find_element_by_class_name(ne.wrapper_close).click()
        if Check.check_exists_by_id(ne.new_email):
            print("New email window - exist (TestCreateNewEmail)")
            mgd.find_element_by_id(ne.close_email_button).click()
            time.sleep(1)
            if Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper):
                print("Block wrapper - exist (TestCreateNewEmail)")
                Check.find_element_by_class_name_and_text(ne.close_editor_confirmation_button, 'Delete Draft').click()

    # @unittest.skip("ok")
    def test_email_send_full(self):

        mgd.find_element_by_id(ne.to_field_input).send_keys("example")
        time.sleep(1)
        Check.assert_equal_xpath(
            self, ne.to_autocomplete_dropdown_item_1, 1, "Autocomplete 'To' not found", "Check - Autocomplete 'To'")
        drop_down_to_click = mgd.find_element_by_xpath(ne.to_autocomplete_dropdown_item_1)
        time.sleep(1)
        drop_down_to_click.click()
        time.sleep(1)
        mgd.find_element_by_id(ne.cc_field_input).send_keys("barb@ty.ty")
        time.sleep(1)
        Check.assert_equal_xpath(
            self, ne.cc_autocomplete_dropdown_item_1, 1, "Autocomplete 'Cc' not found", "Check - Autocomplete 'Cc'")
        time.sleep(1)
        drop_down_cc_click = mgd.find_element_by_xpath(ne.cc_autocomplete_dropdown_item_1)
        time.sleep(1)
        drop_down_cc_click.click()
        time.sleep(1)
        mgd.find_element_by_id(ne.bcc_field_input).send_keys("exadel1@botf03.net")
        time.sleep(1)
        Check.assert_equal_xpath(
            self, ne.to_autocomplete_dropdown_item_1, 1, "Autocomplete 'Bcc' not found", "Check - Autocomplete 'Bcc'")
        time.sleep(1)
        drop_down_bcc_click = mgd.find_element_by_xpath(ne.bcc_autocomplete_dropdown_item_1)
        drop_down_bcc_click.click()
        time_for_subj = datetime.now()
        now_time = time_for_subj.strftime("%Y %d %b %H:%M:%S")
        time_sub = "Autotest full " + now_time
        mgd.find_element_by_id(ne.subject_field_input).send_keys(time_sub)
        time.sleep(3)
        mgd.find_element_by_class_name(ne.text_panel_button).click()
        body_text = mgd.find_element_by_xpath(ne.body_text_in_new_email)
        bold_text = mgd.find_element_by_class_name(ne.bold_text_panel)
        italic_text = mgd.find_element_by_class_name(ne.italic_text_panel)
        underline_text = mgd.find_element_by_class_name(ne.underline_text_panel)
        ul_marked_text = mgd.find_element_by_class_name(ne.ul_marked_list_text_panel)
        oi_marked_text = mgd.find_element_by_class_name(ne.oi_marked_list_text_panel)
        link_text_panel = mgd.find_element_by_class_name(ne.link_text_panel)
        body_text.click()
        body_text.send_keys("Common\n")
        bold_text.click()
        body_text.send_keys("bold\n")
        italic_text.click()
        body_text.send_keys("bold+italic\n")
        underline_text.click()
        body_text.send_keys("bold+italic+underline\n")
        bold_text.click()
        body_text.send_keys("italic+underline\n")
        underline_text.click()
        body_text.send_keys("italic\n")
        italic_text.click()
        underline_text.click()
        body_text.send_keys("underline\n")
        bold_text.click()
        body_text.send_keys("bold+underline\n")
        bold_text.click()
        underline_text.click()
        ul_marked_text.click()
        body_text.send_keys("ul_marked_1\nul_marked_2\nul_marked_3\n")
        ul_marked_text.click()
        oi_marked_text.click()
        body_text.send_keys("oi__marked_1\noi__marked_2\noi__marked_3\n")
        oi_marked_text.click()
        link_text_panel.click()
        link_input_name = mgd.find_element_by_xpath(ne.link_input_name)
        link_input_address = mgd.find_element_by_xpath(ne.link_input_address)
        link_confirm = mgd.find_element_by_class_name(ne.link_confirm)
        link_input_name.send_keys("Google")
        link_input_address.send_keys("https://www.google.com")
        link_confirm.click()
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(2)
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(2)
        mgd.find_element_by_id(mw.spinner).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(1)
        message = Check.find_element_by_xpath_and_text('//*[@id="list"]/li/div[3]/strong[2]', time_sub)
        self.assertNotEqual(message, None, 'Email not found')
        print('Check - Email sent')
        message.click()
        time.sleep(1)
        to_field = Check.find_element_by_xpath_and_text(ed.to_email_details, 'fre.der@example.com')
        self.assertNotEqual(to_field, None, '"To" field incorrect')
        print('Check - "To" field')

        cc_field = Check.find_element_by_xpath_and_text(ed.cc_email_details, 'barb@ty.ty')
        self.assertNotEqual(cc_field, None, '"Cc" field incorrect')
        print('Check - "Cc" field')

        subject_field = Check.find_element_by_xpath_and_text(ed.subject_email_details, time_sub)
        self.assertNotEqual(subject_field, None, '"Subject" field incorrect')
        print('Check - "Subject" field')
        driver = Maw.get_driver()
        driver.switch_to.frame(mgd.find_element_by_id("message-content-iframe"))
        Check.assert_equal_xpath_for_iframe(
            self, ed.common, 1, 'Common text not found', 'Check - common text')
        Check.assert_equal_xpath_for_iframe(
            self, ed.bold, 1, 'bold text not found', 'Check - bold text')
        Check.assert_equal_xpath_for_iframe(
            self, ed.bold_italic, 1, 'bold+italic text not found', 'Check - bold+italic text')
        Check.assert_equal_xpath_for_iframe(
            self, ed.bold_italic_underline, 1, 'bold+italic+underline text not found',
            'Check - bold+italic+underline text')
        Check.assert_equal_xpath_for_iframe(
            self, ed.italic_underline, 1, 'italic+underline text not found', 'Check - italic+underline text')
        Check.assert_equal_xpath_for_iframe(
            self, ed.italic, 1, 'italic text not found', 'Check - italic text')
        Check.assert_equal_xpath_for_iframe(
            self, ed.underline, 1, 'underline text not found', 'Check - underline text')
        Check.assert_equal_xpath_for_iframe(
            self, ed.bold_underline, 1, 'bold+underline text not found', 'Check - bold+underline text')
        len_ui = str(len(driver.find_elements_by_xpath(ed.ui)))
        Check.assert_equal_xpath_for_iframe(
            self, ed.ui, 1, 'ui text not found', 'Check - ui text, ' + len_ui + ' elements')
        len_oi = str(len(driver.find_elements_by_xpath(ed.oi)))
        Check.assert_equal_xpath_for_iframe(
            self, ed.oi, 1, 'oi text not found', 'Check - oi text, ' + len_oi + ' elements')
        Check.assert_equal_xpath_for_iframe(
            self, ed.link, 1, 'link text not found', 'Check - link text')
        driver.switch_to.default_content()
        time.sleep(1)

    # @unittest.skip("ok")
    def test_email_send_1_to(self):
        mgd.find_element_by_id(ne.to_field_input).send_keys("exadel1")
        time.sleep(2)
        Check.assert_equal_xpath(
            self, ne.to_autocomplete_dropdown_item_1, 1, "Autocomplete 'To' not found", "Check - Autocomplete 'To'")
        drop_down_to_click = mgd.find_element_by_xpath(ne.to_autocomplete_dropdown_item_1)
        time.sleep(2)
        drop_down_to_click.click()
        time_for_subj = datetime.now()
        now_time = time_for_subj.strftime("%Y %d %b %H:%M:%S")
        time_sub = "Autotest 'To' " + now_time
        mgd.find_element_by_id(ne.subject_field_input).send_keys(time_sub)
        time.sleep(1)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        time.sleep(1)
        mgd.find_element_by_xpath(mw.sent_items_folder).click()
        time.sleep(1)
        mgd.find_element_by_id(mw.spinner).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, mw.spinner_not_spinning)))
        time.sleep(2)
        message = Check.find_element_by_xpath_and_text(mw.list_of_messages, time_sub)
        self.assertNotEqual(message, None, 'Email not found')
        print('Check - Email sent')

    # @unittest.skip("ok")
    def test_email_send_2_cc(self):
        mgd.find_element_by_id(ne.cc_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        Check.assert_equal_xpath(
            self, ne.cc_autocomplete_dropdown_item_1, 1, "Autocomplete 'Cc' not found", "Check - Autocomplete 'Cc '")
        drop_down_cc_click = mgd.find_element_by_xpath(ne.cc_autocomplete_dropdown_item_1)
        time.sleep(2)
        drop_down_cc_click.click()
        time_for_subj = datetime.now()
        now_time = time_for_subj.strftime("%Y %d %b %H:%M:%S")
        mgd.find_element_by_id(ne.subject_field_input).send_keys("Autotest 'Cc' ", now_time)
        time.sleep(5)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        Check.assert_equal_class_name(
            self, ne.block_wrapper_header, 1, 'Alert block is missing ', 'Check - Alert block')
        mgd.find_element_by_class_name(ne.wrapper_close).click()

    # @unittest.skip("ok")
    def test_email_send_3_bcc(self):
        mgd.find_element_by_id(ne.bcc_field_input).send_keys("exadel1@botf03.net")
        time.sleep(2)
        Check.assert_equal_xpath(
            self, ne.to_autocomplete_dropdown_item_1, 1, "Autocomplete 'Bcc' not found", "Check - Autocomplete 'Bcc'")
        drop_down_bcc_click = mgd.find_element_by_xpath(ne.bcc_autocomplete_dropdown_item_1)
        time.sleep(2)
        drop_down_bcc_click.click()
        time_for_subj = datetime.now()
        now_time = time_for_subj.strftime("%Y %d %b %H:%M:%S")
        mgd.find_element_by_id(ne.subject_field_input).send_keys("Autotest 'Bcc' ", now_time)
        time.sleep(2)
        Check.assert_equal_xpath(self, ne.send_email_button, 1, 'Send button not found', 'Check - Send button')
        mgd.find_element_by_xpath(ne.send_email_button).click()
        Check.assert_equal_class_name(
            self, ne.block_wrapper_header, 1, 'Alert block is missing ', 'Check - Alert block')
        mgd.find_element_by_class_name(ne.wrapper_close).click()


if __name__ == '__main__':
    unittest.main()
