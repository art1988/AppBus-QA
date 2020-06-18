package net.portal.pages.server_configuration;

import net.portal.forms.EnvironmentDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Environments extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonDeleteTop")
    private WebElement deleteButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonReloadTop")
    private WebElement refreshButton;

    @FindBy(id = "table:tableForm:entityTable:environmentNameColumn:filter")  //was table:tableForm:entityTable:j_idt50:filter
    private WebElement environmentNameSearchField;


    public Environments(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Server Configuration > Environments") );
    }

    public EnvironmentDetails addEnvironment()
    {
        addNewButton.click();
        System.out.println("Environments : Add New button was clicked");

        return new EnvironmentDetails(driver);
    }

    public FollowingItemsWillBeDeleted deleteEnvironment()
    {
        deleteButton.click();
        System.out.println("Environments : Delete button was clicked");

        return new FollowingItemsWillBeDeleted(driver);
    }

    public void clickRefresh()
    {
        refreshButton.click();
        System.out.println("Environments : Refresh button was clicked");
    }

    public void searchForEnvironment(String envName)
    {
        environmentNameSearchField.sendKeys(envName);
    }

    /**
     * Click by checkbox near with Environment Name = envName
     * @param envName
     */
    public void selectEnvironment(String envName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + envName + "\")').parent().prev().find(\"input\").click()");
    }
}
