package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class DeleteDocumentPopup extends PageObject
{
    @FindBy(name = "Are you sure you want to delete selected document?")
    private MobileElement title;

    @FindBy(name = "No")
    private MobileElement no;

    @FindBy(name = "Yes")
    private MobileElement yes;


    public DeleteDocumentPopup(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (title.isDisplayed() & yes.isDisplayed());
    }

    public void clickYes()
    {
        yes.click();

        System.out.println("Yes was clicked");
    }
}
