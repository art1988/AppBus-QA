package net.portal.forms;

import net.portal.constants.Retries;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.security.KeyPair;

//User & Role Management > Navigation --> Navigation items --> Add New --> [Item Assignment Details]

public class NavTreeItemAssignmentDetails extends PageObject

{
    @FindBy(xpath = "//span[contains(.,'Item Assignment Details')]")
    private WebElement popWindowHead;

    @FindBy(id = "itemDetailForm:saveItem")
    private WebElement addItemButton;

    @FindBy(id = "itemDetailForm:itemAssignmentDetailsCancelButton")
    private WebElement cancelButton;

    @FindBy(xpath = "//span[@class='ui-button-text ui-c'][contains(.,'Create New Item')]")
    private WebElement createNewItemButtonByXp;

    @FindBy(id = "itemDetailForm:itemAssignmentDetailsCreateNewItemButton")
    private WebElement createNewItemButton;

    //@FindBy(xpath = "//span[contains(@class,'ui-button-icon-left ui-icon ui-c button-view-class')]")
    @FindBy(xpath = "//span[@class='ui-button-icon-left ui-icon ui-c button-view-class']")
    private WebElement viewDataIcon;

    @FindBy(id = "itemDetailForm:controllerItemPropertiesTable_data")
    private WebElement tableOfButton;

    @FindBy(id = "itemDetailForm:itemAssignmentDialog")
    private WebElement wholePopWindow;

    @FindBy(id = "viewValueDlg")
    private WebElement viewValueDialogWindow;

    @FindBy(id = "itemDetailForm:defaultItemSelection:0")
    private WebElement itemList;

    @FindBy(id = "itemDetailForm:itemAssignmentDialog_title")
    private WebElement windowHeader;


    public NavTreeItemAssignmentDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return  ((JavascriptExecutor) driver).executeScript("return $('#itemDetailForm\\\\:itemAssignmentDialog_title').text()").equals("Item Assignment Details");
    }

    public void selectChildNvgItem(String parentItemName, String childItemName, boolean addJSON, boolean override) throws InterruptedException
    {
        popWindowHead.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().clear();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(childItemName);
        Thread.sleep(2_000);
        String xP = "//span[@style='cursor: pointer;'][contains(.,'" + parentItemName + "')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
        //xP = "//span[@class='ui-treenode-label ui-corner-all ui-state-hover'][contains(.,'" + childItemName + "')]";
        //driver.findElement(By.xpath(xP)).click();

        this.selectNvgItem(childItemName, addJSON, override);
    }

    public void selectNvgItem(String itemName, boolean addJSON) throws InterruptedException
    {
        this.selectNvgItem(itemName, addJSON, false);
    }

    public void selectNvgItem(String itemName, boolean addJSON, boolean override) throws InterruptedException
    {
        String json = "{\n" +
                "    \"glossary\": {\n" +
                "        \"title\": \"example glossary\"\n" +
                "    }\n" +
                "}";
        Thread.sleep(4_000);
        //String xP = "//span[contains(.,'" + itemName + "')]";
        //itemList.findElement(By.xpath(xP)).click();
        String JScode = "$('#itemDetailForm\\\\:defaultItemSelection').find(\"span:contains('REPLACE')\").click()";
        JScode = JScode.replace("REPLACE", itemName);
        System.out.println("JScode : " + JScode);
        ((JavascriptExecutor) driver).executeScript(JScode);

        Thread.sleep(1_000);

        if (override)
        {
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            System.out.println("windowHeader.getText() : " + windowHeader.getText());
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            Thread.sleep(1_000);
        }

        if (addJSON)
        {
            Thread.sleep(1_000);
            //ViewData vDataPop = this.clickViewDataIcon(); //doesn't work in -DheadlessRun="true" mode
            //vDataPop.setValue(json);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            Thread.sleep(2_000);
            driver.switchTo().activeElement().sendKeys(json);
            /*
            ViewData vDataPop = new ViewData (driver);
            vDataPop.sendTextToActiveField(json);
            */
            Thread.sleep(1_000);
            ViewData vDataPop = new ViewData (driver);
            Thread.sleep(1_000);
            if (override)
            {
                vDataPop.clickOk2();
                Thread.sleep(1_000);
            }
                else {
                        vDataPop.clickCancel();
                        Thread.sleep(1_000);
                        }

        }

    }

    public ViewData clickViewDataIcon(String itemName) throws InterruptedException
    {
                Thread.sleep(1_000);
                //Retries.RETRY_10_TIMES.run(() -> viewDataIcon.click()); //Retry
                String xP = "//span[contains(.,'" + itemName + "')]";
                itemList.findElement(By.xpath(xP)).click();
                Thread.sleep(1_000);
                driver.switchTo().activeElement().sendKeys(Keys.TAB);
                Thread.sleep(1_000);
                driver.switchTo().activeElement().sendKeys(Keys.TAB);
                Thread.sleep(1_000);
                driver.switchTo().activeElement().sendKeys(Keys.TAB);
                Thread.sleep(1_000);
                System.out.println("driver.findElement(By.id(\"itemDetailForm:controllerItemPropertiesTable_data\")).getText()" + driver.findElement(By.id("itemDetailForm:controllerItemPropertiesTable_data")).getText());
                driver.switchTo().activeElement().sendKeys(Keys.SPACE);
                Thread.sleep(1_000);
                //tableOfButton.findElement(By.tagName("button")).click();
                Thread.sleep(1_000);
                return new ViewData (driver);
    }

    public void clickAddItemButton() throws InterruptedException
    {
        addItemButton.click();
    }

    public void clickCancelButton() throws InterruptedException
    {
        cancelButton.click();
    }

    public ItemDetails clickCreateNewItem() throws InterruptedException
    {
        createNewItemButton.click();
        return new ItemDetails(driver);
    }

    public void selectItem(String itemName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailForm\\\\:defaultItemSelection li:contains(\"" + itemName + "\")').find(\"span\")[2].click()");
    }

}
