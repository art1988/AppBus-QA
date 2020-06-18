package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class SaveDraftPopup extends PageObject
{

    @FindBy(name = "Delete Draft")
    private MobileElement title;

    @FindBy(name = "Save")
    private MobileElement saveButton;

    @FindBy(name = "Cancel")
    private MobileElement cancelButton;


    public SaveDraftPopup(AppiumDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (title.isDisplayed() & saveButton.isDisplayed());
    }

    public String getTitle()
    {
        return title.getText();
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("Save button was clicked");
    }
}
