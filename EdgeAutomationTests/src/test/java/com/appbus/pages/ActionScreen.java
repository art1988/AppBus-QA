package com.appbus.pages;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class ActionScreen extends PageObject
{
    @FindBy(name = "Reload")
    private MobileElement reload;

    @FindBy(name = "Home")
    private MobileElement home;

    @FindBy(name = "Print")
    private MobileElement print;


    public ActionScreen(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue( isInit() );
    }

    private boolean isInit()
    {
        return ( reload.isDisplayed() & home.isDisplayed() & print.isDisplayed() );
    }

    public void clickHome()
    {
        home.click();
        System.out.println("Home button was clicked");
    }
}
