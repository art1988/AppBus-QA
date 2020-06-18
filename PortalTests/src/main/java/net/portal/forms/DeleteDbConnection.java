package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class DeleteDbConnection extends PageObject
{

    public DeleteDbConnection(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#dbConnectionsForm\\\\:deleteDialog_title').text()").equals("Delete Db connectionDelete Db connection") );
    }

    public void clickYes()
    {
        ((JavascriptExecutor) driver).executeScript("$('#dbConnectionsForm\\\\:deleteYesButton').click()");
        System.out.println("DeleteDbConnection : Yes button was clicked");
    }
}
