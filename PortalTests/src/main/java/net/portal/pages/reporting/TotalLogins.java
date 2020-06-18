package net.portal.pages.reporting;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class TotalLogins extends PageObject
{
    public TotalLogins(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Reporting > Total Logins") );
    }

    public void clickCSVIcon()
    {
        ((JavascriptExecutor) driver).executeScript("$('#printForm\\\\:csvPrintButton').click()");

        System.out.println("CSV icon was clicked...");
    }
}
