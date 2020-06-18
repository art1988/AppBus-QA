package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ContextDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:name")
    private WebElement nameField;

    @FindBy(id = "entity:dialogsForm:description")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;


    public ContextDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Context Detail") );
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
        addButton.click();
        System.out.println("ContextDetail : Add button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("ContextDetail : Cancel button was clicked");
    }
}
