package com.appbus.pages.event_related;

import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;

public class EventInviteesOption
{
    private static final String class_addNewInvitee = "icon-icon_plus",
                                class_searchField   = "filter-contacts-input",
                                id_accept           = "apply-changes-icon",
                                id_close            = "close-form-icon";


    public EventInviteesOption()
    {
        JSExecutor.injectJQuery();

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('.appointment-form .header-text:contains(\"Invite\")')") );
    }

    /**
     * Click by + button to select invitee by name.
     * Cursor is placed in search field by default.
     * @param inviteeName
     */
    public void selectInviteeByName(String inviteeName)
    {
        JSExecutor.clickByElementByClassName(class_addNewInvitee);

        JSExecutor.setTextForFieldByClassName(class_searchField, inviteeName);

        JSExecutor.clickViaJQuery("$('.search-contact-item .name:contains(\"" + inviteeName + "\")')");

        System.out.println(inviteeName + " was selected as invitee");
    }

    public void clickAccept()
    {
        JSExecutor.clickByElement(id_accept);

        System.out.println("Accept was clicked");
    }

    public void clickClose()
    {
        JSExecutor.clickByElement(id_close);

        System.out.println("Close was clicked");
    }
}
