package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.MarketDataMenuItems;
import com.appbus.pages.tabs.ChartsTab;
import com.appbus.pages.tabs.GoogleFinanceTab;
import com.appbus.pages.tabs.WatchlistTab;
import io.appium.java_client.MobileElement;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class MarketData
{
    @Test
    public void marketData()
    {
        ActiveHamburgerMenu menu = new ActiveHamburgerMenu(FunctionalTest.getDriver());

        MarketDataMenuItems marketDataMenuItems = menu.clickMarketData();

        WatchlistTab watchList = marketDataMenuItems.clickWatchlist();

        // Wait until charts tab is fully loaded
        MobileElement chartsTab = (MobileElement)(new WebDriverWait(FunctionalTest.getDriver(), 45)).until(ExpectedConditions.visibilityOfElementLocated(By.name("UBS")));
        // Then click Charts
        ChartsTab charts = marketDataMenuItems.clickCharts();

        Scroller.scrollRight("Google Finance");

        GoogleFinanceTab financeTab = marketDataMenuItems.clickGoogleFinance();
    }
}
