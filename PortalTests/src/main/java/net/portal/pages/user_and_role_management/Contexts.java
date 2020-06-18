package net.portal.pages.user_and_role_management;

import net.portal.forms.ContextDetail;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Contexts extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteButton;


    public Contexts(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Contexts") );
    }

    public ContextDetail addContext()
    {
        addNewButton.click();
        System.out.println("Contexts : Add New button was clicked");

        return new ContextDetail(driver);
    }

    public void selectContext(String contextName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + contextName + "\")').parent().prev().find('span')[0].click()");
        System.out.println("Context with name = " + contextName + " was selected...");
    }

    public FollowingItemsWillBeDeleted deleteContext()
    {
        deleteButton.click();
        System.out.println("Contexts : Delete button was clicked");

        return new FollowingItemsWillBeDeleted(driver);
    }
}
