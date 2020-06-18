package com.appbus.pages.event_related;

import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;
import tests.source.FunctionalTest;

// Non-native, so no need to extends from PageObject
/**
 * Event preview in All Events side bar with one button "Show in the grid"
 */
public class EventPreviewInAllEvents
{
    private static final String class_EventTitle = "subject",
                                class_EventDate  = "date";

    private static final String id_ShowInTheGridButton = "tooltip-panel-btn";


    public EventPreviewInAllEvents()
    {
        JSExecutor.injectJQuery();

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('.CalendarEventPreview " + "." + class_EventTitle + "')") &
                 JSExecutor.isVisibleViaJQuery("$('#" + id_ShowInTheGridButton + "')") );
    }

    public NewEvent clickShowInTheGrid()
    {
        JSExecutor.clickViaJQuery("$('#" + id_ShowInTheGridButton + "')");
        System.out.println("Show in the grid was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return new NewEvent(FunctionalTest.getDriver(), true);
    }

    public String getEventTitle()
    {
        return JSExecutor.getTextViaJQuery("$('.CalendarEventPreview" + " ." + class_EventTitle + "')");
    }

    public String getEventDate()
    {
        return JSExecutor.getTextViaJQuery("$('.CalendarEventPreview" + " ." +  class_EventDate + "')");
    }
}
