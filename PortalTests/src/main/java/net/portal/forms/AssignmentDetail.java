package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class AssignmentDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;


    public AssignmentDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Assignment Detail") );
    }

    /**
     * Set Application by name
     * @param appName name of Application to set
     */
    public void setApplication(String appName)
    {
        // Expand Application dropdown
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:property-application span').click()");

        // Select Application
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:property-application_items li:contains(\"" + appName + "\")').click()");
    }

    /**
     * Get selected value from Application dropdown
     * @return
     */
    public String getApplication()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:property-application_label').text()"));
    }

    public void clickCancel()
    {
        cancelButton.click();

        System.out.println("AssignmentDetail : Cancel button was clicked");
    }
}
