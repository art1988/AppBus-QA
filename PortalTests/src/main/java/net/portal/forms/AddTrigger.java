package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class AddTrigger extends PageObject
{
    @FindBy(id = "addTriggerForm:interval")
    private WebElement intervalField;

    @FindBy(id = "addTriggerForm:repeatCountInput")
    private WebElement repeatField;

    @FindBy(id = "addTriggerForm:triggerSaveButton")
    private WebElement saveButton;

    @FindBy(id = "addTriggerForm:triggerDirectEditingSaveButton")
    private WebElement directSaveButton;

    @FindBy(id = "addTriggerForm:triggerCancelButton")
    private WebElement cancelButton;



    public AddTrigger(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addTriggerDlg_title').text()").equals("Add trigger"));
    }

    public void setType(String type) throws InterruptedException
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#addTriggerForm\\\\:triggerType label').click()");

        ((JavascriptExecutor) driver).executeScript("$('#addTriggerForm\\\\:triggerType_items li:contains(\"" + type + "\")').click()");

        Thread.sleep(500);
    }

    public void setInterval(String value) throws InterruptedException
    {
        intervalField.clear();
        intervalField.sendKeys(value);

        Thread.sleep(500);
    }

    /**
     *
     * @param intervalType can be 'Ms', 'Sec', 'Min' or 'Hours'
     */
    public void setIntervalType(String intervalType) throws InterruptedException
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#addTriggerForm\\\\:simpleIntervalType_label').click()");

        ((JavascriptExecutor) driver).executeScript("$('#addTriggerForm\\\\:simpleIntervalType_items li:contains(\"" + intervalType + "\")').click()");

        Thread.sleep(500);
    }

    /**
     *
     * @param repeatType can be 'forever' or 'count'
     */
    public void setRepeatType(String repeatType) throws InterruptedException
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#addTriggerForm\\\\:repeatType_label').click()");

        ((JavascriptExecutor) driver).executeScript("$('#addTriggerForm\\\\:repeatType_items li:contains(\"" + repeatType + "\")').click()");

        Thread.sleep(500);
    }

    public void setRepeatValue(String repeatValue) throws InterruptedException
    {
        repeatField.clear();
        repeatField.sendKeys(repeatValue);

        Thread.sleep(500);
    }

    public void clickSave()
    {
        try
        {
            saveButton.click();
        }
        catch (NoSuchElementException e)
        {
            directSaveButton.click();
        }

        System.out.println("AddTrigger : Save button was clicked");
    }
}
