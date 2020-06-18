package com.appbus.pages.event_related;

import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Scroller;
import org.junit.Assert;

// Non-native, so no need to extends from PageObject

/**
 * Class represent All Events sidebar that can be invoked by clicking 'All events' button and 'Show all occurrences'
 */
public class AllEventsSideBar
{

    public AllEventsSideBar()
    {
        JSExecutor.injectJQuery();

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('#all-appointments-panel .button:contains(\"All\")')") &
                 JSExecutor.isVisibleViaJQuery("$('#all-events-infinite-scroll')") );
    }

    public EventPreviewInAllEvents clickEventByName(String eventName)
    {
        JSExecutor.clickViaJQuery("$('#all-events-scroll-wrapper .infinite-item .event-title:contains(\"" + eventName + "\")')");
        System.out.println("Was clicked by event with name = " + eventName);

        return new EventPreviewInAllEvents();
    }

    public boolean isEventVisibleByName(String eventName)
    {
        return JSExecutor.isVisibleViaJQuery("$('#all-events-scroll-wrapper .event-title:contains(\"" + eventName + "\")')");
    }

    public void scrollDown()
    {
        Scroller.scrollDownOneScreenOfAllEvents();
    }

    /**
     * Click All Event button. It will close this sidebar.
     */
    public void clickAllEvents()
    {
        JSExecutor.clickViaJQuery("$('.all-appointments-button')");

        System.out.println("All Events button was clicked. Sidebar was closed.");
    }
}
