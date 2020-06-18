package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class AddJob extends PageObject
{
    @FindBy(id = "addJobForm:name")
    private WebElement nameField;

    @FindBy(id = "addJobForm:description")
    private WebElement descriptionField;

    @FindBy(id = "addJobForm:jobTriggersTable:addTriggerButton")
    private WebElement addTriggerButton;

    @FindBy(id = "addJobForm:saveButtonOnAddJob")
    private WebElement saveButton;

    @FindBy(id = "addJobForm:cancelButtonOnAddJob")
    private WebElement cancelButton;



    public AddJob(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addJobDlg_title').text()").equals("Add job") );
    }

    public void setName(String jobName)
    {
        nameField.clear();
        nameField.sendKeys(jobName);
    }

    /**
     *
     * @param actionName may be Publish event or Call service
     */
    public void setAction(String actionName)
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:action_label').click()");

        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:action_items li:contains(\"" + actionName + "\")').click()");
    }

    public void setDescription(String description)
    {
        descriptionField.clear();
        descriptionField.sendKeys(description);
    }

    public ViewData viewTopic()
    {
        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:jobDataTable_data button')[0].click()");
        System.out.println("View topic was clicked");

        return new ViewData(driver);
    }

    public ViewData viewMessage()
    {
        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:jobDataTable_data button')[1].click()");
        System.out.println("View message was clicked");

        return new ViewData(driver);
    }

    public ViewData viewEnvironment()
    {
        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:jobDataTable_data button')[0].click()");
        System.out.println("View environment was clicked");

        return new ViewData(driver);
    }

    public ViewData viewApiData()
    {
        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:jobDataTable_data button')[1].click()");
        System.out.println("View apiData was clicked");

        return new ViewData(driver);
    }

    public ViewData viewName()
    {
        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:jobDataTable_data button')[2].click()");
        System.out.println("View name was clicked");

        return new ViewData(driver);
    }

    public ViewData viewProject()
    {
        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:jobDataTable_data button')[3].click()");
        System.out.println("View project was clicked");

        return new ViewData(driver);
    }

    public AddTrigger addTrigger()
    {
        addTriggerButton.click();
        System.out.println("AddJob : Add trigger button was clicked");

        return new AddTrigger(driver);
    }

    public void clickSave()
    {
        ((JavascriptExecutor) driver).executeScript("$('#addJobForm\\\\:saveButtonOnAddJob').click()");
        System.out.println("AddJob : Save button was clicked");
    }
}
