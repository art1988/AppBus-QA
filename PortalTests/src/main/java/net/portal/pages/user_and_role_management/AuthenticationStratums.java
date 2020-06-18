package net.portal.pages.user_and_role_management;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.StratumDetail;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class AuthenticationStratums extends PageObject
{
    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonDeleteTop")
    private WebElement deleteButton;


    public AuthenticationStratums(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Authentication Stratums") );
    }

    public StratumDetail addNewStratum()
    {
        addNewButton.click();
        System.out.println("Authentication Stratums : Add New button was clicked");

        return new StratumDetail(driver);
    }

    public void selectStratum(String stratumName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + stratumName + "\")').parent().prev().find('span')[0].click()");
        System.out.println("Stratum with name = " + stratumName + " was selected...");
    }

    public FollowingItemsWillBeDeleted deleteStratum()
    {
        deleteButton.click();
        System.out.println("Authentication Stratums : Delete button was clicked");

        return new FollowingItemsWillBeDeleted(driver);
    }
}
