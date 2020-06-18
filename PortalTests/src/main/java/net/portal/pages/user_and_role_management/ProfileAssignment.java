package net.portal.pages.user_and_role_management;

import net.portal.forms.AssignmentDetail;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ProfileAssignment extends PageObject
{
    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;


    public ProfileAssignment(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Profile Assignment") );
    }

    public AssignmentDetail addProfileAssignment()
    {
        addNewButton.click();
        System.out.println("ProfileAssignment : Add New button was clicked...");

        return new AssignmentDetail(driver);
    }
}
