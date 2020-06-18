package net.portal.pages.pool_management;

import net.portal.forms.PoolDetails;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Pool extends PageObject
{
    @FindBy(id = "poolForm:addButton")
    private WebElement addPoolButton;

    @FindBy(id = "poolForm:reloadButton")
    private WebElement refreshButton;



    public Pool(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Pool Management > Pools") );
    }

    public PoolDetails addPool()
    {
        addPoolButton.click();
        System.out.println("Pool : Add pool button was clicked");

        return new PoolDetails(driver);
    }
}
