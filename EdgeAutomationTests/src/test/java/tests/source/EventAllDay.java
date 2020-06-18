package tests.source;

import com.appbus.pages.constants.Context;
import com.appbus.pages.event_related.*;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.tabs.CalendarTab;
import org.junit.Assert;
import org.junit.Test;

import java.text.SimpleDateFormat;
import java.util.Date;

public class EventAllDay
{
    private final String class_allDayLabel = "appointments-only-with-allday-title";


    @Test
    public void eventAllDay() throws InterruptedException
    {
        //ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver()); // (1) - Single run
        //CommunicationsMenuItems communicationsMenuItems = hamburgerMenu.clickCommunications(); // (1)

        CommunicationsMenuItems communicationsMenuItems = new CommunicationsMenuItems(FunctionalTest.getDriver()); // (2) - bulk run

        Scroller.scrollRight("Calendar");

        CalendarTab calendarTab = communicationsMenuItems.clickCalendar();

        calendarTab.clickToday();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        // Let's check that there is no 'all day' label in the left upper corner for today
        if( JSExecutor.getTextByClassName(class_allDayLabel).equals("0") == false )
        {
            System.err.println("[!] Today has one or more events with all day label.");
            System.err.println("[!] Please, remove those events and rerun the test.");
            System.err.println("[!] Test was stopped.");

            return; // stop test
        }

        NewEvent newEvent = calendarTab.clickNewEvenButton();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        JSExecutor.injectJQuery();

        String eventTitle = "! ALL_day Event";
        newEvent.setTitle(eventTitle);

        newEvent.clickAllDayCheckbox();

        System.out.println("Assert that timezone field is disabled...");
        Assert.assertTrue((Boolean) FunctionalTest.getDriver().executeScript("return $('.edit-info .clickable.field.separator .title:contains(\"Timezone\")').parent().hasClass(\"disabled\")"));

        System.out.println("Assert that Starts/Ends doesn't have time...");
        Assert.assertFalse(newEvent.getStartsDate().contains(":"));
        Assert.assertFalse(newEvent.getEndsDate().contains(":"));

        newEvent.clickAccept();

        Thread.sleep(3_000);

        System.out.println("Scroll page down to 11 PM...");
        FunctionalTest.getDriver().executeScript("document.querySelector('.day-left-col').iScroll.scrollToElement($('li.time-cell .time:contains(\"11 PM\")')[0], 0)");

        System.out.println("Assert that 'all day' label is still visible in the left upper corner...");
        Assert.assertEquals("all day", JSExecutor.getTextViaJQuery("$('." + class_allDayLabel + "')"));

        System.out.println("Click by just created 'all day' event");
        JSExecutor.clickViaJQuery("$('." + class_allDayLabel + "').next().children()");
        EventPreview eventPreview = new EventPreview();

        System.out.println("Assert that event preview has correct values...");
        Assert.assertEquals(eventTitle, eventPreview.getEventTitle());
        Assert.assertEquals(new SimpleDateFormat("d MMMM, E").format(new Date()), eventPreview.getEventDate());

        // Edit just created all day event and set repeat on the next day
        newEvent = eventPreview.clickEditEvent();

        EventRepeatOption eventRepeatOption = newEvent.clickRepeatLabel();

        eventRepeatOption.repeatEveryDay(1);
        eventRepeatOption.clickApply();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        EventEndRepeatOption eventEndRepeatOption = newEvent.clickEndRepeatLabel();

        eventEndRepeatOption.endRepeatAfterANumberOfOccurrences(2); // this mean that event will be only for current day and the next
        eventEndRepeatOption.clickApply();

        newEvent.clickAccept(); // Final accept

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        calendarTab.clickArrowRight(); // move to next day

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        System.out.println("Assert that next day also has 'all day' label...");
        Assert.assertEquals("all day", JSExecutor.getTextViaJQuery("$('." + class_allDayLabel + "')"));

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        calendarTab.clickWeek();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        System.out.println("Assert that week has only 2 'all day' event's...");
        Assert.assertEquals("! ALL_day Event! ALL_day Event", JSExecutor.getTextViaJQuery("$('#all-day-events-week .all-day-events-week-list-container')"));
        Assert.assertEquals("all day", JSExecutor.getTextViaJQuery("$('.all-day-events-week-caption')"));

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        CalendarTab.findEventByName(eventTitle).click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        eventPreview = new EventPreview();
        AllEventsSideBar allEventsSideBar = eventPreview.clickShowAllOccurrences();

        System.out.println("*** Making sure that there are only 2 events with title = " + eventTitle + " ***");
        Assert.assertEquals("! ALL_day Event! ALL_day Event", JSExecutor.getTextViaJQuery("$('#all-events-infinite-scroll li:nth-child(even) .event-title')"));

        System.out.println("Assert that events have 'all day' mark in date cell...");
        Assert.assertEquals("all dayall day", JSExecutor.getTextViaJQuery("$('#all-events-infinite-scroll .events-list .appointment-date')"));

        allEventsSideBar.clickAllEvents(); // Close sidebar

        System.out.println("Delete event...");
        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        CalendarTab.findEventByName(eventTitle).click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        eventPreview = new EventPreview();
        eventPreview.clickDeleteEvent(true).delete(false);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        Assert.assertNull(CalendarTab.findEventByName(eventTitle));
    }

}
