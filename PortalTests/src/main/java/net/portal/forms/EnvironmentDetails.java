package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class EnvironmentDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:environmentName")
    private WebElement nameField;

    @FindBy(id = "entity:dialogsForm:environmentDescription")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;


    public EnvironmentDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Environment details") );
    }

    public void setEnvironmentName(String name)
    {
        nameField.clear();
        nameField.sendKeys(name);
    }

    public void setEnvironmentDescription(String description)
    {
        descriptionField.sendKeys(description);
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("EnvironmentDetails : Add button was clicked");
    }
}
