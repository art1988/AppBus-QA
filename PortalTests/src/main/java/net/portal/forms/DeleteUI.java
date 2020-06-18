package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeleteUI extends PageObject
{

    @FindBy(xpath = "//div[@class='ui-dialog-content ui-widget-content'][contains(.,'Are you sure you want to delete?')]")
    private WebElement sureToDelNote;

    public DeleteUI(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#uiCatalogForm\\\\:appDeleteConfirm_title').text()").equals("Delete UI"));
    }

    public void clickYesButton() throws InterruptedException
    {
        sureToDelNote.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        System.out.println(driver.switchTo().activeElement().getText());
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        System.out.println("DeleteUI : Yes button was clicked");
    }
}
