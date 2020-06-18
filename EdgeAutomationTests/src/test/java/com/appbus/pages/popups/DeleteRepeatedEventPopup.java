package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class DeleteRepeatedEventPopup extends PageObject implements Deletable
{
    @FindBy(name = "Delete single appointment or the whole sequence?")
    private MobileElement title;

    @FindBy(name = "Single")
    private MobileElement single;

    @FindBy(name = "Sequence")
    private MobileElement sequence;

    @FindBy(name = "Cancel")
    private MobileElement cancel;


    public DeleteRepeatedEventPopup(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( title.isDisplayed() & sequence.isDisplayed() & cancel.isDisplayed() );
    }

    @Override
    public void delete(boolean isSingle)
    {
        if( isSingle == true )
        {
            single.click();
            System.out.println("Single was clicked");
        }
        else
        {
            sequence.click();
            System.out.println("Sequence was clicked");
        }
    }

    @Override
    public void cancel()
    {
        cancel.click();
        System.out.println("Cancel was clicked");
    }
}
