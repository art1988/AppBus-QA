package net.portal.pages.reporting;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class UserDevicesOld extends PageObject
{
    public UserDevicesOld(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Device management > User Devices") );
    }

    public void clickFindDevicesTab()
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-tabs-nav li')[0].click()");

        System.out.println("Find Devices tab was clicked...");
    }

    public void clickReviewWipeListTab()
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-tabs-nav li')[1].click()");

        System.out.println("Review Wipe-List tab was clicked...");
    }

    public void clickOSVersionsTab()
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-tabs-nav li')[2].click()");

        System.out.println("OS Versions tab was clicked...");
    }

    public void selectOSType(String osType)
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:tabs\\\\:console label').click()");

        // select
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:tabs\\\\:console_items li:contains(\"" + osType + "\")').click()");
    }
}
