package net.portal.pages.reporting;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class HitsPerPage extends PageObject
{
    @FindBy(id = "barchartform:searchApplyButton")
    private WebElement applyButton;



    public HitsPerPage(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Reporting > Hits Per Page") );
    }

    public void clickCSVIcon()
    {
        ((JavascriptExecutor) driver).executeScript("$('#barchartform\\\\:csvButton').click()");

        System.out.println("CSV icon was clicked...");
    }
}
