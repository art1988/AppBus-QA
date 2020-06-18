package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class AlertDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:log-event-action")
    private WebElement actionField;

    @FindBy(id = "entity:dialogsForm:log-event-subject")
    private WebElement subjectField;

    @FindBy(id = "entity:dialogsForm:log-event-body")
    private WebElement bodyTextArea;

    @FindBy(id = "entity:dialogsForm:log-event-description")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;



    public AlertDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Alert Details") );
    }

    public void setAction(String action)
    {
        actionField.clear();
        actionField.sendKeys(action);
    }

    public void setEmailGroup(String emailGroupName)
    {
        // Expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:log-event-email-name label').click()");

        // Choose item
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:log-event-email-name_items li:contains(\"" + emailGroupName + "\")').click()");

        System.out.println(emailGroupName + " was selected");
    }

    public String getEmailGroup()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:log-event-email-name label').text()"));
    }

    public void setSubject(String subject)
    {
        subjectField.clear();
        subjectField.sendKeys(subject);
    }

    public void setBody(String bodyText)
    {
        bodyTextArea.clear();
        bodyTextArea.sendKeys(bodyText);
    }

    public void setDescription(String description)
    {
        descriptionField.clear();
        descriptionField.sendKeys(description);
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("AlertDetails : Add button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("AlertDetails : Cancel button was clicked");
    }
}
