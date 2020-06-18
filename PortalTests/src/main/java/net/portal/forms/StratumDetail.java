package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class StratumDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:name")
    private WebElement nameFiled;

    @FindBy(id = "entity:dialogsForm:expiration")
    private WebElement expirationField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;


    public StratumDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Stratum Detail") );
    }

    public void setName(String stratumName)
    {
        nameFiled.sendKeys(stratumName);
    }

    public void setExpiration(int expiration)
    {
        expirationField.sendKeys(String.valueOf(expiration));
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("Stratum Detail : Add button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("Stratum Detail : Cancel button was clicked");
    }
}
