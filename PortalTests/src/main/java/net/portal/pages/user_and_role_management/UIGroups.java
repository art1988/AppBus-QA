package net.portal.pages.user_and_role_management;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.UIGroupDetails;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class UIGroups extends PageObject
{
    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteButton;

    @FindBy(xpath = "//*[text()='Following items will be deleted']")
    private WebElement titleOfDelPopup;

    public UIGroups(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > UI Groups") );
    }

    public UIGroupDetails addUIGroup()
    {
        addNewButton.click();
        System.out.println("UIGroups : add new button was clicked");

        return new UIGroupDetails(driver);
    }

    public FollowingItemsWillBeDeleted deleteUIGroup(String groupName)
    {
        // Select group name
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2):contains(\"" + groupName + "\")').prev().find(\"input\").click()");

        deleteButton.click();

        return new FollowingItemsWillBeDeleted(driver);
    }

    public void ConfirmDelete() throws InterruptedException
    {

        titleOfDelPopup.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        System.out.println("GroupDetails : PopUp windows Delete button was clicked)");

    }
}
