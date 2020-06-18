package com.appbus.pages.event_related;

import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;

// Non-native, so no need to extends from PageObject
public class EventAlertOption
{
    private static final String id_Apply    = "apply-changes-icon";


    public EventAlertOption()
    {
        JSExecutor.injectJQuery();

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('.form-body .edit-header .header-text:contains(\"Alert\")')") );
    }

    public void setAlertTime(String alertTime)
    {
        JSExecutor.clickViaJQuery("$('.edit-info .timezone-text .title:contains(\"" + alertTime + "\")')");
        System.out.println("Alert time was set as " + alertTime);
    }

    public void clickApply()
    {
        JSExecutor.clickByElement(id_Apply);
        System.out.println("Apply button was clicked");
    }
}
