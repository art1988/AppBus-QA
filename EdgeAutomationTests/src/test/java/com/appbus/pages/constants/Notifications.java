package com.appbus.pages.constants;

public enum Notifications
{
    EMAIL_RECEIVED("You have 1 new email(s)"),
    DOCUMENT_DOWNLOADED("Document Downloaded."),
    EVENT_REMINDER("Event Reminder");

    private final String notificationText;


    Notifications(final String notificationText)
    {
        this.notificationText = notificationText;
    }

    public String getNotificationText()
    {
        return notificationText;
    }
}
