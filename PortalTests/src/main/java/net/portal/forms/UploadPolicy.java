package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class UploadPolicy extends PageObject
{
    @FindBy(id = "policyUploadDlgForm:policyUploadChoser_input")
    private WebElement chooseField;

    @FindBy(className = "ui-fileupload-upload")
    private WebElement uploadButton;

    @FindBy(id = "policyUploadDlgForm:policyUploadCloseButton")
    private WebElement closeButton;


    public UploadPolicy(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#policyUploadDlgForm\\\\:uploadPolicyDialog_title').text()").equals("Upload Policy") );
    }

    public void chooseFile(String fullPathToFile)
    {
        chooseField.sendKeys(fullPathToFile);
    }

    public void clickUpload()
    {
        uploadButton.click();
        System.out.println("UploadPolicy: Upload was clicked");
    }

    public void clickClose()
    {
        closeButton.click();
        System.out.println("Close button was clicked");
    }
}
