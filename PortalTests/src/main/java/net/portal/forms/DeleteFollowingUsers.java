package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeleteFollowingUsers extends PageObject
{
    @FindBy(id = "delete:deleteForm:confirmDeleteButton")
    private WebElement deleteButton;


    public DeleteFollowingUsers(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#delete\\\\:deleteForm\\\\:deleteDialog_title').text()").equals("Delete Following Users") );
    }

    // Get one or more users
    public String getListOfUsersToDelete()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#delete\\\\:deleteForm\\\\:displayMulti_list').text()"));
    }

    public void clickDelete()
    {
        deleteButton.click();
        System.out.println("DeleteFollowingUsers : Delete was clicked");
    }
}
