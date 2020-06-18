from content import Elements, Other
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CE = Elements
CO = Other


def by_id_and_text(driver, id_elem, text):
    for elem in driver.find_elements_by_id(id_elem):
        if elem.get_attribute('textContent') == text:
            return elem


def by_id_and_value(driver, id_elem, value):
    for elem in driver.find_elements_by_id(id_elem):
        if elem.get_attribute(name='value') == value:
            return elem


def by_class_name_and_text(driver, class_name, text):
    for elem in driver.find_elements_by_class_name(class_name):
        if elem.get_attribute('textContent') == text:
            return elem


def by_xpath_and_text(driver, xpath, text):
    for elem in driver.find_elements_by_xpath(xpath):
        if elem.get_attribute('textContent') == text:
            return elem


def by_css_selector_and_text(driver, css_selector, text):
    for elem in driver.find_elements_by_css_selector(css_selector):
        if elem.get_attribute('textContent') == text:
            return elem


def by_class_name_and_value(driver, class_name, value):
    for elem in driver.find_elements_by_class_name(class_name):
        if elem.get_attribute(name='value') == value:
            return elem


def by_class_name_and_custom_attribute(driver, class_name, custom_attribute, value):
    for elem in driver.find_elements_by_class_name(class_name):
        if elem.get_attribute(name=custom_attribute) == value:
            return elem


def login(driver, wait, EC, By):
    domain = driver.find_element_by_id(CE.domain).get_attribute(name='value')
    if CO.domain != domain:
        raise Exception('Wrong domain')
    driver.find_element_by_name(CE.username).send_keys(CO.test_user_name)
    driver.find_element_by_name(CE.password).send_keys(CO.password)
    driver.find_element_by_id(CE.login_button).click()
    wait.until(EC.element_to_be_clickable((By.ID, CE.formheader)))
    if not driver.find_element_by_id(CE.formheader):
        raise Exception('Form header not found')
    environment = driver.find_element_by_id(CE.select_environment).get_attribute('textContent')
    if CO.default_test_environment != environment:
        raise Exception('Wrong Environment')


def login_to_dev(driver, wait, EC, By):
    domain = driver.find_element_by_id(CE.domain).get_attribute(name='value')
    if CO.domain != domain:
        raise Exception('Wrong domain')
    driver.find_element_by_name(CE.username).send_keys(CO.dev_user_name)
    driver.find_element_by_name(CE.password).send_keys(CO.password)
    driver.find_element_by_id(CE.login_button).click()
    wait.until(EC.element_to_be_clickable((By.ID, CE.formheader)))
    if not driver.find_element_by_id(CE.formheader):
        raise Exception('Form header not found')
    environment = driver.find_element_by_id(CE.select_environment).get_attribute('textContent')
    if CO.default_dev_environment != environment:
        raise Exception('Wrong Environment')


def start_create_config(driver, datetime, calendar, time):
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

    if not by_class_name_and_text(driver, CE.titlebar_panel, CO.provisioning_config_panel_title):
        raise Exception('Wrong title bar name')

    if not by_id_and_text(driver, CE.config_select_label, CO.select_configuration):
        raise Exception(CO.select_configuration, 'is missing')

    start_time_disabled = driver.find_element_by_id(CE.config_start_time).get_attribute(name='aria-disabled')
    if start_time_disabled != 'true':
        raise Exception('Start time is not disabled')
    if driver.find_element_by_id(CE.config_add).get_attribute(name='aria-disabled') == 'true':
        raise Exception('Add button disabled')
    driver.find_element_by_id(CE.config_add).click()
    driver.find_element_by_id(CE.config_start_time_for_new_config)
    pop_up_title = driver.find_element_by_id(CE.config_start_time_for_new_config_title).get_attribute('textContent')
    if pop_up_title != CO.add_new_config_title:
        raise Exception('Pop-up title incorrect')
    time.sleep(1)

    # data manipulating was here
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
    picker_day_to_select = by_class_name_and_text(driver, CE.config_date_picker_day, tomorrow_day)
    time.sleep(1)
    picker_day_to_select.click()
    time.sleep(1)
    new_start_time = driver.find_element_by_id(CE.config_set_new_start_time).get_attribute(name='value')
    if new_start_time != start_time_set_tomorrow:
        print('new_start_time', new_start_time, "- start_time_set_tomorrow", start_time_set_tomorrow)
        raise Exception('Date is incorrect')

    driver.find_element_by_id(CE.config_start_time_ok_button).click()
    time.sleep(2)
    sets_start_time = driver.find_element_by_id(CE.config_start_time).get_attribute(name='value')
    if sets_start_time == '':
        print('Start time not sets')
        time.sleep(2)
    sets_start_time = driver.find_element_by_id(CE.config_start_time).get_attribute(name='value')
    if sets_start_time != start_time_set_tomorrow:
        print('sets_start_time', sets_start_time, "- start_time_set_tomorrow", start_time_set_tomorrow)
        raise Exception('Date is incorrect')
    new_config = driver.find_element_by_id(CE.config_select_label).get_attribute('textContent')
    if new_config != CO.new_config:
        raise Exception('Wrong config name')


def service_name(service_count):
    return r'#form\3a servicesTable_data > tr:nth-child(' + str(service_count + 1) + ') > td:nth-child(1)'


def service_values(service_count):
    return r'#form\3a servicesTable_data > tr:nth-child(' + str(service_count + 1) + ') > td:nth-child(2)'


def service_value_string_name(service_count):
    return '#form\:servicesTable\:' + str(
        service_count) + '\:serviceValuesTable_data > tr:nth-child(1) > td:nth-child(1)'


def service_value_string_value(service_count):
    return '#form\:servicesTable\:' + str(
        service_count) + '\:serviceValuesTable_data > tr:nth-child(1) > td:nth-child(2)'


def service_value_property_1(service_count):
    return r'#form\:servicesTable\:' + str(
        service_count) + r'\:serviceValuesTable_data > tr:nth-child(1) > td:nth-child(1)'


def service_value_property_value_1(service_count):
    return r'#form\:servicesTable\:' + str(
        service_count) + r'\:serviceValuesTable_data > tr:nth-child(1) > td:nth-child(2)'


def service_value_property_2(service_count):
    return r'#form\:servicesTable\:' + str(
        service_count) + r'\:serviceValuesTable_data > tr:nth-child(2) > td:nth-child(1)'


def service_value_property_value_2(service_count):
    return r'#form\:servicesTable\:' + str(
        service_count) + r'\:serviceValuesTable_data > tr:nth-child(2) > td:nth-child(2)'


def select_config(driver, wait, config_name):
    driver.find_element_by_id(CE.config_select_label).click()
    if 'z-index' not in driver.find_element_by_id(CE.config_select_panel).get_attribute(name='style'):
        driver.find_element_by_id(CE.config_select_label).click()
        if not driver.find_element_by_id(CE.config_select_list):
            raise Exception('The list of configs is missing')
    time.sleep(2)
    item = by_class_name_and_text(driver, CE.menu_list_item, config_name)
    if item:
        item_text = item.get_attribute('textContent')
        item.click()
        wait.until(EC.invisibility_of_element_located((By.ID, CE.loading_bar)))
        item_dd_text = driver.find_element_by_id(CE.config_select_label).get_attribute('textContent')
        if item_text != item_dd_text or item_dd_text != config_name:
            print('\nitem_text:', item_text, 'item_dd_text:', item_dd_text, 'config_name:', config_name)
            raise Exception('Wrong config name')
        return True
    else:
        return False


def user_device_row(ud_count):
    return r'#form\3a tabs\3a dataTable_data > tr:nth-child(' + str(ud_count) + ')'


def wait_until_invisibility(driver, wait, elem):
    driver.implicitly_wait(3)
    if driver.find_elements_by_id(elem):
        wait.until(EC.invisibility_of_element_located((By.ID, elem)))
    driver.implicitly_wait(15)
