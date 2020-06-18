package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class DeleteJSlibrary extends PageObject
{

    public DeleteJSlibrary(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#serviceCatalogForm\\\\:confirmDialog_title').text()").equals("Delete JS libraryDelete JS library") );
    }

    public void clickYes()
    {
        ((JavascriptExecutor) driver).executeScript("$('#serviceCatalogForm\\\\:confirmDialogYesButton').click()");
        System.out.println("DeleteJSlibrary : Yes button was clicked");
    }
}
