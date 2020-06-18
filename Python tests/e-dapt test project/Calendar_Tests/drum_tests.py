import time
from datetime import datetime, timedelta
from datetime import timedelta
import calendar
import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
import Check
import Config.Calendar
from Config.Calendar import main_calendar
from main_app_window import Maw, driver_instance
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytz

mgd = Maw.get_devices()
cal = Config.Calendar.main_calendar.Elements
driver_instance.implicitly_wait(5)
wait = WebDriverWait(mgd, 10)
timezone_default = 'Asia/Yekaterinburg'


def setUpModule():
    print('Start: calendar_tests.py\n')


def tearDownModule():
    print('End: calendar_tests.py\n')
    # driver_instance.quit()


# @unittest.skip('Ok')
class Test3StartsEndsDrum(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            if Check.check_exists_by_id(cal.close_edit_button):
                mgd.find_element_by_id(cal.close_edit_button).click()
            if Check.check_exists_by_class_name(cal.apply_unsaved_changes):
                print('Block wrapper "Apply unsaved changes" - exist')
                mgd.find_element_by_xpath(cal.no_apply_unsaved_changes).click()

            mgd.find_element_by_class_name(cal.today_button).click()
            view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Week')
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Week View is selected')
            else:
                view_button.click()
                view_button_select = view_button.get_attribute(name='class')
                if 'selected' in view_button_select:
                    print('Check - Week View is selected')
                else:
                    raise Exception('Week view is not selectable')

            mgd.find_element_by_id(cal.spinner).click()
            # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, cal.rotated)))
            time.sleep(2)

            view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Day')
            view_button_select = view_button.get_attribute(name='class')
            if 'selected' in view_button_select:
                print('Check - Day View is selected')
            else:
                view_button.click()
                view_button_select = view_button.get_attribute(name='class')
                if 'selected' in view_button_select:
                    print('Check - Day View is selected')
                else:
                    raise Exception('Day view is not selectable')

        @classmethod
        def tearDownClass(cls):
            pass

        def setUp(self):
            mgd.find_element_by_id(cal.add_event_button).click()
            wait.until(ec.visibility_of_element_located((By.CLASS_NAME, cal.edit_event)))
            print('Check - window Edit event is open\n')

        def tearDown(self):
            if Check.check_exists_by_id(cal.close_edit_button):
                mgd.find_element_by_id(cal.close_edit_button).click()
            if Check.check_exists_by_class_name(cal.apply_unsaved_changes):
                print('Block wrapper "Apply unsaved changes" - exist')
                mgd.find_element_by_xpath(cal.no_apply_unsaved_changes).click()

        def test2_drum_starts_hours_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=60)
            time_delta_2 = timedelta(hours=11)
            modify_time = starts_time_1 + time_delta
            modify_time_2 = starts_time_1 - time_delta_2
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_hours)
            first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if second_value == '12':
                if modify_time_2 == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif second_value != '12':
                if modify_time == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_ends_hours_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=60)
            time_delta_2 = timedelta(hours=11)
            modify_time = ends_time_1 + time_delta
            modify_time_2 = ends_time_1 - time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_hours)
            first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_hours_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

            if second_value == '12':
                if modify_time_2 == ends_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif second_value != '12':
                if modify_time == ends_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_starts_minutes_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=5)
            modify_time = starts_time_1 + time_delta
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_minutes)
            first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_minutes_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=5)
            modify_time = ends_time_1 + time_delta
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_minutes)
            first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

            if modify_time == ends_time_2:
                print('Check - Ends time is right')
            else:
                raise Exception('Ends time is incorrect')

        def test2_drum_starts_hours_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=60)
            time_delta_2 = timedelta(hours=11)
            modify_time = starts_time_1 - time_delta
            modify_time_2 = starts_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_hours)
            first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_hours_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
            time.sleep(1)

            second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            if second_value == '11':
                if modify_time_2 == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif second_value != '11':
                if modify_time == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_ends_hours_up(self):

            now_timezone = mgd.find_element_by_xpath(cal.timezone).get_attribute('innerText')
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(hours=1)
            time_delta_2 = timedelta(hours=11)
            modify_time = ends_time_1 - time_delta
            modify_time_2 = ends_time_1 - time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_hours)
            first_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_hours_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_hours_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.hours).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')

            drum_container = mgd.find_element_by_id(cal.drum_container).get_attribute(name='data-value')
            print('drum_container ', drum_container)
            drum_container_time = datetime.strptime(drum_container[:19], "%Y-%m-%dT%H:%M:%S")
            container_time_tz = drum_container_time.astimezone(pytz.timezone(now_timezone))
            print('tz name ', datetime.tzname(container_time_tz))
            print('drum_container_time ', drum_container_time)
            print('ends_time_1 ', ends_time_1)
            print('container_time_tz ', container_time_tz)
            modify_time = ends_time_1 - time_delta
            print('modify_time ', modify_time)
            if container_time_tz == modify_time:
                print('container_time_tz == modify_time - YES')
            else:
                print('container_time_tz == modify_time - NO')

        def test2_drum_starts_minutes_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=5)
            time_delta_2 = timedelta(minutes=55)
            modify_time = starts_time_1 - time_delta
            modify_time_2 = starts_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_minutes)
            first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if second_value == '55':
                if modify_time_2 == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif second_value != '55':
                if modify_time == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_ends_minutes_up(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(minutes=5)
            time_delta_2 = timedelta(minutes=55)
            modify_time = ends_time_1 - time_delta
            modify_time_2 = ends_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_minutes)
            first_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_minutes_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_minutes_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.minutes).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

            if second_value == '55':
                if modify_time_2 == ends_time_2:
                    print('Check - Ends time is right')
                else:
                    raise Exception('Ends time is incorrect')
            elif second_value != '55':
                if modify_time == ends_time_2:
                    print('Check - Ends time is right')
                else:
                    raise Exception('Ends time is incorrect')
            else:
                raise Exception('Something went wrong')

        def test2_drum_starts_am_pm(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(hours=12)
            modify_time = starts_time_1 + time_delta
            modify_time_2 = starts_time_1 - time_delta
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_ampm)
            first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            if first_value == 'AM':
                hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_down)
                actions = ActionChains(driver_instance)

                actions.move_to_element(hover_drum).click().perform()

                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                try:
                    actions.click(hidden_arrow).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                time.sleep(1)
                second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('second_value', second_value)
                ############
                if second_value == 'PM':
                    print('Check - change of value')
                else:
                    raise Exception('The value is the same')
                mgd.find_element_by_id(cal.yes_edit_button).click()
                time.sleep(1)
                starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

                if second_value == 'PM':
                    if modify_time == starts_time_2:
                        print('Check - Starts time is right')
                    else:
                        raise Exception('Starts time is incorrect')
                else:
                    raise Exception('Something went wrong')

                # second
                mgd.find_element_by_xpath(cal.starts_day_view).click()
                hover_drum = mgd.find_element_by_id(cal.drum_ampm)
                first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('first_value', first_value)
                if first_value == 'PM':
                    hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
                    actions = ActionChains(driver_instance)

                    actions.move_to_element(hover_drum).click().perform()

                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                    try:
                        actions.click(hidden_arrow).perform()
                    except:
                        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                    time.sleep(1)
                    second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                    print('second_value', second_value)
                    ############
                    if second_value == 'AM':
                        print('Check - change of value')
                    else:
                        raise Exception('The value is the same')
                    mgd.find_element_by_id(cal.yes_edit_button).click()
                    time.sleep(1)
                    starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                    starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

                    if second_value == 'AM':
                        if starts_time_1 == starts_time_2:
                            print('Check - Starts time is right')
                        else:
                            raise Exception('Starts time is incorrect')
                    else:
                        raise Exception('Something went wrong')
                else:
                    raise Exception('Wrong interval')
            elif first_value == 'PM':
                hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
                actions = ActionChains(driver_instance)

                actions.move_to_element(hover_drum).click().perform()

                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                try:
                    actions.click(hidden_arrow).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                time.sleep(1)
                second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('second_value', second_value)
                ############
                if second_value == 'AM':
                    print('Check - change of value')
                else:
                    raise Exception('The value is the same')
                mgd.find_element_by_id(cal.yes_edit_button).click()
                time.sleep(1)
                starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

                if second_value == 'AM':
                    if modify_time_2 == starts_time_2:
                        print('Check - Starts time is right')
                    else:
                        raise Exception('Starts time is incorrect')
                else:
                    raise Exception('Something went wrong')

                # second
                mgd.find_element_by_xpath(cal.starts_day_view).click()
                hover_drum = mgd.find_element_by_id(cal.drum_ampm)
                first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('first_value', first_value)
                if first_value == 'AM':
                    hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_down)
                    actions = ActionChains(driver_instance)

                    actions.move_to_element(hover_drum).click().perform()

                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                    try:
                        actions.click(hidden_arrow).perform()
                    except:
                        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                    time.sleep(1)
                    second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                    print('second_value', second_value)
                    ############
                    if second_value == 'PM':
                        print('Check - change of value')
                    else:
                        raise Exception('The value is the same')
                    mgd.find_element_by_id(cal.yes_edit_button).click()
                    time.sleep(1)
                    starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                    starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

                    if second_value == 'PM':
                        print(modify_time)
                        print(modify_time_2)

                        if starts_time_1 == starts_time_2:
                            print('Check - Starts time is right')
                        else:
                            raise Exception('Starts time is incorrect')
                    else:
                        raise Exception('Something went wrong')
                else:
                    raise Exception('Wrong interval')
            else:
                raise Exception('Something went wrong')

        def test2_drum_ends_am_pm(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(hours=12)
            modify_time = ends_time_1 + time_delta
            modify_time_2 = ends_time_1 - time_delta
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_ampm)
            first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            if first_value == 'AM':
                hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_down)
                actions = ActionChains(driver_instance)

                actions.move_to_element(hover_drum).click().perform()

                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                try:
                    actions.click(hidden_arrow).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                time.sleep(1)
                second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('second_value', second_value)
                ############
                if second_value == 'PM':
                    print('Check - change of value')
                else:
                    raise Exception('The value is the same')
                time.sleep(1)
                yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                if 'disabled' in yes_button_attr:
                    print('Check - Yes button not disabled')
                else:
                    raise Exception('For Yes button "disabled" is missing')
                message = 'The date should be after'
                error_message = mgd.find_element_by_class_name(cal.data_error_drum).get_attribute('innerText')
                if message not in error_message:
                    raise Exception('Error message not found', 'error_message -', error_message)
                print('Check - error message')

                # second
                mgd.find_element_by_xpath(cal.ends_day_view).click()
                hover_drum = mgd.find_element_by_id(cal.drum_ampm)
                first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('first_value', first_value)
                if first_value == 'PM':
                    hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
                    actions = ActionChains(driver_instance)

                    actions.move_to_element(hover_drum).click().perform()

                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                    try:
                        actions.click(hidden_arrow).perform()
                    except:
                        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                    time.sleep(1)
                    second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                    print('second_value', second_value)
                    ############
                    if second_value == 'AM':
                        print('Check - change of value')
                    else:
                        raise Exception('The value is the same')
                    yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                    if 'disabled' in yes_button_attr:
                        print('Check - Yes button not disabled')
                    else:
                        raise Exception('For Yes button "disabled" is missing')
                    Check.find_element_by_class_name_and_text(cal.data_error_drum, 'The date should be after')
                    print('Check - error message')
                    # mgd.find_element_by_id(cal.yes_edit_button).click()
                    # time.sleep(1)
                    # ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
                    # ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

                #     if second_value == 'AM':
                #         if ends_time_1 == ends_time_2:
                #             print('Check - 2Ends time is right')
                #         else:
                #             raise Exception('Ends time is incorrect')
                #     else:
                #         raise Exception('Something went wrong')
                # else:
                #     raise Exception('Wrong interval')
            elif first_value == 'PM':
                hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_up)
                actions = ActionChains(driver_instance)

                actions.move_to_element(hover_drum).click().perform()

                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                try:
                    actions.click(hidden_arrow).perform()
                except:
                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_up)))
                time.sleep(1)
                second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('second_value', second_value)
                ############
                if second_value == 'AM':
                    print('Check - change of value')
                else:
                    raise Exception('The value is the same')
                yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                if 'disabled' in yes_button_attr:
                    print('Check - Yes button disabled')
                else:
                    raise Exception('For Yes button "disabled" is missing')
                Check.find_element_by_class_name_and_text(cal.data_error_drum, 'The date should be after')
                print('Check - error message')
                # mgd.find_element_by_id(cal.yes_edit_button).click()
                # time.sleep(1)
                # ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
                # ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
                #
                # if second_value == 'AM':
                #     if modify_time_2 == ends_time_2:
                #         print('Check - 3Ends time is right')
                #     else:
                #         raise Exception('Ends time is incorrect')
                # else:
                #     raise Exception('Something went wrong')

                # second

                # mgd.find_element_by_xpath(cal.ends_day_view).click()
                hover_drum = mgd.find_element_by_id(cal.drum_ampm)
                first_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                print('first_value', first_value)
                if first_value == 'AM':
                    hidden_arrow = mgd.find_element_by_id(cal.drum_ampm_down)
                    actions = ActionChains(driver_instance)

                    actions.move_to_element(hover_drum).click().perform()

                    wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                    try:
                        actions.click(hidden_arrow).perform()
                    except:
                        wait.until(ec.element_to_be_clickable((By.ID, cal.drum_ampm_down)))
                    time.sleep(1)
                    second_value = mgd.find_element_by_id(cal.ampm).get_attribute(name='data-drum-value')
                    print('second_value', second_value)
                    ############
                    if second_value == 'PM':
                        print('Check - change of value')
                    else:
                        raise Exception('The value is the same')
                    yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                    if 'disabled' in yes_button_attr:
                        raise Exception('Check - Yes button not disabled')

                    if Check.find_element_by_class_name_and_text(
                            cal.data_error_drum, 'The date should be after') is not None:
                        raise Exception('Error message exist')

                    mgd.find_element_by_id(cal.yes_edit_button).click()
                    time.sleep(1)
                    ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
                    ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

                    if second_value == 'PM':
                        print(modify_time)
                        print(modify_time_2)

                        if ends_time_1 == ends_time_2:
                            print('Check - 4Ends time is right')
                        else:
                            raise Exception('Ends time is incorrect')
                    else:
                        raise Exception('Something went wrong')
                else:
                    raise Exception('Wrong interval')
            else:
                raise Exception('Something went wrong')

        def test2_drum_starts_day_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1)
            time_delta_2 = timedelta(days=11)
            modify_time = starts_time_1 + time_delta
            modify_time_2 = starts_time_1 - time_delta
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_day)
            first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")

            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_day_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1)
            time_delta_2 = timedelta(days=11)
            modify_time = ends_time_1 + time_delta
            modify_time_2 = ends_time_1 - time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_day)
            first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_day_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")

            if modify_time == ends_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_starts_day_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1)
            today_month = datetime.now().strftime("%m")
            today_year = datetime.now().strftime("%Y")
            calendar_days = calendar.monthrange(int(today_year), int(today_month))
            time_delta_2 = timedelta(days=int(calendar_days[1]) - 1)
            modify_time = starts_time_1 - time_delta
            modify_time_2 = starts_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_day)
            first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
            time.sleep(1)

            second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            if first_value != '1':
                mgd.find_element_by_id(cal.yes_edit_button).click()
                time.sleep(1)
                starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
                print('modify_time', modify_time)
                print('starts_time_2', starts_time_2)

                if modify_time == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')
            elif first_value == '1':
                mgd.find_element_by_id(cal.yes_edit_button).click()
                time.sleep(1)
                starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
                starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
                print('modify_time_2', modify_time_2)
                print('starts_time_2', starts_time_2)

                if modify_time_2 == starts_time_2:
                    print('Check - Starts time is right')
                else:
                    raise Exception('Starts time is incorrect')

        def test2_drum_ends_day_up(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1)
            time_delta_2 = timedelta(days=11)
            modify_time = ends_time_1 - time_delta
            modify_time_2 = ends_time_1 + time_delta_2
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_day)
            first_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_day_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_day_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.day).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            if first_value != '1':
                yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
                if 'disabled' in yes_button_attr:
                    print('Check - Yes button disabled')
                else:
                    raise Exception('For Yes button "disabled" is missing')
                Check.find_element_by_class_name_and_text(cal.data_error_drum, 'The date should be after')

        def test2_drum_starts_month_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=5)
            modify_time = starts_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_month)
            first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print('modify_time', modify_time)
            print('starts_time_2', starts_time_2)
            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_month_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=5)
            modify_time = ends_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_month)
            first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_month_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print('modify_time', modify_time)
            print('ends_time_2', ends_time_2)
            if modify_time == ends_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_starts_month_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=4)
            modify_time = starts_time_1 - time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_month)
            first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
            time.sleep(1)

            second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(starts_time_2)
            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_month_up(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=4)
            modify_time = ends_time_1 - time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_month)
            first_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_month_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_month_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.month).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            yes_button_attr = mgd.find_element_by_id(cal.yes_edit_button).get_attribute(name='class')
            if 'disabled' in yes_button_attr:
                print('Check - Yes button disabled')
            else:
                raise Exception('For Yes button "disabled" is missing')
            Check.find_element_by_class_name_and_text(cal.data_error_drum, 'The date should be after')

        def test2_drum_starts_year_down(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1, weeks=52)
            modify_time = starts_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_year)
            first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(starts_time_2)
            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_year_down(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(days=1, weeks=52)
            modify_time = ends_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_year)
            first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_year_down)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_down)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print('modify_time', modify_time)
            print('ends_time_2', ends_time_2)
            if modify_time == ends_time_2:
                print('Check - Ends time is right')
            else:
                raise Exception('Ends time is incorrect')

        def test2_drum_starts_year_up(self):
            starts_1 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_1 = datetime.strptime(starts_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=2609)
            modify_time = starts_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.starts_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_year)
            first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_year_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            starts_2 = mgd.find_element_by_xpath(cal.starts_day_view).get_attribute('innerText')
            starts_time_2 = datetime.strptime(starts_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(starts_time_2)
            if modify_time == starts_time_2:
                print('Check - Starts time is right')
            else:
                raise Exception('Starts time is incorrect')

        def test2_drum_ends_year_up(self):
            ends_1 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_1 = datetime.strptime(ends_1, "%d %b %Y %I:%M %p")
            time_delta = timedelta(weeks=2609)
            modify_time = ends_time_1 + time_delta
            today_day = datetime.now().strftime("%d")
            mgd.find_element_by_xpath(cal.ends_day_view).click()

            #################
            hover_drum = mgd.find_element_by_id(cal.drum_year)
            first_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('first_value', first_value)
            hidden_arrow = mgd.find_element_by_id(cal.drum_year_up)
            actions = ActionChains(driver_instance)

            actions.move_to_element(hover_drum).click().perform()

            wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
            try:
                actions.click(hidden_arrow).perform()
            except:
                wait.until(ec.element_to_be_clickable((By.ID, cal.drum_year_up)))
            time.sleep(1)
            second_value = mgd.find_element_by_id(cal.year).get_attribute(name='data-drum-value')
            print('second_value', second_value)
            ############
            if first_value != second_value:
                print('Check - change of value')
            else:
                raise Exception('The value is the same')
            mgd.find_element_by_id(cal.yes_edit_button).click()
            time.sleep(1)
            ends_2 = mgd.find_element_by_xpath(cal.ends_day_view).get_attribute('innerText')
            ends_time_2 = datetime.strptime(ends_2, "%d %b %Y %I:%M %p")
            modify_time = modify_time.replace(day=int(today_day))
            print(modify_time)
            print(ends_time_2)
            if modify_time == ends_time_2:
                print('Check - Ends time is right')
            else:
                raise Exception('Ends time is incorrect')
