package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class DeleteDraftPopup extends PageObject
{
    @FindBy(name = "Delete selected drafts?")
    private MobileElement title;

    @FindBy(name = "OK")
    private MobileElement okButton;

    @FindBy(name = "Cancel")
    private MobileElement cancelButton;


    public DeleteDraftPopup(AppiumDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (title.isDisplayed() & okButton.isDisplayed());
    }

    public String getTitle()
    {
        return title.getText();
    }

    public void clickOk()
    {
        okButton.click();
        System.out.println("OK button was clicked");
    }
}
