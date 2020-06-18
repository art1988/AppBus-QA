package com.appbus.pages.helpers;

import com.appbus.pages.constants.DayOfWeek;
import org.junit.Assert;
import tests.source.FunctionalTest;

import java.text.SimpleDateFormat;
import java.time.Month;
import java.util.Calendar;
import java.util.EnumMap;

public class RepeatEventHelper
{
    /**
     * Map every day of week to jquery statement:
     * .next()               - Sun
     * .next().next()        - Mon
     * .next().next().next() - Tue
     * etc.
     */
    private static EnumMap<DayOfWeek, String> daysOfWeek = new EnumMap<>(DayOfWeek.class);

    private static final String NO_EVENT = "[]";

    /**
     * Initialize map by given time
     * @param time
     */
    public static void initDaysOfWeek(String time)
    {
        StringBuffer jqueryStatementStart = new StringBuffer("return $('li.time-cell .time:contains(\"" + time + "\")').closest('li').next()"); // Start from Sun

        for( DayOfWeek day : DayOfWeek.values() )
        {
            daysOfWeek.put(day, jqueryStatementStart.toString());

            jqueryStatementStart.append(".next()");
        }
    }

    public static void assertSingleDay(DayOfWeek day, boolean shouldHasEvent, String eventTitle)
    {
        if( shouldHasEvent == true )
        {
            Assert.assertFalse(FunctionalTest.getDriver().executeScript(daysOfWeek.get(day) + ".has(\"div\").has(\"span:contains('" + eventTitle + "')\")").toString().equals(NO_EVENT));
        }
        else
        {
            Assert.assertTrue(FunctionalTest.getDriver().executeScript(daysOfWeek.get(day) + ".has(\"div\").has(\"span:contains('" + eventTitle + "')\")").toString().equals(NO_EVENT));
        }
    }

    /**
     * <p>Check week by going through days.</p>
     * <p>IMPORTANT: hasEvent must have strict order of days: beginning from Sun, Mon, ..., ends with Sat</p>
     * @param eventTitle title of event
     * @param hasEvent order of days to check. Must have strict order of days: beginning from Sun
     */
    public static void assertWeek(String eventTitle, boolean... hasEvent)
    {
        for( int i = 0; i < hasEvent.length; i++ )
        {
            assertSingleDay(DayOfWeek.values()[i], hasEvent[i], eventTitle);
        }
    }

    /**
     * Go through day cells in Month view and assert that dayWithEvent cell has event with subject = eventTitle.
     * <p>
     * Note: To assert all month on absence of event with subject = eventTitle, need to set dayWithEvent = 0
     * @param dayWithEvent day of month with wanted event
     * @param eventTitle title of wanted event
     */
    public static void assertMonth(int dayWithEvent, String eventTitle, Calendar calendar)
    {
        boolean wholeMonthDoesntHaveEvent = true;

        int maxDayOfMonth = calendar.getActualMaximum(Calendar.DAY_OF_MONTH);
        System.out.println("maxDayOfMonth = " + maxDayOfMonth);

        for( int day = 1; day < maxDayOfMonth+1; day++ )
        {
            String foundEventsTitleInCell = String.valueOf(FunctionalTest.getDriver().executeScript("return $('#grid-month-cell-" + day + " .appointments-container .event-item-month .subject:contains(\"" + eventTitle + "\")').text()"));

            // For particular day(a day with event) we should get one repeated event with title = eventTitle
            // if dayWithEvent = 0 then all month doesn't have event with subject = eventTitle
            if( dayWithEvent == day )
            {
                Assert.assertEquals(eventTitle, foundEventsTitleInCell);

                System.out.println("On " + day +
                                   " of " + new SimpleDateFormat("MMM").format(calendar.getTime()) +
                                   " " + calendar.get(Calendar.YEAR) + " event with title = " + eventTitle + " was found !");

                wholeMonthDoesntHaveEvent = false;

                continue;
            }

            Assert.assertEquals("", foundEventsTitleInCell); // for all others days there is no such event in cell
        }

        if( wholeMonthDoesntHaveEvent )
        {
            System.out.println("Whole month " + new SimpleDateFormat("MMM").format(calendar.getTime()) +
                               " " + calendar.get(Calendar.YEAR) +
                               " doesn't have event with title = " + eventTitle);
        }
    }
}
