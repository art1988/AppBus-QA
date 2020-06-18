class Other:
    dev_login_url = 'https://128.66.200.101:9613/edapt-admin'
    test_login_url = 'https://dev-msa-qa.botf03.net:9613/edapt-admin/login.jsp'

    #######
    domain = 'botf03.net'
    dev_user_name = 'milshtyu'
    test_user_name = 'edapt-setup'
    password = '511maps'
    ######

    default_test_environment = 'edapt-demo'
    default_dev_environment = 'edapt'

    # Provisioning Config
    provisioning_config_panel_title = 'Device management > Provisioning Config'
    select_configuration = '---- Select configuration -----'
    select_type = '---- Select type -----'
    gateway_select_type = '---- Select type ----'
    service_select_gateway = '---- Select gateway ----'
    current_config = 'Current config'
    upcoming_config = 'Upcoming config'
    add_new_config_title = 'Add new config'
    new_config = 'New config'
    ui_button = 'ui-button'
    ui_state_disabled = 'ui-state-disabled'
    table_ok_mark = 'ok-mark-24.png'
    table_x_mark = 'x-mark-24.png'
    config_service_property_values_no_records = 'No records found.'
    user_details_no_records = 'No records were found'
    sure_to_delete = 'Sure to delete?'
    error_expired_config = ''
    error_do_not_have_current_config = "You don't have current config. To work correct move one of " \
                                       "the upcoming configs to current by changing start date."

    # User Devices
    find_devices_tab = 'Find Devices'
    review_wipe_list_tab = 'Review Wipe-List'
    os_versions_tab = 'OS Versions'
    ios_input = 'IOS'
    android_input = 'ANDROID'
    windows_input = 'WINDOWS'
    osx_input = 'OSX'

    # Notification messages
    message_successfully_saved = 'Successfully saved.'
    message_successfully_deleted = 'Successfully deleted.'
    message_certificate_successfully_uploaded = 'Certificate has been successfully uploaded.'
    certificate_missing_name = "Field 'Certificate name:' cannot be empty."
    gateway_missing_name = "Field 'gatewayDlgForm:gatewayDlgName' cannot be empty."
    gateway_missing_client = "Field 'Client dropdown:' cannot be empty."
    gateway_missing_trust = "Field 'Trust dropdown:' cannot be empty."
    gateway_invalid_format = 'Invalid format or value (value must be less then 99999999 and more then 0)'
    gateway_already_exists = 'Gateway with this name already exists.'
    service_missing_name = "Field 'Name:' cannot be empty."
    service_name_already_exists = 'Service with this name already exists.'
    service_property_successfully_deleted = 'Successfully deleted.'
    upload_config_do_not_forget = "Uploaded config. Don't forget to save."
    start_time_changed = 'Start time has been successfully changed.'
    unable_to_remove_certificate = "Unable to remove certificate. Probably, it's used by one of gateways."
    unable_to_remove_gateway = "Unable to remove gateway. Probably, it's used by one of services."
    certificate_invalid_date_for_config = 'Invalid date for the config type.'

    # Container
    item_unchecked = 'ui-selectcheckboxmenu-unchecked'
    item_checked = 'ui-selectcheckboxmenu-checked'
    no_records_found = 'No records found.'

    # Email Groups
    reassign_error = '1_test_email_group is in use. Please reassign it on Alerts page '

    # Device Log
    decoded_folder = 'Decoded'
    encoded_folder = 'Encoded'
    failed_folder = 'Failed'
    temporary_folder = 'Temporary'
    aria_sort_ascending = 'ascending'
    aria_sort_descending = 'descending'
    aria_sort_other = 'other'


class Elements:

    # Login
    #
    # id
    domain = 'domain'
    login_button = 'loginButton'
    reset = 'resetButton'

    # name
    username = 'username'
    password = 'password'

    # css_selector

    # Main
    #
    # id
    loading_bar = 'ajaxLoadingBar_modal'
    pop_up_form = 'form'

    # Menu bar
    #
    # id
    formheader = 'formheader'
    environment_menu = 'environmentMenu'
    select_environment = 'environmentForm:environmentSelect_label'

    # class name
    main_notification_title = 'ui-growl-title'
    main_notification_message = 'ui-growl-message'

    # provisioning config
    #
    # id
    config_select_label = 'form:configsSelect_label'
    config_select_list = 'form:configsSelect_items'
    config_select_panel = 'form:configsSelect_panel'
    config_item_1 = 'form:configsSelect_1'
    config_item_2 = 'form:configsSelect_2'
    config_start_time = 'form:configStartTime_input'
    config_add = 'form:addConfigButton'
    config_start_time_for_new_config = 'setStartTimeForNewConfigDlg'
    config_start_time_for_new_config_title = 'setStartTimeForNewConfigDlg_title'
    config_set_new_start_time = 'setStartTimeForNewConfigForm:setStartTimeForNewConfigCalendar_input'
    config_start_time_ok_button = 'setStartTimeForNewConfigForm:setStartTimeForNewConfigButton'
    config_copy = 'form:copyConfigButton'
    config_delete = 'form:deleteConfigButton'
    config_select_file = 'form:jsonUpload_input'
    config_upload = 'form:uploadConfigButton'
    config_download = 'form:downloadConfigButton'
    config_revert = 'form:revertConfigButton'
    config_apply = 'form:saveConfigButton'
    config_add_certificate = 'form:certificatesTable:addCertificate'
    config_edit_certificate_0 = 'form:certificatesTable:0:editCertificate'
    config_delete_certificate_0 = 'form:certificatesTable:0:removeCertificate'
    config_delete_certificate_conform = 'certificateRemoveDlgForm:yesButtonCertificate'
    config_download_certificate_1 = 'form:certificatesTable:1:downloadCertificate'
    config_cert_modal = 'certificateDlg_modal'
    config_cert_name = 'certificateDlgForm:certificateDlgName'
    config_cert_select_file = 'certificateDlgForm:certificateDataChooseButton_input'
    config_cert_false_uploaded = 'certificateDlgForm:dataUploadedFalse'
    config_cert_true_uploaded = 'certificateDlgForm:dataUploadedTrue'
    config_cert_type = 'certificateDlgForm:certificateDlgTypeSelect'
    config_cert_type_drop_down = 'certificateDlgForm:certificateDlgTypeSelect_label'
    config_cert_password = 'certificateDlgForm:certificateDlgPassword'
    config_cert_select_type_list = 'certificateDlgForm:certificateDlgTypeSelect_items'
    config_add_gateway = 'form:gatewaysTable:addGateway'
    config_delete_gateway_conform = 'gatewayRemoveDlgForm:yesButtonGateway'
    config_add_service = 'form:servicesTable:addService'
    config_delete_service_conform = 'serviceRemoveDlgForm:yesButtonservice'
    config_cert_type_item_1 = 'certificateDlgForm:certificateDlgTypeSelect_1'
    config_cert_type_item_2 = 'certificateDlgForm:certificateDlgTypeSelect_2'
    config_cert_save_changes = 'certificateDlgForm:saveCertificateChanges'
    cert_table_0_data_name = 'form:certificatesTable:0:certificateName'
    cert_table_1_data_name = 'form:certificatesTable:1:certificateName'
    cert_table_2_data_name = 'form:certificatesTable:2:certificateName'
    cert_table_0_data_type = 'form:certificatesTable:0:certificateType'
    cert_table_1_data_type = 'form:certificatesTable:1:certificateType'
    cert_table_2_data_type = 'form:certificatesTable:2:certificateType'
    cert_table_0_data_password = 'form:certificatesTable:0:certificatePassword'
    cert_table_1_data_password = 'form:certificatesTable:1:certificatePassword'
    cert_table_2_data_password = 'form:certificatesTable:2:certificatePassword'
    config_gateway_name = 'gatewayDlgForm:gatewayDlgName'
    config_gateway_client_dd = 'gatewayDlgForm:gatewayClientSelect_label'
    config_gateway_client_list = 'gatewayDlgForm:gatewayClientSelect_items'
    config_gateway_client_items = 'gatewayDlgForm:gatewayClientSelect_'  # number after '_'
    config_gateway_trust_dd = 'gatewayDlgForm:gatewayTrustSelect_label'
    config_gateway_trust_list = 'gatewayDlgForm:gatewayTrustSelect_items'
    config_gateway_trust_items = 'gatewayDlgForm:gatewayTrustSelect_'  # number after '_'
    config_gateway_port = 'gatewayDlgForm:gatewayDlgPort'
    config_gateway_host = 'gatewayDlgForm:gatewayDlgHost'
    config_gateway_save = 'gatewayDlgForm:gatewayDlgSaveButton'
    config_gateway_cancel = 'gatewayDlgForm:gatewayDlgCancelButton'
    gateway_table_0_name = 'form:gatewaysTable:0:gatewayName'
    gateway_table_0_client = 'form:gatewaysTable:0:gatewayClient'
    gateway_table_0_trust = 'form:gatewaysTable:0:gatewayTrust'
    gateway_table_0_port = 'form:gatewaysTable:0:gatewayPort'
    gateway_table_0_host = 'form:gatewaysTable:0:gatewayHost'
    gateway_table_1_name = 'form:gatewaysTable:1:gatewayName'
    gateway_table_1_client = 'form:gatewaysTable:1:gatewayClient'
    gateway_table_1_trust = 'form:gatewaysTable:1:gatewayTrust'
    gateway_table_1_port = 'form:gatewaysTable:1:gatewayPort'
    gateway_table_1_host = 'form:gatewaysTable:1:gatewayHost'
    config_service_name = 'serviceDlgForm:serviceDlgName'
    config_service_select_gateway = 'serviceDlgForm:serviceDlgGatewaySelect_label'
    config_service_select_gateway_list = 'serviceDlgForm:serviceDlgGatewaySelect_items'
    config_service_select_gateway_items = 'serviceDlgForm:serviceDlgGatewaySelect_'  # number after '_'
    config_service_property_values = 'serviceDlgForm:serviceDlgValuesTable_data'
    config_service_add_button = 'serviceDlgForm:serviceDlgValuesTable:serviceDlgValuesTableAddButton'
    config_service_add_dialog = 'addServiceEntryValueDlg'
    config_service_add_select = 'addServiceEntryDlgForm:addServiceEntryDropDown'
    config_service_add_select_label = 'addServiceEntryDlgForm:addServiceEntryDropDown_label'
    config_service_add_select_list = 'addServiceEntryDlgForm:addServiceEntryDropDown_items'
    config_service_add_select_items = 'addServiceEntryDlgForm:addServiceEntryDropDown_'             # number after '_'
    config_service_add_ok = 'addServiceEntryDlgForm:addServiceEntryValueDlgConfrim'
    # config_service_detail_property_value = 'serviceDlgForm:serviceDlgValuesTable:0:j_idt309'
    config_service_detail_delete_action = 'serviceDlgForm:serviceDlgValuesTable:0:serviceDlgValuesTableRemoveButton'
    config_service_save = 'serviceDlgForm:serviceDlgSaveButton'
    config_service_cancel = 'serviceDlgForm:serviceDlgCancelButton'
    config_delete_modal = 'configRemoveConfirmDlg'

    # class_name
    titlebar_panel = 'ui-panel-titlebar'
    dialog_titlebar = 'ui-dialog-titlebar'
    dialog_message = 'ui-confirm-dialog-message'
    content_panel = 'ui-panel-content'
    file_name_for_upload = 'ui-fileupload-filename'
    # config_items = 'ui-selectonemenu-list-item'
    menu_list_item = 'ui-selectonemenu-list-item'
    widget_overlay = 'ui-widget-overlay'
    config_date_picker_month = 'ui-datepicker-month'
    config_date_picker_year = 'ui-datepicker-year'
    config_date_picker_day = 'ui-state-default'
    config_date_picker_day_highlight = 'ui-state-highlight'
    config_date_picker_day_highlight_plus = 'ui-state-default ui-state-highlight'
    config_date_picker_next = 'ui-datepicker-next'
    config_date_picker_prev = 'ui-datepicker-prev'
    config_date_picker_div = 'ui-datepicker-div'
    config_buttons = 'ui-button-text'
    config_cert_progress_bar = 'ui-progressbar'
    config_error_panel = 'form:errorPanel'
    config_delete_expired_config = 'form:deleteExpiredConfig'
    config_make_upcoming = 'form:turnExpiredToUpcoming'
    config_start_time_for_expired_config = 'setNewStartTimeForExpiredConfigDlg'
    config_start_time_for_expired_config_modal = 'setNewStartTimeForExpiredConfigDlg_modal'
    config_time_for_expired_input = 'setNewStartTimeForExpiredConfigForm:newStartTimeForExpiredConfigCalendar_input'
    config_ok_for_expired_input = 'setNewStartTimeForExpiredConfigForm:updateExpiredConfig'

    # css_selector
    config_cert_upload_file_name = 'div.ui-fileupload-files > div > div > div:nth-child(2)'
    config_cert_upload_file_size = 'div.ui-fileupload-files > div > div > div:nth-child(3)'
    config_service_add_value_close = '#addServiceEntryValueDlg > div.ui-dialog-titlebar.ui-widget-header.ui-helper-clearfix.ui-corner-top.ui-draggable-handle > a'
    cert_table_0_data_img = r'#form\3a certificatesTable_data > tr:nth-child(1) > td:nth-child(2) > img'
    cert_table_1_data_img = r'#form\3a certificatesTable_data > tr.ui-widget-content.ui-datatable-odd > td:nth-child(2) > img'
    cert_table_2_data_img = r'#form\3a certificatesTable_data > tr:nth-child(3) > td:nth-child(2) > img'
    service_table_0_name = r'#form\3a servicesTable_data > tr:nth-child(1) > td:nth-child(1)'
    details_value_property_name = r'#serviceDlgForm\3a serviceDlgValuesTable_data > tr > td:nth-child(1)'
    date_picker_day_css = '.ui-datepicker-calendar .ui-state-default'
    config_service_detail_property_value = '#serviceDlgForm\:serviceDlgValuesTable_data > tr:nth-child(1) > td:nth-child(2)'

    # xpath
    config_cert_cancel_upload = '//*[@id="certificateDlgForm:certificateDataChooseButton"]/div[1]/button[2]'

    # User Devices
    #
    # id
    find_devices_content = 'form:tabs:findDevicesTab'
    wipe_list_content = 'form:tabs:reviewWipeListTab'
    os_version_content = 'form:tabs:osVersionsTab'
    lookup_button = 'form:tabs:lookupButton'
    founds_data_table_forms = 'form:tabs:dataTableForm'
    fd_select_column = 'form:tabs:dataTable:selectAll'
    fd_device_id_column = 'form:tabs:dataTable:deviceId'
    fd_last_login_column = 'form:tabs:dataTable:lastlogin'
    fd_last_status_column = 'form:tabs:dataTable:status'
    fd_table = 'form:tabs:dataTable_data'
    wipe_button = 'form:tabs:wipe'
    refresh_button = 'form:tabs:refresh'
    os_type_dd = 'form:tabs:osTypeFilter_label'
    os_type_dd_list = 'form:tabs:osTypeFilter_items'
    os_detailed_chart = 'form:tabs:detailedChartCheckboxFilter'
    os_start_date = 'form:tabs:startDateFilter'
    os_ends_date = 'form:tabs:endDateFilter'
    os_apply_button = 'form:tabs:applyButton'
    os_dd_list_n_string = 'form:tabs:osTypeFilter_'
    rpp_options = 'dataTableForm:dataTable:j_id36'

    # Class Name
    ud_tabs_to_select = 'ui-corner-top'
    user_dd_select = 'ui-selectonemenu-trigger'
    check_box_main = 'ui-chkbox-box'
    row_highlight = 'ui-state-highlight'
    row_aria_selected = 'aria-selected'
    os_chart_canvas = 'jqplot-event-canvas'

    # Name
    user_input = 'form:tabs:user_editableInput'

    # Css celector
    cart_panel = r'#form\3a tabs\3a chartPanel > span'


class UserDetailsElements:

    # id
    filter_form = 'form:filter'
    filter_toggler = 'form:filter_toggler'
    filter_header = 'form:filter_header'
    user_dropdown = 'form:userDropDownList'
    start_date = 'form:startDateFilter_input'
    end_date = 'form:endDateFilter_input'
    apply_button = 'form:applyButton'
    user_session_statistic_table = 'dataTableForm:dataTable'
    statistic_table_head = 'dataTableForm:dataTable_head'
    statistic_table_data = 'dataTableForm:dataTable_data'
    navigation_actions_dialog = 'dataTableForm:navigationDlg'
    navigation_actions_head = 'dataTableForm:navigationTable_head'
    navigation_actions_data = 'dataTableForm:navigationTable_data'
    close_nav_actions_button = 'dataTableForm:closeButton'
    date_picker = 'ui-datepicker-div'

    # css selector
    start_calendar_button = r'#form\:startDateFilter > button:nth-child(2)'
    end_calendar_button = r'#form\:endDateFilter > button:nth-child(2)'
    date_picker_day_css = '.ui-datepicker-calendar .ui-state-default'

    # class
    date_picker_month = 'ui-datepicker-month'
    date_picker_year = 'ui-datepicker-year'
    date_picker_next = 'ui-datepicker-next'
    date_picker_prev = 'ui-datepicker-prev'
    date_picker_day = 'ui-state-default'
    paginator_current = 'ui-paginator-current'
    paginator_button = 'ui-paginator-page'
    paginator_next_button = 'ui-paginator-next'
    paginator_last_button = 'ui-paginator-last'
    paginator_prev_button = 'ui-paginator-prev'
    paginator_first_button = 'ui-paginator-first'
    # name
    user_input = 'form:userDropDownList_editableInput'


class DocumentAuditElements:
    # id
    filter_header = 'mainForm:tabs:filterPanel_header'
    filter = 'mainForm:tabs:filterPanel_content'
    start_date = 'mainForm:tabs:startDateFilter_input'
    end_date = 'mainForm:tabs:endDateFilter_input'
    apply_filter = 'mainForm:tabs:applyFiletButton'
    od_statistic = 'mainForm:tabs:openDownloadStatisticPanel_header'
    od_content = 'mainForm:tabs:openDownloadStatisticPanel_content'
    download_per_file_type_header = 'mainForm:tabs:downloadsPerFileTypePanel_header'
    download_per_file_type = 'mainForm:tabs:downloadsPerFileTypePanel_content'
    opens_per_file_type_header = 'mainForm:tabs:opensPerFileTypePanel_header'
    opens_per_file_type = 'mainForm:tabs:opensPerFileTypePanel_content'
    total_usage_per_file_type_header = 'mainForm:tabs:totalUsagePerFileTypePanel_header'
    total_usage_per_file_type = 'mainForm:tabs:totalUsagePerFileTypePanel_content'
    overall_users_statistic_header = 'mainForm:tabs:overallUsersStatisticPanel_header'
    overall_users_statistic = 'mainForm:tabs:overallUsersStatisticPanel_content'
    date_picker = 'ui-datepicker-div'

    # class
    date_picker_month = 'ui-datepicker-month'
    date_picker_year = 'ui-datepicker-year'
    date_picker_next = 'ui-datepicker-next'
    date_picker_prev = 'ui-datepicker-prev'
    date_picker_day = 'ui-state-default'

    # name
    username_input = 'mainForm:tabs:usernameFilter'

    # css selector
    documents_usage_folder = 'li.ui-state-default:nth-child(1)'
    users_folder = 'li.ui-state-default:nth-child(2)'
    date_picker_day_css = '.ui-datepicker-calendar .ui-state-default'


class TotalLoginsElements:

    # id
    filter = 'filter_header'
    filter_content = 'filter_content'
    user_group = 'statisticUser:userGroupFilter_label'
    application = 'statisticUser:apllicationFilter_label'
    start_date_input = 'statisticUser:startDateFilter_input'
    end_date_input = 'statisticUser:endDateFilet_input'
    apply_button = 'statisticUser:filterApplyButton'
    tl_table = 'dataTableForm:dataTableCount'
    date_picker = 'ui-datepicker-div'

    # class
    date_picker_trigger = 'ui-datepicker-trigger'
    date_picker_month = 'ui-datepicker-month'
    date_picker_year = 'ui-datepicker-year'
    date_picker_next = 'ui-datepicker-next'
    date_picker_prev = 'ui-datepicker-prev'
    date_picker_day = 'ui-state-default'
    date_picker_active = 'ui-state-active'

    # css selector
    date_picker_day_css = '.ui-datepicker-calendar .ui-state-default'
    # name
    user_input = 'statisticUser:orUserFilter'


class ContainerElements:

    # id
    filter_panel = 'form:filterPanel'
    start_date = 'form:startFilterDate_input'
    end_date = 'form:endFilterDate_input'
    severity_label = 'form:severity_label'
    device_type_label = 'form:deviceTypeFilter_label'
    visible_columns_label = 'form:visibleColumns_label'
    visible_columns_panel = 'form:visibleColumns_panel'
    user_filter = 'form:userFilter'
    reset_filter_button = 'form:restoreFiltersButton'
    apply_filter_button = 'form:applyFiltersButton'
    cont_log_table = 'dataTableForm:logsTable'
    table_head = 'dataTableForm:logsTable_head'
    start_date_column = 'dataTableForm:logsTable:startDateColumn'
    first_name_column = 'dataTableForm:logsTable:firstNameColumn'
    first_name_column_filter = 'dataTableForm:logsTable:firstNameColumn:filter'
    last_name_column = 'dataTableForm:logsTable:lastNameColumn'
    last_name_column_filter = 'dataTableForm:logsTable:lastNameColumn:filter'
    user_column = 'dataTableForm:logsTable:uidColumn'
    user_column_filter = 'dataTableForm:logsTable:uidColumn:filter'
    session_column = 'dataTableForm:logsTable:sessionIdColumn'
    session_column_filter = 'dataTableForm:logsTable:sessionIdColumn:filter'
    device_type_column = 'dataTableForm:logsTable:deviseTypeColumn'
    context_column = 'dataTableForm:logsTable:contextColumn'
    context_column_filter = 'dataTableForm:logsTable:contextColumn:filter'
    message_column = 'dataTableForm:logsTable:messageColumn'
    date_picker = 'ui-datepicker-div'
    end_date_column = 'dataTableForm:logsTable:endDateColumn'
    device_column = 'dataTableForm:logsTable:deviceColumn'
    device_column_filter = 'dataTableForm:logsTable:deviceColumn:filter'
    domain_column = 'dataTableForm:logsTable:domainColumn'
    severity_column = 'dataTableForm:logsTable:severityColumn'
    component_column = 'dataTableForm:logsTable:componentColumn'
    type_column = 'dataTableForm:logsTable:typeColumn'
    tags_column = 'dataTableForm:logsTable:tagsColumn'
    tags_column_filter = 'dataTableForm:logsTable:tagsColumn:filter'
    os_type_column = 'dataTableForm:logsTable:osTypeColumn'
    os_version_column = 'dataTableForm:logsTable:osVersionColumn'
    os_version_column_filter = 'dataTableForm:logsTable:osVersionColumn:filter'
    address_column = 'dataTableForm:logsTable:addressColumn'
    address_column_filter = 'dataTableForm:logsTable:addressColumn:filter'
    device_ip_column = 'dataTableForm:logsTable:deviseIpColumn'
    device_ip_column_filter = 'dataTableForm:logsTable:deviseIpColumn:filter'
    latitude_column = 'dataTableForm:logsTable:latitudeColumn'
    longitude_column = 'dataTableForm:logsTable:longitudeColumn'

    # class
    panel_left = 'ui-toolbar-group-left'
    panel_right = 'ui-toolbar-group-right'
    checkbox_item = 'ui-selectcheckboxmenu-list-item'
    date_picker_trigger = 'ui-datepicker-trigger'
    date_picker_month = 'ui-datepicker-month'
    date_picker_year = 'ui-datepicker-year'
    date_picker_next = 'ui-datepicker-next'
    date_picker_prev = 'ui-datepicker-prev'
    date_picker_day = 'ui-state-default'
    date_picker_active = 'ui-state-active'
    date_picker_title = 'ui-datepicker-title'
    paginator_current = 'ui-paginator-current'
    paginator_button = 'ui-paginator-page'
    paginator_next_button = 'ui-paginator-next'
    paginator_last_button = 'ui-paginator-last'
    paginator_prev_button = 'ui-paginator-prev'
    paginator_first_button = 'ui-paginator-first'
    column_title = 'ui-column-title'
    empty_message = 'ui-datatable-empty-message'

    # Css
    date_picker_day_css = '.ui-datepicker-calendar .ui-state-default'


class LoginLogoutElements:

    # id
    filter_header = 'filter_header'
    filter_content = 'filter_content'
    user_input = 'loginglogoutStatistic:userFilter'
    application_label = 'loginglogoutStatistic:applicationFilter'
    start_date_input = 'loginglogoutStatistic:startDateFilter_input'
    end_date_input = 'loginglogoutStatistic:endDateFilter_input'
    apply_filter_button = 'loginglogoutStatistic:filterApplyButton'
    login_logout_table = 'dataTableForm:dataTable'
    paginator = 'dataTableForm:dataTable_paginator_top'
    user_column = 'dataTableForm:dataTable:userColumn'
    device_column = 'dataTableForm:dataTable:deviceColumn'
    login_column = 'dataTableForm:dataTable:loginColumn'
    logout_column = 'dataTableForm:dataTable:logoutColumn'
    working_time_column = 'dataTableForm:dataTable:workingTimeColumn'
    application_column = 'dataTableForm:dataTable:applicationColumn'
    date_picker = 'ui-datepicker-div'
    application_items = 'loginglogoutStatistic:applicationFilter_items'
    application_string = 'loginglogoutStatistic:applicationFilter_'  # number after '_'

    # class
    date_picker_trigger = 'ui-datepicker-trigger'
    date_picker_month = 'ui-datepicker-month'
    date_picker_year = 'ui-datepicker-year'
    date_picker_next = 'ui-datepicker-next'
    date_picker_prev = 'ui-datepicker-prev'
    date_picker_day = 'ui-state-default'
    date_picker_active = 'ui-state-active'
    date_picker_title = 'ui-datepicker-title'
    paginator_current = 'ui-paginator-current'
    paginator_button = 'ui-paginator-page'
    paginator_next_button = 'ui-paginator-next'
    paginator_last_button = 'ui-paginator-last'
    paginator_prev_button = 'ui-paginator-prev'
    paginator_first_button = 'ui-paginator-first'
    column_title = 'ui-column-title'
    empty_message = 'ui-datatable-empty-message'

    # css
    date_picker_day_css = '.ui-datepicker-calendar .ui-state-default'


class EmailGroupsElements:

    # id
    add_new_button = 'table:tableForm:buttonTopPanel:tableButtonAddNewTop'
    delete_button = 'table:tableForm:buttonTopPanel:tableButtonDeleteTop'
    refresh_button = 'table:tableForm:buttonTopPanel:tableButtonReloadTop'
    edit_group_0_button = 'table:tableForm:entityTable:0:edit'
    email_groups_detail = 'entity:dialogsForm:entityDialog'
    egd_name = 'entity:dialogsForm:email-group-name'
    egd_content = 'entity:dialogsForm:email-group-content'
    egd_description = 'entity:dialogsForm:email-group-description'
    egd_add_button = 'entity:dialogsForm:addEntity'
    egd_cancel_button = 'entity:dialogsForm:cancelEntity'
    delete_dialog = 'delete:deleteForm:deleteDialog'
    delete_confirm = 'delete:deleteForm:confirmDeleteButton'
    delete_cancel = 'delete:deleteForm:cancelDeleteButton'
    file_upload_choose = 'entity:dialogsForm:emailGroupDetailsChooseButton_input'
    error_dialog = 'errorForm:errorDialog'
    error_form_list = 'errorForm:errorContent_list'
    error_close = 'errorForm:closeButton'

    # class
    file_upload_upload = 'ui-fileupload-upload'
    file_upload_cancel = 'ui-fileupload-cancel'
    file_upload_progress = 'ui-fileupload-progress'
    file_upload_content = 'ui-fileupload-content'

    # css selector
    loaded_name = '.ui-fileupload-row > div:nth-child(2)'
    loaded_size = '.ui-fileupload-row > div:nth-child(3)'
    loaded_cancel_upload = 'button.ui-fileupload-cancel:nth-child(1)'


class AlertsElements:

    # id
    add_new_button = 'table:tableForm:buttonTopPanel:tableButtonAddNewTop'
    delete_button = 'table:tableForm:buttonTopPanel:tableButtonDeleteTop'
    refresh_button = 'table:tableForm:buttonTopPanel:tableButtonReloadTop'
    edit_alert_0_button = 'table:tableForm:entityTable:0:edit'
    alert_details = 'entity:dialogsForm:entityDialog'
    ad_actions = 'entity:dialogsForm:log-event-action'
    ad_email_group_dd = 'entity:dialogsForm:log-event-email-name'
    ad_subject = 'entity:dialogsForm:log-event-subject'
    ad_body = 'entity:dialogsForm:log-event-body'
    ad_description = 'entity:dialogsForm:log-event-description'
    ad_add_button = 'entity:dialogsForm:addEntity'
    ad_cancel_button = 'entity:dialogsForm:cancelEntity'
    delete_dialog = 'delete:deleteForm:deleteDialog'
    delete_confirm = 'delete:deleteForm:confirmDeleteButton'
    delete_cancel = 'delete:deleteForm:cancelDeleteButton'

    # css selector


class DeviceLogElements:

    # id
    log_folder = 'tabs:deviceLog:selectedFolder'
    log_folder_label = 'tabs:deviceLog:selectedFolder_label'
    folder_list = 'tabs:deviceLog:selectedFolder_items'
    crash_log_table = 'tabs:logForm:deviceLogTable'
    upload_device_log_button = 'tabs:deviceLog:uploadDeviceLogButton'
    upload_device_log_choose_button = 'deviceLogUploadDlgForm:fileUpload_input'
    upload_decoded_log_dialog = 'deviceLogUploadDlgForm:j_idt295'
    upload_decoded_log_close = 'deviceLogUploadDlgForm:clodeButton'
    upload_decoded_log_upload = 'deviceLogUploadDlgForm:uploadBtn'
    file_name_column = 'tabs:logForm:deviceLogTable:fileNameColumn'
    file_name_filter = 'tabs:logForm:deviceLogTable:fileNameColumn:filter'
    platform_column = 'tabs:logForm:deviceLogTable:platformTypeColumn'
    platform_drop_down_filter = 'tabs:logForm:deviceLogTable:j_idt253_label'
    platform_drop_down_table = 'tabs:logForm:deviceLogTable:j_idt253_items'
    device_id_column = 'tabs:logForm:deviceLogTable:deviceIdColumn'
    device_id_filter = 'tabs:logForm:deviceLogTable:deviceIdColumn:filter'
    when_column = 'tabs:logForm:deviceLogTable:whenColumn'
    when_filter = 'tabs:logForm:deviceLogTable:j_idt260_input'
    size_column = 'tabs:logForm:deviceLogTable:sizeColumn'
    action_column = 'tabs:logForm:deviceLogTable:actionColumn'
    view_action_first_str = 'tabs:logForm:deviceLogTable:0:viewLastBtn'
    download_action_first_str = 'tabs:logForm:deviceLogTable:0:downloadLink'
    delete_action_first_str = 'tabs:logForm:deviceLogTable:0:deleteItem'
    log_dialog = 'tabs:logForm:deviceLogDlg'
    log_dialog_ok = 'tabs:logForm:okButton'
    delete_dialog = 'tabs:logForm:deleteConfirm'
    delete_dialog_yes = 'tabs:logForm:yesButton'
    delete_dialog_no = 'tabs:logForm:noButton'

    # class
    empty_message = 'ui-datatable-empty-message'
    paginator_current = 'ui-paginator-current'
    paginator_button = 'ui-paginator-page'
    paginator_next_button = 'ui-paginator-next'
    paginator_last_button = 'ui-paginator-last'
    paginator_prev_button = 'ui-paginator-prev'
    paginator_first_button = 'ui-paginator-first'
    log_dialog_container = 'ui-scrollpanel-container'
    preformatted = 'preformatted'
    date_picker_trigger = 'ui-datepicker-trigger'
    date_picker_month = 'ui-datepicker-month'
    date_picker_year = 'ui-datepicker-year'
    date_picker_next = 'ui-datepicker-next'
    date_picker_prev = 'ui-datepicker-prev'
    date_picker_day = 'ui-state-default'
    date_picker_active = 'ui-state-active'
    date_picker_title = 'ui-datepicker-title'
    row_highlight = 'ui-state-highlight'
    upload_file_name = 'ui-fileupload-filename'
    main_notification_title = 'ui-growl-title'
    main_notification_message = 'ui-growl-message'

    # css
    date_picker_day_css = '.ui-datepicker-calendar .ui-state-default'
