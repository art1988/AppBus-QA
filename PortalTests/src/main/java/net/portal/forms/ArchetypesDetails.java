package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ArchetypesDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:itemControllerTypeName")
    private WebElement nameFiled;

    @FindBy(id = "entity:dialogsForm:itemControllerTypeDescription")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;


    public ArchetypesDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Archetypes Details") );
    }

    public void setName(String archetypeName)
    {
        nameFiled.sendKeys(archetypeName);
    }

    public void setDescription(String description)
    {
        descriptionField.sendKeys(description);
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("ItemControllerTypeDeatils : Add button was clicked");
    }
}
