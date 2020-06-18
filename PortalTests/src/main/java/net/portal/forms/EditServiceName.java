package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class EditServiceName extends PageObject
{
    @FindBy(id = "editServiceNameForm:editServiceName")
    private WebElement nameField;

    @FindBy(id = "editServiceNameForm:editServiceNameSaveButton")
    private WebElement saveButton;


    public EditServiceName(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#editServiceNameDlg_title').text()").equals("Edit service name") );
    }

    public void setName(String name)
    {
        nameField.clear();
        nameField.sendKeys(name);
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("EditServiceName : Save button was clicked");
    }
}
