package com.appbus.pages.menuItems;

import com.appbus.pages.PageObject;
import com.appbus.pages.tabs.BloombergTab;
import com.appbus.pages.tabs.FidelityTab;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class InternetMenuItems extends PageObject
{
    @FindBy(name = "Google")
    private MobileElement google;

    @FindBy(name = "Bloomberg")
    private MobileElement bloomberg;

    @FindBy(name = "Fidelity")
    private MobileElement fidelity;


    public InternetMenuItems(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( google.isDisplayed() & bloomberg.isDisplayed() );
    }

    public BloombergTab clickBloomberg()
    {
        bloomberg.click();
        System.out.println("Bloomberg tab was clicked");

        return new BloombergTab();
    }

    public FidelityTab clickFidelity()
    {
        fidelity.click();
        System.out.println("Fidelity tab was clicked");

        return new FidelityTab();
    }
}
