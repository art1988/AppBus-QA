package com.appbus.pages;

import com.appbus.pages.tabs.SharePointTab;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class AttachScreen extends PageObject
{
    @FindBy(name = "SharePoint")
    private MobileElement sharePoint;

    @FindBy(name = "Sharedrive")
    private MobileElement shareDrive;

    @FindBy(name = "Documents")
    private MobileElement documents;


    public AttachScreen(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( sharePoint.isDisplayed() & shareDrive.isDisplayed() );
    }


    public SharePointTab clickSharePoint()
    {
        sharePoint.click();
        System.out.println("SharePoint was clicked");

        return new SharePointTab(driver);
    }
}
