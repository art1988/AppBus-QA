package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

// Select policy popup which appears after clicking on Add Item Assignment Details form if Override checkbox was checked
public class SelectPolicyOverride extends PageObject
{
    @FindBy(id = "addPropertyForm:okButton") //was j_idt302:j_idt306
    private WebElement okButton;



    public SelectPolicyOverride(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addPropertyDlg_title').text()").equals("Select policy") );
    }

    public void selectPolicy(String policyName)
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#addPropertyForm\\\\:addPropertyDropdown label').click()"); //was "#j_idt303\\:addPropertyDropdown label"

        // select policy
        ((JavascriptExecutor) driver).executeScript("$('#addPropertyForm\\\\:addPropertyDropdown_items li:contains(\"" + policyName + "\")').click()"); //was "#j_idt303\\:addPropertyDropdown_items li:contains("

        System.out.println("The following policy was chosen : " + policyName);
    }

    public void clickOk()
    {
        okButton.click();

        System.out.println("SelectPolicyOverride : Ok button was clicked");
    }
}
