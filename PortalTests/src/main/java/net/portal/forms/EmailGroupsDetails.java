package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class EmailGroupsDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:email-group-name")
    private WebElement nameField;

    @FindBy(id = "entity:dialogsForm:email-group-content")
    private WebElement contentArea;

    @FindBy(id = "entity:dialogsForm:email-group-description")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;



    public EmailGroupsDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Email Groups Details") );
    }

    public void setName(String name)
    {
        nameField.clear();
        nameField.sendKeys(name);
    }

    public void setContent(String content)
    {
        contentArea.clear();
        contentArea.sendKeys(content);
    }

    public void setDescription(String description)
    {
        descriptionField.clear();
        descriptionField.sendKeys(description);
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("EmailGroupsDetails : Add button was clicked...");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("EmailGroupsDetails : Cancel button was clicked...");
    }

}
