package com.appbus.pages.tabs;

import com.appbus.pages.PageObject;
import com.appbus.pages.constants.CalendarOption;
import com.appbus.pages.constants.Context;
import com.appbus.pages.event_related.AllEventsSideBar;
import com.appbus.pages.event_related.NewEvent;
import com.appbus.pages.helpers.JSExecutor;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.support.FindBy;
import tests.source.FunctionalTest;

import java.text.SimpleDateFormat;
import java.time.YearMonth;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class CalendarTab extends PageObject
{
    @FindBy(name = "Day")
    private MobileElement day;

    @FindBy(name = "Week")
    private MobileElement week;

    @FindBy(name = "Month")
    private MobileElement month;

    @FindBy(name = "Year")
    private MobileElement year;

    @FindBy(name = "Today")
    private MobileElement today;

    @FindBy(name = "]")
    private MobileElement arrowLeft;

    @FindBy(name = "%")
    private MobileElement arrowRight;

    @FindBy(name = "All events")
    private MobileElement allEvents;

    /**
     * Non-native elements
     */
    private static final String id_AddNewEvent   = "calendar-add-button",
                                id_RefreshButton = "calendar-header-spinner";

    // Date interval
    private MobileElement dateStart;
    private MobileElement dateEnd;
    private MobileElement dateYear;
    private MobileElement dayOfWeek;
    private MobileElement dateMonth;

    // Day of week labels of month mode (pick random 3)
    private MobileElement sunLabel, wedLabel, satLabel;

    // Month names of year mode (pick random 3)
    private MobileElement janLabel, junLabel, decLabel;

    private CalendarOption curOption;


    public CalendarTab(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }


    private boolean isInit()
    {
        return (day.isDisplayed() & year.isDisplayed() & today.isDisplayed());
    }

    public void clickDay()
    {
        day.click();
        System.out.println("Day was clicked");
        curOption = CalendarOption.DAY;
    }

    public void clickWeek()
    {
        week.click();
        System.out.println("Week was clicked");
        curOption = CalendarOption.WEEK;
    }

    public void clickMonth()
    {
        month.click();
        System.out.println("Month was clicked");
        curOption = CalendarOption.MONTH;
    }

    public void clickYear()
    {
        year.click();
        System.out.println("Year was clicked");
        curOption = CalendarOption.YEAR;
    }

    public void clickToday()
    {
        today.click();
        System.out.println("Today was clicked");
        curOption = CalendarOption.DAY;
    }

    // Init date interval in header and related elements of selected calendar option
    public void initDateHeader(int day, String month, int year, String dOfWeek)
    {
        switch (curOption)
        {
            case DAY:
                dateStart = (MobileElement) driver.findElement(By.name(day + " " + month));
                dateYear  = (MobileElement) driver.findElement(By.name(String.valueOf(year)));
                dayOfWeek = (MobileElement) driver.findElement(By.name(dOfWeek));
                break;

            case WEEK:
                // Get calendar, clear it and set week number and year
                Calendar calendar = new GregorianCalendar();
                calendar.clear();

                // Get week number
                SimpleDateFormat simpleDateformat = new SimpleDateFormat("w");
                int week = Integer.parseInt(simpleDateformat.format(new Date()));

                calendar.setFirstDayOfWeek(Calendar.SUNDAY);
                calendar.set(Calendar.WEEK_OF_YEAR, week);
                calendar.set(Calendar.YEAR, year);

                // Now get the first day of week
                Date date = calendar.getTime();

                simpleDateformat = new SimpleDateFormat("d");
                int firstDayOfWeek = Integer.parseInt(simpleDateformat.format(date));

                // Check that day is from next month, for ex: 29 Apr - 5 May or 29 Jul - 4 Aug
                if( (firstDayOfWeek + 6) >= Calendar.getInstance().getActualMaximum(Calendar.DAY_OF_MONTH) )
                {
                    YearMonth yearMonth = YearMonth.now();

                    Date lastDateOfWeek;

                    String nextMonth = yearMonth.plusMonths(1).getMonth().toString(),
                           prevMonth = yearMonth.minusMonths(1).getMonth().toString();

                    // The current day is from current month
                    if( day <  firstDayOfWeek )
                    {
                        lastDateOfWeek = lastDayOfLastWeek(year, yearMonth.getMonthValue() - 1);
                        nextMonth = yearMonth.getMonth().toString();
                    }
                    else
                    {
                        lastDateOfWeek = lastDayOfLastWeek(year, yearMonth.getMonthValue());
                        prevMonth = yearMonth.getMonth().toString();
                    }

                    int lastDayOfNextWeek = Integer.parseInt(simpleDateformat.format(lastDateOfWeek));

                    nextMonth = nextMonth.substring(0, 1).toUpperCase() + nextMonth.substring(1).toLowerCase();
                    nextMonth = nextMonth.substring(0, 3);

                    prevMonth = prevMonth.substring(0, 1).toUpperCase() + prevMonth.substring(1).toLowerCase();
                    prevMonth = prevMonth.substring(0, 3);

                    dateStart = (MobileElement) driver.findElement(By.name(firstDayOfWeek + " " + prevMonth));
                    dateEnd   = (MobileElement) driver.findElement(By.name(lastDayOfNextWeek + " " + nextMonth));
                    dateYear  = (MobileElement) driver.findElement(By.name(String.valueOf(year)));
                    break;
                }
                else // we are on the same month
                {
                    dateStart = (MobileElement) driver.findElement(By.name(firstDayOfWeek + " " + month));
                    dateEnd   = (MobileElement) driver.findElement(By.name((firstDayOfWeek + 6) + " " + month));
                    dateYear  = (MobileElement) driver.findElement(By.name(String.valueOf(year)));
                    break;
                }

            case MONTH:
                dateMonth = (MobileElement) driver.findElement(By.name(month));
                dateYear  = (MobileElement) driver.findElement(By.name(String.valueOf(year)));
                initDaysOfWeek();
                break;

            case YEAR:
                dateYear  = (MobileElement) driver.findElement(By.name(String.valueOf(year)));
                initMonths();
                break;
        }

        System.out.println("Date interval was initialized");
    }

    // Init 3 days of week for month option
    private void initDaysOfWeek()
    {
        sunLabel = (MobileElement) driver.findElement(By.name("Sun"));
        wedLabel = (MobileElement) driver.findElement(By.name("Wed"));
        satLabel = (MobileElement) driver.findElement(By.name("Sat"));
    }

    private void initMonths()
    {
        janLabel = (MobileElement) driver.findElement(By.name("JAN"));
        junLabel = (MobileElement) driver.findElement(By.name("JUN"));
        decLabel = (MobileElement) driver.findElement(By.name("DEC"));
    }

    public String getStartDate()
    {
        return dateStart.getText();
    }

    public String getEndDate()
    {
        return dateEnd.getText();
    }

    public String getYear()
    {
        return dateYear.getText();
    }

    public String getDayOfWeek()
    {
        return dayOfWeek.getText();
    }

    /**
     * Switch one day/week/month/year backward ( -1 )
     */
    public void clickArrowLeft()
    {
        arrowLeft.click();
        System.out.println("Arrow left was clicked");
    }

    /**
     * Switch one day/week/month/year forward ( +1 )
     */
    public void clickArrowRight()
    {
        arrowRight.click();
        System.out.println("Arrow right was clicked");
    }

    public AllEventsSideBar clickAllEvents()
    {
        allEvents.click();
        System.out.println("All events was clicked");

        FunctionalTest.switchContext(Context.WEBVIEW);

        return new AllEventsSideBar();
    }

    public NewEvent clickNewEvenButton()
    {
        JSExecutor.clickByElement(id_AddNewEvent);
        System.out.println("Add new event button was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return new NewEvent(driver);
    }

    public void clickRefreshButton()
    {
        JSExecutor.clickByElement(id_RefreshButton);
        System.out.println("Refresh button was clicked");
    }

    /**
     * Trying to find event in Calendar grid (Day, Week, Month) by event name
     * @param eventName Name of event
     * @return found event or null (in case if event was not found)
     */
    public static MobileElement findEventByName(String eventName)
    {
        MobileElement foundElement = null;

        try
        {
            foundElement = (MobileElement) FunctionalTest.getDriver().findElement(By.name(eventName));
        }
        catch (org.openqa.selenium.NoSuchElementException ex)
        {
            System.err.println("Event with name: " + eventName + " was not found !");
        }

        return foundElement; // null in case if event was not found
    }

    /** month is 1 through 12 for Jan through Dec */
    private static Date lastDayOfLastWeek(int year, int month)
    {
        final int LAST_DAY_OF_WEEK = Calendar.SATURDAY;

        Calendar cal = Calendar.getInstance();

        cal.set(year, month - 1, 1); // Calendar’s month is 0-based, so subtract 1
        cal.set(Calendar.DAY_OF_MONTH, cal.getActualMaximum(Calendar.DAY_OF_MONTH)); // set to last day of month

        // is this also the last day of the week?
        int dayOfWeek = cal.get(Calendar.DAY_OF_WEEK);
        if (dayOfWeek != LAST_DAY_OF_WEEK)
        {
            cal.add(Calendar.DAY_OF_WEEK, LAST_DAY_OF_WEEK - dayOfWeek);

            return cal.getTime();
        }

        return cal.getTime();
    }

}
