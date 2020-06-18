package net.portal.pages.pool_management;

import net.portal.forms.PoolProviderDetails;
import net.portal.pages.DeletePoolProvider;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class PoolProviders extends PageObject
{
    @FindBy(id = "poolProviders:addButton")
    private WebElement addButton;



    public PoolProviders(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Pool Management > Pool Providers") );
    }

    public PoolProviderDetails addPoolProvider()
    {
        addButton.click();
        System.out.println("PoolProviders : Add button was clicked");

        return new PoolProviderDetails(driver);
    }

    /**
     * Edit pool provider by name
     * @param poolProviderName name of pool provider to edit
     */
    public PoolProviderDetails editPoolProvider(String poolProviderName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#poolProviders\\\\:poolProvidersTable_data tr td:contains(\"" + poolProviderName + "\")').next().next().find(\"button\")[0].click()");

        return new PoolProviderDetails(driver);
    }

    /**
     * Delete pool provider by name
     * @param poolProviderName name of pool provider to delete
     * @return
     */
    public DeletePoolProvider deletePoolProvider(String poolProviderName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#poolProviders\\\\:poolProvidersTable_data tr td:contains(\"" + poolProviderName + "\")').next().next().find(\"button\")[1].click()");

        return new DeletePoolProvider(driver);
    }

}
