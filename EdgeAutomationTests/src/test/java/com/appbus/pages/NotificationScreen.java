package com.appbus.pages;

import com.appbus.pages.constants.Notifications;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.support.FindBy;

public class NotificationScreen extends PageObject
{
    @FindBy(name = "Today")
    private MobileElement todayButton;

    @FindBy(name = "All")
    private MobileElement allButton;


    public NotificationScreen(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( todayButton.isDisplayed() & allButton.isDisplayed() );
    }

    /**
     * Click by notification message inside Notification Screen
     */
    public void clickByNotificationMessage(Notifications notification)
    {
        MobileElement notifElement = (MobileElement) driver.findElement(By.name(notification.getNotificationText()));
        notifElement.click();

        System.out.println(notification.getNotificationText() + " notification message was clicked");
    }

}
