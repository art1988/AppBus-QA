package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class PoolProviderDetails extends PageObject
{
    @FindBy(id = "addEditPoolProviderForm:name")
    private WebElement nameField;

    @FindBy(id = "addEditPoolProviderForm:metadataUrl")
    private WebElement metadataURLField;

    @FindBy(id = "addEditPoolProviderForm:addInstanceUrl")
    private WebElement addInstanceURLField;

    @FindBy(id = "addEditPoolProviderForm:deleteInstanceUrl")
    private WebElement deleteInstanceURLField;

    @FindBy(id = "addEditPoolProviderForm:validateInstanceUrl")
    private WebElement validateInstanceURLField;

    @FindBy(id = "addEditPoolProviderForm:poolProviderSaveButton")
    private WebElement saveButton;

    @FindBy(id = "addEditPoolProviderForm:poolProviderCancelButton")
    private WebElement cancelButton;



    public PoolProviderDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addEditPoolProviderDlg_title').text()").equals("Pool provider details") );
    }

    public void setName(String name) throws InterruptedException
    {
        nameField.clear();
        nameField.sendKeys(name);

        Thread.sleep(500);
    }

    public void setMetadataURL(String metadataURL) throws InterruptedException
    {
        metadataURLField.clear();
        metadataURLField.sendKeys(metadataURL);

        Thread.sleep(500);
    }

    public void setAddInstanceURL(String addInstanceURL) throws InterruptedException
    {
        addInstanceURLField.clear();
        addInstanceURLField.sendKeys(addInstanceURL);

        Thread.sleep(500);
    }

    public void setDeleteInstanceURL(String deleteInstanceURL) throws InterruptedException
    {
        deleteInstanceURLField.clear();
        deleteInstanceURLField.sendKeys(deleteInstanceURL);

        Thread.sleep(500);
    }

    public void setValidateInstanceURL(String validateInstanceURL) throws InterruptedException
    {
        validateInstanceURLField.clear();
        validateInstanceURLField.sendKeys(validateInstanceURL);

        Thread.sleep(500);
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("PoolProviderDetails : Save button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("PoolProviderDetails : Cancel button was clicked");
    }

}
