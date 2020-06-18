package com.appbus.pages;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriverException;
import org.openqa.selenium.support.FindBy;

public class LockPage extends PageObject
{
    @FindBy(name = "pswd")
    private MobileElement passwordField;

    @FindBy(name = "Unlock")
    private MobileElement unlockButton;


    public LockPage(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( passwordField.isDisplayed() & unlockButton.isDisplayed() );
    }

    public void setPassword(String pswd)
    {
        passwordField.clear();
        passwordField.click(); // need to click after unsuccessful unlock
        passwordField.sendKeys(pswd);
    }

    public ActiveHamburgerMenu clickUnlcok()
    {
        unlockButton.click();
        System.out.println("Unlock button was clicked");

        MobileElement loginFailLabel = null;
        try
        {
            // in case of wrong password login
            loginFailLabel = (MobileElement) driver.findElement(By.name("Login failed. Probably, invalid user name or password. Tap here for details..."));
        }
        catch ( WebDriverException ex )
        {
            // can't find login fail label element => logon was successful...
            return new ActiveHamburgerMenu(driver);
        }

        return null; //... otherwise still on Lock page
    }
}
