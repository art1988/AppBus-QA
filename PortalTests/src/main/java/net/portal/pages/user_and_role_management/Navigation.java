package net.portal.pages.user_and_role_management;

import net.portal.constants.Retries;
import net.portal.forms.ItemAssignmentDetails;
import net.portal.forms.NavTreeItemAssignmentDetails;
import net.portal.forms.UIGroupDetails;
import net.portal.pages.DeleteItemPopup;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Navigation extends PageObject
{
    @FindBy(id = "tableButtonAddNewGroup")
    private WebElement addGroupButton;

    @FindBy(id = "tableButtonAddNewTop")
    private WebElement addNavigationItem;

    @FindBy(xpath = "//*[text()='Preview']") //span[@class='ui-button-icon-left ui-icon ui-c submenu-navigation-class']
    private WebElement previewButton;

    @FindBy(xpath = "//label[contains(.,'---- Select UI group ----')]")
    private WebElement expandUIgrpList;


    public Navigation(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElements(By.className("ui-panel-title")).get(0).getText().equals("User & Role Management > Navigation") );
    }

    public void selectProfile(String profileName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#profile .ui-icon-triangle-1-s').click()"); // expand dropdown

        ((JavascriptExecutor) driver).executeScript("$('#profile_items li:contains(\"" + profileName + "\")').click()");

        System.out.println(profileName + " profile was selected");
    }

    public void selectUIgrp(String grpName) throws InterruptedException
    {
        expandUIgrpList.click();
        Thread.sleep(1_000);
        String xP = "//li[contains(.,'" + grpName + "')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
        System.out.println(grpName + " profile was selected");
    }

    public UIGroupDetails addGroup()
    {
        addGroupButton.click();

        System.out.println("Add Group button was clicked");

        return new UIGroupDetails(driver);
    }

    public void clickPreview()
    {
        Retries.RETRY_50_TIMES.run(() -> previewButton.click()); //Retry
        System.out.println("Preview button was clicked");

    }

    public UIGroupDetails addUIGroup()
    {

        addGroupButton.click();

        System.out.println("Add UI Group button was clicked");

        return new UIGroupDetails(driver);
    }

    public ItemAssignmentDetails addNavigationItem() throws InterruptedException
    {
        addNavigationItem.click();

        Thread.sleep(3_000);

        return new ItemAssignmentDetails(driver);
    }

    public NavTreeItemAssignmentDetails addNewNvgItem() throws InterruptedException
    {
        addNavigationItem.click();

        Thread.sleep(3_000);

        return new NavTreeItemAssignmentDetails(driver);
    }

    public void moveItemDown(String itemName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even:contains(\"" + itemName + "\")').parent().next().find(\"button\")[2].click()");
        System.out.println(itemName + " was moved down");
    }

    public void moveItemUp(String itemName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even:contains(\"" + itemName + "\")').parent().next().find(\"button\")[3].click()");
        System.out.println(itemName + " was moved up");
    }

    public DeleteItemPopup deleteItem(String itemName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even:contains(\"" + itemName + "\")').parent().next().find(\"button\")[1].click()");
        System.out.println(itemName + " was deleted");

        return new DeleteItemPopup(driver);
    }

    public ItemAssignmentDetails editItem(String itemName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even:contains(\"" + itemName + "\")').parent().next().find(\"button\")[0].click()");
        System.out.println(itemName + " was edited");

        return new ItemAssignmentDetails(driver);
    }

    public DeleteItemPopup deleteNavigationGroups()
    {
        ((JavascriptExecutor) driver).executeScript("$('#deleteBtnGroup').click()");
        System.out.println("Delete navigation group was clicked");

        return new DeleteItemPopup(driver);
    }
}
