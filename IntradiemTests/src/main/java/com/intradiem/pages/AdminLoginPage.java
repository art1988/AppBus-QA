package com.intradiem.pages;

import io.appium.java_client.AppiumDriver;
import org.junit.Assert;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class AdminLoginPage extends PageObject
{
    @FindBy(id = "inputUserName")
    private WebElement usernameField;

    @FindBy(id = "inputPassword")
    private WebElement passwordField;

    @FindBy(css = ".md-raised")
    private WebElement loginButton;


    public AdminLoginPage(WebDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( usernameField.isDisplayed() & passwordField.isDisplayed() );
    }

    public void setUsername(String username)
    {
        usernameField.click();
        usernameField.sendKeys(username);
    }

    public void setPassword(String password)
    {
        passwordField.click();
        passwordField.sendKeys(password);
    }

    public UsersPage logon()
    {
        loginButton.click();

        return new UsersPage(driver);
    }
}
