package com.appbus.pages.menuItems;

import com.appbus.pages.PageObject;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.tabs.SharePointTab;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

/**
 *  List of menu items of Documents section
 */
public class DocumentsMenuItems extends PageObject
{

    @FindBy(name = "SharePoint")
    private MobileElement sharePoint;

    @FindBy(name = "Sharedrive")
    private MobileElement shareDrive;

    @FindBy(name = "Documents")
    private MobileElement documents;


    public DocumentsMenuItems(AppiumDriver driver)
    {
        super(driver);

        Scroller.scrollLeft("SharePoint");

        Assert.assertTrue(isInit());
    }

    // We see initial menu elements
    private boolean isInit()
    {
        try
        {
            Thread.sleep(5_000);
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        return ( sharePoint.isDisplayed() & shareDrive.isDisplayed() );
    }

    public SharePointTab clickSharePoint()
    {
        sharePoint.click();
        System.out.println("SharePoint tab was clicked");

        return new SharePointTab(driver);
    }
}
