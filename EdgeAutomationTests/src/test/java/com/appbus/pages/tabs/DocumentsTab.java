package com.appbus.pages.tabs;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class DocumentsTab extends PageObject
{
    @FindBy(name = "All documents")
    private MobileElement allDocumentsLabel;

    @FindBy(name = "Cloud")
    private MobileElement cloudButton;

    @FindBy(name = "Device")
    private MobileElement deviceButton;


    public DocumentsTab(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( allDocumentsLabel.isDisplayed() & cloudButton.isDisplayed() & deviceButton.isDisplayed() );
    }
}
