package net.portal.pages.portal_administration;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RoleDetail;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Roles extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteButton;

    @FindBy(id = "filterForm:restoreFiltersButton")
    private WebElement resetFilterButton;

    @FindBy(id = "filterForm:applyFiltersButton")
    private WebElement applyFilterButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonReloadTop")
    private WebElement refreshButton;


    public Roles(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Portal administration > Roles") );
    }

    public RoleDetail addNewRole()
    {
        addNewButton.click();
        System.out.println("Roles : Add New button was clicked");

        return new RoleDetail(driver);
    }

    /**
     * Delete selected role. Need to select first.
     */
    public FollowingItemsWillBeDeleted deleteRole()
    {
        deleteButton.click();
        System.out.println("Roles : Delete button was clicked");

        return new FollowingItemsWillBeDeleted(driver);
    }

    public void clickDownload(String roleName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + roleName + "\")').parent().next().next().next().find(\"button\")[1].click()");
        System.out.println("Download button was clicked for role = " + roleName);
    }

    public RoleDetail editRole(String roleName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + roleName + "\")').parent().next().next().next().next().find(\"button\").click()");
        return new RoleDetail(driver);
    }

    public RoleDetail copyRole(String roleName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + roleName + "\")').parent().next().next().next().find(\"button\")[2].click()");
        System.out.println("Roles : copy button was clicked for role = " + roleName);

        return new RoleDetail(driver);
    }

    public void selectRole(String roleName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + roleName + "\")').parent().prev().find(\"span\").click()");
        System.out.println("Role : " + roleName + " was selected");
    }

    /**
     * Expand Permission filter dropdown and filter by roleToFilter
     * @param roleToFilter
     */
    public void filter(String roleToFilter)
    {
        ((JavascriptExecutor) driver).executeScript("$('#filterForm\\\\:filter_label').click()"); // expand dropdown

        ((JavascriptExecutor) driver).executeScript("$('#filterForm\\\\:filter_items li:contains(\"" + roleToFilter + "\")').click()");
    }

    /**
     * Click Apply button to filter result
     */
    public void clickApply()
    {
        applyFilterButton.click();
        System.out.println("Roles : Apply button was clicked");
    }

    /**
     * Reset filter result
     */
    public void clickReset()
    {
        resetFilterButton.click();
        System.out.println("Roles : Reset button was clicked");
    }

    public void clickRefresh()
    {
        refreshButton.click();
        System.out.println("Roles : refresh button was clicked");
    }
}
