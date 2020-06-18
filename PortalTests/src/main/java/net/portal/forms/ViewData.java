package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ViewData extends PageObject
{
    @FindBy(id = "viewJobDataForm:okButton")
    private WebElement okButton; // Scheduler -> Add job -> View data

    @FindBy(id = "viewValueForm:okBtnViewDlg") //j_idt485:okBtnViewDlg //j_idt389:okBtnViewDlg
    private WebElement ok2Button; //User & Role Management > Navigation: Navigation items: Add New --> Item Assignment Details

    @FindBy(id = "viewJobDataForm:cancelButton") // was "j_idt299:j_idt302"
    private WebElement viewDataCancelButton;




    public ViewData(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (
                ((JavascriptExecutor) driver).executeScript("return $('#viewJobDataDlg_title').text()").equals("View data")||
                        ((JavascriptExecutor) driver).executeScript("return $('#viewValueDlg_title').text()").equals("View data")
                );
    }

    /**
     * Set value for ViewData form. Uses CodeMirror Editor
     * @param value value to set
     */
    public void setValue(String value)
    {
        StringBuffer jsCode = new StringBuffer("doc = $('.CodeMirror')[0].CodeMirror;");
        jsCode.append("doc.setValue('" + value + "');");

        ((JavascriptExecutor) driver).executeScript(jsCode.toString());
    }

    public void clickOk()
    {
        ((JavascriptExecutor) driver).executeScript("$('#viewJobDataForm\\\\:okButton').click()");
        System.out.println("ViewData : OK1 button was clicked");
    }

    public void clickOk2()
    {
        ok2Button.click();
        System.out.println("ViewData : OK2 button was clicked");
    }

    public void clickCancel()
    {
        viewDataCancelButton.click();
        System.out.println("ViewData : Cancel button was clicked");
    }

    public void sendTextToActiveField(String json)
    {
        driver.switchTo().activeElement().sendKeys(json);
    }
}
