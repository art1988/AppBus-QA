package com.appbus.pages;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class LoginPage extends PageObject
{
    @FindBy(name = "user")
    private MobileElement loginField;

    @FindBy(name = "pswd")
    private MobileElement passwordField;

    @FindBy(name = "domain")
    private MobileElement domainField;

    @FindBy(name = "tfa")
    private MobileElement tfaField;

    @FindBy(name = "Log In")
    private MobileElement loginButton;


    public LoginPage(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (loginField.isDisplayed() & passwordField.isDisplayed() & loginButton.isDisplayed());
    }

    public void enterUser(String userName)
    {
        loginField.clear();
        loginField.sendKeys(userName);
    }

    public void enterPassword(String pswd)
    {
        passwordField.clear();
        passwordField.sendKeys(pswd);
    }

    public void enterDomain(String domain)
    {
        domainField.clear();
        domainField.sendKeys(domain);
    }

    public void enterTfa(String tfa)
    {
        tfaField.clear();
        tfaField.sendKeys(tfa);
    }

    public ActiveHamburgerMenu logon()
    {
        loginButton.click();

        return new ActiveHamburgerMenu(driver);
    }
}
