package net.portal.pages.pool_management;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RdpDetails;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class VDIs extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonDeleteTop")
    private WebElement deleteButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonReloadTop")
    private WebElement refreshButton;


    public VDIs(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Pool Management > VDIs") );
    }

    public RdpDetails addVDI()
    {
        addNewButton.click();
        System.out.println("VDIs : Add New button was clicked");

        return new RdpDetails(driver);
    }

    public void clickRefresh()
    {
        refreshButton.click();
        System.out.println("VDIs : Refresh button was clicked");
    }

    public FollowingItemsWillBeDeleted clickDelete()
    {
        deleteButton.click();
        System.out.println("VDIs : Delete button was clicked");

        return new FollowingItemsWillBeDeleted(driver);
    }

    /**
     * Click edit button for VDI by name
     * @param vdiName Computer name
     * @return
     */
    public RdpDetails editVDI(String vdiName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data td:contains(\"" + vdiName + "\")').next().next().next().next().find(\"button\").click()");

        return new RdpDetails(driver);
    }

    public void clickSelectAllCheckbox()
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_head .ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c')[0].click()");

        System.out.println("VDIs : Select All Checkbox was checked");
    }
}
