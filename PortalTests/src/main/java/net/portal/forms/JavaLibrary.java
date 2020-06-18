package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class JavaLibrary extends PageObject
{
    @FindBy(name = "addEditJavaLibForm:javaLibName")
    private WebElement nameField;

    @FindBy(name = "addEditJavaLibForm:javaLibDescription")
    private WebElement descriptionField;

    @FindBy(id = "addEditJavaLibForm:javaLibUpload_input")
    private WebElement chooseButton;

    @FindBy(className = "ui-fileupload-upload")
    private WebElement uploadButton;

    @FindBy(id = "addEditJavaLibForm:javaLibSave")
    private WebElement saveButton;

    @FindBy(id = "addEditJavaLibForm:javaLibCancel")
    private WebElement cancelButton;


    public JavaLibrary(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addEditJavaLibDlg_title').text()").equals("Java Library") );
    }

    public void setName(String javaLibName)
    {
        nameField.clear();
        nameField.sendKeys(javaLibName);
    }

    public void setDescription(String description)
    {
        descriptionField.sendKeys(description);
    }

    public void chooseFile(String fullPathToFile)
    {
        chooseButton.sendKeys(fullPathToFile);
    }

    public void clickUpload()
    {
        uploadButton.click();
        System.out.println("JavaLibrary: Upload button was clicked");
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("JavaLibrary: Save button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("JavaLibrary: Cancel button was clicked");
    }
}
