package net.portal.pages.device_management;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

import java.util.List;

public class UserDevices extends PageObject
{
    @FindBy(linkText = "Find Devices")
    private WebElement findDevicesSheet;

    @FindBy(linkText = "Review Wipe-List")
    private WebElement reviewWipeListSheet;

    @FindBy(xpath = "//a[contains(.,'OS Versions')]")
    private WebElement osVersionsSheet;

    @FindBy(id = "form:tabs:user") //input[@name='form:tabs:user_editableInput']
    private WebElement userInputField;

    @FindBy(id = "form:tabs:user_panel") //input[@name='form:tabs:user_editableInput']
    private WebElement userInputList;

    @FindBy(xpath = "//li[@data-label='edapt-setup']")
    private WebElement edaptSetupItem;

    @FindBy(id = "form:tabs:lookupButton")
    private WebElement lookupButton;

    @FindBy(id = "form:tabs:applyButton")
    private WebElement applyButton;

    @FindBy(id = "form:tabs:osTypeFilter_label")
    private WebElement osTypeLabel;

    @FindBy(id = "form:tabs:osTypeFilter_items")
    private WebElement osTypeItems;

    @FindBy(id = "form:tabs:dataTable")
    private WebElement deviceTable;

    @FindBy(id = "form:tabs:dataTable_data")
    private WebElement deviceTableRows;

    @FindBy(id = "form:tabs:startDateFilter_input")
    private WebElement startDateField;


    public UserDevices(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Device management > User Devices") );
    }

    public void selectUnactiveMainCheckBox() throws InterruptedException
    {
        WebElement cell = driver.findElement(By.id("form:tabs:dataTable:selectAll"));
        Thread.sleep(1_000);
        cell.findElement(By.xpath("//div[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default']")).click();
        Thread.sleep(1_000);
        System.out.println("UserDevices : MainCheckBox was clicked...");
    }

    public void setStartDate(String date) throws InterruptedException
    {
        startDateField.click();
        Thread.sleep(1_000);
        startDateField.clear();
        Thread.sleep(1_000);
        startDateField.sendKeys(date);
        Thread.sleep(1_000);
        System.out.println("UserDevices : setStartDate : date was entered...");
        applyButton.click();
        Thread.sleep(1_000);
        System.out.println("UserDevices : setStartDate : Apply button was clicked...");
    }

    public void selectMainCheckBox() throws InterruptedException
    {
        WebElement row = driver.findElement(By.id("form:tabs:dataTable_head"));
        Thread.sleep(1_000);
        row.findElement(By.xpath("//th/div[*]")).click();
        Thread.sleep(1_000);
        System.out.println("UserDevices : MainCheckBox was clicked...");
    }

    public boolean countSelectedRows() throws InterruptedException
    {

        Thread.sleep(1_000);
        //List<WebElement> items = deviceTableRows.findElements(By.xpath("//tr[contains(@class,'ui-widget-content ui-datatable-odd ui-datatable-selectable') || contains(@class,'ui-widget-content ui-datatable-odd ui-datatable-selectable ui-state-hover')]"));
        List<WebElement> items = deviceTableRows.findElements(By.xpath("//tr[contains(@data-ri,*)]"));
        System.out.println("UserDevices : countSelectedRows : Size of items is " + items.size());

        int itemNumber = 0;
        boolean selectedAll = true;
        for(int i=0; i < items.size(); i++)
        {
            String selected = items.get(i).getAttribute("aria-selected").toString(); itemNumber ++;
            if (!selected.equals("true")) selectedAll = false;
            //System.out.println("UserDevices : items.get(i).selected : " + selected);
        }
        System.out.println("UserDevices : countSelectedRows : itemNumber is : " + itemNumber);
        return selectedAll;
    }

    public boolean countDeselectedRows() throws InterruptedException
    {

        Thread.sleep(1_000);
        //List<WebElement> items = deviceTableRows.findElements(By.xpath("//tr[contains(@class,'ui-widget-content ui-datatable-odd ui-datatable-selectable') || contains(@class,'ui-widget-content ui-datatable-odd ui-datatable-selectable ui-state-hover')]"));
        List<WebElement> items = deviceTableRows.findElements(By.xpath("//tr[contains(@data-ri,*)]"));
        System.out.println("UserDevices : countDeselectedRows : Size of items is " + items.size());

        int itemNumber = 0;
        boolean deselectedAll = true;
        for(int i=0; i < items.size(); i++)
        {
            String selected = items.get(i).getAttribute("aria-selected").toString(); itemNumber ++;
            if (!selected.equals("false")) deselectedAll = false;
            //System.out.println("UserDevices : items.get(i).selected : " + selected);
        }
        System.out.println("UserDevices : countDeselectedRows : itemNumber is : " + itemNumber);
        return deselectedAll;
    }

    public String getContentOfRow1() throws InterruptedException
    {

        Thread.sleep(1_000);
        List<WebElement> items = deviceTableRows.findElements(By.xpath("//tr[contains(@data-ri,*)]"));
        System.out.println("UserDevices : Size of items is " + items.size());
        String firstRow = items.get(0).getText();
        System.out.println("UserDevices : firstRow is : " + firstRow);
        return firstRow;
    }

    public boolean selectLastRow() throws InterruptedException
    {

        boolean success = false;
        Thread.sleep(1_000);
        List<WebElement> itemsmore = deviceTableRows.findElements(By.xpath("//tr[contains(@data-rk,*)]"));
        System.out.println("UserDevices : selectDeselectLastRow: Size of items is " + itemsmore.size());
        Thread.sleep(1_000);
        itemsmore.get(itemsmore.size()-1).click();
        Thread.sleep(1_000);
        String selected = itemsmore.get(itemsmore.size()-1).getAttribute("aria-selected").toString();
        System.out.println("UserDevices : selectDeselectLastRow: Selected after click is : " + selected);
        if (selected.equals("true")) success = true;
        return success;
    }

    public void deselectSelectedRow() throws InterruptedException
    {

        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[@class='ui-chkbox-icon ui-icon ui-c ui-icon-check']")).click();
        Thread.sleep(1_000);
        System.out.println("UserDevices : deselectSelectedRow: checkbox was unchecked");

    }

    public void clickOStypeLabel()
    {
        osTypeLabel.click();
        System.out.println("UserDevices : OS Type label was clicked...");
    }

    public void selectUser(String user) throws InterruptedException
    {
        userInputField.findElement(By.tagName("span")).click();
        System.out.println("UserDevices : User Field was clicked...");
        Thread.sleep(1_000);
        String xP = "//li[@data-label='" + user + "']";
        userInputList.findElement(By.xpath(xP)).click();
        System.out.println("UserDevices : User " + user + " was selected...");
        Thread.sleep(1_000);
        lookupButton.click();
        Thread.sleep(1_000);
    }

    public void selectOStype(String os) throws InterruptedException
    {
        osTypeLabel.click();
        Thread.sleep(1_000);
        System.out.println("UserDevices : OS Type label was clicked...");
        Thread.sleep(1_000);
        String xP = "//li[@data-label='" + os + "']";
        osTypeItems.findElement(By.xpath(xP)).click();
        System.out.println("UserDevices : OS item was clicked... : " + os);
        Thread.sleep(1_000);
        applyButton.click();
        System.out.println("UserDevices : Apply button was clicked... : " + os);

    }

    public void clickFindDevicesSheet()
    {
        findDevicesSheet.click();
        System.out.println("UserDevices : Find Devices Sheet was clicked...");
    }

    public boolean ifFindDevicesSheetSelected()
    {
        boolean active = false;
        if (lookupButton.isDisplayed()) active = true;
        System.out.println("findDevicesSheet is selected : " + active);
        return active;
    }

    public void clickReviewWipeListSheet()
    {
        reviewWipeListSheet.click();
        System.out.println("UserDevices : Review Wipe List Sheet was clicked...");
    }

    public void clickOSversionsSheet()
    {
        osVersionsSheet.click();
        System.out.println("UserDevices : OS Versions Sheet was clicked...");
    }

    //old methods are below:

    public void clickFindDevicesTab()
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-tabs-nav li')[0].click()");

        System.out.println("Find Devices tab was clicked...");
    }

    public void clickReviewWipeListTab()
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-tabs-nav li')[1].click()");

        System.out.println("Review Wipe-List tab was clicked...");
    }

    public void clickOSVersionsTab()
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-tabs-nav li')[2].click()");

        System.out.println("OS Versions tab was clicked...");
    }

    public void selectOSType(String osType)
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:tabs\\\\:console label').click()");

        // select
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:tabs\\\\:console_items li:contains(\"" + osType + "\")').click()");
    }

}
