package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class EditAnywayPopup extends PageObject
{

    @FindBy(name = "If you have changed certain events in the sequence, these events will be canceled " +
            "and the corresponding events will again correspond to the sequence; deleted events of the " +
            "sequence will be restored as well")
    private MobileElement title;

    @FindBy(name = "Edit anyway")
    private MobileElement editAnywayButton;

    @FindBy(name = "Cancel")
    private MobileElement cancelButton;


    public EditAnywayPopup(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( title.isDisplayed() & editAnywayButton.isDisplayed() );
    }

    public void clickEditAnyway()
    {
        editAnywayButton.click();

        System.out.println("Edit anyway button was clicked");
    }
}
