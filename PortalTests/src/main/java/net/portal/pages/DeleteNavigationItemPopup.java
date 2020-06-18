package net.portal.pages;

import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeleteNavigationItemPopup extends PageObject
{
    @FindBy(id = "deleteItemForm:yesButton")
    private WebElement yesButton;



    public DeleteNavigationItemPopup(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#deleteItemConfirm_title').text()").equals("Delete item") );
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("DeleteNavigationItemPopup : Yes button was clicked");
    }
}
