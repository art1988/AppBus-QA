package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

//User & Role Management >Navigation items --> Create New Item --> [Item Assignment Details]

public class ItemAssignmentDetails extends PageObject
{
    @FindBy(id = "itemDetailsDlgForm:itemTitle")
    private WebElement idField;

    @FindBy(xpath = "//input[@name='itemDetailsDlgForm:entitlement']")
    private WebElement entitlementField;

    @FindBy(xpath = "//input[@name='itemDetailsDlgForm:tags']")
    private WebElement tagsField;

    @FindBy(id = "itemDetailsDlgForm:itemControllerType_label")
    private WebElement archeTlist;

    @FindBy(id = "itemDetailsDlgForm:itemDisplayTitle")
    private WebElement displayTitleField;

    @FindBy(id = "itemDetailsDlgForm:itemDescription")
    private WebElement descriptionField;

    @FindBy(id = "itemDetailForm:saveItem")
    private WebElement addButton;

    @FindBy(id = "itemDetailsDlgForm:itemDetailsSaveButton")
    private WebElement saveButton;

    @FindBy(id = "itemDetailsDlgForm:itemDetailsCancelButton")
    private WebElement cancelButton;

    @FindBy(id = "itemDetailForm:itemAssignmentDetailsCreateNewItemButton")
    private WebElement createNewItemButton;

    @FindBy(id = "itemDetailForm:controllerItemPropertiesTable:controllerPoliciesAddButton")
    private WebElement addControllerPolicyButton;

    @FindBy(id = "itemDetailForm:navigationItemPropertiesTable:navigationPoliciesAddButton")
    private WebElement addNavigationPolicyButton;



    public ItemAssignmentDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#itemDetailForm\\\\:itemAssignmentDialog_title').text()").equals("Item Assignment Details") ||
                 ((JavascriptExecutor) driver).executeScript("return $('#itemDetailsDlgForm\\\\:itemDetailsDlg_title').text()").equals("Item Assignment Details") ||
                 ((JavascriptExecutor) driver).executeScript("return $('#itemDetailsDlgForm\\\\:itemDetailsDlg_title').text()").equals("Item Copy") );
    }

    public void setControllerType(String archetype) throws InterruptedException
    {
        // expand Controller type select - just to make sure that it is visible during test
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:itemControllerType_panel').css(\"top\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:itemControllerType_panel').css(\"left\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:itemControllerType_panel').css(\"display\", \"block\")");
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:itemControllerType_panel').css(\"z-index\", \"1041\")");

        Thread.sleep(3_000);

        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:itemControllerType_panel li:contains(\"" + archetype + "\")').click()");

        System.out.println(archetype + " was set as Controller type ");
    }

    public void setContext(String contextName) throws InterruptedException
    {
        // expand Contexts dropdown
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:contexts_panel').css(\"top\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:contexts_panel').css(\"left\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:contexts_panel').css(\"display\", \"block\")");
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:contexts_panel').css(\"z-index\", \"1041\")");

        Thread.sleep(3_000);

        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:contexts_panel li:contains(\"" + contextName + "\")').find(\"input\").click()");
    }

    public void setPropertyValue(String propertyName, String propertyValue) throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailsDlgForm\\\\:itemDetailsTable .ui-datatable-tablewrapper tbody td:contains(\"" + propertyName + "\")').next().find(\"input\").val(\"" + propertyValue + "\")");
        Thread.sleep(1_000);
    }

    public void setOverridePropertyValue(String policyName, String policyValue)
    {
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailForm\\\\:updateItem tbody td').filter(function() { return $(this).text() === '" + policyName + "'; }).next().find(\"input\").val(\"" + policyValue + "\")");
    }

    public void setId(String id)
    {
        idField.clear();
        idField.sendKeys(id);
    }

    public void setDisplayTitle(String displayTitle)
    {
        displayTitleField.clear();
        displayTitleField.sendKeys(displayTitle);
    }

    public void setDescription(String description)
    {
        descriptionField.clear();
        descriptionField.sendKeys(description);
    }

    public void clickAdd() throws InterruptedException
    {
        addButton.click();
        System.out.println("ItemAssignmentDetails : Add button was clicked");

        Thread.sleep(4_000);
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("ItemAssignmentDetails : Save button was clicked");
    }

    public void selectArchetype(String arcTname) throws InterruptedException
    {
        archeTlist.click();
        String xP = "//li[@data-label='" + arcTname + "']";
        Thread.sleep(1_000);
        driver.findElement(By.xpath(xP)).click();
        System.out.println("ItemAssignmentDetails : Archetype was choosen");
    }

    public void setEntitlement(String entitText) throws InterruptedException
    {
        entitlementField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(entitText);
        System.out.println("ItemAssignmentDetails : Entitlement was set");
    }

    public void setTags(String tagsText) throws InterruptedException
    {
        tagsField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(tagsText);
        System.out.println("ItemAssignmentDetails : Tags was set");
    }

    public void clickCancel()
    {
        cancelButton.click();
    }

    /**
     * Expand item folder in Item Assignment Details popup
     * @param itemFolder
     */
    public void expandItemFolder(String itemFolder)
    {
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailForm\\\\:defaultItemSelection li:contains(\"" + itemFolder + "\")').find(\"span\").eq(2).prev().click()");
    }

    /**
     * Select Item in Item Assignment Details popup
     * @param itemName ( help, folder, lock, etc. )
     */
    public void selectItem(String itemName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailForm\\\\:defaultItemSelection span:contains(\"" + itemName + "\")').find(\"span\")[2].click()");
    }

    public void clickOverrideCheckbox()
    {
        ((JavascriptExecutor) driver).executeScript("$('#itemDetailForm\\\\:overrideItem div').click()");
        System.out.println("Override checkbox was clicked");
    }

    public SelectPolicyOverride addControllerPolicy()
    {
        addControllerPolicyButton.click();
        System.out.println("ItemAssignmentDetails : Add Controller Policy button was clicked");

        return new SelectPolicyOverride(driver);
    }

    public SelectPolicyOverride addNavigationPolicy()
    {
        addNavigationPolicyButton.click();
        System.out.println("ItemAssignmentDetails : Add Navigation Policy button was clicked");

        return new SelectPolicyOverride(driver);
    }
}
