package net.portal.pages;

import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeleteItemLogPopup extends PageObject
{
    @FindBy(id = "tabs:logForm:yesButton")
    private WebElement yesButton;



    public DeleteItemLogPopup(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#tabs\\\\:logForm\\\\:deleteConfirm_title').text()").equals("Delete Item") );
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("DeleteItemLogPopup : Yes button was clicked");
    }
}
