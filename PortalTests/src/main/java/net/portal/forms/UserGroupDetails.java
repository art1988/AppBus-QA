package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class UserGroupDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:group-name")
    private WebElement nameField;

    @FindBy(id = "entity:dialogsForm:group-description")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:entityEditButton")
    private WebElement editButton;

    @FindBy(id = "entity:dialogsForm:fileUpload_input")
    private WebElement chooseField;

    @FindBy(className = "ui-fileupload-upload")
    private WebElement uploadButton;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:saveEntity")
    private WebElement saveButton;


    public UserGroupDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("User Group Details") );
    }

    public void setName(String userGroupName)
    {
        nameField.clear();
        nameField.sendKeys(userGroupName);
    }

    public void setDescription(String userGroupDescription)
    {
        descriptionField.clear();
        descriptionField.sendKeys(userGroupDescription);
    }

    public ListOfUsers clickEdit()
    {
        editButton.click();
        System.out.println("UserGroupDetails: Edit was clicked");

        return new ListOfUsers(driver);
    }

    public void chooseFile(String fullPathToFile)
    {
        chooseField.sendKeys(fullPathToFile);
    }

    public void clickUpload()
    {
        uploadButton.click();
        System.out.println("UserGroupDetails: Upload was clicked");
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("UserGroupDetails: Add was clicked");
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("UserGroupDetails: Save was clicked");
    }
}
