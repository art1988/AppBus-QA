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
import org.junit.Assert;
import org.junit.Test;

import java.time.Month;
import java.util.Calendar;

public class RepeatEventEveryMonth
{
    private Calendar calendar;

    private EventEndRepeatOption eventEndRepeatOption;

    private boolean shouldBe5Repetition;


    @Test
    public void repeatEventEveryMonth() throws InterruptedException
    {
        //ActiveHamburgerMenu mm = new ActiveHamburgerMenu(FunctionalTest.getDriver());  // (1) - single run
        //CommunicationsMenuItems communicationsMenuItems = mm.clickCommunications();    // (1)

        //Scroller.scrollRight("Calendar"); // (1)
        CalendarTab calendarTab = new CalendarTab(FunctionalTest.getDriver());
                                  //communicationsMenuItems.clickCalendar(); // (1)

        calendarTab.clickToday();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        JSExecutor.injectJQuery();

        NewEvent eventRepEveryMonth = calendarTab.clickNewEvenButton();

        String eventTitle = "! rep_e_month";

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        eventRepEveryMonth.setTitle(eventTitle);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3000);

        calendar = Calendar.getInstance();
        calendar.setFirstDayOfWeek(Calendar.SUNDAY);

        int currentDayOfMonth = calendar.get(Calendar.DAY_OF_MONTH); // On this day event was created

        System.out.println("Creating repeat event of each month on " + currentDayOfMonth + " ...");

        EventRepeatOption eventRepeatOption = eventRepEveryMonth.clickRepeatLabel();

        eventRepeatOption.repeatEveryMonthOnDayOfMonth(1, currentDayOfMonth);
        eventRepeatOption.clickApply();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3000);

        eventEndRepeatOption = eventRepEveryMonth.clickEndRepeatLabel();

        eventEndRepeatOption.endRepeatInDate(); // Click by In date label
        setCorrectEndRepeatDate();
        eventEndRepeatOption.clickApply();

        eventRepEveryMonth.clickAccept(); // Final apply of event

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3000);

        calendarTab.clickMonth();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        for( int i = 0; i < 4; i++ )
        {
            RepeatEventHelper.assertMonth(currentDayOfMonth, eventTitle, calendar);

            // set currentDayOfMonth back
            currentDayOfMonth = Calendar.getInstance().get(Calendar.DAY_OF_MONTH);

            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(3000);

            // Move to next month
            calendarTab.clickArrowRight();
            Thread.sleep(3000);

            // add +1 month in calendar instance since we pressed arrow right button in month view
            calendar.add(Calendar.MONTH, 1);

            // In case if repeated event was created on 31st day and the next month has 30 days then
            // repeated event should be shifted on 30th day.
           //if( currentDayOfMonth == Calendar.getInstance().getActualMaximum(Calendar.DAY_OF_MONTH) )
            //{
                if( currentDayOfMonth > calendar.getActualMaximum(Calendar.DAY_OF_MONTH) )
                {
                    currentDayOfMonth = calendar.getActualMaximum(Calendar.DAY_OF_MONTH);
                }
           // }

            FunctionalTest.switchContext(Context.WEBVIEW);
            Thread.sleep(3000);
        }

        if( shouldBe5Repetition == true ) // in case if event was created on 1-st day of any month
        {
            RepeatEventHelper.assertMonth(currentDayOfMonth, eventTitle, calendar);

            // and the next month should not have that event
            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(3000);

            // Move to next month
            calendarTab.clickArrowRight();
            Thread.sleep(3000);

            // add +1 month in calendar instance since we pressed arrow right button in month view
            calendar.add(Calendar.MONTH, 1);

            FunctionalTest.switchContext(Context.WEBVIEW);
            Thread.sleep(3000);

            RepeatEventHelper.assertMonth(0, eventTitle, calendar);
        }
        else
        {
            System.out.println("Making sure that whole month doesn't have event with title = " + eventTitle);
            RepeatEventHelper.assertMonth(0, eventTitle, calendar);
        }

        // Delete event...
        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3000);

        // Move one month back
        calendarTab.clickArrowLeft();
        Thread.sleep(3000);

        // subtract -1 month in calendar instance since we pressed arrow left button in month view
        calendar.add(Calendar.MONTH, -1);

        System.out.println("Trying to delete event with name = " + eventTitle);
        CalendarTab.findEventByName(eventTitle).click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        EventPreview eventPreview = new EventPreview();

        eventPreview.clickDeleteEvent(true).delete(false);

        System.out.println("Checking that there is no event on prev. months...");
        for( int i = 0; i < 5; i++ )
        {
            FunctionalTest.switchContext(Context.WEBVIEW);
            Thread.sleep(3000);

            RepeatEventHelper.assertMonth(0, eventTitle, calendar);

            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(3000);

            // Move one month back
            calendarTab.clickArrowLeft();
            Thread.sleep(3000);

            // subtract -1 month in calendar instance since we pressed arrow left button in month view
            calendar.add(Calendar.MONTH, -1);
        }
    }

    /**
     * By design of test: [+5 month] from current and [-1 day] in End date -> In date
     */
    private void setCorrectEndRepeatDate() throws InterruptedException
    {
        Calendar cal = Calendar.getInstance();

        int curDayOfMonth = cal.get(Calendar.DAY_OF_MONTH);

        // Firstly, set year - 1 from current
        eventEndRepeatOption.drumYearUp();
        Thread.sleep(1000);

        // Secondly, add +5 months from current
        for( int i = 0; i < 5; i++ )
        {
            eventEndRepeatOption.drumMonthDown();
            Thread.sleep(500);
        }

        // Finally set day -1 from current
        if( curDayOfMonth == 1 )
        {
            // do nothing if current day is 1
            shouldBe5Repetition = true;
        }
        else
        {
            eventEndRepeatOption.drumDayUp(); // else set day -1 from current
        }
        Thread.sleep(1000);

        // Check warning message about correct bounds
        if( JSExecutor.isVisibleViaJQuery("$('.date-error')") == true )
        {
            // If we see warning message about bounds - add +1 year
            eventEndRepeatOption.drumYearDown();
            Thread.sleep(500);
        }

        System.out.println("End Repeat: In date was set as: " + eventEndRepeatOption.getDayValue() + " "
                                                              + Month.of(eventEndRepeatOption.getMonthValue() + 1).name() + " "
                                                              + eventEndRepeatOption.getYearValue());
    }
}
