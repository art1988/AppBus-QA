import Config
import time
import calendar
# import datetime
from datetime import datetime, timedelta
from datetime import timedelta
from main_app_window import Maw, driver_instance
import Config.Mail
import Config.Calendar
from Config.Calendar import main_calendar
from Config.Mail import email_details, main_window, new_email
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# config shortcut
mgd = Maw.get_devices()
ed = Config.Mail.email_details.Elements
mw = Config.Mail.main_window.Elements
ne = Config.Mail.new_email.Elements
cal = Config.Calendar.main_calendar.Elements
driver = Maw.get_driver()
driver_instance.implicitly_wait(5)
wait = WebDriverWait(mgd, 10)


def check_exists_by_id(id_el):
    return len(mgd.find_elements_by_id(id_el)) > 0


def check_exists_by_class_name(class_name):
    return len(mgd.find_elements_by_class_name(class_name)) > 0


def check_exists_by_xpath(xpath):
    return len(mgd.find_elements_by_xpath(xpath)) > 0


def assert_equal_id(self, id_element, compare, error_message, success_message):
    if self.assertEqual(check_exists_by_id(id_element), compare, error_message):
        return
    else:
        print(success_message)


def assert_equal_class_name(self, class_name_element, compare, error_message, success_message):
    if self.assertEqual(check_exists_by_class_name(class_name_element), compare, error_message):
        return
    else:
        print(success_message)


def assert_equal_xpath(self, xpath_element, compare, error_message, success_message):
    if self.assertEqual(check_exists_by_xpath(xpath_element), compare, error_message):
        return
    else:
        print(success_message)


def check_exists_by_xpath_for_iframe(xpath):
    return len(driver.find_elements_by_xpath(xpath)) > 0


def assert_equal_xpath_for_iframe(self, xpath_element, compare, error_message, success_message):
    if self.assertEqual(check_exists_by_xpath_for_iframe(xpath_element), compare, error_message):
        return
    else:
        print(success_message)


def find_element_by_id_and_text(id_elem, text):
    for elem in mgd.find_elements_by_id(id_elem):
        if elem.get_attribute('innerText') == text:
            return elem


def find_element_by_class_name_and_text(class_name, text):
    for elem in mgd.find_elements_by_class_name(class_name):
        if elem.get_attribute('innerText') == text:
            return elem


def find_element_by_xpath_and_text(xpath, text):
    for elem in mgd.find_elements_by_xpath(xpath):
        if elem.get_attribute('innerText') == text:
            return elem


def find_element_by_css_selector_and_text(css_selector, text):
    for elem in mgd.find_elements_by_css_selector(css_selector):
        if elem.get_attribute('innerText') == text:
            return elem


def assert_in_id_text(self, id_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_id(id_element).text
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_class_name_text(self, class_name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_class_name(class_name_element).text
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_name_text(self, name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_name(name_element).text
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_xpath_text(self, xpath_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath(xpath_element).text
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_id_value(self, id_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_id(id_element).get_attribute(name="value")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_class_name_value(self, class_name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_class_name(class_name_element).get_attribute(name="value")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_name_value(self, name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_name(name_element).get_attribute(name="value")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_xpath_value(self, xpath_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath(xpath_element).get_attribute(name="value")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_id_class(self, id_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_id(id_element).get_attribute(name="class")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_class_name_class(self, class_name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_class_name(class_name_element).get_attribute(name="class")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_name_class(self, name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_name(name_element).get_attribute(name="class")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_in_xpath_class(self, xpath_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath(xpath_element).get_attribute(name="class")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_not_in_id_text(self, id_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_id(id_element).text
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_class_name_text(self, class_name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_class_name(class_name_element).text
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_name_text(self, name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_name(name_element).text
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_xpath_text(self, xpath_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath(xpath_element).text
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_id_value(self, id_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_id(id_element).get_attribute(name="value")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_class_name_value(self, class_name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_class_name(class_name_element).get_attribute(name="value")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_name_value(self, name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_name(name_element).get_attribute(name="value")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_xpath_value(self, xpath_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath(xpath_element).get_attribute(name="value")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_id_class(self, id_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_id(id_element).get_attribute(name="class")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_class_name_class(self, class_name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_class_name(class_name_element).get_attribute(name="class")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_name_class(self, name_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_name(name_element).get_attribute(name="class")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_not_in_xpath_class(self, xpath_element, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath(xpath_element).get_attribute(name="class")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message)


def assert_empty_xpath_value(xpath_element, not_none_message, none_message):
    a = mgd.find_element_by_xpath(xpath_element).get_attribute(name="value")
    if a is None:
        print(none_message)
        return
    else:
        print(not_none_message)


def find_element_by_qwe(qwe, text):
    for elem in mgd.find_elements_by_xpath('//*[@id="list"]/li/div[4]/text(', qwe, ')'):
        if elem.text == text:
            return elem


def element_is_visible_class_name(class_name, displayed_message, not_displayed_message):
    a = mgd.find_element_by_class_name(class_name)
    if a.is_displayed():
        print(displayed_message)
    else:
        print(not_displayed_message)


def autocomplete_cycle(start_number, end_number, input_field):
    number = start_number
    while number < end_number:
        mgd.find_element_by_id(input_field).send_keys('cont@autotest.ab')
        if number == 1:
            print('Dropdown contain ' + str(len(mgd.find_elements_by_class_name(ne.dropdown_items))) + ' elements')
        time.sleep(1)
        if "emailInput-to" in input_field:
            drop_dawn_element = '//*[@id="newEmail"]/div[2]/div/div[1]/div[3]/div[1]/div[' + str(number) + ']/div'
        elif 'emailInput-cc' in input_field:
            drop_dawn_element = '//*[@id="newEmail"]/div[2]/div/div[2]/div[3]/div[1]/div[' + str(number) + ']/div'
        elif 'emailInput-bcc' in input_field:
            drop_dawn_element = '//*[@id="newEmail"]/div[2]/div/div[3]/div[3]/div[1]/div[' + str(number) + ']/div'
        else:
            raise Exception('Something wrong in: ' + input_field)
        time.sleep(2)
        hover_autocomplite = mgd.find_element_by_class_name(ne.dropdown_items)
        hidden_email = mgd.find_element_by_xpath(drop_dawn_element)
        actions = ActionChains(driver_instance)

        actions.move_to_element(hover_autocomplite).perform()
        actions.move_to_element(hidden_email).click().perform()
        # time.sleep(1)
        number += 1


def check_exists_emails_by_xpath(xpath):
    return len(mgd.find_elements_by_xpath(xpath)) == 14


def check_exists_contacts_by_class_name(
        class_name, number_of_elem, error_message_more, error_message_less, success_message):
    len_of_list = len(mgd.find_elements_by_class_name(class_name))
    if len_of_list == number_of_elem:
        print(success_message, "(" + str(len_of_list) + ")")
    elif len_of_list > number_of_elem:
        raise Exception(error_message_more, "(" + str(len_of_list) + ")")
    elif len_of_list < number_of_elem:
        raise Exception(error_message_less,  "(" + str(len_of_list) + ")")


def assert_equal_xpath_for_emails(self, xpath_element, compare, error_message, success_message):
    if self.assertEqual(check_exists_emails_by_xpath(xpath_element), compare, error_message):
        return
    else:
        print(success_message)


def flag_in_n_message(n):
    a = '//*[@id="list"]/li[' + str(n) + ']/div[2]/i'
    return a


def flag_in_n_message_attr(n):
    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(n) + ']/div[2]/i').get_attribute(name="class")
    return a


def flag_in_n_message_click(n):
    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(n) + ']/div[2]/i')
    a.click()
    print('Check - select flag in message in' + str(n) + 'row')


def checkbox_in_n_message_click(n):
    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(n) + ']/div[1]/i')
    a.click()
    print('Check - Click on checkbox in message in ' + str(n) + ' row')


def date_in_n_message(self, n, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(n) + ']/div[4]')
    b = a.get_attribute('innerText')
    if self.assertIn(compare_in, b, error_message):
        return
    else:
        print(success_message)
        return b


def message_in_n_row(n):
    mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(n) + ']')


def assert_in_class_attr_message_in_n_row(self, n, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(n) + ']').get_attribute(name="class")
    if self.assertIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def assert_not_in_class_attr_message_in_n_row(self, n, compare_in, error_message, success_message):
    a = mgd.find_element_by_xpath('//*[@id="list"]/li[' + str(n) + ']').get_attribute(name="class")
    if self.assertNotIn(compare_in, a, error_message):
        return
    else:
        print(success_message, a)


def find_number_of_row_class_name_text(class_name, text):
    a = mgd.find_elements_by_class_name(class_name)
    for elem in a:
        if elem.get_attribute('innerText') == text:
            return a.index(elem) + 1


def check_week_date(class_name):
    week_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    week_title_list = week_title.split(' ')

    current_time = datetime.now()
    current_week = current_time.weekday()

    time_delta_first = 0
    time_delta_second = 0

    if current_week != 6:
        time_delta_first = current_week + 1
        time_delta_second = 5 - current_week
    elif current_week == 6:
        time_delta_first = 0
        time_delta_second = current_week

    time_delta_week_first = timedelta(days=time_delta_first)
    time_delta_week_second = timedelta(days=time_delta_second)

    modify_time_first = current_time.replace(microsecond=0, second=0, minute=0, hour=0) - time_delta_week_first
    modify_time_second = current_time.replace(microsecond=0, second=0, minute=0, hour=0) + time_delta_week_second
    week_date_first = week_title_list[0] + ' ' + week_title_list[1] + ' ' + week_title_list[5]
    week_date_second = week_title_list[3] + ' ' + week_title_list[4] + ' ' + week_title_list[5]

    new_date_modify_time_1 = time.strptime(str(modify_time_first), "%Y-%m-%d %H:%M:%S")
    new_date_modify_time_2 = time.strptime(str(modify_time_second), "%Y-%m-%d %H:%M:%S")
    new_date_week_date_1 = time.strptime(week_date_first, "%d %b %Y")
    new_date_week_date_2 = time.strptime(week_date_second, "%d %b %Y")

    if new_date_week_date_1 == new_date_modify_time_1 and new_date_modify_time_2 == new_date_week_date_2:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def check_week_date_minus(class_name):
    week_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    week_title_list = week_title.split(' ')
    current_time = datetime.now()
    time_delta = timedelta(days=7)

    summ_date = current_time - time_delta
    modify_time = summ_date.strftime("%d %b %Y")

    week_date_first = week_title_list[0] + ' ' + week_title_list[1] + ' ' + week_title_list[5]
    week_date_second = week_title_list[3] + ' ' + week_title_list[4] + ' ' + week_title_list[5]

    newdate1 = time.strptime(modify_time, "%d %b %Y")
    newdate2 = time.strptime(week_date_first, "%d %b %Y")
    newdate3 = time.strptime(week_date_second, "%d %b %Y")

    if newdate2 <= newdate1 <= newdate3:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def check_week_date_plus(class_name):
    week_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    week_title_list = week_title.split(' ')
    current_time = datetime.now()
    time_delta = timedelta(days=7)

    summ_date = current_time + time_delta
    modify_time = summ_date.strftime("%d %b %Y")

    week_date_first = week_title_list[0] + ' ' + week_title_list[1] + ' ' + week_title_list[5]
    week_date_second = week_title_list[3] + ' ' + week_title_list[4] + ' ' + week_title_list[5]

    newdate1 = time.strptime(modify_time, "%d %b %Y")
    newdate2 = time.strptime(week_date_first, "%d %b %Y")
    newdate3 = time.strptime(week_date_second, "%d %b %Y")

    if newdate2 <= newdate1 <= newdate3:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def check_day_date(class_name):
    day_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    day_title_list = day_title.split(' ')
    current_time = datetime.now()
    now_time = current_time.strftime("%d %b %Y")
    now_time_list = now_time.split(' ')

    if day_title_list[1] == now_time_list[1]:
        print('Check - Month in navigation title')
    else:
        raise Exception('Month in navigation title is incorrect')
    if int(day_title_list[0]) == int(now_time_list[0]):
        print('Check - Day in navigation title')
    else:
        raise Exception('Day in navigation title is incorrect')
    if day_title_list[2] == now_time_list[2]:
        print('Check - Year in navigation title')
    else:
        raise Exception('Year in navigation title is incorrect')


def check_day_date_minus(class_name):
    day_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    day_title_list = day_title.split(' ')
    current_time = datetime.now()
    time_delta = timedelta(days=1)

    summ_date = current_time - time_delta
    modify_time = summ_date.strftime("%d %b %Y")

    day_date = day_title_list[0] + ' ' + day_title_list[1] + ' ' + day_title_list[2]

    newdate1 = time.strptime(modify_time, "%d %b %Y")
    newdate2 = time.strptime(day_date, "%d %b %Y")

    if newdate2 == newdate1:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def check_day_date_plus(class_name):
    day_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    day_title_list = day_title.split(' ')
    current_time = datetime.now()
    time_delta = timedelta(days=1)

    summ_date = current_time + time_delta
    modify_time = summ_date.strftime("%d %b %Y")

    day_date = day_title_list[0] + ' ' + day_title_list[1] + ' ' + day_title_list[2]

    newdate1 = time.strptime(modify_time, "%d %b %Y")
    newdate2 = time.strptime(day_date, "%d %b %Y")

    if newdate2 == newdate1:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def check_month_date(class_name):
    month_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    month_title_list = month_title.split(' ')
    current_time = datetime.now()
    now_time = current_time.strftime("%b %Y")
    now_time_list = now_time.split(' ')

    if month_title_list[0] == now_time_list[0]:
        print('Check - Month in navigation title')
    else:
        raise Exception('Month in navigation title is incorrect')
    if month_title_list[1] == now_time_list[1]:
        print('Check - Year in navigation title')
    else:
        raise Exception('Year in navigation title is incorrect')


def check_month_date_minus(class_name):
    month_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    month_title_list = month_title.split(' ')
    current_time = datetime.now()
    time_delta = timedelta(days=30)

    summ_date = current_time - time_delta
    modify_time = summ_date.strftime("%b %Y")

    month_date = month_title_list[0] + ' ' + month_title_list[1]

    newdate1 = time.strptime(modify_time, "%b %Y")
    newdate2 = time.strptime(month_date, "%b %Y")

    if newdate2 == newdate1:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def check_month_date_plus(class_name):
    month_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    month_title_list = month_title.split(' ')
    current_time = datetime.now()
    time_delta = timedelta(days=31)

    summ_date = current_time + time_delta
    modify_time = summ_date.strftime("%b %Y")

    month_date = month_title_list[0] + ' ' + month_title_list[1]

    newdate1 = time.strptime(modify_time, "%b %Y")
    newdate2 = time.strptime(month_date, "%b %Y")

    print('Date1 -', newdate1)
    print('Date2 -', newdate2)

    if newdate2 == newdate1:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def check_year_date(class_name):
    year_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    year_title_list = year_title.split(' ')
    current_time = datetime.now()
    now_time = current_time.strftime("%Y")
    now_time_list = now_time.split(' ')

    if year_title_list[0] == now_time_list[0]:
        print('Check - Year in navigation title')
    else:
        raise Exception('Year in navigation title is incorrect')


def check_year_date_minus(class_name):
    year_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    year_title_list = year_title.split(' ')
    current_time = datetime.now()
    now_time = current_time.strftime("%Y")
    now_time_list = now_time.split(' ')
    current_year = int(year_title_list[0])
    year_expect_right = int(now_time_list[0]) - 1
    if current_year == year_expect_right:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def check_year_date_plus(class_name):
    year_title = mgd.find_element_by_class_name(class_name).get_attribute('innerText')
    year_title_list = year_title.split(' ')
    current_time = datetime.now()
    now_time = current_time.strftime("%Y")
    now_time_list = now_time.split(' ')
    current_year = int(year_title_list[0])
    year_expect_right = int(now_time_list[0]) + 1
    if current_year == year_expect_right:
        print('Check - Date in navigation title')
    else:
        raise Exception('Date in navigation title is incorrect')


def starts_field(starts_xpath):
    starts = mgd.find_element_by_xpath(starts_xpath).get_attribute('innerText')
    current_time = datetime.now().replace(microsecond=0, second=0)
    # time_delta = timedelta(minutes=15)
    # summ_time = current_time + time_delta
    # print('current_time ' + str(current_time))
    # print('starts ' + starts)
    # starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
    # print('starts_time ' + str(starts_time))
    # print('summ_time ' + str(summ_time))
    #
    # if summ_time > starts_time > current_time:
    #     print('Check - Date in Starts field')
    # else:
    #     raise Exception('Date in Starts field is incorrect')
    starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
    hour_time = datetime.now().replace(microsecond=0, second=0, minute=0)
    if hour_time + timedelta(minutes=15) >= current_time:
        print('15 minutes')
        if hour_time + timedelta(minutes=15) == starts_time:
            print('Check - Date in Starts field')
        else:
            raise Exception('Date in Starts field is incorrect')
    elif hour_time + timedelta(minutes=30) >= current_time:
        print('30 minutes')
        if hour_time + timedelta(minutes=30) == starts_time:
            print('Check - Date in Starts field')
        else:
            raise Exception('Date in Starts field is incorrect')
    elif hour_time + timedelta(minutes=45) >= current_time:
        print('45 minutes')
        if hour_time + timedelta(minutes=45) == starts_time:
            print('Check - Date in Starts field')
        else:
            raise Exception('Date in Starts field is incorrect')
    elif hour_time + timedelta(minutes=60) >= current_time:
        print('60 minutes')
        if hour_time + timedelta(minutes=60) == starts_time:
            print('Check - Date in Starts field')
        else:
            raise Exception('Date in Starts field is incorrect')


def ends_field(starts_xpath, ends_xpath):
    starts = mgd.find_element_by_xpath(starts_xpath).get_attribute('innerText')
    ends = mgd.find_element_by_xpath(ends_xpath).get_attribute('innerText')
    starts_time = datetime.strptime(starts, "%d %b %Y %I:%M %p")
    ends_time = datetime.strptime(ends, "%d %b %Y %I:%M %p")
    if starts_time + timedelta(minutes=30) == ends_time:
        print('Check - Date in Ends field')
    else:
        raise Exception('Date in Ends field is incorrect')


def find_cell_number(starts_time_cut):
    time_list = ['0:00', '0:30', '1:00', '1:30', '2:00', '2:30', '3:00', '3:30', '4:00', '4:30', '5:00', '5:30',
                 '6:00', '6:30', '7:00', '7:30', '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30',
                 '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00',
                 '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30',
                 '23:00', '23:30']
    starts_time_cut = starts_time_cut.split(':')
    starts_time_cut_plus = starts_time_cut[0] + ':00'
    index_1 = time_list.index(starts_time_cut_plus)
    index_2 = index_1 + 1
    splits_times_1 = time_list[index_1].split(':')
    splits_times_2 = time_list[index_2].split(':')
    if splits_times_1[1] <= starts_time_cut[1] < splits_times_2[1]:
        number = index_1
    elif splits_times_2[1] <= starts_time_cut[1]:
        number = index_2
    else:
        raise Exception('SMTH WRNG')
    cell_number = number
    return str(cell_number)
    # cells = 'grid-day-cell-' + str(cell_number)
    # mgd.find_element_by_id(cells).click()
    # of return mgd.find_element_by_id(cells) ????????


def find_cell_week_number(starts_time_cut):
    time_list = ['0:00', '0:30', '1:00', '1:30', '2:00', '2:30', '3:00', '3:30', '4:00', '4:30', '5:00', '5:30',
                 '6:00', '6:30', '7:00', '7:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
                 '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00',
                 '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30',
                 '23:00', '23:30']
    starts_time_cut = starts_time_cut.split(':')
    starts_time_cut_plus = starts_time_cut[0] + ':00'
    index_1 = time_list.index(starts_time_cut_plus)
    index_2 = index_1 + 1
    splits_times_1 = time_list[index_1].split(':')
    splits_times_2 = time_list[index_2].split(':')
    if splits_times_1[1] <= starts_time_cut[1] < splits_times_2[1]:
        number = index_1
    elif splits_times_2[1] <= starts_time_cut[1]:
        number = index_2
    else:
        raise Exception('SMTHNG WRNG')

    today_week_day = datetime.today().weekday()
    # print(today_week_day)
    if today_week_day == 7:
        week_day = 0
    elif today_week_day != 7:
        week_day = today_week_day + 1
    else:
        raise Exception('SMTHNG WRNG')

    cell_number = number
    # cell_week = str(cell_number) + '-' + str(week_day)
    cell_week = list()
    cell_week.append(cell_number)
    cell_week.append(week_day)
    return cell_week
    # cells = 'grid-day-cell-' + str(cell_number)
    # mgd.find_element_by_id(cells).click()


def event_in_cells(event_name, event_value, start_cell_number):

    current_time = datetime.now()
    now_week = current_time.strftime('%w')
    if now_week == 7:
        count = 0
    elif int(now_week) < 7:
        count = now_week
    else:
        raise Exception('SMTHNG WRNG')
    cell_number = start_cell_number[:-1]
    cell_count = cell_number + str(count)
    id_elem = 'grid-week-cell-' + start_cell_number + ''
    # mgd.find_element_by_id(cal.spinner).click()
    # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))

    mgd.find_element_by_id(id_elem).click()
    title_text = mgd.find_element_by_css_selector(cal.event_name_prvw).get_attribute('innerText')
    if event_name in title_text:
        print('Check - Event in start cell')
    else:
        raise Exception('ERRRRRRROR')

    actions = ActionChains(driver_instance)
    element = mgd.find_element_by_class_name(cal.navigation_right)
    actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
    # actions

    value = 0
    count_rep = int(count)
    while value != event_value:
        print('value', value)
        if count_rep != 7:
            cell_count = cell_number + str(count_rep)
            id_elem = 'grid-week-cell-' + cell_count + ''
            # print('cell_count', cell_count)
            # print('cell_number', cell_number)
            # print('count_rep', count_rep)
            # print('id_elem', id_elem)
            # mod_cell_count = str(int(cell_number[:-1]) - 1) + '-' + str(count_rep)
            # print('mod_cell_count', mod_cell_count)
            # time.sleep(5)
            # print('count_rep', count_rep)
            mgd.find_element_by_id(id_elem).click()
            if not find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
                actions = ActionChains(driver_instance)
                element = mgd.find_element_by_class_name(cal.navigation_right)
                actions.move_to_element(element).move_by_offset(-5, -5).click().perform()

                cell_count = str(int(cell_number[:-1]) - 1) + '-' + str(count_rep)
                id_elem = 'grid-week-cell-' + cell_count + ''
                mgd.find_element_by_id(id_elem).click()

            title_text = mgd.find_element_by_css_selector(cal.event_name_prvw).get_attribute('innerText')
            if event_name in title_text:
                pass
                # print('Check - Event in cell ', count_rep)
            else:
                raise Exception('Event not in cell', count_rep)

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_right)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
            value += 1
            count_rep += 1
        elif count_rep == 7:
            mgd.find_element_by_class_name(cal.navigation_right).click()
            time.sleep(1)
            count_rep = 0
            cell_count = cell_number + str(count_rep)
            id_elem = 'grid-week-cell-' + cell_count + ''

            mgd.find_element_by_id(id_elem).click()
            title_text = mgd.find_element_by_css_selector(cal.event_name_prvw).get_attribute('innerText')
            if event_name in title_text:
                pass
                # print('Check - Event' + str(value) + 'in cell ', count_rep)
            else:
                raise Exception('Event not in cell', count_rep)

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_right)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
            value += 1
            count_rep += 1


def event_in_specific_cells(event_name, event_count, start_cell_number):

    current_time = datetime.now()
    now_week = current_time.strftime('%w')
    if now_week == 7:
        count = 0
    elif int(now_week) < 7:
        count = now_week
    else:
        raise Exception('SMTHNG WRNG')
    cell_number = start_cell_number[:-1]
    # cell_count = cell_number + str(count)
    # id_elem = 'grid-week-cell-' + start_cell_number + ''
    # print('count', count)
    value = 1
    count_rep = int(count)
    while value != event_count:
        if count_rep != 7:
            # print('if count_rep', count_rep)
            cell_count = cell_number + str(count_rep)
            id_elem = 'grid-week-cell-' + cell_count + ''
            # print('id_elem-if', id_elem)

            mgd.find_element_by_id(id_elem)
            # print('Check - Event ' + str(value) + ' in cell ', count_rep, ' event_name -', event_name)
            value += 1
            count_rep += 1
        elif count_rep == 7:
            # print('elif count_rep', count_rep)
            mgd.find_element_by_class_name(cal.navigation_right).click()
            time.sleep(1)
            count_rep = 0
            cell_count = cell_number + str(count_rep)
            id_elem = 'grid-week-cell-' + cell_count + ''
            # print('id_elem-elif', id_elem)

            mgd.find_element_by_id(id_elem)
            # print('Check - Event ' + str(value) + ' in cell ', count_rep, ' event_name -', event_name)
            # if event_name in title_text:
            #     print('Check - Event ' + str(value) + 'in cell ', count_rep)
            # else:
            #     raise Exception('ERRRRRRROR')

            # actions = ActionChains(driver_instance)
            # element = mgd.find_element_by_class_name(cal.navigation_right)
            # actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
            value += 1
            count_rep += 1
    if count_rep == 7:
        # print('if-2 count_rep', count_rep)
        mgd.find_element_by_class_name(cal.navigation_right).click()
        time.sleep(1)
        count_rep = 0

    cell_count = cell_number + str(count_rep)
    id_elem = 'grid-week-cell-' + cell_count + ''
    # print('id_elem-after-while', id_elem)
    return id_elem


def event_in_cells_custom(event_name, rep_days, event_value, start_cell_number):

    current_time = datetime.now()
    now_week = current_time.strftime('%w')

    cell_number = start_cell_number[:-1]
    id_elem = 'grid-week-cell-' + start_cell_number + ''
    print('cell_number', cell_number)
    # mgd.find_element_by_id(cal.spinner).click()
    # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))

    mgd.find_element_by_id(id_elem).click()
    if not find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_class_name(cal.navigation_right)
        actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
        cell_number = str(int(start_cell_number[:-2]) - 1) + '-' + str(start_cell_number[-1:])
        id_elem = 'grid-week-cell-' + cell_number + ''
        mgd.find_element_by_id(id_elem).click()

    title_text = mgd.find_element_by_css_selector(cal.event_name_prvw).get_attribute('innerText')
    if event_name in title_text:
        pass
        # print('Check - Event in cell')
    else:
        raise Exception('Event not in cell')
    time.sleep(1)
    actions = ActionChains(driver_instance)
    element = mgd.find_element_by_class_name(cal.navigation_right)
    actions.move_to_element(element).move_by_offset(-5, -5).click().perform()

    print('days', rep_days)
    value = 1
    days_len = len(rep_days)
    print('days_len', days_len)
    x = int(now_week)
    now_week_index = rep_days.index(x)
    print('now_week_index', now_week_index)

    if now_week_index == days_len - 1:
        mgd.find_element_by_class_name(cal.navigation_right).click()
        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

    else:
        new_days_list = rep_days[now_week_index:]
        print('days', rep_days)
        print('new_days_list', new_days_list)
        for day_number in new_days_list:
            cell_count = cell_number + str(day_number)
            id_elem = 'grid-week-cell-' + cell_count + ''

            mgd.find_element_by_id(id_elem).click()
            if not find_element_by_css_selector_and_text(cal.event_name_prvw, event_name):
                actions = ActionChains(driver_instance)
                element = mgd.find_element_by_class_name(cal.navigation_right)
                actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
                cell_number = str(int(start_cell_number[:-2]) - 1) + '-'
                cell_count = cell_number + str(day_number)
                id_elem = 'grid-week-cell-' + cell_count + ''
                mgd.find_element_by_id(id_elem).click()
            title_text = mgd.find_element_by_css_selector(cal.event_name_prvw).get_attribute('innerText')
            if event_name in title_text:
                pass
                # print('Check - Event in cell ', day_number)
            else:
                raise Exception('Event not in cell', day_number)

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_right)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
            value += 1
        mgd.find_element_by_class_name(cal.navigation_right).click()
        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)

    while value <= event_value:

        for day_number in rep_days:
            cell_count = cell_number + str(day_number)
            id_elem = 'grid-week-cell-' + cell_count + ''
            time.sleep(1)
            mgd.find_element_by_id(id_elem).click()
            title_text = mgd.find_element_by_css_selector(cal.event_name_prvw).get_attribute('innerText')
            if event_name in title_text:
                pass
                # print('Check - Event in cell ', day_number)
            else:
                raise Exception('Event not found', day_number)

            actions = ActionChains(driver_instance)
            element = mgd.find_element_by_class_name(cal.navigation_right)
            actions.move_to_element(element).move_by_offset(-5, -5).click().perform()
            value += 1
        mgd.find_element_by_class_name(cal.navigation_right).click()
        time.sleep(1)


def event_in_cells_month(event_name, event_value, start_cell_number_css):
    ''' Add function 29 - 30 days for Feb '''
    # mgd.find_element_by_id(cal.spinner).click()
    # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))

    view_button = find_element_by_class_name_and_text(cal.view_button, 'Month')
    view_button_select = view_button.get_attribute(name='class')
    if 'selected' in view_button_select:
        print('Check - Month View is selected')
    else:
        view_button.click()
        view_button_select = view_button.get_attribute(name='class')
        if 'selected' in view_button_select:
            print('Check - Month View is selected')
        else:
            raise Exception('Month view is not selectable')

    i = 1
    while i <= event_value:
        time.sleep(2)
        elem = find_element_by_css_selector_and_text(start_cell_number_css, event_name)
        if elem is []:
            time.sleep(2)
        elem = find_element_by_css_selector_and_text(start_cell_number_css, event_name)
        if elem is []:
            raise Exception('ERRRRRRROR')
        time.sleep(1)
        actions = ActionChains(driver_instance)
        actions.move_to_element(elem).click().perform()
        print('Check - Event ' + str(i))

        actions = ActionChains(driver_instance)
        element = mgd.find_element_by_class_name(cal.navigation_right)
        actions.move_to_element(element).move_by_offset(-5, -5).click().perform()

        mgd.find_element_by_class_name(cal.navigation_right).click()
        # mgd.find_element_by_id(cal.spinner).click()
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
        time.sleep(2)
        i += 1


# def week_of_month(year, month, day):
#     first_week_month = datetime(year, month, 1).isocalendar()[1]
#     if month == 1 and first_week_month > 10:
#         first_week_month = 0
#     user_date = datetime(year, month, day).isocalendar()[1]
#     if month == 1 and user_date > 10:
#         user_date = 0
#     print('week of month',  user_date - first_week_month)
#     return user_date - first_week_month


def day_of_week_in_month(year, month, week_number, day_of_week_name):
    ''' All week_day inputs most be: mon = 1, sun = 7 '''
    week_day_number = time.strptime(day_of_week_name, '%A').tm_wday + 1
    print('week_day_number', week_day_number)
    current_time = datetime.now()

    date_input = str(year) + ' ' + str(month) + ' ' + '01'
    date_current = datetime.strptime(str(date_input), "%Y %m %d")
    # print('date2', date_current)
    week_day_to_first_day_of_month = date_current.strftime('%w')
    if week_day_to_first_day_of_month == '0':
        week_day_to_first_day_of_month = '7'
    print('week_day_to_first_day_of_month', week_day_to_first_day_of_month)
    month_days_count = calendar.monthrange(int(year), int(month))
    print('month_days_count', month_days_count)
    # now_day = current_time.strftime('%d')
    # timedelta_to_first_day = timedelta(days=int(now_day) - 1)
    # first_day_of_month = current_time - timedelta_to_first_day
    # print('first_day_of_month', first_day_of_month)
    # now_week_day = current_time.strftime('%w')
    # print('now_week_day', now_week_day)
    # week_day_to_first_day_of_month = first_day_of_month.strftime('%w')

    # print('week_day_to_first_day_of_month', week_day_to_first_day_of_month)
    # if week_day == 0:
    #     week_day = 7
    # month_detail = calendar.monthrange(int(year), int(month))
    # day_in_month = month_detail[1]
    # # da
    # if day_of_week == 1:
    #     week_coeff = 7
    # elif day_of_week == 2:
    #     week_coeff = 14
    # elif day_of_week == 3:
    #     week_coeff = 21
    # elif day_of_week == 4:
    #     week_coeff = 28
    if week_number == 'first':
        week_number = 1
    elif week_number == 'second':
        week_number = 2
    elif week_number == 'third':
        week_number = 3
    elif week_number == 'fourth':
        week_number = 4
    elif week_number == 'last':
        week_number = 5

    week_coeff = 7 * week_number

    if int(week_day_to_first_day_of_month) <= int(week_day_number):
        week_coeff = int(week_coeff) - 7

    print('week_coeff', week_coeff)

    week_days_difference = int(week_day_to_first_day_of_month) - int(week_day_number)
    print('week_days_difference', week_days_difference)
    answer = week_coeff + 1 - week_days_difference
    print(day_of_week_name + ' - ' + str(week_number) + ' is:', answer)
    if answer > month_days_count[1]:
        answer = answer - 7
    # print('month', month)
    # if month == '02':
    #     if answer >= 29:
    #         answer = answer - 7
    print('answer', answer)
    return answer
