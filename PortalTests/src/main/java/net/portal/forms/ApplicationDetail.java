package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ApplicationDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:name")
    private WebElement nameField;

    @FindBy(id = "entity:dialogsForm:description")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;


    public ApplicationDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Application Detail"));
    }

    public void setName(String contextName)
    {
        nameField.sendKeys(contextName);
    }

    public void setDescription(String description)
    {
        descriptionField.sendKeys(description);
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("ApplicationDetail : Add button was clicked");
    }

    /**
     * Click Cancel button on Contexts page
     */
    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("ApplicationDetail : Cancel button was clicked");
    }

}
