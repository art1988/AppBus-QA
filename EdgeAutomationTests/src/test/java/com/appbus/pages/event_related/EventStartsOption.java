package com.appbus.pages.event_related;

import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;

// Non-native, so no need to extends from PageObject
public class EventStartsOption
{
    private static final String id_Hours   = "hours",
                                id_Minutes = "minutes",
                                id_AmPm    = "amPm",

                                id_Apply    = "apply-changes-icon";


    public EventStartsOption()
    {
        JSExecutor.injectJQuery();

        try
        {
            Thread.sleep(4000);
        } catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('.form-body .edit-header .header-text:contains(\"Starts\")')") &
                 JSExecutor.isVisibleViaJQuery("$('.edit-info .date-separator:contains(\"Time\")')") &
                 JSExecutor.isVisibleViaJQuery("$('.edit-info .date-separator:contains(\"Date\")')") );
    }

    /**
     * Set Starts time for Event
     * @param hour can be [0, 12]
     * @param minutes can be [0, 5, 10, 15, ..., 55]
     * @param am_pm can be 0 for AM and 1 for PM
     */
    public void setTime(int hour, int minutes, int am_pm) throws InterruptedException
    {
        JSExecutor.setTextForSelect(id_Hours, String.valueOf(hour));
        Thread.sleep(1000); // necessary for correct saving due to debounce of js function

        JSExecutor.setTextForSelect(id_Minutes, String.valueOf(minutes));
        Thread.sleep(1000); // necessary for correct saving due to debounce of js function

        JSExecutor.setTextForSelect(id_AmPm, String.valueOf(am_pm));

        System.out.println("Time was set as: " + hour + ":" + minutes + " " + ((am_pm == 0) ? "AM" : "PM"));
    }

    public void clickApply()
    {
        JSExecutor.clickByElement(id_Apply);
        System.out.println("Apply button was clicked");
    }
}
