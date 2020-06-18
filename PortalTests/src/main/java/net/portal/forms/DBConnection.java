package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DBConnection extends PageObject
{
    @FindBy(name = "dbCOnnectionForm:name")
    private WebElement nameField;

    @FindBy(name = "dbCOnnectionForm:host")
    private WebElement hostField;

    @FindBy(name = "dbCOnnectionForm:port")
    private WebElement portField;

    @FindBy(name = "dbCOnnectionForm:dbName")
    private WebElement dbNameField;

    @FindBy(name = "dbCOnnectionForm:dbSchema")
    private WebElement dbSchemaField;

    @FindBy(name = "dbCOnnectionForm:username")
    private WebElement dbUsernameField;

    @FindBy(id = "dbCOnnectionForm:password")
    private WebElement passwordField;


    @FindBy(id = "dbCOnnectionForm:testConnectionButton")
    private WebElement testConnectionButton;

    @FindBy(id = "dbCOnnectionForm:saveConnectionButton")
    private WebElement saveButton;

    @FindBy(id = "dbCOnnectionForm:cancelConnectionButton")
    private WebElement cancelButton;


    public DBConnection(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addEditDbConnectionDlg_title').text()").equals("DB Connection") );
    }

    public void setName(String connectionName)
    {
        nameField.clear();
        nameField.sendKeys(connectionName);
    }

    public void setType(String type)
    {
        ((JavascriptExecutor) driver).executeScript("$('#dbCOnnectionForm\\\\:dbType_label').click()"); // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#dbCOnnectionForm\\\\:dbType_items li:contains(\"" + type + "\")').click()");

        System.out.println("Type = " + type + " was selected");
    }

    public void setHost(String host)
    {
        hostField.sendKeys(host);
    }

    public void setPort(String port)
    {
        portField.sendKeys(port);
    }

    public void setDbName(String dbName)
    {
        dbNameField.sendKeys(dbName);
    }

    public void setDbSchema(String dbSchema)
    {
        dbSchemaField.sendKeys(dbSchema);
    }

    public void setDbUsername(String username)
    {
        dbUsernameField.sendKeys(username);
    }

    public void setPassword(String password)
    {
        passwordField.sendKeys(password);
    }

    public void clickTestConnection()
    {
        testConnectionButton.click();
        System.out.println("CreateUI : Test connection was clicked");
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("CreateUI : Save button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("CreateUI : Cancel button was clicked");
    }

}
