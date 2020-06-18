package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DownloadServiceClientLibrary extends PageObject
{
    @FindBy(id = "serviceDashboard:downloadClientLibDlgForm:downloadLink")
    private WebElement downloadButton;



    public DownloadServiceClientLibrary(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#serviceDashboard\\\\:downloadClientLibDlg_title').text()").equals("Download service client library"));
    }

}
