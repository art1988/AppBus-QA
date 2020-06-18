new_email_button = mgd.find_element_by_id(mw.new_email_button)
new_email_button.click()
exd1 = 'exadel1@botf03.net'
exd2 = 'exadel2@botf03.net'
name1 = 'Autotest flag'
name2 = 'Autotest sort'

mgd.find_element_by_id(ne.to_field_input).send_keys(exd1)
mgd.find_element_by_id(ne.subject_field_input).send_keys(name1 + ' 01')
mgd.find_element_by_xpath(ne.send_email_button).click()
time.sleep(2)

new_email_button.click()
mgd.find_element_by_id(ne.to_field_input).send_keys(exd1)
mgd.find_element_by_id(ne.subject_field_input).send_keys(name1 + ' 02')
mgd.find_element_by_xpath(ne.send_email_button).click()
time.sleep(2)

new_email_button.click()
mgd.find_element_by_id(ne.to_field_input).send_keys(exd1)
mgd.find_element_by_id(ne.subject_field_input).send_keys(name2 + ' 01')
mgd.find_element_by_xpath(ne.send_email_button).click()
time.sleep(2)

new_email_button.click()
mgd.find_element_by_id(ne.to_field_input).send_keys(exd1)
mgd.find_element_by_id(ne.common).send_keys(name2 + ' 02')
mgd.find_element_by_xpath(ne.send_email_button).click()
time.sleep(2)

new_email_button.click()
mgd.find_element_by_id(ne.to_field_input).send_keys(exd1)
mgd.find_element_by_id(ne.subject_field_input).send_keys(name2 + ' 03')
mgd.find_element_by_xpath(ne.send_email_button).click()

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
    mgd.find_element_by_xpath(mw.sorting_date_arrow_icon).click()
time.sleep(2)

if 'opened' in sorting_dropdawn_list:
    mgd.find_element_by_id(mw.small_sorting_button).click()
time.sleep(2)

wait.until(ec.visibility_of_element_located((By.ID, mw.list)))
# mgd.find_element_by_xpath(mw.flag_in_2th_message).click()
Check.flag_in_n_message_click('2')