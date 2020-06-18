package tests.source;

import com.appbus.pages.constants.Context;
import com.appbus.pages.event_related.AllEventsSideBar;
import com.appbus.pages.event_related.EventPreviewInAllEvents;
import com.appbus.pages.event_related.NewEvent;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.tabs.CalendarTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;

public class AllEvents
{
    @Test
    public void allEvents() throws InterruptedException
    {
        /*   Single-run setup
        ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver());
        CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications();

        Scroller.scrollRight("Calendar");

        CalendarTab calendarTab = commMenuItems.clickCalendar();
        */

        CalendarTab calendarTab = new CalendarTab(FunctionalTest.getDriver()); // bulk run

        calendarTab.clickToday();
        Thread.sleep(4000);

        calendarTab.clickWeek();
        Thread.sleep(5000);

        ///
        System.out.println("Move to +2 weeks forward...");
        calendarTab.clickArrowRight();
        Thread.sleep(5000);

        calendarTab.clickArrowRight();
        Thread.sleep(5000);
        ///

        FunctionalTest.switchContext(Context.WEBVIEW);
        JSExecutor.injectJQuery();

        // Save current week range in header
        String weekRange = JSExecutor.getTextViaJQuery("$('.navigator-title')");
        System.out.println("weekRange = " + weekRange);

        System.out.println("Click near 9PM by the fifth cell...");
        JSExecutor.clickViaJQuery("$('li.time-cell .time:contains(\"9 P\")').closest('li').next().next().next().next().next()"); // Thu

        // Save day of month
        String dayOfMonth = JSExecutor.getTextViaJQuery("$('.top-title-panel li:contains(\"Thu\")')").substring(4); // Thu %day%
        System.out.println("dayOfMonth = " + dayOfMonth);

        FunctionalTest.switchContext(Context.NATIVE);
        NewEvent newEvent = new NewEvent(FunctionalTest.getDriver());
        FunctionalTest.switchContext(Context.WEBVIEW);

        String eventTitle = "Single [all event] autotest";

        newEvent.setTitle(eventTitle);
        newEvent.clickAccept();

        ///
        System.out.println("Move to -2 weeks backward...");
        FunctionalTest.switchContext(Context.NATIVE);

        calendarTab.clickArrowLeft();
        Thread.sleep(5000);

        calendarTab.clickArrowLeft();
        Thread.sleep(5000);
        ///

        System.out.println("Looking for single event in All events sidebar...");
        AllEventsSideBar allEventsSideBar = calendarTab.clickAllEvents();

        while( allEventsSideBar.isEventVisibleByName(eventTitle) != true )
        {
            allEventsSideBar.scrollDown();
            Thread.sleep(3000);
        }

        System.out.println("Event with name " + eventTitle + " was found");

        System.out.println("Making sure that found event is under " + dayOfMonth + " header...");
        Assert.assertTrue((Boolean) FunctionalTest.getDriver().executeScript("return $('#all-events-scroll-wrapper .infinite-item:contains(\"" + eventTitle + "\")')" +
                                                                                    ".prevAll('.infinite-item:has(.group-title)')" +
                                                                                    ".eq(0)" +
                                                                                    ".is(':contains(\"" + dayOfMonth + "\")')"));

        EventPreviewInAllEvents eventPreviewInAllEvents = allEventsSideBar.clickEventByName(eventTitle);

        System.out.println("Making sure that found event has correct title and date...");
        Assert.assertEquals(eventTitle, eventPreviewInAllEvents.getEventTitle());
        Assert.assertTrue(eventPreviewInAllEvents.getEventDate().contains("9:00 PM – 9:30 PM"));

        NewEvent eventInGrid = eventPreviewInAllEvents.clickShowInTheGrid();
        Thread.sleep(4000);

        FunctionalTest.switchContext(Context.WEBVIEW);

        // Get week range after clicking of 'Show in the grid'
        String weekRangeAfter = JSExecutor.getTextViaJQuery("$('.navigator-title')");

        System.out.println("Making sure that week range is correct after clicking of 'Show in the grid' button...");
        Assert.assertEquals(weekRange, weekRangeAfter);

        eventInGrid.clickDelete(false).delete(true);

        // Trying to find deleted event by title
        MobileElement shouldBeNull = CalendarTab.findEventByName(eventTitle);

        Assert.assertNull(shouldBeNull);

        // Scroll back to the left
        Scroller.scrollLeft("Accenture Portal");
    }
}
