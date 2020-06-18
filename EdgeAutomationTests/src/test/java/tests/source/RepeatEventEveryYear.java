package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.event_related.*;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.RepeatEventHelper;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.tabs.CalendarTab;
import org.junit.Assert;
import org.junit.Test;

import java.text.SimpleDateFormat;
import java.time.Month;
import java.time.YearMonth;
import java.util.Calendar;


public class RepeatEventEveryYear
{
    private CalendarTab calendarTab;
    private EventEndRepeatOption eventEndRepeatOption;


    @Test
    public void repeatEventEveryYear() throws InterruptedException
    {
        //ActiveHamburgerMenu mm = new ActiveHamburgerMenu(FunctionalTest.getDriver());  // (1) - single run
        //CommunicationsMenuItems communicationsMenuItems = mm.clickCommunications();    // (1)

        //Scroller.scrollRight("Calendar"); // (1)

        calendarTab = new CalendarTab(FunctionalTest.getDriver());
                      //communicationsMenuItems.clickCalendar(); // (1)

        calendarTab.clickToday();
        calendarTab.clickWeek();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        JSExecutor.injectJQuery();

        NewEvent repEventEveryYear = calendarTab.clickNewEvenButton(); // Create event

        String eventTitle = "! rep_e_year";

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        repEventEveryYear.setTitle(eventTitle);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);

        EventRepeatOption eventRepeatOption = repEventEveryYear.clickRepeatLabel();

        int dayOfMonth = Calendar.getInstance().get(Calendar.DAY_OF_MONTH); // Get current day

        YearMonth yearMonth = YearMonth.now();
        String month = yearMonth.getMonth().toString();

        // By design of test: create rep. event every year on current day of current month
        eventRepeatOption.repeatEveryYearOnDate(1, dayOfMonth, month.substring(0, 1) + month.substring(1).toLowerCase());
        eventRepeatOption.clickApply();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);

        eventEndRepeatOption = repEventEveryYear.clickEndRepeatLabel();
        String endRepeat = setCorrectEndRepeatDate();
        eventRepeatOption.clickApply();

        repEventEveryYear.clickAccept(); // final approval of event
        System.out.println("*** Yearly repeated event with name = " + eventTitle + " was created... ***");

        // Initialize mutable calendar instance
        Calendar calendar = Calendar.getInstance();
        calendar.setFirstDayOfWeek(Calendar.SUNDAY);

        // Move year forward from current to (current + 3)
        for( int yearNum = 0; yearNum < 3; yearNum++ )
        {
            checkYear(dayOfMonth, eventTitle, calendar);

            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(2_000);

            calendarTab.clickYear(); // switch to Year view
            calendarTab.clickArrowRight(); // get next year

            // add +1 year in calendar instance since we pressed arrow right button in year view
            calendar.add(Calendar.YEAR, +1);
        }

        // we are on the year that should not have event - checking it ( current_year + 3 )

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        // First 3 capitalized letters of current month
        String curMonth = new SimpleDateFormat("MMM").format(calendar.getTime()).toUpperCase();

        // Click by current month in the year = current_year + 3
        JSExecutor.clickViaJQuery("$('.year-picker .month-title:contains(\"" + curMonth + "\")')");
        Thread.sleep(2_000);

        RepeatEventHelper.assertMonth(0, eventTitle, calendar);

        // Go back to prev. year to rename yearly repeated event
        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);

        calendarTab.clickYear();
        calendarTab.clickArrowLeft();
        calendar.add(Calendar.YEAR, -1);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        // Click by current month title
        JSExecutor.clickViaJQuery("$('.year-picker .month-title:contains(\"" + curMonth + "\")')");
        Thread.sleep(2_000);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);

        CalendarTab.findEventByName(eventTitle).click(); // Click by event

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        EventPreview eventPreview = new EventPreview();
        NewEvent eventToEdit = eventPreview.clickEditEvent(); // Click edit event

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        // Set new title of yearly repeated event and save as sequence
        eventTitle = "[ed] Yearly";
        eventToEdit.setTitle(eventTitle);

        System.out.println("Making sure that Start Repeat and End Repeat dates are correct...");

        String startRepeat = String.valueOf(dayOfMonth) + " " +
                             month.substring(0, 1) + month.substring(1).toLowerCase().substring(0, 2) + " " +
                             yearMonth.getYear();

        Assert.assertEquals(startRepeat, eventToEdit.getStartRepeatDate());
        Assert.assertEquals(endRepeat, eventToEdit.getEndRepeatDate());

        eventToEdit.clickAccept(true).clickSequence(false);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        CalendarTab.findEventByName(eventTitle).click(); // Click by event

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        eventPreview = new EventPreview();
        AllEventsSideBar allEventsSideBar = eventPreview.clickShowAllOccurrences();

        System.out.println("Checking that event with name = " + eventTitle + " is visible...");
        Assert.assertTrue(allEventsSideBar.isEventVisibleByName(eventTitle));

        System.out.println("*** Making sure that there are only 3 events with title = " + eventTitle + " ***");
        Assert.assertEquals("[ed] Yearly[ed] Yearly[ed] Yearly", JSExecutor.getTextViaJQuery("$('#all-events-infinite-scroll li:nth-child(even) .event-title')"));

        // Close All Events Side Bar
        allEventsSideBar.clickAllEvents();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        CalendarTab.findEventByName(eventTitle).click(); // Click by event

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        eventPreview = new EventPreview();
        eventToEdit = eventPreview.clickEditEvent();

        eventEndRepeatOption = eventToEdit.clickEndRepeatLabel();
        eventEndRepeatOption.endRepeatAfterANumberOfOccurrences(2); // set end repeat after a number of occurrences = 2 by design of test
        eventEndRepeatOption.clickApply();

        // Final approval of event as Sequence and edit anyway
        eventToEdit.clickAccept(true).clickSequence(true).clickEditAnyway();
        Thread.sleep(2_000);

        // For this year event should be deleted. Checking it
        Assert.assertNull(CalendarTab.findEventByName(eventTitle));

        System.out.println("Checking that 2 previous years have event...");
        // By design of test: 2 previous years must have event - checking it
        for( int yearNum = 2; yearNum > 0; yearNum-- )
        {
            calendarTab.clickYear();
            calendarTab.clickArrowLeft();
            calendar.add(Calendar.YEAR, -1);

            checkYear(dayOfMonth, eventTitle, calendar);

            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(2_000);
        }

        System.out.println("*** Trying to delete event with title = " + eventTitle + " completely... ***");

        CalendarTab.findEventByName(eventTitle).click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        eventPreview = new EventPreview();
        eventPreview.clickDeleteEvent(true).delete(false);
        Thread.sleep(2_000);

        Assert.assertNull(CalendarTab.findEventByName(eventTitle));

        System.out.println("*** Making sure that next 3 years doesn't have event with title = " + eventTitle + " on month = " + curMonth + " ***");
        for( int yearNum = 0; yearNum < 3; yearNum++ )
        {
            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(2_000);

            calendarTab.clickYear();
            calendarTab.clickArrowRight();
            calendar.add(Calendar.YEAR, +1);

            FunctionalTest.switchContext(Context.WEBVIEW);
            Thread.sleep(2_000);

            // Click by current month title
            JSExecutor.clickViaJQuery("$('.year-picker .month-title:contains(\"" + curMonth + "\")')");
            Thread.sleep(2_000);

            RepeatEventHelper.assertMonth(0, eventTitle, calendar);
        }
    }

    /**
     * By design of test: set day = 1; leave current month; set year +3 from current.
     * <p>
     * If the date is 1st January, then set day = 1; month = december; set year +2 from current.
     * <p>
     * This mean that repeated every year event should appear in current_year, current_year + 1 and current_year + 2
     * @return String of End Repeat field that has format like 1 Oct 2021
     */
    private String setCorrectEndRepeatDate() throws InterruptedException
    {
        YearMonth yearMonth = YearMonth.now();

        int currentDay   = Calendar.getInstance().get(Calendar.DAY_OF_MONTH),
            currentMonth = yearMonth.getMonth().getValue() - 1;

        int yearToSet = yearMonth.getYear() + 3;


        if ( currentMonth != 0 && currentDay == 1 ) // 1st day of any month except January
        {
            yearMonth = yearMonth.minusMonths(1);
        }
        else if ( currentMonth == 0 && currentDay == 1 ) // 1st day of January
        {
            yearToSet = yearMonth.getYear() + 2;
            yearMonth = yearMonth.minusMonths(1);
        }

        int monthToSet = yearMonth.getMonth().getValue() - 1;

        eventEndRepeatOption.endRepeatInDate(1, monthToSet, yearToSet);

        String monthStr = yearMonth.getMonth().toString();

        return "1 " +  monthStr.substring(0, 1) + monthStr.substring(1).toLowerCase().substring(0, 2) + " " + yearToSet;
    }

    /**
     * Pick up 3 random months and check presence of repeated event in them.
     * <p>
     * Anyway, method will check presence of yearly repeated event for current month (the month on which it was created)
     * @param dayWithEvent day of month that has yearly repeated event
     * @param eventTitle title of yearly repeated event
     * @throws InterruptedException
     */
    private void checkYear(int dayWithEvent, String eventTitle, Calendar calendar) throws InterruptedException
    {
        System.out.println("Checking the following year : " + calendar.get(Calendar.YEAR));

        // First 3 capitalized letters of current month
        String curMonth = new SimpleDateFormat("MMM").format(calendar.getTime()).toUpperCase();
        System.out.println("curMonth = " + curMonth);

        for( int i = 0; i < 3; i++ )
        {
            FunctionalTest.switchContext(Context.NATIVE);
            Thread.sleep(2_000);

            calendarTab.clickYear(); // switch to Year view

            Month month = Month.values()[(int)(Math.random() * 12)]; // picked month

            String monthNameCapitalized3Letters = month.toString().substring(0, 3);

            FunctionalTest.switchContext(Context.WEBVIEW);
            Thread.sleep(2_000);

            System.out.println("Picked month is: " + monthNameCapitalized3Letters);
            // Each time when month was changed, set this month's value for calendar instance
            calendar.set(Calendar.MONTH, month.getValue() - 1);

            // Click on month header to open month view ( from year view -> to month view )
            JSExecutor.clickViaJQuery("$('.year-picker .month-title:contains(\"" + monthNameCapitalized3Letters + "\")')");
            Thread.sleep(2_000);

            // If picked month equals current month => must have repeated event
            if( monthNameCapitalized3Letters.equals(curMonth) )
            {
                RepeatEventHelper.assertMonth(dayWithEvent, eventTitle, calendar);
            }
            else // picked month doesn't have repeated event
            {
                RepeatEventHelper.assertMonth(0, eventTitle, calendar);
            }
        }

        // Anyway, check that desired month has yearly repeated event
        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);

        calendarTab.clickYear(); // switch to Year view

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        // Click by header of current month
        JSExecutor.clickViaJQuery("$('.year-picker .month-title:contains(\"" + curMonth + "\")')");
        Thread.sleep(2_000);

        // Set back current month for calendar instance
        // calendar - is mutable instance
        calendar.set(Calendar.MONTH, Calendar.getInstance().get(Calendar.MONTH));
        Thread.sleep(2_000);

        RepeatEventHelper.assertMonth(dayWithEvent, eventTitle, calendar);
    }

}
