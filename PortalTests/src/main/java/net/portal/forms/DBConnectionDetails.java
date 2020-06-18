package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DBConnectionDetails extends PageObject
{
    @FindBy(id = "dbConnectionsForm:viewOkButton")
    private WebElement okButton;

    @FindBy(id = "dbConnectionsForm:viewTestCOnnectionButton")
    private WebElement testConnectionButton;


    public DBConnectionDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#dbConnectionsForm\\\\:dbConnectionViewDlg_title').text()").equals("DB Connection Details") );
    }

    public String getName()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#dbConnectionsForm\\\\:viewTable').find(\"td\").filter(function() { return $(this).text() === 'Name'; }).next().text()"));
    }

    public String getType()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#dbConnectionsForm\\\\:viewTable td:contains(\"Type\")').next().text()"));
    }

    public void clickTestConnection()
    {
        testConnectionButton.click();
        System.out.println("DBConnectionDetails : Test connection was clicked");
    }
}
