package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class DeleteContactPopup extends PageObject
{
    @FindBy(name = "Delete")
    private MobileElement delete;

    @FindBy(name = "Cancel")
    private MobileElement cancel;

    @FindBy(name = "Delete contact?")
    private MobileElement title;


    public DeleteContactPopup(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( title.isDisplayed() & delete.isDisplayed() & cancel.isDisplayed() );
    }

    public void confirmDelete()
    {
        delete.click();
        System.out.println("Delete contact button was clicked");
    }
}
