package net.portal.pages.audit;

import net.portal.forms.AlertDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Alerts extends PageObject
{
    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonDeleteTop")
    private WebElement deleteButton;



    public Alerts(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Audit > Alerts") );
    }

    public AlertDetails addAlert()
    {
        addNewButton.click();
        System.out.println("Alerts : Add New button was clicked");

        return new AlertDetails(driver);
    }

    /**
     * Select Alert by name
     * @param actionName name of Alert to select
     */
    public void selectAlert(String actionName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + actionName + "\")').parent().prev().find(\"input\").click()");

        System.out.println(actionName + " was selected");
    }

    public FollowingItemsWillBeDeleted deleteAlert()
    {
        deleteButton.click();

        return new FollowingItemsWillBeDeleted(driver);
    }
}
