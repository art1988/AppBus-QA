package net.portal.pages.user_and_role_management;

import net.portal.constants.Retries;
import net.portal.forms.ItemAssignmentDetails;
import net.portal.forms.MoveToRoot;
import net.portal.forms.SelectParentItem;
import net.portal.forms.UploadItem;
import net.portal.pages.DeleteNavigationItemPopup;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class NavigationItems extends PageObject
{
    @FindBy(id = "form:addNewItemButtonTop")
    private WebElement createNewItemButton;

    @FindBy(id = "form:reloadButtonTop")
    private WebElement refreshButton;

    @FindBy(id = "form:buttonNewJsonUploadWizard")
    private WebElement uploadItemButton;

    @FindBy(id = "form:idFilterInput")
    private WebElement idFilterField;

    @FindBy(xpath = "//span[contains(.,'ID')]")
    private WebElement idHeadOfColumn;




    public NavigationItems(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Navigation Items") );
    }

    public ItemAssignmentDetails addNavigationItem()
    {
        createNewItemButton.click();
        System.out.println("NavigationItems : Create New Item was clicked");

        return new ItemAssignmentDetails(driver);
    }

    /**
     * In case if Navigation Item has children it becomes link
     * @param id
     * @return the same page
     */
    public NavigationItems clickNavigationItemLink(String id)
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:table_data td a:contains(\"" + id + "\")').click()");

        return this;
    }

    /**
     * Click by ROOT link in breadcrumb
     * @return the same page
     */
    public NavigationItems clickROOTLink()
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:breadcrumb a:contains(\"ROOT\")').click()");

        return this;
    }

    public void searchForId(String navItemID)
    {
        idFilterField.clear();
        idFilterField.sendKeys(navItemID);
    }

    public void clickRefresh()
    {
        Retries.RETRY_50_TIMES.run(() -> refreshButton.click()); //Retry
        System.out.println("NavigationItems : Refresh button was clicked");
    }

    public UploadItem clickUploadItem()
    {
        uploadItemButton.click();
        System.out.println("NavigationItems : Upload Item button was clicked");

        return new UploadItem(driver);
    }

    /**
     * Make copy of navigationItemId
     * @param navigationItemId
     * @return
     */
    public ItemAssignmentDetails copyNavigationItem(String navigationItemId)
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:table_data tr td:contains(\"" + navigationItemId + "\")').next().find(\"button\")[6].click()");
        System.out.println("Copy of " + navigationItemId);

        return new ItemAssignmentDetails(driver);
    }

    public void downloadJsonFile(String navigationItemId)
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:table_data tr td:contains(\"" + navigationItemId + "\")').next().find(\"button\")[5].click()");
        System.out.println("Download JSON file for : " + navigationItemId);
    }

    public SelectParentItem moveToAnotherItemAsChild(String navigationItemId)
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:table_data tr td:contains(\"" + navigationItemId + "\")').next().find(\"button\")[3].click()");
        System.out.println("Move to another item as child was clicked for : " + navigationItemId);

        return new SelectParentItem(driver);
    }

    public MoveToRoot moveToTheRootLevel(String navigationItemId)
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:table_data tr td:contains(\"" + navigationItemId + "\")').next().find(\"button\")[4].click()");
        System.out.println("Move to the root level was clicked for : " + navigationItemId);

        return new MoveToRoot(driver);
    }

    public DeleteNavigationItemPopup deleteNavigationItem(String navigationItemId)
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:table_data tr td:contains(\"" + navigationItemId + "\")').next().find(\"button\")[2].click()");
        System.out.println("Delete the following nav. item : " + navigationItemId);

        return new DeleteNavigationItemPopup(driver);
    }

    public ItemAssignmentDetails clickAddChildNavigationItemIcon() throws InterruptedException
    {
        idHeadOfColumn.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000); ////button[contains(.,'addChildItemForDirectButton')]
        //System.out.println("Icon id is: " + driver.switchTo().activeElement().getAttribute("id"));
        if (driver.switchTo().activeElement().getAttribute("id").contains("addChildItemForDirectButton")) {}
        else { driver.switchTo().activeElement().sendKeys(Keys.TAB); }
        Thread.sleep(1_000);
        //System.out.println("Icon id is: " + driver.switchTo().activeElement().getAttribute("id"));
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);

        System.out.println("NavigationItems : Add New Child Item Icon was clicked");

        return new ItemAssignmentDetails(driver);
    }


}
