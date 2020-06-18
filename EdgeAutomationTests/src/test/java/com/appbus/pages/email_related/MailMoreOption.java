package com.appbus.pages.email_related;

import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;

// Non-native, so no need to extends from PageObject
public class MailMoreOption
{
    public MailMoreOption()
    {
        JSExecutor.injectJQuery();

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('.dd-menu-items .dropdown-list-folders .dropdown-item:contains(\"read\")')") &
                 JSExecutor.isVisibleViaJQuery("$('.dd-menu-items .dropdown-list-folders .dropdown-item:contains(\"important\")')") );
    }

    public void markAsUnread()
    {
        JSExecutor.clickViaJQuery("$('.dd-menu-items .dropdown-list-folders .dropdown-item:contains(\"unread\")')");
        System.out.println("Mark as unread was clicked");
    }

    public void markAsRead()
    {
        JSExecutor.clickViaJQuery("$('.dd-menu-items .dropdown-list-folders .dropdown-item:contains(\"read\")')");
        System.out.println("Mark as read was clicked");
    }

    public void markAsImportant()
    {
        JSExecutor.clickViaJQuery("$('.dd-menu-items .dropdown-list-folders .dropdown-item:contains(\"important\")')");
        System.out.println("Mark as important was clicked");
    }
}
