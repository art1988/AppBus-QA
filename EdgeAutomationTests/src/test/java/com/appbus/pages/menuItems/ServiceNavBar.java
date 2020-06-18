package com.appbus.pages.menuItems;

import com.appbus.pages.*;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

/**
 *  4 constant buttons on top of the menu
 */
public class ServiceNavBar extends PageObject
{
    @FindBy(name = "BT GlobalNav Default@2x")
    private MobileElement hamburgerMenuButton;

    @FindBy(name = "ServiceNav Notif Default@2x")
    private MobileElement notificationButton;

    @FindBy(name = "ServiceNav Action Default@2x")
    private MobileElement actionButton;

    @FindBy(name = "ServiceNav Search Default@2x")
    private MobileElement searchButton;


    public ServiceNavBar(AppiumDriver driver)
    {
        super(driver);

        try
        {
            Thread.sleep(5_000);
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        Assert.assertTrue(isInit());
    }

    // We see those buttons
    private boolean isInit()
    {
        return (hamburgerMenuButton.isDisplayed() & notificationButton.isDisplayed() &
                actionButton.isDisplayed() & searchButton.isDisplayed());
    }

    public ActiveHamburgerMenu clickHamburgerMenu()
    {
        hamburgerMenuButton.click();
        System.out.println("Hamburger menu button was clicked");

        return new ActiveHamburgerMenu(driver);
    }

    public NotificationScreen clickNotification()
    {
        notificationButton.click();
        System.out.println("Notification button was clicked");

        return new NotificationScreen(driver);
    }

    /**
     * Contains 3 options: reload, home and print
     */
    public ActionScreen clickAction()
    {
        actionButton.click();
        System.out.println("Action button was clicked");

        return new ActionScreen(driver);
    }

    public SearchScreen clickSearch()
    {
        searchButton.click();
        System.out.println("Search menu button was clicked");

        return new SearchScreen(driver);
    }

}
