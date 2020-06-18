package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class PoolDetails extends PageObject
{
    @FindBy(id = "addEditPoolForm:name")
    private WebElement nameField;

    @FindBy(id = "addEditPoolForm:poolSaveButton")
    private WebElement saveButton;



    public PoolDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addEditPoolDlg_title').text()").equals("Pool details"));
    }

    public void setName(String poolName)
    {
        nameField.clear();
        nameField.sendKeys(poolName);
    }

    public void setProvider(String providerName)
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#addEditPoolForm\\\\:provider_label').click()");

        // select item
        ((JavascriptExecutor) driver).executeScript("$('#addEditPoolForm\\\\:provider_items li:contains(\"" + providerName + "\")').click()");
    }

    public void clickSave()
    {
        saveButton.click();

        System.out.println("PoolDetails : Save button was clicked");
    }
}
