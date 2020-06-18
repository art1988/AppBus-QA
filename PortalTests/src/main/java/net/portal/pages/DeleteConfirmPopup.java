package net.portal.pages;

import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeleteConfirmPopup extends PageObject
{
    @FindBy(id = "deleteConfirmForm:deleteConfirmYesButton")
    private WebElement yesButton;


    public DeleteConfirmPopup(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        //Sure to delete?
        return ( ((JavascriptExecutor) driver).executeScript("return $('#deleteConfirm .ui-confirm-dialog-message').text()").equals("Are you sure you want to delete?") );
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("DeleteConfirmPopup : Yes button was clicked");
    }
}
