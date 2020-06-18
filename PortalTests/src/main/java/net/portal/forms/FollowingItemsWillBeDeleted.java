package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class FollowingItemsWillBeDeleted extends PageObject
{
    @FindBy(id = "delete:deleteForm:confirmDeleteButton")
    private WebElement deleteButton;


    public FollowingItemsWillBeDeleted(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#delete\\\\:deleteForm\\\\:deleteDialog_title').text()").equals("Following items will be deleted") );
    }

    public String getListOfItemsToDelete()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#delete\\\\:deleteForm\\\\:displayMulti_list').text()"));
    }

    public void clickDelete()
    {
        ((JavascriptExecutor) driver).executeScript("$('#delete\\\\:deleteForm\\\\:confirmDeleteButton').click()");
        System.out.println("FollowingItemsWillBeDeleted : Delete was clicked");
    }
}
