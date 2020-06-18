package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class SelectPolicy extends PageObject
{
    @FindBy(id = "addPropertyForm:addPropertyOkButton")
    private WebElement okButton;


    public SelectPolicy(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addPropertyDlg_title').text()").equals("Select policy") );
    }

    public void addPolicy(String policyName)
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#addPropertyForm\\\\:addPropertyDropdown span').click()");

        ((JavascriptExecutor) driver).executeScript("$('#addPropertyForm\\\\:addPropertyDropdown_items li:contains(\"" + policyName + "\")').click()");

        System.out.println(policyName + " was added");
    }

    public void clickOk()
    {
        okButton.click();
        System.out.println("SelectProperty : Ok was clicked");
    }

    public void expandPolicyDropdown()
    {
        ((JavascriptExecutor) driver).executeScript("$('#addPropertyForm\\\\:addPropertyDropdown span').click()");
    }
}
