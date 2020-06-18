package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.event_related.EventEndRepeatOption;
import com.appbus.pages.event_related.EventPreview;
import com.appbus.pages.event_related.EventRepeatOption;
import com.appbus.pages.event_related.NewEvent;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.RepeatEventHelper;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.tabs.CalendarTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;

public class RepeatEventEveryWeek
{
    @Test
    public void repeatEventEveryWeek() throws InterruptedException
    {
        /* Single run setup
        ActiveHamburgerMenu mm = new ActiveHamburgerMenu(FunctionalTest.getDriver());
        CommunicationsMenuItems communicationsMenuItems = mm.clickCommunications();

        Scroller.scrollRight("Calendar"); */

        CalendarTab calendarTab = new CalendarTab(FunctionalTest.getDriver()); // (2) bulk run
                                  //communicationsMenuItems.clickCalendar(); // (1) single run

        calendarTab.clickWeek();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        JSExecutor.injectJQuery();

        String time = "4 PM";
        System.out.println("Click near " + time + " by the third cell...");
        JSExecutor.clickViaJQuery("$('li.time-cell .time:contains(\"" + time + "\")').closest('li').next().next().next()"); // Tue

        // Save Start Repeat day
        String startRepDay = JSExecutor.getTextViaJQuery("$('.top-title-panel li:contains(\"Tue\")')").substring(4); // Tue %day%
        System.out.println("Start Repeat day = " + startRepDay);

        FunctionalTest.switchContext(Context.NATIVE);

        NewEvent newEvent = new NewEvent(FunctionalTest.getDriver());

        FunctionalTest.switchContext(Context.WEBVIEW);

        String repeatEventTitle = "rep_evr_Wk";
        newEvent.setTitle(repeatEventTitle);

        FunctionalTest.switchContext(Context.NATIVE);

        EventRepeatOption eventRepeatOption = newEvent.clickRepeatLabel();

        System.out.println("Setting of all weekdays to make sure that switcher changes from 'Custom' to 'On weekdays'");
        eventRepeatOption.repeatEveryWeek(true, 1, new String[]{"Mon", "Wed", "Thu", "Fri"});
        Assert.assertTrue((Boolean) FunctionalTest.getDriver().executeScript("return $('.repeat-subform__tabs span:contains(\"On\")').hasClass(\"selected\")"));
        Assert.assertFalse((Boolean) FunctionalTest.getDriver().executeScript("return $('.repeat-subform__tabs span:contains(\"Cus\")').hasClass(\"selected\")"));

        Thread.sleep(2000);

        eventRepeatOption.repeatEveryWeek(true, 1, new String[]{"Sun", "Thu", "Sat"});
        Thread.sleep(5000);

        eventRepeatOption.clickApply();

        FunctionalTest.switchContext(Context.NATIVE);
        EventEndRepeatOption eventEndRepeatOption = newEvent.clickEndRepeatLabel();

        eventEndRepeatOption.endRepeatAfterANumberOfOccurrences(13);
        eventEndRepeatOption.clickApply();

        newEvent.clickAccept(); // Final apply
        Thread.sleep(4000);

        System.out.println("Check that rep.events were created successfully...");

        RepeatEventHelper.initDaysOfWeek(time);

        for( int weekNum = 1; weekNum < 5; weekNum++ )
        {
            FunctionalTest.switchContext(Context.WEBVIEW);
            Thread.sleep(2000);

            if( weekNum == 1 ) // First week
            {
                RepeatEventHelper.assertWeek(repeatEventTitle, false, false, true, false, true, false, true);

                FunctionalTest.switchContext(Context.NATIVE);
                Thread.sleep(2000);

                calendarTab.clickArrowRight(); // +1 week forward
                continue;
            }

            if( weekNum == 4) // Last week
            {
                RepeatEventHelper.assertWeek(repeatEventTitle, true, false, true, false, false, false, false);
                break;
            }

            RepeatEventHelper.assertWeek(repeatEventTitle, true, false, true, false, true, false, true);

            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(2000);

            calendarTab.clickArrowRight(); // +1 week forward
        }

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4000);

        // Click by rep.every week event
        MobileElement repWeekEvent = CalendarTab.findEventByName(repeatEventTitle);
        repWeekEvent.click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        EventPreview eventPreview = new EventPreview();

        System.out.println("Checking that rep.every week event has correct title and time range...");
        Assert.assertEquals(repeatEventTitle, eventPreview.getEventTitle());
        Assert.assertTrue(eventPreview.getEventDate().contains("4:00 PM – 4:30 PM"));

        newEvent = eventPreview.clickEditEvent(); // Click Edit

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        System.out.println("Checking that Start Repeat day = " + startRepDay);
        Assert.assertTrue(newEvent.getStartRepeatDate().contains(startRepDay));

        // Edit event's title
        String newTitle = "[ed] " + newEvent.getTitle();
        newEvent.setTitle(newTitle);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4000);

        // Leave only Sun active
        newEvent.clickRepeatLabel().repeatEveryWeek(true, 1, new String[]{"Tue", "Thu", "Sat"});
        Thread.sleep(1000);
        newEvent.clickAccept();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4000);

        newEvent.clickEndRepeatLabel().endRepeatAfterANumberOfOccurrences(4); // Edit occurrence num and set = 4
        newEvent.clickAccept();

        newEvent.clickAccept(true).clickSequence(true).clickEditAnyway(); // Final accept as sequence

        //
        System.out.println("Move +2 weeks forward...");
        calendarTab.clickArrowRight();
        Thread.sleep(3000);

        calendarTab.clickArrowRight();
        Thread.sleep(3000);
        //

        for( int weekNum = 1; weekNum < 7; weekNum++ )
        {
            FunctionalTest.switchContext(Context.WEBVIEW);
            Thread.sleep(2000);

            if( weekNum == 1 ) // First week
            {
                RepeatEventHelper.assertWeek(newTitle, false, false, false, false, false, false, false);

                FunctionalTest.switchContext(Context.NATIVE);
                Thread.sleep(2000);

                calendarTab.clickArrowLeft(); // -1 week backward
                continue;
            }

            if( weekNum == 6 ) // Last week
            {
                RepeatEventHelper.assertWeek(newTitle, false, false, false, false, false, false, false);

                break;
            }

            RepeatEventHelper.assertWeek(newTitle, true, false, false, false, false, false, false); // Has event only on Sun

            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(2000);

            calendarTab.clickArrowLeft(); // -1 week backward
        }

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        // Move +1 week forward
        calendarTab.clickArrowRight();
        Thread.sleep(3000);

        CalendarTab.findEventByName(newTitle).click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        System.out.println("Trying to delete single event in sequence...");
        eventPreview = new EventPreview();
        eventPreview.clickDeleteEvent(true).delete(true);

        System.out.println("Checking that event was deleted as single...");
        Assert.assertNull(CalendarTab.findEventByName(newTitle));

        // Move +1 week forward
        calendarTab.clickArrowRight();
        Thread.sleep(3000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4_000);

        // Make deliberate auto refresh to check issue ED-3328: title should be the same
        calendarTab.clickRefreshButton();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4_000);

        MobileElement repEvrWeekToDelete = CalendarTab.findEventByName(newTitle);
        Assert.assertNotNull(repEvrWeekToDelete);

        repEvrWeekToDelete.click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        System.out.println("Trying to delete event as sequence...");
        eventPreview = new EventPreview();
        eventPreview.clickDeleteEvent(true).delete(false);

        System.out.println("Checking that event was deleted as sequence...");
        Assert.assertNull(CalendarTab.findEventByName(newTitle));

        calendarTab.clickArrowRight();
        Thread.sleep(3000);

        Assert.assertNull(CalendarTab.findEventByName(newTitle));
    }
}
