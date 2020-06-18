package net.portal.pages.portal_administration;

import net.portal.forms.DeleteFollowingUsers;
import net.portal.forms.UserDetail;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.util.List;

public class Users extends PageObject
{
    @FindBy(id = "table:tableForm:entityTable:userNameColumn:filter")
    private WebElement userNameSearchField;

    @FindBy(xpath = "//span[contains(.,'User Name')]")
    private WebElement userNameSearchFieldByXpath;

    @FindBy(id = "table:tableForm:entityTable:firstNameColumn:filter")
    private WebElement firstNameSearchField;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewUserButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteUserButton;

    @FindBy(id = "table:tableForm:entityTable:0:edit") //the first row button, filter one user before click
    private WebElement editUserButton;

    @FindBy(xpath = "//div[contains(@class,'ui-datatable-header ui-widget-header ui-corner-top')]")
    private WebElement usersLabel;

    @FindBy(xpath = "//label[contains(.,'UniqueName')]") //(//label[contains(.,'UniqueName')])[2]
    private WebElement uniqueNameItem;

    @FindBy(xpath = "//div[@class='ui-selectcheckboxmenu-items-wrapper']/ul") //9 "//div[@class='ui-selectcheckboxmenu-items-wrapper']/ul/li[3]"
    private WebElement uniqueNameSquare;

    @FindBy(xpath = "//span[@class='ui-button-icon-left ui-icon ui-c button-accept-class']")
    //span[class()='ui-button-text ui-c'][contains(.,'Accept')]
    private WebElement acceptIcon;


    public Users(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Portal administration > Users") );
    }

    public UserDetail addNewUser()
    {
        addNewUserButton.click();
        System.out.println("Add new User was clicked");

        return new UserDetail(driver);
    }

    public DeleteFollowingUsers deleteUser()
    {
        deleteUserButton.click();
        System.out.println("Delete User was clicked");

        return new DeleteFollowingUsers(driver);
    }

    public void editUserButton() throws InterruptedException
    {
        //editUserButton.click();
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable\\\\:0\\\\:edit').click()");
        /*
        String xP = "//th[contains(.,'User permissions')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
         */
        System.out.println("Edit User was clicked");

    }

    public void clickUniqueNameItem() throws InterruptedException
    {

        //uniqueNameSquare.click(); //9
        Thread.sleep(1_000);
        //uniqueNameSquare.click();
        Thread.sleep(1_000);
        WebElement tmp = uniqueNameSquare.findElement(By.xpath("//*[@role='group']"));
        //System.out.println("tmp.getText() is : " + tmp.getText());
        List <WebElement> items = tmp.findElements(By.className("ui-chkbox"));
        System.out.println("size of items is " + items.size());

        int itemNumber = 0;
        for(int i=0; i < items.size(); i++)
        {
            if (items.get(i).toString().contains("UniqueName")) itemNumber = i;
            //else System.out.println("items.get(i).toString(): " + items.get(i).toString());
        }

        if (items.get(itemNumber).toString().contains("UniqueName"))
        {
            items.get(itemNumber).click(); System.out.println("UniqueName item was clicked");
        }
        else
            {
                items.get(items.size()-1).click(); System.out.println("ATTENTION!: UniqueName item wasn't clicked, was clicked the : " + items.get(itemNumber).toString());
            }


    }

    public void clickElementByXpath(String x)
    {
        driver.findElement(By.xpath(x)).click();
        System.out.println(x + " item was clicked");

    }

    public void clickAcceptIcon()
    {
        acceptIcon.click();
        System.out.println("Accept icon was clicked");

    }

    public void selectkAllItems() throws InterruptedException
    {
        usersLabel.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        System.out.println("Select all items was clicked");

    }

    public void searchForUserName(String userName)
    {
        userNameSearchField.sendKeys(userName);
    }

    public void searchForUserNameByXpath(String userName) throws InterruptedException
    {
        userNameSearchFieldByXpath.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(userName);
    }

    public void searchForFirstName(String firstName)
    {
        firstNameSearchField.sendKeys(firstName);
    }

    public void clickSelectAllCheckbox()
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_head .ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c')[0].click()");

        System.out.println("Users : Select All Checkbox was checked");
    }
}
