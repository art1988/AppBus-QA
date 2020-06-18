package net.portal.pages;

import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeleteItemPopup extends PageObject
{
    @FindBy(id = "yesButton")
    private WebElement yesButton;


    public DeleteItemPopup(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#deleteItemConfirm_title').text()").equals("Delete Item") );
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("DeleteItemPopup : Yes button was clicked");
    }
}
