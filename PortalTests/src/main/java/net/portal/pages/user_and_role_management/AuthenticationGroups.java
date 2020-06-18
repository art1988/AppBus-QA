package net.portal.pages.user_and_role_management;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.StratumGroupDetail;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class AuthenticationGroups extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteButton;


    public AuthenticationGroups(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Authentication Groups") );
    }

    public StratumGroupDetail addNewAuthenticationGroup()
    {
        addNewButton.click();
        System.out.println("AuthenticationGroups : Add New button was clicked");

        return new StratumGroupDetail(driver);
    }

    /**
     * Get list of Stratums by Group Name
     * @param groupName
     * @return
     */
    public String getListOfStratums(String groupName)
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + groupName + "\")').parent().next().text()"));
    }

    public void selectGroupName(String groupName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + groupName + "\")').parent().prev().find('span')[0].click()");
        System.out.println("Group with name = " + groupName + " was selected...");
    }

    public FollowingItemsWillBeDeleted deleteGroup()
    {
        deleteButton.click();
        System.out.println("AuthenticationGroups : Delete button was clicked");

        return new FollowingItemsWillBeDeleted(driver);
    }
}
