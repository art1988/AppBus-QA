package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class DeleteJavaLib extends PageObject
{

    public DeleteJavaLib(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#serviceCatalogForm\\\\:confirmDialog_title').text()").equals("Delete Java libDelete Java lib") );
    }

    public void clickYes()
    {
        ((JavascriptExecutor) driver).executeScript("$('#serviceCatalogForm\\\\:confirmDialogYesButton').click()");

        System.out.println("DeleteJavaLib : Yes button was clicked");
    }
}
