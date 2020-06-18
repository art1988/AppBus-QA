package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.util.List;

public class ServiceDetails extends PageObject
{
    JavascriptExecutor js = (JavascriptExecutor)driver;

    @FindBy(id = "serviceDlgForm:serviceDlgSaveButton")
    private WebElement saveButton;

    @FindBy(id = "serviceDlgForm:serviceDlgCancelButton")
    private WebElement cancelButton;

    @FindBy(id = "serviceDlgForm:serviceDlgName")
    private WebElement serviceNameInput;

    @FindBy(id = "serviceDlgForm:serviceDlgGatewaySelect_label")
    private WebElement gatewayField;

    @FindBy(id = "serviceDlgForm:serviceDlgGatewaySelect_1")
    private WebElement gatewayListItem01;

    @FindBy(id = "serviceDlgForm:serviceDlgValuesTable:serviceDlgValuesTableAddButton")
    private WebElement addPolicyButton;

    @FindBy(id = "serviceDlgForm:serviceDlgValuesTable:0:serviceDlgValuesTableRemoveButton")
    private WebElement theFirstValueDeleteButton;

    @FindBy(id = "serviceDlgForm:serviceDlgGatewaySelect_items")
    private WebElement gatewayNamesList;

    @FindBy(id = "serviceDlgForm:serviceDlgValuesTable_data")
    private WebElement serviceValuesTable;


    public ServiceDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#serviceDlg_title').text()").equals("Service details"));
    }

    public void setGatewayTheFirstItem() throws InterruptedException
    {
        String xP = "//label[contains(.,'---- Select gateway ----')]";
        driver.findElement(By.xpath(xP)).click();
        //gatewayField.click();
        //js.executeScript("return $('#serviceDlgForm\\\\:serviceDlgGatewaySelect').click()");
        //Thread.sleep(2_000);
        //driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(2_000);
        js.executeScript("return $('#serviceDlgForm\\\\:serviceDlgGatewaySelect_1').click()");
        Thread.sleep(2_000);
        //driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        //gatewayListItem01.click();
        System.out.println("ServiceDetails : the first gateway item was selected");
    }

    public void setGatewayByName(String nm) throws InterruptedException
    {
        String xP = "//label[contains(.,'---- Select gateway ----')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(2_000);
        xP = "//li[contains(.,'" + nm + "')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(2_000);
        //driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        //gatewayListItem01.click();
        System.out.println("ServiceDetails : the following gateway item was selected: " + nm);
    }

    public String getGatewayName() throws InterruptedException
    {
        String gn = gatewayField.getText();
        System.out.println("ServiceDetails : the following gateway name was detected: " + gn);

        return gn;
    }

    public void clickSave() throws InterruptedException
    {
        saveButton.click();
        Thread.sleep(1_000);
        System.out.println("ServiceDetails : Save button was clicked");
    }

    public AddPolicy clickAddPolicy() throws InterruptedException
    {
        addPolicyButton.click();
        Thread.sleep(1_000);
        System.out.println("ServiceDetails : Add Policy was clicked");

        return new AddPolicy(driver);
    }

    public void clickCancel() throws InterruptedException
    {
        cancelButton.click();
        Thread.sleep(1_000);
        System.out.println("ServiceDetails : Cancel button was clicked");
    }

    public void inputServiceName(String nm) throws InterruptedException
    {
        serviceNameInput.clear();
        Thread.sleep(1_000);
        serviceNameInput.sendKeys(nm);
        System.out.println("ServiceDetails : Service name (" + nm + ") was set");
    }

    public String getServiceName() throws InterruptedException
    {
        String sn = js.executeScript("return $('#serviceDlgForm\\\\:serviceDlgName').text()").toString();
        //String sn = serviceNameInput.getText();
        Thread.sleep(1_000);
        System.out.println("ServiceDetails : Service name is " + sn);

        return sn;
    }

    public String getPolicyParms() throws InterruptedException
    {
        String svt = serviceValuesTable.getText();
        Thread.sleep(1_000);
        System.out.println("ServiceDetails : serviceValuesTable name is " + svt);

        return svt;
    }

    public void setGatewayName(String gname) throws InterruptedException
    {
        gatewayField.click();
        Thread.sleep(1_000);
        //serviceNameInput.sendKeys(nm);
        System.out.println("ServiceDetails : Service name (" + gname + ") was set");
    }

    public String setLastGatewayItem() throws InterruptedException
    {
        gatewayField.click();
        Thread.sleep(1_000);
        List <WebElement> items = gatewayNamesList.findElements(By.tagName("li"));
        String gateName = items.get(items.size()-1).getText();
        items.get(items.size()-1).click();
        System.out.println("ServiceDetails : Gateway name (" + gateName + ") was set");

        return gateName;
    }

    public void setFocusOnGatewayField() throws InterruptedException
    {
        gatewayField.click();
        Thread.sleep(1_000);
        gatewayField.click();
        System.out.println("ServiceDetails : setFocusOnGatewayField() method completed its work");
    }

    public boolean deleteTheFirstValue() throws InterruptedException
    {

            if (serviceValuesTable.getText().contains("No records found."))
            {
                System.out.println("ServiceDetails : theFirstValueDeleteButton was not clicked");
                return false;
            }
            else {
                theFirstValueDeleteButton.click();
                System.out.println("ServiceDetails : theFirstValueDeleteButton was clicked");
                return true;
            }

    }
}
