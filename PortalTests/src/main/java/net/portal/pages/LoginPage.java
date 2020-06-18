package net.portal.pages;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.junit.Assert;

public class LoginPage extends PageObject
{
    @FindBy(name = "username")
    private WebElement userNameField;

    @FindBy(name = "password")
    private WebElement passwordField;

    @FindBy(id = "loginButton")
    private WebElement loginButton;

    @FindBy(id = "resetButton")
    private WebElement resetButton;


    public LoginPage(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( userNameField.isDisplayed() & passwordField.isDisplayed() & loginButton.isDisplayed() & resetButton.isDisplayed() );
    }

    public void enterUserName(String userName)
    {
        userNameField.clear();
        userNameField.sendKeys(userName);
    }

    public void enterPassword(String password)
    {
        passwordField.clear();
        passwordField.sendKeys(password);
    }

    public void clickLogin()
    {
        loginButton.click();
        System.out.println("Login button was clicked");
    }

    // Get revision info from Login page footer
    public String getRevision()
    {
        // Login page doesn't have jquery -> inject in
        StringBuffer jsCode = new StringBuffer("var addscript = window.document.createElement('script'); ");
        jsCode.append("addscript.type = 'text/javascript'; ");
        jsCode.append("addscript.src = 'https://code.jquery.com/jquery-3.3.1.min.js'; ");
        jsCode.append("document.body.appendChild(addscript); ");

        ((JavascriptExecutor) driver).executeScript(jsCode.toString());

        try
        {
            Thread.sleep(5_000); // Wait until file is download
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        System.out.println("JQuery was injected.");

        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#footer').text().trim()"));
    }
}
