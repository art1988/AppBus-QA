package com.appbus.pages.email_related;

import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;

// Non-native, so no need to extends from PageObject
public class MailMoveOption
{
    public MailMoveOption()
    {
        JSExecutor.injectJQuery();

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('.dd-menu-items .dropdown-list-folders .dropdown-item:contains(\"Inbox\")')") &
                JSExecutor.isVisibleViaJQuery("$('.dd-menu-items .dropdown-list-folders .dropdown-item:contains(\"Junk\")')") );
    }

    public void moveToJunk()
    {
        JSExecutor.clickViaJQuery("$('.dd-menu-items .dropdown-list-folders .move-to-folder-name:contains(\"Junk\")')");
        System.out.println("Move to Junk E-Mail was clicked");
    }

    public void moveToInbox()
    {
        JSExecutor.clickViaJQuery("$('.dd-menu-items .dropdown-list-folders .move-to-folder-name:contains(\"Inbox\")')");
        System.out.println("Move to Inbox was clicked");
    }
}
