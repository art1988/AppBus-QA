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

public class RepeatEventEveryDay
{
    @Test
    public void repeatEventEveryDay() throws InterruptedException
    {
        ActiveHamburgerMenu mm = new ActiveHamburgerMenu(FunctionalTest.getDriver());
        CommunicationsMenuItems communicationsMenuItems = mm.clickCommunications();

        Scroller.scrollRight("Calendar");

        CalendarTab calendarTab = communicationsMenuItems.clickCalendar();

        calendarTab.clickWeek();

        FunctionalTest.switchContext(Context.WEBVIEW);

        JSExecutor.injectJQuery();

        String time = "2 PM";
        System.out.println("Click near " + time + " by the third cell...");
        JSExecutor.clickViaJQuery("$('li.time-cell .time:contains(\"" + time + "\")').closest('li').next().next().next()");

        FunctionalTest.switchContext(Context.NATIVE);

        NewEvent newEvent = new NewEvent(FunctionalTest.getDriver());

        FunctionalTest.switchContext(Context.WEBVIEW);

        String repeatEventTitle = "rep_evr_Day";
        newEvent.setTitle(repeatEventTitle);

        FunctionalTest.switchContext(Context.NATIVE);
        EventRepeatOption eventRepeatOption = newEvent.clickRepeatLabel();
        eventRepeatOption.repeatEveryDay(1);
        eventRepeatOption.clickApply();

        FunctionalTest.switchContext(Context.NATIVE);
        EventEndRepeatOption eventEndRepeatOption = newEvent.clickEndRepeatLabel();

        /*
        Date today = new Date();

        java.util.Calendar cal = new GregorianCalendar();
        cal.clear();

        cal.setTime(today);

        int curDayOfMonth = cal.get(java.util.Calendar.DAY_OF_MONTH); // Get current day of month

        //eventEndRepeatOption.endRepeatInDate(curDayOfMonth + 8); // +8;
        */
        eventEndRepeatOption.endRepeatInDate(); // +6 - by default
        eventEndRepeatOption.clickApply();

        Thread.sleep(2000);

        // Final apply for new event
        newEvent.clickAccept();

        // Check amount of repeated events
        System.out.println("Checking the amount of repeated events...");

        RepeatEventHelper.initDaysOfWeek(time);

        RepeatEventHelper.assertWeek(repeatEventTitle, false, false, true, true, true, true, true);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4000);

        calendarTab.clickArrowRight(); // Get next week
        Thread.sleep(5000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        System.out.println("Checking that only Sun and Mon has rep. event...");

        RepeatEventHelper.assertWeek(repeatEventTitle, true, true, false, false, false, false, false);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4000);

        // Edit repeated event
        MobileElement repEvent = CalendarTab.findEventByName(repeatEventTitle);
        repEvent.click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        EventPreview eventPreview = new EventPreview();

        // Make sure that it is repeated event
        System.out.println("Checking that repeated event has correct title and date");
        Assert.assertEquals(repeatEventTitle, eventPreview.getEventTitle());
        Assert.assertTrue(eventPreview.getEventDate().contains("2:00 PM – 2:30 PM,"));

        // Check of ED-3073
        System.out.println("Trying to change title of repeated event...");
        newEvent = eventPreview.clickEditEvent();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        repeatEventTitle = newEvent.getTitle() + " [edited]"; // Edit existing title of repeated event

        newEvent.setTitle(repeatEventTitle);
        newEvent.clickAccept(true).clickSequence(false);
        Thread.sleep(3000);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(12000);

        repEvent = CalendarTab.findEventByName(repeatEventTitle);
        repEvent.click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        eventPreview = new EventPreview();

        // Delete _single_ rep. event
        System.out.println("Delete _single_ event...");
        eventPreview.clickDeleteEvent(true).delete(true);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        System.out.println("Checking that Sun doesn't have rep. event...");
        RepeatEventHelper.assertWeek(repeatEventTitle, false, true, false, false, false, false, false);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4000);

        repEvent = CalendarTab.findEventByName(repeatEventTitle);
        repEvent.click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        eventPreview = new EventPreview();
        // Delete _sequence_ rep. event
        System.out.println("Delete _sequence_ event...");
        eventPreview.clickDeleteEvent(true).delete(false);
        Thread.sleep(5000);

        System.out.println("Checking that repeated event with name = " + repeatEventTitle + " is no longer exists...");

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        RepeatEventHelper.assertWeek(repeatEventTitle, false, false, false, false, false, false, false);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4000);

        calendarTab.clickArrowLeft(); // Get prev.week

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        RepeatEventHelper.assertWeek(repeatEventTitle, false, false, false, false, false, false, false);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(7000);
    }

}
