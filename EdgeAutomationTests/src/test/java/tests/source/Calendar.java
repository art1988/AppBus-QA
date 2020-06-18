package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.event_related.EventPreview;
import com.appbus.pages.event_related.NewEvent;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.CalendarTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;

import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.YearMonth;
import java.util.Date;

public class Calendar
{
    @Test
    public void calendar() throws InterruptedException
    {
        FunctionalTest.switchContext(Context.NATIVE);

        LocalDateTime today = LocalDateTime.now();

        int day = today.getDayOfMonth();
        String month = today.getMonth().toString();
        month = month.substring(0, 1).toUpperCase() + month.substring(1).toLowerCase();
        month = month.substring(0,3);
        int year = today.getYear();

        SimpleDateFormat simpleDateformat = new SimpleDateFormat("EEEE");
        String dayOfWeek = simpleDateformat.format(new Date());

        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver()); //(1) - bulk run
        ActiveHamburgerMenu hamburgerMenu = navBar.clickHamburgerMenu(); // (1) - bulk run
                                            //new ActiveHamburgerMenu(FunctionalTest.getDriver()); // (2) - non-bulk
        CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications();

        Scroller.scrollRight("Calendar");

        CalendarTab calendarTab = commMenuItems.clickCalendar();

        // Click Day mode
        calendarTab.clickDay();
        Thread.sleep(2000);
        calendarTab.initDateHeader(day, month, year, dayOfWeek);

        // Click Week mode
        calendarTab.clickWeek();
        Thread.sleep(2000);
        calendarTab.initDateHeader(day, month, year, dayOfWeek);

        // Click Month mode
        calendarTab.clickMonth();
        Thread.sleep(2000);
        calendarTab.initDateHeader(day, month, year, dayOfWeek);

        YearMonth curMonth = YearMonth.now();
        // Check month and year switching
        for(int n = 0; n < 13; n++) // Switch 13 months back
        {
            calendarTab.clickArrowLeft(); // Get prev. month

            curMonth = curMonth.minusMonths(1);
            String prevMonth = curMonth.getMonth().toString();
            prevMonth = prevMonth.substring(0, 1).toUpperCase() + prevMonth.substring(1).toLowerCase();
            prevMonth = prevMonth.substring(0,3);

            if(prevMonth.startsWith("Dec"))
            {
                year--;
            }

            calendarTab.initDateHeader(day, prevMonth, year, dayOfWeek);
        }

        // Click Year mode
        calendarTab.clickYear();
        calendarTab.initDateHeader(day, month, year, dayOfWeek);

        calendarTab.clickArrowRight(); // Click next year
        calendarTab.initDateHeader(day, month, ++year, dayOfWeek);

       // ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver());
        //CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications();

       // Scroller.scrollRight("Calendar");

       // CalendarTab calendarTab = commMenuItems.clickCalendar();
        calendarTab.clickToday();

        Thread.sleep(4000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(20000);

        NewEvent newEvent = calendarTab.clickNewEvenButton();

        FunctionalTest.switchContext(Context.WEBVIEW);

        String eventTitle    = "Event from autotest_unique",
               eventLocation = "Autotest location";

        newEvent.setTitle(eventTitle);
        newEvent.setLocation(eventLocation);

        newEvent.clickAccept();
        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3000);

        System.out.println("Day mode: checking that event was created successfully...");
        MobileElement justCreatedEvent = CalendarTab.findEventByName(eventTitle);
        Assert.assertEquals(eventTitle, justCreatedEvent.getText());

        calendarTab.clickWeek();
        System.out.println("Week mode: checking that event was created successfully...");
        justCreatedEvent = CalendarTab.findEventByName(eventTitle);
        Assert.assertEquals(eventTitle, justCreatedEvent.getText());

        calendarTab.clickMonth();
        System.out.println("Month mode: checking that event was created successfully...");
        justCreatedEvent = CalendarTab.findEventByName(eventTitle);
        Assert.assertEquals(eventTitle, justCreatedEvent.getText());

        calendarTab.clickToday();
        Thread.sleep(2000);

        justCreatedEvent.click();
        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(5000);

        EventPreview eventPreview = new EventPreview();
        eventPreview.clickDeleteEvent(false).delete(true);

        System.out.println("Checking that event was deleted successfully...");
        Thread.sleep(5000);
        justCreatedEvent = CalendarTab.findEventByName(eventTitle);
        Assert.assertEquals(null, justCreatedEvent);
    }
}
