package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class LogLast200Lines extends PageObject
{
    @FindBy(id = "tabs:logForm:okButton")
    private WebElement okButton;



    public LogLast200Lines(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#tabs\\\\:logForm\\\\:deviceLogDlg_title').text()").equals("Log Last 200 Lines"));
    }

    public String getContent()
    {
        return String.valueOf( ((JavascriptExecutor) driver).executeScript("return $('.preformatted').text()") );
    }

    public void clickOk()
    {
        okButton.click();
        System.out.println("LogLast200Lines: Ok button was clicked");
    }
}
