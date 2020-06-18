package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class RoleAssignmentDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;


    public RoleAssignmentDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Role Assignment Detail") );
    }

    public void setRole(String roleName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:property-role_panel li:contains(\"" + roleName + "\")').click()");
        System.out.println("Role : " + roleName + " was selected");
    }

    public void setUser(String userName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:property-user_panel li:contains(\"" + userName + "\")').click()");
        System.out.println("User : " + userName + " was selected");
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("RoleAssignmentDetail : Add button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("RoleAssignmentDetail : Cancel button was clicked");
    }
}
