package net.portal.pages.audit;

import net.portal.forms.LogLast200Lines;
import net.portal.pages.DeleteItemLogPopup;
import net.portal.pages.DeleteItemPopup;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class DeviceLog extends PageObject
{
    public DeviceLog(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Audit > Device Log") );
    }

    public void clickFullLogTab()
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-tabs-nav li')[0].click()");

        System.out.println("Full Log tab was clicked...");
    }

    /**
     * Select folder on Full Log tab
     */
    public void selectFolder(String folderName)
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#tabs\\\\:deviceLog\\\\:selectedFolder_label').click()");

        // Choose folder
        ((JavascriptExecutor) driver).executeScript("$('#tabs\\\\:deviceLog\\\\:selectedFolder_items li:contains(\"" + folderName + "\")').click()");

        System.out.println(folderName + " was selected");
    }

    /**
     * Click Decode button
     * @param fileName
     */
    public void decode(String fileName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#tabs\\\\:logForm\\\\:deviceLogTable_data tr td:contains(\"" + fileName + "\")').next().next().next().next().next().find(\"button\")[0].click()");

        System.out.println("Decode button was clicked for " + fileName);
    }

    public LogLast200Lines viewLast200Lines(String fileName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#tabs\\\\:logForm\\\\:deviceLogTable_data tr td:contains(\"" + fileName + "\")').next().next().next().next().next().find(\"button\")[0].click()");

        return new LogLast200Lines(driver);
    }

    public DeleteItemLogPopup deleteLog(String fileName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#tabs\\\\:logForm\\\\:deviceLogTable_data tr span:contains(\"" + fileName + "\")').parent().next().next().next().next().next().find(\"button\")[2].click()");

        return new DeleteItemLogPopup(driver);
    }


    public void clickCrashTab()
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-tabs-nav li')[1].click()");

        System.out.println("Crash tab was clicked...");
    }
}
