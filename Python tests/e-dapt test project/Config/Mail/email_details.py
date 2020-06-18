class Elements:
    #
    # ID Elements
    #

    #
    # Class Name Elements
    #
    back_button = 'button-back'
    message_view_folder_name = 'message-view-folder-name'
    email_message_show = 'email-message-show'
    #
    # Xpath Elements
    #
    from_email_details = '//*[@id="main-app-window"]/div/div[4]/div[2]/div/div/div[1]/div[1]/div[2]/span'
    to_email_details = '//*[@id="main-app-window"]/div/div[4]/div[2]/div/div/div[1]/div[1]/div[3]/span'
    cc_email_details = '//*[@id="main-app-window"]/div/div[4]/div[2]/div/div/div[1]/div[1]/div[4]/span'
    bcc_email_details = '//*[@id="main-app-window"]/div/div[4]/div[2]/div/div/div[1]/div[1]/div[5]/span'
    subject_email_details = '//*[@id="main-app-window"]/div/div[4]/div[2]/div/div/div[1]/div[2]/span'
    # email body
    common = '/html/body/p[1]'
    bold = '/html/body/p[2]/strong'
    bold_italic = '/html/body/p[3]/em/strong'
    bold_italic_underline = '/html/body/p[4]/u/em/strong'
    italic_underline = '/html/body/p[5]/u/em'
    italic = '/html/body/p[6]/em'
    underline = '/html/body/p[7]/u'
    bold_underline = '/html/body/p[8]/u/strong'
    ui = '/html/body/ul/li'
    oi = '/html/body/ol/li'
    link = '/html/body/p[9]/a'
