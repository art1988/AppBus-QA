package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class RoleDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:name")
    private WebElement roleNameFiled;

    // Add button if 'Add New' was clicked
    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    // Save button if 'Edit' was clicked
    @FindBy(id = "entity:dialogsForm:saveEntity")
    private WebElement saveButton;

    @FindBy(id = "entity:dialogsForm:role-upload_input")
    private WebElement chooseField;

    @FindBy(className = "ui-fileupload-upload")
    private WebElement uploadButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;


    public RoleDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Role Detail") );
    }

    public void setRoleName(String roleName)
    {
        roleNameFiled.clear();
        roleNameFiled.sendKeys(roleName);
    }

    /**
     * Expands single role node
     * @param roleNode name of role node
     */
    public void expandRoleNode(String roleNode) throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:role-permissions-tree span:contains(\"" + roleNode + "\")').prev().prev().prev().click()");
        Thread.sleep(2_000);
        System.out.println("RoleDetail : " + roleNode + " was expanded...");
    }

    public void selectRole(String roleName) throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('.ui-treenode-label.ui-corner-all:contains(\"" + roleName + "\")').click()");
        Thread.sleep(2_000);
        System.out.println("RoleDetail : " + roleName + " was selected...");
    }

    /**
     * Set value for Role landing permission dropdown.
     * Note: there is no animation for selection on web page but after clicking Save - it will save selected value
     * @param landingPermission capitalized value
     */
    public void setRoleLandingPermission(String landingPermission)
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:role-landingPermission_input').val(\"" + landingPermission + "\")");
    }

    public void clickAdd()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:addEntity').click()");

        System.out.println("RoleDetail : Add button was clicked");
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("RoleDetail : Save button was clicked");
    }

    public void chooseFile(String fullPathToFile)
    {
        chooseField.sendKeys(fullPathToFile);
    }

    public void clickUpload()
    {
        uploadButton.click();
        System.out.println("RoleDetail: Upload was clicked");
    }

    public void clickCancel()
    {
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:cancelEntity').click()");

        System.out.println("RoleDetail: Cancel was clicked");
    }
}
