package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class MoveToRoot extends PageObject
{
    @FindBy(id = "moveRoorForm:yesMoveRoot")
    private WebElement yesButton;



    public MoveToRoot(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#moveItemToRootConfirm_title').text()").equals("Move to root"));
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("MoveToRoot : Yes button was clicked");
    }
}
