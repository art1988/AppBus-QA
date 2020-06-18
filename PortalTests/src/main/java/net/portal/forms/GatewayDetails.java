package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.util.List;

public class GatewayDetails  extends PageObject
{
    @FindBy(id = "gatewayDlgForm:gatewayDlgName")
    private WebElement gatewayNmaeInput;

    @FindBy(id = "gatewayDlgForm:gatewayClientSelect_label")
    private WebElement clientDropDownField;

    @FindBy(id = "gatewayDlgForm:gatewayClientSelect_1")
    private WebElement clientCertItem01;

    @FindBy(id = "gatewayDlgForm:gatewayTrustSelect_label")
    private WebElement trustDropDownField;

    @FindBy(id = "gatewayDlgForm:gatewayTrustSelect_1")
    private WebElement trustCertItem01;

    @FindBy(id = "gatewayDlgForm:gatewayDlgPort")
    private WebElement portField;

    @FindBy(id = "gatewayDlgForm:gatewayDlgHost")
    private WebElement hostField;

    @FindBy(id = "gatewayDlgForm:gatewayDlgCancelButton")
    private WebElement cancelButton;

    @FindBy(id = "gatewayDlgForm:gatewayDlgSaveButton")
    private WebElement saveButton;

    public GatewayDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#gatewayDlg_title').text()").equals("Gateway details"));
    }

    public void clickSave() throws InterruptedException
    {
        saveButton.click();
        Thread.sleep(2_000);
        System.out.println("activeElement is: " + driver.switchTo().activeElement().getText());
        if(saveButton.isDisplayed())
            {
                for (int i=0; i< 10; i++)
                {
                    if(saveButton.isDisplayed()) saveButton.click();
                    if(saveButton.isDisplayed()) { int sleep = i * 5000;  Thread.sleep(sleep); }
                    else break;
                    if (i == 9) System.out.println("ATTENTION !!! GatewayDetails : Save button is not working!");
                }
            }

        System.out.println("GatewayDetails : Save button was clicked");
    }

    public void clickSaveForNoteCheck() throws InterruptedException
    {
        saveButton.click();
        Thread.sleep(2_000);
        System.out.println("GatewayDetails : Save button was simply  clicked");
    }

    public void setName(String nm) throws InterruptedException
    {
        gatewayNmaeInput.clear();
        Thread.sleep(1_000);
        gatewayNmaeInput.sendKeys(nm);
        Thread.sleep(1_000);
        System.out.println("GatewayDetails : Gateway name (" + nm + ") was set");
    }

    public void setPort(String pt) throws InterruptedException
    {
        portField.clear();
        Thread.sleep(1_000);
        portField.sendKeys(pt);
        Thread.sleep(1_000);
        System.out.println("GatewayDetails : Port (" + pt + ") was set");
    }

    public void setHost(String ht) throws InterruptedException
    {
        hostField.clear();
        Thread.sleep(1_000);
        hostField.sendKeys(ht);
        Thread.sleep(1_000);
        System.out.println("GatewayDetails : Host (" + ht + ") was set");
    }

    public String setClientCertificateTheFirstItem() throws InterruptedException
    {
        clientDropDownField.click();
        Thread.sleep(1_000);
        clientCertItem01.click();
        Thread.sleep(1_000);
        String CertName = clientDropDownField.getText();
        System.out.println("GatewayDetails : the first item (Client Certificate name) was selected");

        return CertName;
    }

    public void setClientCertificateByName(String nm) throws InterruptedException
    {
        clientDropDownField.click();
        Thread.sleep(1_000);
        String xP = "//li[contains(.,'" + nm + "')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
        System.out.println("GatewayDetails : the following item (Client Certificate name) was selected: " + nm);
    }

    public String setTrustCertificateTheFirstItem() throws InterruptedException
    {
        trustDropDownField.click();
        Thread.sleep(1_000);
        trustCertItem01.click();
        Thread.sleep(1_000);
        String certName = trustDropDownField.getText();
        System.out.println("GatewayDetails : the first item (Trust Certificate name) was selected");

        return certName;
    }

    public void setTrustCertificateByName(String nm) throws InterruptedException
    {
        trustDropDownField.click();
        Thread.sleep(1_000);
        String xP = "//li[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'][contains(.,'" + nm + "')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
        System.out.println("GatewayDetails : the following item (Trust Certificate name) was selected: " + nm);
    }
}
