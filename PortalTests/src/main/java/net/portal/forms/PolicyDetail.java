package net.portal.forms;

import net.portal.pages.DeleteConfirmPopup;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class PolicyDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:name")
    private WebElement nameField;

    @FindBy(id = "entity:dialogsForm:description")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:itemPropertiesTable:addItemPropertyBtn")
    private WebElement addItemPropertyButton;

    @FindBy(id = "entity:dialogsForm:itemPropertiesTable:deleteItemPropertyBtn")
    private WebElement deleteItemPropertyButton;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addPropertyButton; // in case if Add New button was clicked

    @FindBy(id = "entity:dialogsForm:saveEntity")
    private WebElement savePropertyButton; // in case if Edit button was clicked

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;

    private int itemPropertyIndex;


    public PolicyDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
        // TODO: if click edit of existing -> then need to init itemPropertyIndex
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Policy Detail") );
    }

    public void setName(String name)
    {
        nameField.clear();
        nameField.sendKeys(name);
    }

    public void setDescription(String description)
    {
        descriptionField.clear();
        descriptionField.sendKeys(description);
    }

    /**
     * Checks Item checkbox
     * @throws InterruptedException
     */
    public void checkItem() throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:navigationItem span').click()");
        System.out.println("PropertyDetail : Item checkbox was clicked");

        Thread.sleep(2_000);
    }

    /**
     * Checks Group checkbox
     * @throws InterruptedException
     */
    public void checkGroup() throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:navigationGroup_input').click()");
        System.out.println("PropertyDetail : Group checkbox was clicked");

        Thread.sleep(2_000);
    }

    public void checkGroupRequired() throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:navigationGroupRequired_input').click()");
        System.out.println("PropertyDetail : Group required checkbox was clicked");

        Thread.sleep(1_000);
    }

    public void checkGroupMultiple() throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:navigationMultipleGroup_input').click()");
        System.out.println("PropertyDetail : Group required checkbox was clicked");

        Thread.sleep(1_000);
    }

    public void checkDevice() throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:device span').click()");
        System.out.println("PropertyDetail : Device checkbox was clicked");

        Thread.sleep(1_000);
    }

    public void checkDeviceMultiple()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:deviceMultiple span').click()");
        System.out.println("PropertyDetail : Device multiple checkbox was clicked");
    }

    public void checkProvision()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:provision span').click()");
        System.out.println("PropertyDetail : Provision checkbox was clicked");
    }

    public void checkProvisionService()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:provisionService span').click()");
        System.out.println("PropertyDetail : Provision service checkbox was clicked");
    }

    public void addItemProperty(String archetypeName, String parameterGroup, boolean isRequired, boolean isMultiple) throws InterruptedException
    {
        addItemPropertyButton.click();

        Thread.sleep(1_000);

        // show Controller type dropdown
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:controllerTypeDropdownAdd_panel').css(\"display\", \"block\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:controllerTypeDropdownAdd_panel').css(\"top\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:controllerTypeDropdownAdd_panel').css(\"left\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:controllerTypeDropdownAdd_panel').css(\"z-index\", \"1041\")");

        Thread.sleep(3_000);

        // Select Controller type (archetype)
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:controllerTypeDropdownAdd_panel li:contains(\"" + archetypeName + "\")').click()");

        // show Parameter group dropdown
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:paramterGroupDropdownAdd_panel').css(\"display\", \"block\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:paramterGroupDropdownAdd_panel').css(\"top\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:paramterGroupDropdownAdd_panel').css(\"left\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:paramterGroupDropdownAdd_panel').css(\"z-index\", \"1041\")");

        // Select parameter group
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:paramterGroupDropdownAdd_panel li:contains(\"" + parameterGroup + "\")').click()");

        if(isRequired)
        {
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            //((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:j_idt155_input').click()");

        }

        if(isMultiple)
        {
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            //((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable\\\\:" + itemPropertyIndex + "\\\\:j_idt156_input').click()");
        }

        itemPropertyIndex++;
    }

    public void setType(String type)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:type .ui-icon-triangle-1-s').click()"); // expand dropdown

        ((JavascriptExecutor) driver).executeScript("$(\"#entity\\\\:dialogsForm\\\\:type_items li:contains('" + type + "')\").click()");
    }

    public DeleteConfirmPopup deleteItemProperty()
    {
        deleteItemPropertyButton.click();

        return new DeleteConfirmPopup(driver);
    }

    public void selectAllItemProperties()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:itemPropertiesTable table').find('input').eq(0).click()");
    }

    public void clickAdd()
    {
        addPropertyButton.click();

        System.out.println("PolicyDetail : Add button was clicked");
    }

    public void clickSave()
    {
        savePropertyButton.click();

        System.out.println("PolicyDetail : Save property button was clicked");
    }

    public void clickCancel()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:cancelEntity').click()");

        System.out.println("PolicyDetail : Cancel button was clicked");
    }
}
