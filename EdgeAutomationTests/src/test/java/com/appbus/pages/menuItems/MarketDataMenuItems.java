package com.appbus.pages.menuItems;

import com.appbus.pages.PageObject;
import com.appbus.pages.tabs.ChartsTab;
import com.appbus.pages.tabs.GoogleFinanceTab;
import com.appbus.pages.tabs.WatchlistTab;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class MarketDataMenuItems extends PageObject
{
    @FindBy(name = "Watchlist")
    private MobileElement watchList;

    @FindBy(name = "Company Profile")
    private MobileElement companyProfile;

    @FindBy(name = "Options")
    private MobileElement options;

    @FindBy(name = "Charts")
    private MobileElement charts;

    @FindBy(name = "Google Finance")
    private MobileElement googleFinance;


    public MarketDataMenuItems(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( watchList.isDisplayed() & companyProfile.isDisplayed() & options.isDisplayed() );
    }

    public WatchlistTab clickWatchlist()
    {
        watchList.click();
        System.out.println("Watchlist tab was clicked");

        return new WatchlistTab(driver);
    }

    public ChartsTab clickCharts()
    {
        charts.click();
        System.out.println("Charts tab was clicked");

        return new ChartsTab();
    }

    public GoogleFinanceTab clickGoogleFinance()
    {
        googleFinance.click();
        System.out.println("Google Finance tab was clicked");

        return new GoogleFinanceTab(driver);
    }
}
