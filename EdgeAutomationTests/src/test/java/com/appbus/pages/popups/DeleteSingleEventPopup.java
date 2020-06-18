package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class DeleteSingleEventPopup extends PageObject implements Deletable
{
    @FindBy(name = "Delete this event?")
    private MobileElement title;

    @FindBy(name = "Delete")
    private MobileElement delButton;

    @FindBy(name = "Cancel")
    private MobileElement cancelButton;


    public DeleteSingleEventPopup(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (title.isDisplayed() & delButton.isDisplayed());
    }

    @Override
    public void delete(boolean isSingle)
    {
        // isSingle always true
        delButton.click();
        System.out.println("Delete button was clicked");
    }

    @Override
    public void cancel()
    {
        cancelButton.click();
        System.out.println("Cancel was clicked");
    }
}
