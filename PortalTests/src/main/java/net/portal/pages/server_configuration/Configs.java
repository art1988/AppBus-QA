package net.portal.pages.server_configuration;

import net.portal.forms.ConfigDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RestorePreviousConfig;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;

public class Configs extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteButton;


    public Configs(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Server Configuration > Configs") );
    }

    public ConfigDetails addNewConfig()
    {
        addNewButton.click();
        System.out.println("Configs : Add New button was clicked");

        return new ConfigDetails(driver);
    }

    public FollowingItemsWillBeDeleted deleteConfig(String configName) throws InterruptedException
    {
        // Click checkbox near configName
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().prev().find('input').click()");

        deleteButton.click();

        Thread.sleep(2_000);

        return new FollowingItemsWillBeDeleted(driver);
    }

    public ConfigDetails editConfig(String configName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().next().next().next().next().next().next().next().next().next().find(\"button\").click()");

        return new ConfigDetails(driver);
    }

    /**
     * Restore previous config by configName
     * @param configName name of config to restore
     * @return
     */
    public RestorePreviousConfig restorePreviousConfig(String configName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().next().find(\"button\")[2].click()");

        return new RestorePreviousConfig(driver);
    }
}
