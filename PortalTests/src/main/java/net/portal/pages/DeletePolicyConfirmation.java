package net.portal.pages;

import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeletePolicyConfirmation extends PageObject
{
    @FindBy(id = "deleteWithAssignments:deletePolicyConfirmYesButton")
    private WebElement yesButton;

    @FindBy(id = "deleteWithAssignments:deletePolicyConfirmNoButton")
    private WebElement noButton;



    public DeletePolicyConfirmation(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#deleteWithAssignments\\\\:deleteWithAssignmentsDialog_title').text()").equals("Delete policy confirmation") );
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("DeletePolicyConfirmation : Yes button was clicked");
    }
}
