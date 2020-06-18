package com.appbus.pages;

import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.menuItems.DocumentsMenuItems;
import com.appbus.pages.menuItems.InternetMenuItems;
import com.appbus.pages.menuItems.MarketDataMenuItems;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

// Opened hamburger menu
public class ActiveHamburgerMenu extends PageObject
{
    @FindBy(name = "icon web arrow left@2x")
    private MobileElement hamburgerMenu;

    @FindBy(name = "Communications")
    private MobileElement communications;

    @FindBy(name = "Documents")
    private MobileElement documents;

    @FindBy(name = "Market Data")
    private MobileElement marketData;

    @FindBy(name = "Internet")
    private MobileElement internet;
    //....

    @FindBy(name = "Log out")
    private MobileElement logout;

    @FindBy(name = "Lock")
    private MobileElement lock;


    public ActiveHamburgerMenu(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        // Login might be long enough so lets wait 50 seconds of explicit wait
        communications = (MobileElement) (new WebDriverWait(driver, 50)).until(ExpectedConditions.visibilityOfElementLocated(By.name("Communications")));
        documents      = (MobileElement) (new WebDriverWait(driver, 50)).until(ExpectedConditions.visibilityOfElementLocated(By.name("Documents")));
        logout         = (MobileElement) (new WebDriverWait(driver, 50)).until(ExpectedConditions.visibilityOfElementLocated(By.name("Log out")));

        return (communications.isDisplayed() & documents.isDisplayed() & logout.isDisplayed());
    }

    public CommunicationsMenuItems clickCommunications()
    {
        communications.click();
        System.out.println("Communications was clicked");

        return new CommunicationsMenuItems(driver);
    }

    public CommunicationsMenuItems clickCommunications(boolean doNotAssertInitialItems)
    {
        communications.click();
        System.out.println("Communications was clicked");

        return new CommunicationsMenuItems(driver, doNotAssertInitialItems);
    }

    public DocumentsMenuItems clickDocuments()
    {
        documents.click();
        System.out.println("Documents was clicked");

        return new DocumentsMenuItems(driver);
    }

    public MarketDataMenuItems clickMarketData()
    {
        marketData.click();
        System.out.println("Market Data was clicked");

        return new MarketDataMenuItems(driver);
    }

    public InternetMenuItems clickInternet()
    {
        internet.click();
        System.out.println("Internet was clicked");

        return new InternetMenuItems(driver);
    }

    public LoginPage clickLogout()
    {
        logout.click();
        System.out.println("Log out was clicked");

        return new LoginPage(driver);
    }

    public LockPage clickLock()
    {
        lock.click();
        System.out.println("Lock was clicked");

        return new LockPage(driver);
    }
}
