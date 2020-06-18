package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class SettingDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:setting-value")
    private WebElement valueField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;


    public SettingDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Setting Details") );
    }

    public void setGroup(String groupName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:setting-group input').val(\"" + groupName + "\")");
    }

    public void setName(String name)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:setting-name input').val(\"" + name + "\")");
    }

    public void setValue(String value)
    {
        valueField.sendKeys(value);
    }

    public void clickAdd()
    {
        addButton.click();
    }

    public void clickCancel()
    {
        cancelButton.click();
    }
}
