package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.constants.Notifications;
import com.appbus.pages.event_related.EventAlertOption;
import com.appbus.pages.event_related.EventPreview;
import com.appbus.pages.event_related.EventStartsOption;
import com.appbus.pages.event_related.NewEvent;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.CalendarTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class EventAlert
{
    private EventStartsOption eventStartsOption;


    @Test
    public void eventAlert() throws InterruptedException
    {
        //ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver()); // (1) - Single run
        //CommunicationsMenuItems communicationsMenuItems = hamburgerMenu.clickCommunications(); // (1)

        //CommunicationsMenuItems communicationsMenuItems = new CommunicationsMenuItems(FunctionalTest.getDriver()); // (2) - bulk run
        //Scroller.scrollRight("Calendar");

        CalendarTab calendarTab = new CalendarTab(FunctionalTest.getDriver());

        calendarTab.clickToday();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        NewEvent newEvent = calendarTab.clickNewEvenButton();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        String eventTitle = "Event alert autotest";
        newEvent.setTitle(eventTitle);

        FunctionalTest.switchContext(Context.NATIVE);

        eventStartsOption = newEvent.clickStartsLabel();
        setCorrectTimeForAlert();
        Thread.sleep(4000);

        eventStartsOption.clickApply();
        Thread.sleep(4000);

        FunctionalTest.switchContext(Context.NATIVE);

        EventAlertOption eventAlertOption = newEvent.clickAlertLabel();
        eventAlertOption.setAlertTime("At time of event");

        eventAlertOption.clickApply();

        newEvent.clickAccept(); // Final apply of event

        System.out.println("Current time is: " + Calendar.getInstance().getTime());

        FunctionalTest.switchContext(Context.NATIVE);

        calendarTab.clickWeek();

        // Wait until notification alert popup will appear ( 10 mins max )
        System.out.println("Waiting for alert notification pop-up (up to 10 mins)...");
        MobileElement notificationPopup = (MobileElement)(new WebDriverWait(FunctionalTest.getDriver(), 10 * 60 * 1000)).until(ExpectedConditions.visibilityOfElementLocated(By.name(Notifications.EVENT_REMINDER.getNotificationText())));
        Assert.assertNotNull(notificationPopup);

        System.out.println("Navigate to Documents...");
        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver());
        ActiveHamburgerMenu hamburgerMenu = navBar.clickHamburgerMenu();

        hamburgerMenu.clickDocuments();
        Thread.sleep(2000);

        navBar.clickNotification().clickByNotificationMessage(Notifications.EVENT_REMINDER);
        Thread.sleep(2000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        EventPreview eventPreview = new EventPreview();

        System.out.println("Making sure that correct event was opened...");
        Assert.assertEquals(eventTitle, eventPreview.getEventTitle());
        Assert.assertEquals("At time of event", eventPreview.getEventAlertValue());

        System.out.println("Delete event with name = " + eventTitle);
        eventPreview.clickDeleteEvent(false).delete(true);
        Thread.sleep(2000);

        Assert.assertNull(CalendarTab.findEventByName(eventTitle)); // Assert that event was deleted

        Thread.sleep(5000);
    }

    /**
     * Set +5 mins from current system time for event alert
     */
    private void setCorrectTimeForAlert() throws InterruptedException
    {
        Date date = new Date();
        Calendar calendar = GregorianCalendar.getInstance();
        calendar.setTime(date);

        int hour = calendar.get(Calendar.HOUR);   // gets hour in 12h format
        int min  = calendar.get(Calendar.MINUTE); // get cur min
        int amPm = Calendar.AM;                   // AM by default

        if (calendar.get(Calendar.AM_PM) == Calendar.PM)
        {
            amPm = Calendar.PM;
        }

        if ( min >= 55 )
        {
            if( 60 - min <= 1 ) // have less than 1 minute... Need to add +5 more
            {
                min = 5;
            }
            else
            {
                min = 0;
            }

            hour++;

            if( hour == 12 ) // Set PM instead of AM
            {
                amPm = Calendar.PM;
            }

            eventStartsOption.setTime(hour, min, amPm);

            return;
        }

        if ( min % 5 == 0 ) // add +5 if multiple 5
        {
            min += 5;
        }
        else
        {
            int min_to_set = (min / 5) * 5 + 5;

            if( Math.abs(min_to_set - min) <= 1 ) // have less than 1 minute... Need to add +5 more
            {
                min = min_to_set + 5;

                if(min == 60)
                {
                    hour++;
                    min = 5;
                }
            }
            else
            {
                min = min_to_set;
            }
        }

        eventStartsOption.setTime(hour, min, amPm);
    }
}
