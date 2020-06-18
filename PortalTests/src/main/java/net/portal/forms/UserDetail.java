package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class UserDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:name")
    private WebElement userNameField;

    @FindBy(id = "entity:dialogsForm:firstName")
    private WebElement firstNameField;

    @FindBy(id = "entity:dialogsForm:lastName")
    private WebElement lastNameField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;


    public UserDetail(WebDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("User Detail") );
    }

    public void setDomain(String domain)
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:domain_label').click()");

        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:domain_items li:contains(\"" + domain + "\")').click()");
    }

    public void setUserName(String userName)
    {
        userNameField.clear();
        userNameField.sendKeys(userName);
    }

    public void setFirstName(String firstName)
    {
        firstNameField.clear();
        firstNameField.sendKeys(firstName);
    }

    public void setLastName(String lastName)
    {
        lastNameField.clear();
        lastNameField.sendKeys(lastName);
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("UserDetail: add was clicked");
    }
}
