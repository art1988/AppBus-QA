package com.appbus.pages.event_related;

import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;

import java.time.Month;

// Non-native, so no need to extends from PageObject
public class EventEndRepeatOption
{
                                // id's of < select > drums
    private static final String id_DaySelector   = "drumDay",
                                id_MonthSelector = "drumMonth",
                                id_YearSelector  = "drumYear",

                                // id's of arrows up/down (tick drum by one)
                                id_DayUp     = "dial-up-drum_drumDay",
                                id_DayDown   = "dial-down-drum_drumDay",

                                id_MonthUp   = "dial-up-drum_drumMonth",
                                id_MonthDown = "dial-down-drum_drumMonth",

                                id_YearUp    = "dial-up-drum_drumYear",
                                id_YearDown  = "dial-down-drum_drumYear",
                                ////////////////////////////////////////////

                                id_IntervalSelector = "interval-selector",

                                id_Apply    = "apply-changes-icon";

    public EventEndRepeatOption()
    {
        JSExecutor.injectJQuery();

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('.form-body .edit-header .header-text:contains(\"End Repeat\")')") &
                 JSExecutor.isVisibleViaJQuery("$('.edit-info .timezone-text .title:contains(\"Never\")')") );
    }

    public void endRepeatInDate(int endDay, int endMonth, int endYear) throws InterruptedException
    {
        JSExecutor.clickViaJQuery("$('.edit-info .timezone-text .title:contains(\"In\")')");

        JSExecutor.setTextForSelect(id_DaySelector, String.valueOf(endDay));
        Thread.sleep(1000); // necessary for correct saving due to debounce of js function

        JSExecutor.setTextForSelect(id_MonthSelector, String.valueOf(endMonth));
        Thread.sleep(1000); // necessary for correct saving due to debounce of js function

        JSExecutor.setTextForSelect(id_YearSelector, String.valueOf(endYear));
        Thread.sleep(1000); // necessary for correct saving due to debounce of js function

        System.out.println("Was set: End repeat in date " + endDay + " " + Month.values()[endMonth] + " " + endYear);
    }

    /**
     * One tick up of day drum ( -1 day )
     */
    public void drumDayUp()
    {
        JSExecutor.clickByElement(id_DayUp);
        System.out.println("Drum: day up");
    }

    /**
     * One tick down of day drum ( +1 day )
     */
    public void drumDayDown()
    {
        JSExecutor.clickByElement(id_DayDown);
        System.out.println("Drum: day down");
    }

    /**
     * One tick up of month drum ( -1 month )
     */
    public void drumMonthUp()
    {
        JSExecutor.clickByElement(id_MonthUp);
        System.out.println("Drum: month up");
    }

    /**
     * One tick down of month drum ( +1 month )
     */
    public void drumMonthDown()
    {
        JSExecutor.clickByElement(id_MonthDown);
        System.out.println("Drum: month down");
    }

    /**
     * One tick up of year drum ( -1 year )
     */
    public void drumYearUp()
    {
        JSExecutor.clickByElement(id_YearUp);
        System.out.println("Drum: year up");
    }

    /**
     * One tick down of year drum ( +1 year )
     */
    public void drumYearDown()
    {
        JSExecutor.clickByElement(id_YearDown);
        System.out.println("Drum: year down");
    }

    /**
     * Click by In date label
     * Leave End Repeat In Date as default value (+6 days from current day if Repeat was set as Every Day)
     */
    public void endRepeatInDate()
    {
        JSExecutor.clickViaJQuery("$('.edit-info .timezone-text .title:contains(\"In\")')");
        System.out.println("In date was clicked...");
    }

    public void endRepeatAfterANumberOfOccurrences(int occurNum)
    {
        JSExecutor.clickViaJQuery("$('.edit-info .timezone-text .title:contains(\"After a\")')");
        JSExecutor.setTextForSelect(id_IntervalSelector, String.valueOf(occurNum));

        System.out.println("Was set: End Repeat after " + occurNum + " occurrences");
    }

    public void clickApply()
    {
        JSExecutor.clickByElement(id_Apply);
        System.out.println("Apply button was clicked");
    }

    /**
     * Get chosen day value from drum
     * @return day
     */
    public int getDayValue()
    {
        return Integer.parseInt(JSExecutor.getTextFromSelect(id_DaySelector));
    }

    /**
     * Get chosen month value from drum
     * @return 0 - January, 1 - February, ...
     */
    public int getMonthValue()
    {
        return Integer.parseInt(JSExecutor.getTextFromSelect(id_MonthSelector));
    }

    /**
     * Get chosen year value from drum
     * @return year
     */
    public int getYearValue()
    {
        return Integer.parseInt(JSExecutor.getTextFromSelect(id_YearSelector));
    }
}
