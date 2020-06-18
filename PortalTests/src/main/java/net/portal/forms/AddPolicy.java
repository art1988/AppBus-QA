package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class AddPolicy extends PageObject
{
    @FindBy(id = "addServiceEntryDlgForm:addServiceEntryValueDlgConfrim")
    private WebElement okButton;

    @FindBy(id = "addServiceEntryValueDlg")
    private WebElement wholePopUp;

    public AddPolicy(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addServiceEntryValueDlg_title').text()").equals("Add policy"));
    }

    public String clickOk() throws InterruptedException
    {

        String policy = wholePopUp.findElement(By.tagName("label")).getText();

        okButton.click(); //Waiting
        Thread.sleep(1_00);
        System.out.println("AddPolicy : Ok button was clicked, selected policy is :" + policy);

        return policy;
    }

    public void selectPolicy(String policyName) throws InterruptedException
    {
        wholePopUp.findElement(By.tagName("label")).click();
        Thread.sleep(1_00);
        String xP = "//li[@data-label='" + policyName +"']"; //_property_edit
        wholePopUp.findElement(By.xpath(xP)).click();
        Thread.sleep(1_00);
        System.out.println("AddPolicy : Ok button was clicked");
    }
}
