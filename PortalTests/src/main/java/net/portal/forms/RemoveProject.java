package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class RemoveProject extends PageObject
{
    @FindBy(id = "serviceCatalogForm:removeProjectConfirmYesButton")
    private WebElement yesButton;


    public RemoveProject(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#serviceCatalogForm\\\\:removeProjectConfirm_title').text()").equals("Remove project") );
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("RemoveProject : Yes button was clicked");
    }
}
