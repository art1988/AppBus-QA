import time
import unittest
import Check
import Config
import Config.Contacts.main_contacts
from main_app_window import Maw, driver_instance
mgd = Maw.get_devices()
cm = Config.Contacts.main_contacts.Elements
driver_instance.implicitly_wait(15)

def setUpModule():
    print('Start: .py\n')


def tearDownModule():
    print('End: b.py\n')
    driver_instance.quit()


# @unittest.skip("skip")
class TestCreateContacts(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip('Ok')
    def test1_new_contact_crated(self):
        name = 'Can create'
        mgd.find_element_by_xpath(cm.new_contact).click()
        mgd.find_element_by_id(cm.name_input).send_keys(name)
        mgd.find_element_by_xpath(cm.yes_option).click()
        Check.find_element_by_class_name_and_text(cm.contact_title, name).click()
        mgd.find_element_by_xpath(cm.delete_option).click()
        mgd.find_element_by_xpath(cm.delete_button_wrapper).click()
        time.sleep(2)
        if Check.find_element_by_class_name_and_text(cm.contact_title, name):
            print(name, ' not deleted')

    @unittest.skip('Ok')
    def test2_add_new_contacts_for_mail_tests_original(self):
        driver_instance.implicitly_wait(2)
        element_number = 1
        checked_list = []

        list_contact_elements = Maw.get_devices().find_elements_by_class_name(cm.contact_title)

        def check_auto_contact_elements(element, text):
            for elem in element:
                if elem.get_attribute('innerText') == text:
                    return elem

        while element_number < 15:
            if check_auto_contact_elements(list_contact_elements, 'Contact for autotest ' + str(
                    element_number)):
                print('Contact for autotest ' + str(element_number) + ' is found')
                checked_list.append(1)
            else:
                print('Contact for autotest ' + str(element_number) + ' not found')
                checked_list.append(0)
            element_number += 1
            time.sleep(1)
        print(checked_list)

        element_number_create = 1
        while element_number_create < 15:
            for elem in checked_list:
                if elem == 0:
                    mgd.find_element_by_xpath(cm.new_contact).click()
                    mgd.find_element_by_id(cm.name_input).send_keys('Contact for autotest ', element_number_create)
                    mgd.find_element_by_id(cm.contacts_tab).click()
                    mgd.find_element_by_id(cm.email_input).send_keys(element_number_create, 'cont@autotest.ab')
                    mgd.find_element_by_xpath(cm.accept_button).click()
                    element_number_create = element_number_create + 1
                    time.sleep(1)
                    print('Contact for autotest ', element_number_create, ' created')
                else:
                    print('else', element_number_create)
                    element_number_create = element_number_create + 1
                    time.sleep(1)

    # @unittest.skip('Ok')
    def test2_add_new_contacts_for_mail_tests(self):
        driver_instance.implicitly_wait(2)
        element_number = 1
        checked_list = []

        list_contact_elements = Maw.get_devices().find_elements_by_class_name(cm.contact_title)

        company1 = 'Test inc.'
        department1 = 'Department of truth'
        job_title1 = 'High lvl tester'
        work_phone1 = '8965569855'
        home_phone1 = '4568628620'
        mobile_phone = '123501235'
        email2 = '2email@intherow.nom'
        email3 = 'three@mail.mail'
        web_site1 = 'topwebsite.top'
        im_id1 = 'tester_expert_123415'
        work_street1 = '28 line'
        work_city1 = 'City 17'
        work_state1 = 'Hidden'
        work_postal1 = '0011728'
        work_country1 = 'Test village'
        home_street1 = 'Big Lion'
        home_city1 = 'Tree'
        home_state1 = 'South'
        home_postal1 = '5552468'
        home_country1 = 'Cupboard'


        def check_auto_contact_elements(element, text):
            for elem in element:
                if elem.get_attribute('innerText') == text:
                    return elem

        while element_number < 15:
            if check_auto_contact_elements(list_contact_elements, 'Contact for autotest ' + str(
                    element_number)):
                print('Contact for autotest ' + str(element_number) + ' is found')
                checked_list.append(1)
            else:
                print('Contact for autotest ' + str(element_number) + ' not found')
                checked_list.append(0)
            element_number += 1
            time.sleep(1)
        print(checked_list)

        element_number_create = 1
        while element_number_create < 15:
            for elem in checked_list:
                if elem == 0:
                    mgd.find_element_by_xpath(cm.new_contact).click()
                    contacts_tab = Check.find_element_by_id_and_text(cm.one_of_tab, 'Contacts')
                    address_tab = Check.find_element_by_id_and_text(cm.one_of_tab, 'Address')
                    more_tab = Check.find_element_by_id_and_text(cm.one_of_tab, 'More')

                    mgd.find_element_by_id(cm.name_input).send_keys('Contact for autotest ', element_number_create)

                    if element_number_create <= 8:
                        mgd.find_element_by_id(cm.company_input).send_keys(company1)
                        mgd.find_element_by_id(cm.job_title_input).send_keys(job_title1)

                    if element_number_create <= 3:
                        mgd.find_element_by_id(cm.department_input).send_keys(department1)
                        contacts_tab.click()
                        mgd.find_element_by_name(cm.website_input).send_keys(web_site1)
                        address_tab.click()
                        mgd.find_element_by_name(cm.home_city_input).send_keys(home_city1)
                        mgd.find_element_by_name(cm.home_postal_code_input).send_keys(home_postal1)
                        mgd.find_element_by_name(cm.home_state_input).send_keys(home_state1)
                        mgd.find_element_by_name(cm.home_street_input).send_keys(home_street1)
                        mgd.find_element_by_name(cm.home_country_input).send_keys(home_country1)

                    if element_number_create <= 5:
                        contacts_tab.click()
                        mgd.find_element_by_name(cm.business_phone_input).send_keys(work_phone1)
                        address_tab.click()
                        mgd.find_element_by_name(cm.work_street_input).send_keys(work_street1)
                        mgd.find_element_by_name(cm.work_country_input).send_keys(work_country1)
                        mgd.find_element_by_name(cm.work_city_input).send_keys(work_city1)
                        mgd.find_element_by_name(cm.work_state_input).send_keys(work_state1)
                        mgd.find_element_by_name(cm.work_postal_code_input).send_keys(work_postal1)
                        more_tab.click()
                        mgd.find_element_by_name(cm.language_input).send_keys()

                    if element_number_create <= 2:
                        contacts_tab.click()
                        mgd.find_element_by_name(cm.home_phone_input).send_keys(home_phone1)

                    if element_number_create <= 9:
                        contacts_tab.click()
                        mgd.find_element_by_name(cm.mobile_phone_input).send_keys(mobile_phone)

                    if element_number_create <= 4:
                        contacts_tab.click()
                        mgd.find_element_by_name(cm.im_id_input).send_keys(im_id1)
                        more_tab.click()
                        mgd.find_element_by_name(cm.hobbies_input).send_keys()

                    if element_number_create <= 6:
                        contacts_tab.click()
                        mgd.find_element_by_name(cm.email_input_2).send_keys(email2)

                    if element_number_create <= 7:
                        contacts_tab.click()
                        mgd.find_element_by_name(cm.email_input_3).send_keys(email3)

                    contacts_tab.click()
                    mgd.find_element_by_id(cm.email_input).send_keys(element_number_create, 'cont@autotest.ab')
                    mgd.find_element_by_xpath(cm.accept_button).click()
                    element_number_create = element_number_create + 1
                    time.sleep(1)
                    print('Contact for autotest ', element_number_create, ' created')
                else:
                    print('skipped', element_number_create)
                    element_number_create = element_number_create + 1
                    time.sleep(1)

    @unittest.skip('Ok')
    def test3_add_1000_new_contacts(self):
        driver_instance.implicitly_wait(1)
        element_number = 1
        checked_list = [0 for i in range(386)]

        # list_contact_elements = Maw.get_devices().find_elements_by_class_name(cm.contact_title)
        #
        # def check_auto_contact_elements(element, text):
        #     for elem in element:
        #         if elem.get_attribute('innerText') == text:
        #             return elem
        #
        # while element_number < 900:
        #     if check_auto_contact_elements(list_contact_elements, 'one in a thousand ' + str(
        #             element_number)):
        #         print('one in a thousand ' + str(element_number) + ' is found')
        #         checked_list.append(1)
        #     else:
        #         print('one in a thousand ' + str(element_number) + ' not found')
        #         checked_list.append(0)
        #     element_number += 1
        #     time.sleep(1)
        print(checked_list)

        element_number_create = 514
        while element_number_create < 900:
            for elem in checked_list:
                if elem == 0:
                    mgd.find_element_by_xpath(cm.new_contact).click()
                    mgd.find_element_by_id(cm.name_input).send_keys('one in a thousand ', element_number_create)
                    # mgd.find_element_by_id(cm.contacts_tab).click()
                    # mgd.find_element_by_id(cm.email_input).send_keys(element_number_create, 'cont@autotest.ab')
                    mgd.find_element_by_xpath(cm.accept_button).click()
                    element_number_create = element_number_create + 1
                    time.sleep(1)
                    print('one in a thousand ', element_number_create, ' created')
                else:
                    print('else', element_number_create)
                    element_number_create = element_number_create + 1
                    time.sleep(1)

    @unittest.skip('Not Ok')
    def test3_delete_1000_new_contacts(self):
        driver_instance.implicitly_wait(20)
        # element_number = 1
        # checked_list = [0 for i in range(900)]

        # list_contact_elements = Maw.get_devices().find_elements_by_class_name(cm.contact_title)
        #
        # def check_auto_contact_elements(element, text):
        #     for elem in element:
        #         if elem.get_attribute('innerText') == text:
        #             return elem
        #
        # while element_number < 900:
        #     if check_auto_contact_elements(list_contact_elements, 'one in a thousand ' + str(
        #             element_number)):
        #         print('one in a thousand ' + str(element_number) + ' is found')
        #         checked_list.append(1)
        #     else:
        #         print('one in a thousand ' + str(element_number) + ' not found')
        #         checked_list.append(0)
        #     element_number += 1
        #     time.sleep(1)
        # print(checked_list)

        # element_number_create = 900
        # while element_number_create < 900:
        #     for elem in checked_list:
        #         if elem == 0:
        #             mgd.find_element_by_xpath(cm.new_contact).click()
        #             mgd.find_element_by_id(cm.name_input).send_keys('one in a thousand ', element_number_create)
        #             # mgd.find_element_by_id(cm.contacts_tab).click()
        #             # mgd.find_element_by_id(cm.email_input).send_keys(element_number_create, 'cont@autotest.ab')
        #             mgd.find_element_by_xpath(cm.accept_button).click()
        #             element_number_create = element_number_create + 1
        #             time.sleep(1)
        #             print('one in a thousand ', element_number_create, ' created')
        #         else:
        #             print('else', element_number_create)
        #             element_number_create = element_number_create + 1
        #             time.sleep(1)




        # element_number = 1
        # while Check.find_element_by_class_name_and_text(cm.contact_title, 'one in a thousand'):
        #     Check.find_element_by_class_name_and_text(cm.contact_title, 'one in a thousand ' + element_number).click()
        #     time.sleep(1)
        #     mgd.find_element_by_xpath(cm.delete_option).click()
        #     time.sleep(1)
        #     element_number +=1

        while mgd.find_elements_by_xpath("//*[contains(text(), 'one in a thousand')]"):
            mgd.find_elements_by_xpath("//*[contains(text(), 'one in a thousand')]").click()
            time.sleep(1)
            mgd.find_element_by_xpath(cm.delete_option).click()
            time.sleep(1)
