package com.appbus.pages.menuItems;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class AttachmentSubmenu extends PageObject
{
    @FindBy(name = "AttachmentBackItem")
    private MobileElement backButton;

    @FindBy(name = "AttachmentSaveItem")
    private MobileElement downloadButton;

    @FindBy(name = "AttachmentFullScreenItem")
    private MobileElement fullscreenButton;


    public AttachmentSubmenu(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( backButton.isDisplayed() & downloadButton.isDisplayed() );
    }

    public void clickBack()
    {
        backButton.click();
        System.out.println("Back button was clicked");
    }

    public void clickDownload()
    {
        downloadButton.click();
        System.out.println("Download button was clicked");
    }

    public void clickFullscreen()
    {
        fullscreenButton.click();
        System.out.println("Fullscreen button was clicked");
    }
}
