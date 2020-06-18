package com.appbus.pages.tabs;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class WatchlistTab extends PageObject
{
    @FindBy(name = "CIO WMR Recommendation")
    private MobileElement ciowmrLabel;

    @FindBy(name = "Add")
    private MobileElement addButton;

    public WatchlistTab(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ciowmrLabel.isDisplayed() & addButton.isDisplayed() );
    }
}
