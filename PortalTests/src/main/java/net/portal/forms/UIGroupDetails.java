package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.security.KeyPair;

public class UIGroupDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:title")
    private WebElement titleField;

    @FindBy(id = "entity:dialogsForm:description")
    private WebElement descriptionField;

    @FindBy(id = "entity:dialogsForm:propertyValuesTable:defaultPolicyValueAddButon")
    private WebElement addPolicyButton;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "groupDetailForm:saveGroup")
    private WebElement saveButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;

    @FindBy(xpath = "//div[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default ui-state-hover']/span[@class='ui-chkbox-icon ui-icon ui-icon-blank ui-c']")
    private WebElement mainFlag;

    @FindBy(xpath = "//*[@id='entity:dialogsForm:propertyValuesTable:defaultPolicyValueDeleteButon']/span[1 and @class='ui-button-icon-left ui-icon ui-c button-delete-class']")
    private WebElement deleteButton;

    @FindBy(xpath = "//*[text()='Yes']") //"Sure to delete ?" pop up
    private WebElement yesButton;

    @FindBy(xpath = "//*[text()='UI Group:']")
    private WebElement uiGroupLabel;

    @FindBy(xpath = "//*[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-icon-left ui-state-hover']/*[@class='ui-button-text ui-c']")
    private WebElement OkButtonOfPopup;

    @FindBy(id = "groupDetailForm:groupNavigationParameters:0:groupDetailEditValue")
    private WebElement editUIbutton;

    @FindBy(id = "multipleValuesDlg_title")
    private WebElement multiValuesHead;

    @FindBy(id = "groupDetailDialog_title")
    private WebElement uiGRPdetailsHead;

    public UIGroupDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("UI Group Details") ||
                 ((JavascriptExecutor) driver).executeScript("return $('#groupDetailDialog_title').text()").equals("UI Group Details") );
    }

    public void setTitle(String title)
    {
        titleField.clear();
        titleField.sendKeys(title);
    }

    public void setDescription(String dcs)
    {
        descriptionField.clear();
        descriptionField.sendKeys(dcs);
    }

    public SelectPolicy clickAddProperty()
    {
        addPolicyButton.click();
        System.out.println("GroupDetails : Add policy was clicked");

        return new SelectPolicy(driver);
    }

    public void selectGroup(String groupName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#groupDetailForm\\\\:selectUIGroupPanel_content .ui-icon-triangle-1-s').click()"); // Expand dropdown

        ((JavascriptExecutor) driver).executeScript("$('#groupDetailForm\\\\:group-name_items li:contains(\"" + groupName + "\")').click()");

        System.out.println(groupName + " group was selected");
    }

    public void selectUIgroup(String grpName) throws InterruptedException
    {
        uiGroupLabel.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        // //li[text()='uiGRPauto012019.03.25.10.50.03']
        driver.switchTo().activeElement().findElement(By.xpath("//li[text()='" + grpName + "']")).click();
    }

    public void clickEditUIbutton()
    {
        editUIbutton.click();

    }

    public void clickMultiValueAdd() throws InterruptedException {
        multiValuesHead.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
    }

    public void clickMultiValueOk() throws InterruptedException
    {
        OkButtonOfPopup.click();
    }

    public void addTwoValues(String str01, String str02) throws InterruptedException
    {
        multiValuesHead.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(str01);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(str02);
    }

    public WebElement getOkButtonOfPopup() throws InterruptedException
    {
        multiValuesHead.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);

        return driver.switchTo().activeElement().findElement(By.xpath("//*[text()='Ok']"));

    }

    public void addSingleValue(String str) throws InterruptedException
    {
        uiGRPdetailsHead.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(str);
    }

    public void clickUIgrpDetailsSave() throws InterruptedException {
        Thread.sleep(1_000);
        uiGRPdetailsHead.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("GroupDetails : Add was clicked");
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("GroupDetails : Save was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("GroupDetails : Cancel was clicked");
    }

    public void clickDelete()
    {
        deleteButton.click();
        System.out.println("GroupDetails : Delete was clicked");
    }

    public void clickYes()
    {
        yesButton.click();
        System.out.println("GroupDetails : Yes was clicked");
    }

    public void clickMainFlag() throws InterruptedException //select all groups
    {
        descriptionField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        System.out.println("GroupDetails : main Flag was clicked (selecting all og groups)");
    }

    public WebElement getFlagByPolName(String polName) throws InterruptedException
    {

        // //span[@class='ui-chkbox-icon ui-icon ui-c ui-icon-check']

        driver.findElement(By.xpath("//span[text()='" + polName + "']")).click();
        Thread.sleep(1_000);
        WebElement tempFlag = driver.findElement(By.xpath("//span[@class='ui-chkbox-icon ui-icon ui-c ui-icon-check']"));

        System.out.println("UIGroupDetails : got the WebElement that is flag of the " + polName + "UI Group");

        return (tempFlag);
    }
}
