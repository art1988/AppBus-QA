package com.appbus.pages.email_related;

import com.appbus.pages.PageObject;
import com.appbus.pages.helpers.JSExecutor;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class AddContactOption extends PageObject
{
    @FindBy(name = "Add Contact")
    private MobileElement addContactLabel;

    /**
    * Non native elements
    */
    private static final String class_SearchFiled = "filter-contacts-input";


    public AddContactOption(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return addContactLabel.isDisplayed();
    }

    public void searchFor(String contact)
    {
        JSExecutor.setTextForFieldByClassName(class_SearchFiled, contact);
    }
}
