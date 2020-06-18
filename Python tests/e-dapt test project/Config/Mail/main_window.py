# from main_app_window import Maw, driver_instance
# mgd = Maw.get_devices()


class Elements:
    #
    # ID Elements
    #
    new_email_button = "new-email-button"
    spinner = 'email-top-spinner'
    check_option_toggler = 'check-options-toggler'
    check_all_option = 'check-option-All'
    check_none_option = 'check-option-None'
    check_read_option = 'check-option-Read'
    check_unread_option = 'check-option-Unread'
    check_important_option = 'check-option-Important'
    check_unimportant_option = 'check-option-Unimportant'
    message_search_input = 'messagesSearchInput'
    small_sorting_button = 'small-sorting-button-toggler'
    small_more_button = 'small-more-button-toggler'
    small_move_to_button = 'small-move-to-button-toggler'
    list = 'list'
    small_delete_button = 'small-more-button-delete'
    small_search_button = 'small-text-filter-toggler'


    #
    # Class Name Elements
    #
    spinner_not_spinning = 'messages-top-spinner-no-animation'
    spinner_is_spinning = 'messages-top-spinner'
    sorting_button = 'sorting-action-btn' # ????????
    sender = 'sender'
    norecords = 'norecords'
    more_dropdown_item = 'dropdown-item'
    dropdown_list = 'dropdown-list-folders'
    move_to_folder_name = 'move-to-folder-name'
    topic = 'topic'
    block_wrapper = 'block-wrapper'
    block_wrapper_header = 'block-wrapper-header'
    wrapper_ok = 'notification-button save'
    wrapper_cancel = 'notification-button cancel'
    row = 'row'
    close_icon = 'icon-icon_close_filled'
    visibility_of_search = 'EmailTableContentAreaHeaderTextFilter-small'

    #
    # Xpath Elements
    #
    sorting_select = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div/div[1]/a/span'
    message_search_clear = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[3]/i[2]'
    inbox_folder = '//*[@id="emailFolders"]/li[1]/div/div[2]/span[1]'
    inbox_selected_folder = '//*[@id="emailFolders"]/li[1]/div'
    sent_items_folder = '//*[@id="emailFolders"]/li[3]/div/div[2]/span[1]'
    sent_items_selected_folder = '//*[@id="emailFolders"]/li[3]/div'
    deleted_items_folder = '//*[@id="emailFolders"]/li[4]/div/div[2]/span[1]'
    deleted_items_selected_folder = '//*[@id="emailFolders"]/li[4]/div'
    drafts_folder = '//*[@id="emailFolders"]/li[5]/div/div[2]/span[1]'
    drafts_selected_folder = '//*[@id="emailFolders"]/li[5]/div'
    junk_email_folder = '//*[@id="emailFolders"]/li[6]/div/div[2]/span[1]'
    junk_email_selected_folder = '//*[@id="emailFolders"]/li[6]/div'
    list_of_messages = '//*[@id="list"]/li/div[3]/strong[2]'
    date_in_first_message = '//*[@id="list"]/li[1]/div[4]'
    sorting_dropdawn_list = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]'
    sorting_date_arrow_icon = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/ul/li[1]/i'
    sorting_from_arrow_icon = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/ul/li[2]/i'
    sorting_importance_arrow_icon = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/ul/li[3]/i'
    sorting_subject_arrow_icon = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/ul/li[4]/i'
    date_sorting = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/ul/li[1]'
    from_sorting = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/ul/li[2]'
    importance_sorting = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/ul/li[3]'
    subject_sorting = '//*[@id="main-app-window"]/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/ul/li[4]'
    flag_in_1th_message = '//*[@id="list"]/li[1]/div[2]/i'
    flag_in_2th_message = '//*[@id="list"]/li[2]/div[2]/i'
    subject_with_no_subject = '//*[@id="list"]/li[1]/div[3]/strong[2]/i'
    subject_in_1th_message = '//*[@id="list"]/li[1]/div[3]/strong[2]'
    main_checkbox = '//*[@id="check-all-action-btn"]/i'



