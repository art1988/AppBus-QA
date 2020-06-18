package net.portal.pages.reporting;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class Visits extends PageObject
{
    public Visits(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Reporting > Visits") );
    }

    /**
     * Select Application by name
     * @param appName name of Application to select
     */
    public void selectApplication(String appName)
    {
        // expand Application dropdown
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:application span').click()");

        // select item
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:application_items li:contains(\"" + appName + "\")').click()");
    }

    public String getSelectedApplication()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:application label').text()"));
    }
}
