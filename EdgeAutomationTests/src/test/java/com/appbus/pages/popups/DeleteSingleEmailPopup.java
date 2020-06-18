package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class DeleteSingleEmailPopup extends PageObject
{
    @FindBy(name = "Delete this message?")
    private MobileElement title;

    @FindBy(name = "OK")
    private MobileElement okButton;

    @FindBy(name = "Cancel")
    private MobileElement cancelButton;


    public DeleteSingleEmailPopup(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( title.isDisplayed() & okButton.isDisplayed() & cancelButton.isDisplayed() );
    }

    public void clickOk()
    {
        okButton.click();
        System.out.println("OK button was clicked");
    }
}
