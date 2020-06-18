package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ListOfUsers extends PageObject
{
    @FindBy(className = "userSearch")
    private WebElement userSearchField;

    @FindBy(id = "usersDialogForm:userDetailsSaveButton")
    private WebElement saveButton;


    public ListOfUsers(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#usersDialogForm\\\\:userDtailsDlg_title').text()").equals("List of users") );
    }

    public void searchForUser(String user)
    {
        userSearchField.clear();
        userSearchField.sendKeys(user);
    }

    public void clickSelectAllCheckbox()
    {
        ((JavascriptExecutor) driver).executeScript("$('#usersDialogForm\\\\:userDetailsTable\\\\:userDtailsSelectAll .ui-chkbox-icon.ui-icon.ui-c').click()");

        System.out.println("ListOfUsers : Select All Checkbox was checked");
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("ListOfUsers : Save was clicked");
    }
}
