class Elements:
    #
    # ID Elements
    #
    close_button = 'close_button' #1
    profile_tab = 'tab-header-profile' #1
    name_input = 'FullName' #1
    job_title_input = 'JobTitle' #1
    company_input = 'Company' #1
    department_input = 'Department' #1
    birthday_input = 'Birthday' #1
    website_input = 'WebAddress' #1
    email_input = 'Email1' #1
    email_input_2 = 'Email2' #1
    email_input_3 = 'Email3' #1
    im_id_input = 'IMId' #1
    language_input = 'Language' #1
    hobbies_input = 'Hobbies' #1
    contact_tab = 'tab-header-contacts' #1
    address_tab = 'tab-header-address' #1
    more_tab = 'tab-header-more' #1
    close_editor_confirmation = 'close-editor-confirmation' #1
    save_option = 'contact-save-option' #1
    delete_option = 'contact-delete-option' #1
    undo_option = 'contact-undo-option' #1

    #
    # Class Name Elements
    #
    apply_unsaved_changes = 'block-wrapper-header' #1
    contact_card = 'contact-card' #1
    contact_info = 'contact-info' #1
    contact_cards_list = 'contacts-cards-table' #1
    contact_title = 'contact-card__title' #1
    contact_name_in_abc = 'contacts-list-wrapper__contact-name' #1
    contacts_folders_list = 'contacts-folders-list' #1
    block_wrapper = 'block-wrapper' #1
    confirm_button = 'notification-button' #1
    folder_name = 'contacts-folders-list__folder-name' #1
    add_contact_button = 'contacts-left-footer__button-add-contact' #1
    name_title = 'contact-card__title' #1
    name_title_abc = 'contacts-list-wrapper__contact-name' #1
    view_change_button = 'contacts-left-header__change-view-wrapper' #1


    #
    # Name Elements
    #
    business_phone_input = 'Phone' #1
    mobile_phone_input = 'MobilePhone' #1
    home_phone_input = 'HomePhone' #1
    work_street_input = 'BusinessAddressStreet' #1
    work_city_input = 'BusinessAddressCity' #1
    work_state_input = 'BusinessAddressState' #1
    work_postal_code_input = 'BusinessAddressPostalCode' #1
    work_country_input = 'BusinessAddressCountry' #1
    home_street_input = 'HomeAddressStreet' #1
    home_city_input = 'HomeAddressCity' #1
    home_state_input = 'HomeAddressState' #1
    home_postal_code_input = 'HomeAddressPostalCode' #1
    home_country_input = 'HomeAddressCountry' #1
    gender = 'Gender'
    #
    # Xpath Elements
    #
    search_contact = '//*[@id="main-app-window"]/div/div[2]/div[1]/div[1]/input'
    new_contact = '//*[@id="main-app-window"]/div/div[2]/div[3]/div'
    # name_title = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div[2]'
    # name_title_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/div[2]'
    clear_search = '//*[@id="main-app-window"]/div/div[2]/div[1]/div[1]/i[2]' #1
    accept_button = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[1]'
    gender_wrapper = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[2]/div/div/div'
    gender_wrapper_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[2]/div/div/div'
    female = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/span'
    female_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[2]/div/div/div/div[1]'
    male = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/span'
    male_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[2]/div/div/div/div[2]'
    company_info = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[1]/span[2]'
    company_info_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/ul/li[1]/span[2]'
    department_info = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[2]/span[2]'
    department_info_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/ul/li[2]/span[2]'
    job_title_info = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[3]/span[2]'
    job_title_info_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/ul/li[3]/span[2]'
    work_phone_info = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[4]/span[2]'
    work_phone_info_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/ul/li[4]/span[2]'
    email_info = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[5]/span[2]'
    email_info_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/ul/li[5]/span[2]'
    address_info = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[6]/span[2]'
    address_info_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/ul/li[6]/span[2]'
    yes_apply_unsaved_changes = '//*[@id="main-app-window"]/div/div[1]/div/div/div/div/div/div[2]'
    no_apply_unsaved_changes = '//*[@id="main-app-window"]/div/div[1]/div/div/div/div/div/div[3]'
    cancel_apply_unsaved_changes = '//*[@id="main-app-window"]/div/div[1]/div/div/div/div/div/div[4]'
    delete_button_wrapper = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[3]/div/div/div/div/div[1]'
    cancel_button_wrapper = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[3]/div/div/div/div/div[2]'
    contact_modal_window = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]' #1
    # undo_option = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]'
    undo_option_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[3]'
    # yes_option = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]'
    # yes_option_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[1]'
    # delete_option = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[4]'
    # delete_option_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[4]'
    move_to_option = '//*[@id="main-app-window"]/div/div[3]/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]'
    move_to_option_abc = '//*[@id="main-app-window"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]'
    contact_cards_list_xpath = '//*[@id="main-app-window"]/div/div[2]/div[2]'
    # view_change = '//*[@id="main-app-window"]/div/div[2]/div[1]/div[2]'
    abc_contact_list_wrapper = '//*[@id="main-app-window"]/div/div[2]/div[2]/div[1]'
    folder_contacts_select = '//*[@id="main-app-window"]/div/div[2]/div[2]/div/div[1]'
    folder_suggestet_contacts_select = '//*[@id="main-app-window"]/div/div[2]/div[2]/div/div[2]'
    folder_deleted_items_select = '//*[@id="main-app-window"]/div/div[2]/div[2]/div/div[3]'

    #
    # Other
    #
    folder_select = 'contacts-folders-list__folder-item_selected'
    yes_option_active = 'contacts-info-options__option-item_active'

