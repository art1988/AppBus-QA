package net.portal.pages.audit;

import net.portal.forms.EmailGroupsDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class EmailGroups extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteButton;


    public EmailGroups(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Audit > Email Groups") );
    }

    public EmailGroupsDetails addEmailGroup()
    {
        addNewButton.click();
        System.out.println("EmailGroups : Add New button was clicked...");

        return new EmailGroupsDetails(driver);
    }

    public FollowingItemsWillBeDeleted deleteEmailGroup()
    {
        deleteButton.click();
        System.out.println("EmailGroups : Delete button was clicked...");

        return new FollowingItemsWillBeDeleted(driver);
    }

    /**
     * Edit Email Group by name
     * @param nameToEdit name of Email Group to edit
     * @param newName new Name to set
     * @param newContent new Content to set
     * @param newDescription new Description to set
     */
    public void editEmailGroup(String nameToEdit, String newName, String newContent, String newDescription) throws InterruptedException
    {
        // Click Edit icon
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data tr td span:contains(\"" + nameToEdit + "\")').parent().next().next().next().next().find(\"button\").click()");
        System.out.println("Edit icon was clicked for EmailGroup = " + nameToEdit);
        Thread.sleep(1_000);

        // Set new Name
        ((JavascriptExecutor) driver).executeScript("$(\"#table\\\\:tableForm\\\\:entityTable_data tr td input[value*='" + nameToEdit + "']\").val(\"" + newName + "\")");
        Thread.sleep(500);

        // Set new Content
        ((JavascriptExecutor) driver).executeScript("$(\"#table\\\\:tableForm\\\\:entityTable_data tr td input[value*='" + nameToEdit + "']\").parent().next().find(\"textarea\").val(\"" + newContent + "\")");
        Thread.sleep(500);

        // Set new Description
        ((JavascriptExecutor) driver).executeScript("$(\"#table\\\\:tableForm\\\\:entityTable_data tr td input[value*='" + nameToEdit + "']\").parent().next().next().find(\"input\").val(\"" + newDescription + "\")");
        Thread.sleep(500);

        // Click Accept icon
        ((JavascriptExecutor) driver).executeScript("$(\"#table\\\\:tableForm\\\\:entityTable_data tr td input[value*='" + nameToEdit + "']\").parent().next().next().next().next().find(\"button\")[0].click()");
    }

    /**
     * Click checkbox for Email Group by name
     * @param name Name of Email Group
     */
    public void selectEmailGroup(String name)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + name + "\")').parent().prev().find(\"span\").click()");
        System.out.println(name + " was selected...");
    }
}
