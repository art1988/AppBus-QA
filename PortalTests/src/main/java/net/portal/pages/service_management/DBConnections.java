package net.portal.pages.service_management;

import net.portal.forms.DBConnection;
import net.portal.forms.DBConnectionDetails;
import net.portal.forms.DeleteDbConnection;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class DBConnections extends PageObject
{
    @FindBy(id = "dbConnectionsForm:addDbConnectionButton")
    private WebElement addDBConnection;

    @FindBy(id = "dbConnectionsForm:reloadButton")
    private WebElement refreshButton;


    public DBConnections(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Service Management > DB Connections") );
    }

    public DBConnection addDBConnection()
    {
        addDBConnection.click();
        System.out.println("DBConnections : Add DB Connection button was clicked");

        return new DBConnection(driver);
    }

    public DBConnectionDetails viewDBConnection(String connectionName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#dbConnectionsForm\\\\:dbConnectionsTable_data tr td:contains(\"" + connectionName + "\")').next().next().next().next().next().next().find(\"button\")[0].click()");

        return new DBConnectionDetails(driver);
    }

    public DBConnection editDBConnection(String connectionName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#dbConnectionsForm\\\\:dbConnectionsTable_data tr td:contains(\"" + connectionName + "\")').next().next().next().next().next().next().find(\"button\")[1].click()");

        return new DBConnection(driver);
    }

    public DeleteDbConnection deleteDBConnection(String connectionName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#dbConnectionsForm\\\\:dbConnectionsTable_data tr td:contains(\"" + connectionName + "\")').next().next().next().next().next().next().find(\"button\")[2].click()");

        return new DeleteDbConnection(driver);
    }

    public void clickRefresh()
    {
        refreshButton.click();
        System.out.println("DBConnections : Refresh button was clicked");
    }
}
