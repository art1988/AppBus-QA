package net.portal.pages.user_and_role_management;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.UserGroupDetails;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class UserGroups extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewUserGroupButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteUserGroupButton;


    public UserGroups(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Portal administration > User groups") );
    }

    public UserGroupDetails addNewUserGroup()
    {
        addNewUserGroupButton.click();
        System.out.println("Add New User Group was clicked");

        return new UserGroupDetails(driver);
    }

    // Before deletion, select user group first
    public FollowingItemsWillBeDeleted deleteUserGroup() throws InterruptedException
    {
        deleteUserGroupButton.click();
        System.out.println("Delete User Group was clicked");

        Thread.sleep(2_000);

        return new FollowingItemsWillBeDeleted(driver);
    }

    public void clickDownload(String userGroupName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + userGroupName + "\")').parent().next().next().next().children().eq(1).click()");
        System.out.println("Download button was clicked");
    }

    public void selectUserGroup(String userGroupName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + userGroupName + "\")').parent().prev().find('span')[0].click()");
        System.out.println("User group with name = " + userGroupName + " was selected...");
    }

    public UserGroupDetails editUserGroup(String userGroupName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + userGroupName + "\")').parent().next().next().next().next().find(\"button\").click()");

        return new UserGroupDetails(driver);
    }
}
