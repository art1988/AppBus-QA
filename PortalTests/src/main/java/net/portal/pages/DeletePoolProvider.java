package net.portal.pages;

import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class DeletePoolProvider extends PageObject
{

    public DeletePoolProvider(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#poolProviders\\\\:deletePoolProviderDlg_title').text()").equals("Delete pool providerDelete pool provider") );
    }

    public void clickYes()
    {
        ((JavascriptExecutor) driver).executeScript("$('#poolProviders\\\\:yesButton').click()");

        System.out.println("DeletePoolProvider : Yes button was clicked");
    }
}
