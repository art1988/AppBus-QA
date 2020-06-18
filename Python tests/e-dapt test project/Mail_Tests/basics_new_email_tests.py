import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


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


def setUpModule():
    print('Start: basics_new_email_tests.py\n')


def tearDownModule():
    print('End: basics_new_email_tests.py\n')
    # driver_instance.quit()


# @unittest.skip('ok')
class Test1NewEmail(unittest.TestCase):

    def test1_open_close_new_email(self):
        driver_instance.implicitly_wait(0)
        WebDriverWait(driver_instance, 5).until(ec.element_to_be_clickable((By.ID, mw.new_email_button)))
        Check.assert_equal_id(self, mw.new_email_button, 1, "New Email button not found", "Check - New Email button")
        mgd.find_element_by_id(mw.new_email_button).click()
        WebDriverWait(driver_instance, 5).until(ec.element_to_be_clickable((By.ID, ne.close_email_button)))
        Check.assert_equal_id(self, ne.close_email_button, 1, "Close button not found", "Check - Close button")
        time.sleep(1)
        mgd.find_element_by_id(ne.close_email_button).click()
        driver_instance.implicitly_wait(5)

    def setUp(self):
        pass

    def tearDown(self):
        time.sleep(2)
        Check.assert_equal_id(
            self, ne.new_email, 0, "New Email Window did not close", "Check - New Email Window closed")


# @unittest.skip('ok')
class Test2AutocompleteEditorContactButton(unittest.TestCase):
    def setUp(self):
        time.sleep(1)
        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)

    def tearDown(self):
        time.sleep(2)
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_class_name(ne.overlay):
            print('Overlay - exist (Test2)')
            mgd.find_element_by_class_name(ne.overlay).click()
        if Check.check_exists_by_id(ne.new_email):
            print("New email window - exist (Test2)")
            mgd.find_element_by_id(ne.close_email_button).click()
            time.sleep(1)
            if Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper):
                print("Close editor confirmation block wrapper - exist (Test2)")
                Check.find_element_by_class_name_and_text(ne.close_editor_confirmation_button, 'Delete Draft').click()
            driver_instance.implicitly_wait(5)

    # @unittest.skip("ok")
    def test_autocomplete(self):
        Check.autocomplete_cycle(1, 15, ne.to_field_input)
        time.sleep(1)
        Check.assert_equal_xpath_for_emails(
            self, ne.to_emails, 1, '"To" field. The number of emails does not match 14', 'Check - "To" 14 emails')
        time.sleep(1)

        Check.autocomplete_cycle(1, 15, ne.cc_field_input)
        time.sleep(1)
        Check.assert_equal_xpath_for_emails(
            self, ne.cc_emails, 1, '"Cc" field. The number of emails does not match 14', 'Check - "Cc" 14 emails')
        time.sleep(1)

        Check.autocomplete_cycle(1, 15, ne.bcc_field_input)
        time.sleep(1)
        Check.assert_equal_xpath_for_emails(
            self, ne.bcc_emails, 1, '"Bcc" field. The number of emails does not match 14', 'Check - "Bcc" 14 emails')
        time.sleep(1)

    # @unittest.skip("ok")
    def test_editor_toolbar(self):
        mgd.find_element_by_class_name(ne.text_panel_button).click()
        body_text = mgd.find_element_by_xpath(ne.body_text_in_new_email)
        bold_text = mgd.find_element_by_class_name(ne.bold_text_panel)
        italic_text = mgd.find_element_by_class_name(ne.italic_text_panel)
        underline_text = mgd.find_element_by_class_name(ne.underline_text_panel)
        ul_marked_text = mgd.find_element_by_class_name(ne.ul_marked_list_text_panel)
        oi_marked_text = mgd.find_element_by_class_name(ne.oi_marked_list_text_panel)
        link_text_panel = mgd.find_element_by_class_name(ne.link_text_panel)
        unlink_text_panel = mgd.find_element_by_class_name(ne.unlink_text_panel)
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
        time.sleep(5)

        body_text.send_keys(Keys.ARROW_RIGHT)
        body_text.send_keys(Keys.ENTER)
        link_text_panel.click()
        link_input_name = mgd.find_element_by_xpath(ne.link_input_name)
        link_input_address = mgd.find_element_by_xpath(ne.link_input_address)
        link_confirm = mgd.find_element_by_class_name(ne.link_confirm)
        link_input_name.send_keys("Link to no link")
        link_input_address.send_keys("https://www.google.com")
        link_confirm.click()
        body_text.send_keys(Keys.ARROW_RIGHT)
        body_text.send_keys(Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_LEFT)
        body_text.send_keys(Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_LEFT)
        body_text.send_keys(Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_LEFT)
        body_text.send_keys(Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_LEFT)
        unlink_text_panel.click()
        body_text.send_keys(Keys.ARROW_RIGHT)
        body_text.send_keys(Keys.END)
        body_text.send_keys(Keys.ENTER)
        link_text_panel.click()
        link_input_name = mgd.find_element_by_xpath(ne.link_input_name)
        link_input_address = mgd.find_element_by_xpath(ne.link_input_address)
        link_confirm = mgd.find_element_by_class_name(ne.link_confirm)
        link_input_name.send_keys("Link to delete")
        link_input_address.send_keys("https://www.google.com")
        link_confirm.click()
        time.sleep(2)

        Check.assert_equal_xpath(
            self, ne.common, 1, 'Common text not found', 'Check - common text')
        Check.assert_equal_xpath(
            self, ne.bold, 1, 'bold text not found', 'Check - bold text')
        Check.assert_equal_xpath(
            self, ne.bold_italic, 1, 'bold_italic text not found', 'Check - bold_italic text')
        Check.assert_equal_xpath(
            self, ne.bold_italic_underline, 1, 'bold_italic_underline text not found',
            'Check - bold_italic_underline text')
        Check.assert_equal_xpath(
            self, ne.italic_underline, 1, 'italic_underline text not found', 'Check - italic_underline text')
        Check.assert_equal_xpath(
            self, ne.italic, 1, 'italic text not found', 'Check - italic text')
        Check.assert_equal_xpath(
            self, ne.underline, 1, 'underline text not found', 'Check - underline text')
        Check.assert_equal_xpath(
            self, ne.bold_underline, 1, 'bold_underline text not found', 'Check - bold_underline text')
        len_ui = str(len(mgd.find_elements_by_xpath(ne.ui)))
        Check.assert_equal_xpath(
            self, ne.ui, 1, 'ui text not found', 'Check - ui text, ' + len_ui + ' elements')
        len_oi = str(len(mgd.find_elements_by_xpath(ne.oi)))
        Check.assert_equal_xpath(
            self, ne.oi, 1, 'oi text not found', 'Check - oi text, ' + len_oi + ' elements')
        Check.assert_equal_xpath(
            self, ne.link, 1, 'link text not found', 'Check - link text')
        Check.assert_equal_xpath(
            self, ne.link_to_delete, 1, '"Link to not link" text not found', 'Check - "Link to delete" text')
        Check.assert_equal_xpath(
            self, ne.link_to_not_link, 1, '"Link to not link" text not found', 'Check - "Link to not link" text')
        body_text.send_keys(Keys.BACKSPACE)
        Check.assert_equal_xpath(
            self, ne.link_to_delete, 0, '"Link to delete" text is found', 'Check - "Link to delete" text is not found')

    # @unittest.skip('ok')
    def test_add_contact_button(self):
        name = 'France'
        email = 'fre.der@example.com'
        mgd.find_element_by_id(ne.add_contact_button_in_to).click()
        Check.assert_equal_class_name(
            self, ne.add_contact_dropdown, 1, '"To" field. Add contact dropdown do not exist',
            'Check - "To" field. Add contact dropdown')
        # print(mgd.find_element_by_class_name(ne.add_contact_search_input).get_attribute(name='value'))
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, '', '"To" Search input is not clear',
            'Check - "To" Search input is clear')

        mgd.find_element_by_xpath(ne.add_contact_dropdown_item_1).click()
        Check.assert_equal_class_name(
            self, ne.block_wrapper_header, 1, '"To" field. Block wrapper  - not valid email do not exist',
            'Check -"To" field. Not valid email')
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Close').click()
        print('Check - Pop-up window "Not valid email"')

        mgd.find_element_by_class_name(ne.add_contact_search_input).send_keys(name)
        print('Check - Search input')
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, name, 'Search input contain wrong data',
            'Check - Search input contain ')
        wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//*[@class='email' and contains(text(), '" + email + "')]")))
        time.sleep(1)
        element1 = mgd.find_element_by_xpath("//*[@class='email' and contains(text(), '" + email + "')]")
        element1.click()

        # mgd.find_element_by_xpath('//*[@id="addContact"]/div[2]/div/div/div[2]/div[1]/i[2]').click()
        mgd.find_element_by_css_selector("#newEmail ." + ne.search_clear_filled).click()
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, '', '"To" Search input is not clear',
            'Check - "To" Search input is clear')
        time.sleep(2)
        # add code to check selected items
        mgd.find_element_by_class_name(ne.overlay).click()
        #
        #
        mgd.find_element_by_id(ne.add_contact_button_in_cc).click()
        Check.assert_equal_class_name(
            self, ne.add_contact_dropdown, 1, '"Cc" field. Add contact dropdown do not exist',
            'Check - "Cc" field. Add contact dropdown')
        # print(mgd.find_element_by_class_name(ne.add_contact_search_input).get_attribute(name='value'))
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, '', '"Cc" Search input is not clear',
            'Check - "Cc" Search input is clear')

        mgd.find_element_by_xpath(ne.add_contact_dropdown_item_1).click()
        Check.assert_equal_class_name(
            self, ne.block_wrapper_header, 1, '"Cc" field. Block wrapper  - not valid email do not exist',
            'Check -"Cc" field. Not valid email')
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Close').click()
        print('Check - Pop-up window "Not valid email"')

        mgd.find_element_by_class_name(ne.add_contact_search_input).send_keys(name)
        print('Check - Search input')
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, name, 'Search input contain wrong data',
            'Check - Search input contain ')
        wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//*[@class='email' and contains(text(), '" + email + "')]")))
        element1 = mgd.find_element_by_xpath("//*[@class='email' and contains(text(), '" + email + "')]")
        element1.click()

        mgd.find_element_by_css_selector("#newEmail ." + ne.search_clear_filled).click()
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, '', '"Cc" Search input is not clear',
            'Check - "Cc" Search input is clear')
        time.sleep(2)
        # add code to check selected items
        mgd.find_element_by_class_name(ne.overlay).click()
        #
        #
        mgd.find_element_by_id(ne.add_contact_button_in_bcc).click()
        Check.assert_equal_class_name(
            self, ne.add_contact_dropdown, 1, '"Bcc" field. Add contact dropdown do not exist',
            'Check - "Bcc" field. Add contact dropdown')
        # print(mgd.find_element_by_class_name(ne.add_contact_search_input).get_attribute(name='value'))
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, '', '"Bcc" Search input is not clear',
            'Check - "Bcc" Search input is clear')

        mgd.find_element_by_xpath(ne.add_contact_dropdown_item_1).click()
        Check.assert_equal_class_name(
            self, ne.block_wrapper_header, 1, '"Bcc" field. Block wrapper  - not valid email do not exist',
            'Check -"Bcc" field. Not valid email')
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.wrapper_close, 'Close').click()
        print('Check - Pop-up window "Not valid email"')

        mgd.find_element_by_class_name(ne.add_contact_search_input).send_keys(name)
        print('Check - Search input')
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, name, 'Search input contain wrong data',
            'Check - Search input contain ')
        wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//*[@class='email' and contains(text(), '" + email + "')]")))
        element1 = mgd.find_element_by_xpath("//*[@class='email' and contains(text(), '" + email + "')]")
        element1.click()

        mgd.find_element_by_css_selector("#newEmail ." + ne.search_clear_filled).click()
        Check.assert_in_class_name_value(
            self, ne.add_contact_search_input, '', '"Bcc" Search input is not clear',
            'Check - "Bcc" Search input is clear')
        time.sleep(2)
        # add code to check selected items
        mgd.find_element_by_class_name(ne.overlay).click()
        #
        #
        Check.assert_equal_xpath(
            self, ne.to_emails, 1, '"To" field. No contact added', 'Check - "To" field. Contact added')
        Check.assert_equal_xpath(
            self, ne.cc_emails, 1, '"Cc" field. No contact added', 'Check - "Cc" field. Contact added')
        Check.assert_equal_xpath(
            self, ne.bcc_emails, 1, '"Bcc" field. No contact added', 'Check - "Bcc" field. Contact added')


class Test2draft(unittest.TestCase):

    def setUp(self):
        time.sleep(1)
        mgd.find_element_by_id(mw.new_email_button).click()
        time.sleep(1)

    def tearDown(self):
        time.sleep(2)
        driver_instance.implicitly_wait(1)
        if Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper):
            mgd.find_element_by_class_name(ne.overlay).click()
        if Check.check_exists_by_id(ne.new_email):
            print("New email window - exist (Test2)")
            mgd.find_element_by_id(ne.close_email_button).click()
            time.sleep(1)
            if Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper):
                print("Close editor confirmation block wrapper - exist (Test2)")
                Check.find_element_by_class_name_and_text(ne.close_editor_confirmation_button, 'Delete Draft').click()
            driver_instance.implicitly_wait(5)

    def test_draft(self):
        subject = 'Autotest message for saving a draft'
        mgd.find_element_by_id(ne.subject_field_input).send_keys(subject)
        time.sleep(2)
        mgd.find_element_by_id(ne.close_email_button).click()
        Check.check_exists_by_class_name(ne.close_editor_confirmation_block_wrapper)
        time.sleep(1)
        Check.find_element_by_class_name_and_text(ne.close_editor_confirmation_button, 'Save').click()
        time.sleep(1)
        mgd.find_element_by_xpath(mw.drafts_folder).click()
        time.sleep(1)

        Check.assert_in_xpath_class(
            self, mw.drafts_selected_folder, 'selected-folder', 'Wrong selected folder (not drafts)',
            'Check - Selected folder is drafts -')

        Check.find_element_by_class_name_and_text(mw.topic, subject)
        print('Check - draft is found')


