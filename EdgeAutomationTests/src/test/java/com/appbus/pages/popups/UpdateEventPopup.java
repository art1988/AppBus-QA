package com.appbus.pages.popups;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class UpdateEventPopup extends PageObject
{
    @FindBy(name = "Update single appointment or the whole sequence?")
    private MobileElement title;

    @FindBy(name = "Single")
    private MobileElement single;

    @FindBy(name = "Sequence")
    private MobileElement sequence;

    @FindBy(name = "Cancel")
    private MobileElement cancel;


    public UpdateEventPopup(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( title.isDisplayed() & sequence.isDisplayed() & cancel.isDisplayed() );
    }

    public void clickSingle()
    {
        single.click();
        System.out.println("Single was clicked");
    }

    /**
     * Depends of what was edited. If title was edited - no need to show EditAnywayPopup
     * @param editAnyway marker that indicates to show EditAnywayPopup
     * @return EditAnywayPopup if editAnyway == true, null otherwise
     */
    public EditAnywayPopup clickSequence(boolean editAnyway)
    {
        sequence.click();
        System.out.println("Sequence was clicked");

        return ( editAnyway == true ) ? new EditAnywayPopup(driver) : null;
    }
}
