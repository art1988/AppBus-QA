package net.portal.pages.server_configuration;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.SettingDetails;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Settings extends PageObject
{
    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonDeleteTop")
    private WebElement deleteButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonReloadTop")
    private WebElement refreshButton;

    @FindBy(id = "settings:applyFiltersButton")
    private WebElement applyButton;

    @FindBy(id = "settings:restoreFiltersButton")
    private WebElement resetButton;


    public Settings(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Server Configuration > Settings") );
    }

    public SettingDetails addSetting()
    {
        addNewButton.click();
        System.out.println("Settings : Add New button was clicked");

        return new SettingDetails(driver);
    }

    public FollowingItemsWillBeDeleted clickDelete()
    {
        deleteButton.click();

        return new FollowingItemsWillBeDeleted(driver);
    }

    public void selectSetting(String settingName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + settingName + "\")').parent().prev().find(\"span\").click()");
        System.out.println("Setting : " + settingName + " was selected");
    }

    public void clickRefresh()
    {
        refreshButton.click();
    }

    public void selectGroup(String groupName) throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#settings\\\\:groupFilter_label').click()"); // expand Group dropdown
        Thread.sleep(1_000);
        ((JavascriptExecutor) driver).executeScript("$('#settings\\\\:groupFilter_items li:contains(\"" + groupName + "\")').click()"); // select Group
        Thread.sleep(500);

        applyButton.click();

        System.out.println("Settings Filter : Group with name = " + groupName + " was applied");

        Thread.sleep(1_000);
    }

    public void clickReset() throws InterruptedException
    {
        resetButton.click();
        Thread.sleep(2_000);

        System.out.println("Settings Filter : Reset was clicked");
    }

    /**
     * Edit setting by name = settingName and set new value = value
     * @param settingName name of setting to edit
     * @param value new value to set
     * @throws InterruptedException
     */
    public void editSetting(String settingName, String value) throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + settingName + "\")').parent().next().next().next().next().find(\"button\").click()");
        Thread.sleep(1_000);

        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data input:text').val(\"" + value + "\")");
        Thread.sleep(1_000);

        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data input:text').parent().next().next().find(\"button\")[0].click()"); // click accept button
    }
}
