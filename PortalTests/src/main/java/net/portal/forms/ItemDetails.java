package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.util.ArrayList;
import java.util.List;

//User & Role Management > Navigation --> Navigation items --> Add New --> [Item Assignment Details]: Create New Item --> [Item Details]

public class ItemDetails extends PageObject
{
    @FindBy(id = "itemDetailsDlgForm:newItemParent")
    private WebElement parentItemField;

    @FindBy(id = "itemDetailsDlgForm:newItemTitle")
    private WebElement idField;

    @FindBy(id = "itemDetailsDlgForm:newContexts_label")
    private WebElement contextList;

    @FindBy(xpath = "//label[contains(.,'Description:')]")
    private WebElement descriptionField;

    @FindBy(xpath = "//label[contains(.,'Display title:')]")
    private WebElement displayTitleField;

    @FindBy(xpath = "//label[contains(.,'Entitlement:')]")
    private WebElement entitlementField;

    @FindBy(xpath = "//label[contains(.,'Tags:')]")
    private WebElement tagsField;

    @FindBy(xpath = "//span[contains(.,'Save')]")
    private WebElement saveButton;

    @FindBy(xpath = "//label[contains(.,'Navigation policies:')]")
    private WebElement navPoliciesLabel;

    public ItemDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return  ((JavascriptExecutor) driver).executeScript("return $('#newItemDetailsDlg_title').text()").equals("Item Details");
    }

    public void setParentItem(String parentItemID) throws InterruptedException
    {
        parentItemField.click();
        Thread.sleep(1_000);
        String xP = "//li[contains(@data-label,'" + parentItemID + "')]";
        Thread.sleep(1_000);
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
    }

    public void setIdField(String itemID) throws InterruptedException
    {
        idField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(itemID);
        Thread.sleep(1_000);
    }

    public void setDisplaytitleField(String itemTITLE) throws InterruptedException
    {
        displayTitleField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(itemTITLE);
        Thread.sleep(1_000);
    }

    public void setDescriptionField(String itemDSC) throws InterruptedException
    {
        descriptionField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(itemDSC);
        Thread.sleep(1_000);
    }

    public void setArchetype(String itemArchetype) throws InterruptedException
    {
        descriptionField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        String xP = "//li[contains(.,'" + itemArchetype + "')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
    }

    public void setEntitlementField(String itemEntitlement) throws InterruptedException
    {
        entitlementField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(itemEntitlement);
        Thread.sleep(1_000);
    }

    public void setContext(String context) throws InterruptedException
    {
        contextList.click();
        Thread.sleep(1_000);
        String xP = "//li[contains(.,'" + context + "')]";
        WebElement contextPanel = driver.findElement(By.id("itemDetailsDlgForm:newContexts_panel"));
        contextPanel.findElement(By.xpath(xP)).click();
        //        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
    }

    public void setTagsField(String tags) throws InterruptedException
    {
        tagsField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(tags);
        Thread.sleep(1_000);
    }

    public void clickSave() throws InterruptedException
    {
        boolean success = false;
        Thread.sleep(1_000);
        //navPoliciesLabel.click();

        List<WebElement> buttons = driver.findElements(By.tagName("button"));
        List<WebElement> buttonsActive = new ArrayList<WebElement>();
        Thread.sleep(1_00);
        System.out.println("ItemDetails : buttons.size() is : " + buttons.size());
        for(int i=0, j=0; i < buttons.size(); i++)
        {
            String disabled = buttons.get(i).getAttribute("aria-disabled");
            String innerHTML = buttons.get(i).getAttribute("innerHTML");
            String text = buttons.get(i).getText();
            //System.out.println("ItemDetails : detected button is : " + buttons.get(i).getText());
            //System.out.println("ItemDetails : detected button outerHTML is : " + buttons.get(i).getAttribute("innerHTML").toString());
            //System.out.println("ItemDetails : detected button aria-disabled is : " + buttons.get(i).getAttribute("aria-disabled").toString());
            if (disabled.contains("false") && innerHTML.contains("Save") && text.contains("Save"))
            {
                buttonsActive.add(j,buttons.get(i)); j++;
                System.out.println("ItemDetails : detected button is : " + buttons.get(i).getText());
                System.out.println("ItemDetails : detected button outerHTML is : " + buttons.get(i).getAttribute("innerHTML").toString());
                System.out.println("ItemDetails : detected button aria-disabled is : " + buttons.get(i).getAttribute("aria-disabled").toString());
                //buttons.get(i).click(); //it doesn't work at -DheadlessRun="true"
                break;
            }

        }
        Thread.sleep(1_00);
        if (buttonsActive.size()==1)
        {
            String id = buttonsActive.get(0).getAttribute("id");
            id = id.replaceAll("[:]", "\\\\\\\\:");
            System.out.println("ItemDetails : buttonsActive.get(0).getAttribute(\"id\") : " + id);
            System.out.println("ItemDetails : will set the focus() in 2 secs... ");
            Thread.sleep(2_000);
            ((JavascriptExecutor) driver).executeScript("$('#"+ id + "').focus()");
            System.out.println("ItemDetails : just set the focus(), waiting for 1 sec... ");
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            System.out.println("ItemDetails : just pressed SPACE, waiting for 1 sec... ");
            Thread.sleep(1_000);
            //((JavascriptExecutor) driver).executeScript("$('#"+ id + "').click()");
            //buttonsActive.get(0).click(); //it doesn't work at -DheadlessRun="true"
            success = true;
        }

        System.out.println("ItemDetails : Save button's just been clicked : " + success);

    }

    public WebElement getSaveButton() throws InterruptedException
    {
        Thread.sleep(1_000);
        WebElement save = driver.findElement(By.xpath("//span[contains(.,'Save')]"));
        Thread.sleep(1_000);
        return save;
    }


}
