package net.portal.pages;

import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeleteJob extends PageObject
{
    @FindBy(id = "deleteForm:yesButton")
    private WebElement yesButton;



    public DeleteJob(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#deleteForm\\\\:deleteFormTitle_title').text()").equals("Delete job") );
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("DeleteJob : Yes button was clicked");
    }
}
