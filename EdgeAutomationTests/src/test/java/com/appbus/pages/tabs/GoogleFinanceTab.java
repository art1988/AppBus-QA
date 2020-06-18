package com.appbus.pages.tabs;

import com.appbus.pages.PageObject;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class GoogleFinanceTab extends PageObject
{
    @FindBy(name = "Search")
    private MobileElement searchField;

    @FindBy(name = "Finance")
    private MobileElement financeLabel;

    @FindBy(name = "MARKET SUMMARY")
    private MobileElement marketSummaryLabel;


    public GoogleFinanceTab(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( searchField.isDisplayed() & searchField.getText().equals("finance") &
                financeLabel.isDisplayed() & marketSummaryLabel.isDisplayed() );
    }
}
