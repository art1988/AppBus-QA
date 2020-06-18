package com.intradiem.pages;

import io.appium.java_client.AppiumDriver;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class ClientLoginWindow extends PageObject
{
    @FindBy(xpath = "/Window/Custom/Custom[3]/Document/Custom[2]/Edit[1]")
    private WebElement usernameField;

    @FindBy(xpath = "/Window/Custom/Custom[3]/Document/Custom[2]/Edit[2]")
    private WebElement passwordField;

    @FindBy(xpath = "/Window/Custom/Custom[3]/Document/Custom[2]/Button[2]")
    private WebElement loginButton;


    public ClientLoginWindow(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        usernameField = (WebElement) (new WebDriverWait(driver, 50)).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom[2]/Edit[1]")));
        passwordField = (WebElement) (new WebDriverWait(driver, 50)).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom[2]/Edit[2]")));

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
        passwordField.clear();

        passwordField.sendKeys(password);
    }

    public void clickLogin()
    {
        loginButton.click();

        System.out.println("Login was clicked");
    }

}
