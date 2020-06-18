package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class UploadItem extends PageObject
{
    @FindBy(id = "itemUploadWizardDlgForm:fileUpload_input")
    private WebElement chooseField;

    @FindBy(className = "ui-fileupload-upload")
    private WebElement uploadButton;

    @FindBy(id = "itemUploadWizardDlgForm:fileUploadWizard_next")
    private WebElement nextButton;

    @FindBy(id = "itemUploadWizardDlgForm:saveButtonOnParentItemTab")
    private WebElement saveButton;

    @FindBy(id = "itemUploadWizardDlgForm:cancelUploadItem")
    private WebElement cancelButton;



    public UploadItem(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#itemUploadWizardDlgForm\\\\:itemUploadWizardDlg_title').text()").equals("Upload Item") );
    }

    public void chooseFile(String fullPathToFile)
    {
        chooseField.sendKeys(fullPathToFile);
    }

    public void clickUpload()
    {
        uploadButton.click();
        System.out.println("UploadItem: Upload was clicked");
    }

    public void clickNext()
    {
        nextButton.click();
        System.out.println("UploadItem: Next was clicked");
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("UploadItem: Save was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("UploadItem: Cancel was clicked");
    }
}
