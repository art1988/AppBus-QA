package net.portal.forms;

import net.portal.pages.LoginPage;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class LogOff extends PageObject
{
    @FindBy(id = "formheader:confirm")
    private WebElement okButton;


    public LogOff(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#formheader\\\\:confirmDialog2_title').text()").equals("Log off") );
    }

    public LoginPage clickOk()
    {
        okButton.click();
        System.out.println("LogOff : Ok button was clicked");

        return new LoginPage(driver);
    }
}
