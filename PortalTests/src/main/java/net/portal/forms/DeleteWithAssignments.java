package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DeleteWithAssignments extends PageObject
{
    @FindBy(id = "deleteWithAssignments:deleteButton")
    private WebElement deleteButton;

    @FindBy(id = "deleteWithAssignments:cancelButton")
    private WebElement cancelButton;



    public DeleteWithAssignments(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#deleteWithAssignments\\\\:deleteWithAssignmentsDialog_title').text()").equals("Delete with assignments"));
    }

    public void clickDeleteButton()
    {
        deleteButton.click();
        System.out.println("DeleteWithAssignments : Delete button was clicked");
    }

}
