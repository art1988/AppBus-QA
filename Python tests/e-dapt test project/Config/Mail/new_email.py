class Elements:
    #
    # ID Elements
    #
    new_email = 'newEmail'
    to_field_input = "emailInput-to"
    cc_field_input = "emailInput-cc"
    bcc_field_input = "emailInput-bcc"
    subject_field_input = "new-email-subject-input"
    add_contact_button_in_to = 'add-contact-dropdown-toggler-to'
    add_contact_button_in_cc = 'add-contact-dropdown-toggler-cc'
    add_contact_button_in_bcc = 'add-contact-dropdown-toggler-bcc'
    add_attach = "icon-icon_editor_attach"
    not_valid_email = 'statusEmptySender'
    close_email_button = "close-button-icon"
    #
    # Class Name elements
    #
    text_panel_button = "button-show-editor"
    overlay = "overlay"
    add_contact_search_input = "filter-contacts-input"
    add_contact_clear = "icon-icon_close_filled"
    bold_text_panel = 'awesome-icon-bold'
    italic_text_panel = 'awesome-icon-italic'
    underline_text_panel = 'awesome-icon-underline'
    quote_block_text_panel = 'awesome-icon-blockquote'
    ul_marked_list_text_panel = 'awesome-icon-ul'
    oi_marked_list_text_panel = 'awesome-icon-ol'
    link_text_panel = 'awesome-icon-link'
    unlink_text_panel = 'awesome-icon-unlink'
    link_confirm = 'confirm-link-button'
    close_editor_confirmation_block_wrapper = "close-editor-confirmation"
    close_editor_confirmation_button = "notification-button"
    wrapper_close = "notification-button"
    add_contact_dropdown = 'contactDropdown'
    search_contact_input = 'filter-contacts-input'
    search_clear_filled = 'icon-icon_close_filled'
    contact_list_container = 'contactListContainer'
    name_add_contacts = 'name'
    email_add_contacts = 'email'
    block_wrapper_header = 'block-wrapper-header'
    dropdown_items = 'item'
    #
    # Xpath Elements
    #
    to_autocomplete_dropdown_item_1 = '//*[@id="newEmail"]/div[2]/div/div[1]/div[3]/div[1]/div'
    to_autocomplete_dropdown_item_2 = '//*[@id="newEmail"]/div[2]/div/div[1]/div[3]/div[2]'
    cc_autocomplete_dropdown_item_1 = '//*[@id="newEmail"]/div[2]/div/div[2]/div[3]/div[1]'
    cc_autocomplete_dropdown_item_2 = '//*[@id="newEmail"]/div[2]/div/div[2]/div[3]/div[2]'
    bcc_autocomplete_dropdown_item_1 = '//*[@id="newEmail"]/div[2]/div/div[3]/div[3]/div[1]'
    bcc_autocomplete_dropdown_item_2 = '//*[@id="newEmail"]/div[2]/div/div[3]/div[3]/div[2]'
    add_contact_to_dropdown_item_1 = '//*[@id="contactList"]/li[1]/a/div'
    add_contact_to_dropdown_item_2 = '//*[@id="contactList"]/li[2]/a/div'
    link_input_name = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[1]/div[4]/div[1]/input'
    link_input_address = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[1]/div[4]/div[2]/input'
    body_text_in_new_email = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div'
    send_email_button = '//*[@id="newEmail"]/div[3]/a'
    # add_contact_button_in_to = '//*[@id="newEmail"]/div[2]/div/div[1]/div[1]'
    # add_contact_button_in_cc = '//*[@id="newEmail"]/div[2]/div/div[2]/div[1]'
    # add_contact_button_in_bcc = '//*[@id="newEmail"]/div[2]/div/div[3]/div[1]'
    add_contact_dropdown_item_1 = '//*[@id="contactList"]/li[1]/a/div'
    add_contact_dropdown_item_2 = '//*[@id="contactList"]/li[2]/a/div'
    add_contact_dropdown_item_3 = '//*[@id="contactList"]/li[3]/a/div'
    add_contact_dropdown_item_4 = '//*[@id="contactList"]/li[4]/a/div'
    add_contact_dropdown_item_5 = '//*[@id="contactList"]/li[5]/a/div'
    add_contact_dropdown_item_6 = '//*[@id="contactList"]/li[6]/a/div'


    # email address arrays
    to_emails = '//*[@id="bootstrapTagsinput-to"]/span'
    cc_emails = '//*[@id="bootstrapTagsinput-cc"]/span'
    bcc_emails = '//*[@id="bootstrapTagsinput-bcc"]/span'
    # email body
    common = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[1]/div/span/span'
    bold = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[2]/div/span/span'
    bold_italic = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[3]/div/span/span'
    bold_italic_underline = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[4]/div/span/span'
    italic_underline = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[5]/div/span/span'
    italic = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[6]/div/span/span'
    underline = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[7]/div/span/span'
    bold_underline = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[8]/div/span/span'
    ui = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/ul/li/div/span/span'
    oi = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/ol/li/div/span/span'
    link = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[9]/div/a/span/span'
    link_to_not_link = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[10]/div/span/span'
    link_to_delete = '//*[@id="newEmail"]/div[2]/div/div[5]/div/div[2]/div/div/div/div/div[11]/div/a/span/span'

