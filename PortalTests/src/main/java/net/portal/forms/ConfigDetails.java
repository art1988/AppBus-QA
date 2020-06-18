package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;

public class ConfigDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:config-name")
    private WebElement nameField;

    @FindBy(id = "entity:dialogsForm:configUpload_input")
    private WebElement chooseField;

    @FindBy(className = "ui-fileupload-upload")
    private WebElement uploadButton;

    @FindBy(xpath = "//*[@id=\"entity:dialogsForm:addEntity\"]/span[2]")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:saveEntity")
    private WebElement saveButton;

    @FindBy(id = "entity:dialogsForm:cancelEditEntity")
    private WebElement cancelButton;


    public ConfigDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Config Details") );
    }

    public void setName(String configName)
    {
        nameField.clear();
        nameField.sendKeys(configName);
    }

    public void chooseFile(String fullPathToFile)
    {
        chooseField.sendKeys(fullPathToFile);
    }

    public void clickUpload()
    {
        uploadButton.click();
        System.out.println("ConfigDetails: Upload was clicked");
    }

    public void clickBinaryCheckbox()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:binary-config span').click()");
        System.out.println("ConfigDetails : Binary checkbox was clicked");
    }

    public String getContent()
    {
        StringBuffer jsCode = new StringBuffer("doc = $('.CodeMirror')[0].CodeMirror;");
        jsCode.append("return doc.getValue();");

        return String.valueOf(((JavascriptExecutor) driver).executeScript(jsCode.toString()));
    }

    public void setContent(String content)
    {
        StringBuffer jsCode = new StringBuffer("doc = $('.CodeMirror')[0].CodeMirror;");
        jsCode.append("doc.setValue(\"" + content + "\");");

        ((JavascriptExecutor) driver).executeScript(jsCode.toString());
    }

    public void clickAdd()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:addEntity').click()");
        System.out.println("ConfigDetails : Add button was clicked");
    }

    public void clickSave()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:saveEntity').click()");
        System.out.println("ConfigDetails : Save button was clicked");
    }

    public void clickCancel()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:cancelEditEntity').click()");
        System.out.println("ConfigDetails : Cancel button was clicked");
    }
}
