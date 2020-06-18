package com.appbus.pages.helpers;

import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import io.appium.java_client.touch.offset.PointOption;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriverException;
import tests.source.FunctionalTest;

public class Scroller
{
    // Scroll tabs to the right
    private static void scrollOneTabRight()
    {
        (new TouchAction(FunctionalTest.getDriver()))
                .press(PointOption.point(271, 20))
                .moveTo(PointOption.point(-153, 0))
                .release()
                .perform();
    }

    // Scroll tabs to the left
    private static void scrollOneTabLeft()
    {
        (new TouchAction(FunctionalTest.getDriver()))
                .press(PointOption.point(146, 41))
                .moveTo(PointOption.point(383, 3))
                .release()
                .perform();
    }

    /**
     * Smart scroll to the right to element by name
     * @param elementByName
     */
    public static void scrollRight(String elementByName)
    {
        MobileElement element = null;

        try
        {
            element = (MobileElement) FunctionalTest.getDriver().findElement(By.name(elementByName));
            scrollOneTabRight();
        }
        catch ( WebDriverException ex )
        {
            System.out.println(elementByName + " not found. Keep scrolling...");
        }

        if(element != null && element.isDisplayed() == true)
        {
            return;
        }

        scrollOneTabRight();
        scrollRight(elementByName); // do it again
    }

    /**
     * Smart scroll to the left to element by name
     * @param elementByName
     */
    public static void scrollLeft(String elementByName)
    {
        MobileElement element = null;

        try
        {
            element = (MobileElement) FunctionalTest.getDriver().findElement(By.name(elementByName));
            scrollOneTabLeft();
        }
        catch ( WebDriverException ex )
        {
            System.out.println(elementByName + " not found. Keep scrolling...");
        }

        if(element != null && element.isDisplayed() == true)
        {
            return;
        }

        scrollOneTabLeft();
        scrollLeft(elementByName); // do it again
    }

    /**
     * Scroll one screen to the up
     */
    public static void scrollUp()
    {
        (new TouchAction(FunctionalTest.getDriver()))
                .press(PointOption.point(419, 352))
                .moveTo(PointOption.point(-1, 317))
                .release()
                .perform();
    }

    /**
     * Pull down to show search field in Attach popup
     */
    public static void pullDownToShowSearchFiled()
    {
        (new TouchAction(FunctionalTest.getDriver()))
                .press(PointOption.point(551, 465))
                .moveTo(PointOption.point(0, 116))
                .release()
                .perform();
    }

    /**
     * Scroll down one screen of All Events
     */
    public static void scrollDownOneScreenOfAllEvents()
    {
        (new TouchAction(FunctionalTest.getDriver()))
                .press(PointOption.point(644, 983))
                .moveTo(PointOption.point(6, -763))
                .release()
                .perform();
    }
}
