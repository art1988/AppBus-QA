package net.portal.forms;

import net.portal.pages.DeleteConfirmPopup;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ProfileDetail extends PageObject
{
    @FindBy(id = "deleteWithAssignments:j_idt100")
    private WebElement deleteButton;

    @FindBy(id = "entity:dialogsForm:name")
    private WebElement nameField;

    @FindBy(id = "entity:dialogsForm:description")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addProfileButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;

    public ProfileDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
        // TODO: if click edit of existing -> then need to init itemPropertyIndex
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Profile Detail") );
    }

    public void setName(String name)
    {
        nameField.clear();
        nameField.sendKeys(name);
    }

    public void setDescription(String description)
    {
        descriptionField.clear();
        descriptionField.sendKeys(description);
    }

    public void clickAdd()
    {
        addProfileButton.click();
    }

    public void clickCancel()
    {
        cancelButton.click();
    }

    public void clickDelete()
    {
        deleteButton.click();
        System.out.println("deleteWithAssignments : Delete was clicked");

    }

}
