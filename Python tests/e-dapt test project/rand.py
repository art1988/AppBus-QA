# import random
# qwe = 4
# sequence = [0, 1, 2, 3, 4, 5, 6]
# sequence.remove(qwe)
# day_1 = random.choice(sequence)
# print('d1 ', day_1)
# sequence.remove(day_1)
#
# day_2 = random.choice(sequence)
# print('d2 ', day_2)
# sequence.remove(day_2)
#
# day_3 = random.choice(sequence)
# print('d3 ', day_3)
# sequence.remove(day_3)
#
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))
# print(random.choice(sequence))


# a = [1,2,3,4,5,6,7]
# b = 4
# c = a.index(b)
# print(c)
# d = a[c + 1:]
# print(d)
# # print(a[:-1])
# # print(a[:1])
# # print(a[:2])
# # print(a[2:])
# # print(a[2])
# # print(a[-2], a[-1])

# import time
# from datetime import datetime, timedelta
# from datetime import timedelta
# import calendar
# import unittest
# import random
# from selenium import webdriver
# import Check
# import Config.Calendar
# from Config.Calendar import main_calendar
# from main_app_window import Maw, driver_instance
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import pytz
# import datetime
# from datetime import datetime, timedelta
# from datetime import timedelta
# import calendar
# import Check
# import Config.Calendar
# from Config.Calendar import main_calendar
#
# mgd = Maw.get_devices()
# cal = Config.Calendar.main_calendar.Elements
# driver_instance.implicitly_wait(5)
# wait = WebDriverWait(mgd, 20)
# timezone_default = 'Asia/Yekaterinburg'

# def week(year, month, day):
#     first_week_month = datetime.datetime(year, month, 1).isocalendar()[1]
#     print(first_week_month)
#     if month == 1 and first_week_month > 10:
#         first_week_month = 0
#     user_date = datetime.datetime(year, month, day).isocalendar()[1]
#     if month == 1 and user_date > 10:
#         user_date = 0
#     print(user_date - first_week_month)
#     return user_date - first_week_month
#
# print(week(2018, 5, 29))
###########################################################################################

# event_name = 'TestRepEvent_4'
# current_time = datetime.now()
# now_time = current_time.strftime("%H:%M")
# now_day = current_time.strftime('%d')
# now_data = current_time.strftime('%Y %m %d')
# now_week_day = current_time.strftime('%w')
# split = now_data.split(' ')
# print(split)
# now_data_year = split[0]
# now_data_month = split[1]
# now_data_day = split[2]
# if now_data_month[0] == '0':
#     now_data_month = now_data_month[1:]
# if now_data_day[0] == '0':
#     now_data_day = now_data_day[1:]
#
# cal_detail = calendar.monthrange(int(now_data_year), int(now_data_month))
# print('cal_detail', cal_detail)
# last_day = cal_detail[1]
# last_week = Check.week_of_month(int(now_data_year), int(now_data_month), last_day)
# print('last_week', last_week)

# td = last_day - int(now_data_day)
# print('td', td)
# dtime = timedelta(days=td)
# modify_time = current_time + dtime
# print('modify_time', modify_time)
# modify_data = modify_time.strftime('%Y %m %d')
# modify_week_day = modify_time.strftime('%w')
# modify_split = modify_data.split(' ')
# print(modify_split)
# modify_data_year = modify_split[0]
# modify_data_month = modify_split[1]
# modify_data_day = modify_split[2]
# if modify_data_month[0] == '0':
#     modify_data_month = modify_data_month[1:]
# if modify_data_day[0] == '0':
#     modify_data_day = modify_data_day[1:]
#
# print('modify_week_day', modify_week_day)
# print('modify_data_year', modify_data_year)
# print('modify_data_month', modify_data_month)
# print('modify_data_day', modify_data_day)

# view_button = Check.find_element_by_class_name_and_text(cal.view_button, 'Month')
# view_button_select = view_button.get_attribute(name='class')
# if 'selected' in view_button_select:
#     print('Check - Month View is selected')
# else:
#     view_button.click()
#     view_button_select = view_button.get_attribute(name='class')
#     if 'selected' in view_button_select:
#         print('Check - Month View is selected')
#     else:
#         raise Exception('Month view is not selectable')


#############################################
# mgd.find_element_by_class_name(cal.navigation_right).click()
# print('Check - Right button')
# month_title = mgd.find_element_by_class_name(cal.navigation_title).get_attribute('innerText')
# month_title_list = month_title.split(' ')
# print('month_title_list', month_title_list)
# new_month_year = month_title_list[1]
# new_month_month_abbr = month_title_list[0]
# #
# new_month_month = time.strptime(new_month_month_abbr, '%b').tm_mon
# print('new_month_year', new_month_year)
# print('new_month_month', new_month_month)
# if len(str(new_month_month)) == 1:
#     new_month_month = '0' + str(new_month_month)
# print('new_month_month', new_month_month)
#
# cal_new_month_detail = calendar.monthrange(int(new_month_year), int(new_month_month))
# print('cal_detail', cal_new_month_detail)
# new_month_last_day = cal_new_month_detail[1]
# last_week_in_new_month = Check.week_of_month(int(new_month_year), int(new_month_month), new_month_last_day)
# print('last_week_in_new_month', last_week_in_new_month)

#########################################################################################################

# Check.day_of_week_in_month(str(new_month_year), new_month_month, 5, 'Saturday')


