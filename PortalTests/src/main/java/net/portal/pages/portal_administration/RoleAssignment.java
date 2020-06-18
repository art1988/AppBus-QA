package net.portal.pages.portal_administration;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RoleAssignmentDetail;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class RoleAssignment extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonDeleteTop")
    private WebElement deleteButton;


    public RoleAssignment(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Portal administration > Role Assignment") );
    }

    public RoleAssignmentDetail addNewRoleAssignment()
    {
        addNewButton.click();
        System.out.println("RoleAssignment : Add New button was clicked");

        return new RoleAssignmentDetail(driver);
    }

    public FollowingItemsWillBeDeleted deleteRoleAssignment()
    {
        deleteButton.click();
        System.out.println("RoleAssignment : Delete button was clicked");

        return new FollowingItemsWillBeDeleted(driver);
    }

    /**
     * Select Role Assignment item by roleName
     * @param roleName Role Name to select
     */
    public void selectRoleAssignment(String roleName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data td:contains(\"" + roleName + "\")').prev().find(\"input\").click()");
        System.out.println("Role Assignment : " + roleName + " was selected");
    }
}
