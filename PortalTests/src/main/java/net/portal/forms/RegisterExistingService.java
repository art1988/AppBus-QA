package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class RegisterExistingService extends PageObject
{
    @FindBy(id = "addExistingServiceDlg_title")
    private WebElement winTitle;

    @FindBy(id = "addExistingServiceForm:addExistingServicePanel_content")
    private WebElement currentForm;

    @FindBy(id = "addExistingServiceForm:addServiceSaveButton")
    private WebElement saveServiceButton;

    @FindBy(id = "addExistingServiceForm:instancesTable:addItemPropertyBtn")
    private WebElement addInstanceButton;

    @FindBy(id = "addExistingServiceForm:produceTable:addProduceBtn")
    private WebElement addProducesButton;

    @FindBy(id = "addExistingServiceForm:pathTable:addPathBtn")
    private WebElement addPathParamsButton;

    @FindBy(id = "addExistingServiceForm:responseTable:addResponseBtn")
    private WebElement addResponsesButton;

    @FindBy(id = "addExistingServiceForm:consumes")
    private WebElement consumesField;

    @FindBy(id = "addExistingServiceForm:produceTable_data")
    private WebElement producesTable;

    @FindBy(id = "addExistingServiceForm:responseTable_data")
    private WebElement responsesTable;

    @FindBy(xpath = "//tr/td/span[contains(.,'Name:')]/../../td/input")
    private WebElement nameField;

    @FindBy(xpath = "//tr/td[contains(.,'Trigger:')]/..")
    private WebElement triggerFieldTR;

    @FindBy(xpath = "//tr/td[contains(.,'Description:')]/../td/input")
    private WebElement descriptionField;

    @FindBy(xpath = "//tr/td[contains(.,'HTTP method:')]/../td/div/div/span")
    private WebElement selectMethodDropDown;

    @FindBy(xpath = "//li[contains(@data-label,'GET')]")
    private WebElement getItem;

    @FindBy(xpath = "//tbody[contains(@id,'addExistingServiceForm:instancesTable_data')]/tr[contains(@data-ri,'0')]/td[1]/input")
    private WebElement theFirstRowURLfield;

    @FindBy(xpath = "//tbody[contains(@id,'addExistingServiceForm:instancesTable_data')]/tr[contains(@data-ri,'0')]/td/div/div[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default ui-state-active']")
    private WebElement theFirstCheck;

    @FindBy(xpath = "//tbody[contains(@id,'addExistingServiceForm:instancesTable_data')]/tr[contains(@data-ri,'0')]/td/input[@name='addExistingServiceForm:instancesTable:0:usernameColumnCell']")
    private WebElement theFirstRowUsernameField;

    public RegisterExistingService(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addExistingServiceDlg_title').text()").equals("Register existing service") );
    }

    public void clickAddInstance() throws InterruptedException
    {
        addInstanceButton.click();
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : Add Instance Button was clicked");
    }

    public void setName(String name) throws InterruptedException
    {
        Thread.sleep(3_000);
        nameField.clear();
        Thread.sleep(1_000);
        nameField.sendKeys(name);
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : Name field was set");
    }

    public void setConsumes(String mimeType) throws InterruptedException
    {
        consumesField.clear();
        Thread.sleep(1_000);
        consumesField.sendKeys(mimeType);
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : MIME Type was set");
    }

    public void setOneProduces(String produces) throws InterruptedException
    {
        addProducesButton.click();
        Thread.sleep(1_000);
        WebElement in = producesTable.findElement(By.tagName("input"));
        Thread.sleep(1_000);
        in.clear();
        Thread.sleep(1_000);
        in.sendKeys(produces);
        Thread.sleep(1_000);
        in.sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.PAGE_DOWN);
        System.out.println("RegisterExistingService : produces field (the first one) was set");
    }

    public void setOneResponsesCode(String code) throws InterruptedException
    {
        //driver.findElement(By.xpath("//td[contains(.,'Body example:')]/../td/textarea")).click();
        //addPathParamsButton.click();
        //Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        //Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        //Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        //Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        //addResponsesButton.click();
        ((JavascriptExecutor) driver).executeScript("$('#addExistingServiceForm\\\\:responseTable\\\\:addResponseBtn').click()");
        Thread.sleep(1_000);
        WebElement inp = driver.findElement(By.xpath("//tbody[@id='addExistingServiceForm:responseTable_data']/tr[@data-ri='0']/td[1]/input"));
        Thread.sleep(1_000);
        inp.clear();
        Thread.sleep(1_000);
        inp.sendKeys(code);
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : Responses code (the first one) was set");
    }

    public void setTriggerName(String tName) throws InterruptedException
    {
        Thread.sleep(3_000);
        nameField.click();
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(tName);
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : Trigger name field was set");
    }

    public void setDescription(String dsc) throws InterruptedException
    {
        Thread.sleep(3_000);
        descriptionField.clear();
        Thread.sleep(1_000);
        descriptionField.sendKeys(dsc);
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : Description field was set");
    }

    public void setGETmethod() throws InterruptedException
    {
        Thread.sleep(1_000);
        selectMethodDropDown.click();
        Thread.sleep(1_000);
        getItem.click();
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : GET method was set");
    }

    public void setURLfirstField(String url) throws InterruptedException
    {
        Thread.sleep(1_000);
        theFirstRowURLfield.clear();
        Thread.sleep(1_000);
        theFirstRowURLfield.sendKeys(url);
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : URL (of the first instance) was set");
    }

    public void clickCheckOfTheFirstRow() throws InterruptedException
    {
        Thread.sleep(1_000);
        theFirstCheck.click();
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : the check of the first instance was clicked");
    }

    public void setTheFirstUsernameField(String name, String domain) throws InterruptedException
    {
        Thread.sleep(1_000);
        theFirstRowUsernameField.clear();
        Thread.sleep(1_000);
        theFirstRowUsernameField.sendKeys(name);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().clear();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(domain);
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : Username and Domain (of the first instance) was set");
    }

    public void clickSaveButton() throws InterruptedException
    {
        Thread.sleep(1_000);
        ((JavascriptExecutor) driver).executeScript("$('#addExistingServiceForm\\\\:addServiceSaveButton').focus()");
        //saveServiceButton.click();
        ((JavascriptExecutor) driver).executeScript("$('#addExistingServiceForm\\\\:addServiceSaveButton').click()");
        Thread.sleep(1_000);
        System.out.println("RegisterExistingService : Save Service button was clicked");
    }

}
