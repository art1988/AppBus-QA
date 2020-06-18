package com.appbus.pages.event_related;

import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;

import java.util.Arrays;

// Non-native, so no need to extends from PageObject
public class EventRepeatOption
{
    private static final String id_IntervalSelector = "interval-selector",
                                id_DayOfMonth       = "day-of-month-selector",
                                id_MonthSelector    = "month-selector",

                                id_Apply    = "apply-changes-icon";

    public EventRepeatOption()
    {
        JSExecutor.injectJQuery();

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('.form-body .edit-header .header-text:contains(\"Repeat\")')") &
                 JSExecutor.isVisibleViaJQuery("$('.edit-info .timezone-text .title:contains(\"Never\")')") );
    }

    public void repeatEveryDay(int repeatDuration)
    {
        JSExecutor.clickViaJQuery("$('.edit-info .timezone-text .title:contains(\"Day\")')");
        JSExecutor.setTextForSelect(id_IntervalSelector, String.valueOf(repeatDuration));

        System.out.println("Was set: Repeat every " + repeatDuration + " day");
    }

    public void repeatEveryWeek(boolean custom, int repeatDuration, String[] days) throws InterruptedException
    {
        JSExecutor.clickViaJQuery("$('.edit-info .timezone-text .title:contains(\"Week\")')");

        JSExecutor.setTextForSelect(id_IntervalSelector, String.valueOf(repeatDuration));

        if( custom == true )
        {
            JSExecutor.clickViaJQuery("$('.repeat-subform__tabs span:contains(\"Cus\")')");
            System.out.println("Custom was clicked");

            for(int i = 0; i < days.length; i++)
            {
                JSExecutor.clickViaJQuery("$('.repeat-subform__select-circles__options span:contains(\"" + days[i] + "\")')");
                Thread.sleep(1000);
            }

            System.out.println("Was set: Repeat every " + repeatDuration + " week " + "on days: " + Arrays.toString(days));
        }
    }

    public void repeatEveryMonthOnDayOfMonth(int repeatDuration, int day)
    {
        JSExecutor.clickViaJQuery("$('.edit-info .timezone-text .title:contains(\"Month\")')");

        JSExecutor.clickViaJQuery("$('.repeat-subform__tabs span:contains(\"month\")')");

        JSExecutor.setTextForSelect(id_IntervalSelector, String.valueOf(repeatDuration));

        JSExecutor.setTextForSelect(id_DayOfMonth, String.valueOf(day));

        System.out.println("Was set: Repeat every " + repeatDuration + " month on " + day);
    }

    public void repeatEveryYearOnDate(int repeatDuration, int day, String month)
    {
        JSExecutor.clickViaJQuery("$('.edit-info .timezone-text .title:contains(\"Year\")')");

        JSExecutor.clickViaJQuery("$('.repeat-subform__tabs span:contains(\"date\")')");

        JSExecutor.setTextForSelect(id_IntervalSelector, String.valueOf(repeatDuration));

        JSExecutor.setTextForSelect(id_DayOfMonth, String.valueOf(day));

        JSExecutor.setTextForSelect(id_MonthSelector, month);

        System.out.println("Was set: Repeat every " + repeatDuration + " year on " + day + " " + month);
    }

    public void clickApply()
    {
        JSExecutor.clickByElement(id_Apply);
        System.out.println("Apply button was clicked");
    }
}
