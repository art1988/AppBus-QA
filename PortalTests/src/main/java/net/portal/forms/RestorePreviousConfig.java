package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class RestorePreviousConfig extends PageObject
{
    @FindBy(id = "confirmDialogYesButton")
    private WebElement yesButton;

    @FindBy(id = "confirmDialogNoButton")
    private WebElement noButton;



    public RestorePreviousConfig(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#revertConfirmDialog_title').text()").equals("Restore previous config") );
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("RestorePreviousConfig : Yes button was clicked");
    }
}
