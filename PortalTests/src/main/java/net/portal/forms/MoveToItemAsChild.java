package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;


public class MoveToItemAsChild  extends PageObject
{
    @FindBy(id = "moveItemForm:yesMoveItem")
    private WebElement yesButton;

    @FindBy(xpath = "//span[contains(.,'Move to item as child')]")
    private WebElement winTitle;

    public MoveToItemAsChild(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#moveItemAssignmentConfirm_title').text()").equals("Move to item as child"));
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("MoveToItemAsChild : Ok button was clicked");
    }

    public void clickYesByTab() throws InterruptedException
    {
        Thread.sleep(1_000);
        winTitle.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        System.out.println("MoveToItemAsChild : Ok button was selected by TABs and clicked");
    }
}
