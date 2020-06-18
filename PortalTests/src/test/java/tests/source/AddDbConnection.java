package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.DBConnection;
import net.portal.forms.DeleteDbConnection;
import net.portal.pages.HeaderMenu;
import net.portal.pages.service_management.DBConnections;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddDbConnection
{
    @Test
    public void addDbConnection() throws InterruptedException
    {
        System.out.println("--------- START OF AddDbConnection ---------");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        DBConnections dbConnectionsPage = headerMenu.clickDBConnections();
        
        DBConnection dbConnectionsPopup = dbConnectionsPage.addDBConnection();
        Thread.sleep(4_000);

        String connectionName = "AT db Conn name_8",
               type = "SQL Server",
               host = "128.66.200.140",
               port = "1433",
               dbName = "appbus",
               dbSchema = "dbo",
               dbUsername = "edapt",
               password = "edapt";

        dbConnectionsPopup.setName(connectionName);
        dbConnectionsPopup.setType(type);
        dbConnectionsPopup.setHost(host);
        dbConnectionsPopup.setPort(port);
        dbConnectionsPopup.setDbName(dbName);
        dbConnectionsPopup.setDbSchema(dbSchema);
        dbConnectionsPopup.setDbUsername(dbUsername);
        dbConnectionsPopup.setPassword(password);
        Thread.sleep(2_000);

        dbConnectionsPopup.clickTestConnection();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.TEST_SUCCESSFUL.getNotificationText(), notificationPopup.getText());
        Thread.sleep(3_000);

        dbConnectionsPopup.clickSave();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.DB_CONNECTION_WAS_SAVED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(3_000);

        // Making sure that record is in the list
        Assert.assertTrue( (boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dbConnectionsForm\\\\:dbConnectionsTable_data tr td:contains(\"" + connectionName + "\")').is(\":visible\")"));

        // Rename just created connection
        dbConnectionsPopup = dbConnectionsPage.editDBConnection(connectionName);
        Thread.sleep(1_000);

        connectionName += " [edited]";

        dbConnectionsPopup.setName(connectionName);
        dbConnectionsPopup.clickSave();
        Thread.sleep(3_000);

        // Add new connection with the same name -> make sure that warning will appear
        dbConnectionsPopup = dbConnectionsPage.addDBConnection();
        Thread.sleep(1_000);

        dbConnectionsPopup.setName(connectionName);
        dbConnectionsPopup.clickSave();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertTrue(notificationPopup.getText().startsWith(Notifications.DB_CONNECTION_NAME_ALREADY_EXISTS.getNotificationText()));

        dbConnectionsPopup.clickCancel();
        Thread.sleep(2_000);

        dbConnectionsPage.clickRefresh();
        Thread.sleep(2_000);

        // Making sure that record still is in the list
        Assert.assertTrue( (boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dbConnectionsForm\\\\:dbConnectionsTable_data tr td:contains(\"" + connectionName + "\")').is(\":visible\")"));

        // Edit just created and change port
        // TODO: Uncomment after fixing of ED-3629
        /*
        dbConnectionsPopup = dbConnectionsPage.editDBConnection(connectionName);
        Thread.sleep(20_000);

        port = "1111";
        dbConnectionsPopup.setPort(port);
        dbConnectionsPopup.clickSave();
        Thread.sleep(3_000);

        // Click View
        DBConnectionDetails dbConnectionDetails = dbConnectionsPage.viewDBConnection(connectionName);
        Thread.sleep(1_000);

        Assert.assertEquals(connectionName, dbConnectionDetails.getName());
        Assert.assertEquals(type, dbConnectionDetails.getType());
        // ...
        */

        // Delete created connection
        DeleteDbConnection deleteDbConnectionPopup = dbConnectionsPage.deleteDBConnection(connectionName);
        Thread.sleep(2_000);

        deleteDbConnectionPopup.clickYes();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertTrue(notificationPopup.getText().startsWith(Notifications.DB_CONNECTION_WAS_REMOVED.getNotificationText()));

        Thread.sleep(3_000);
        System.out.println("Making sure that db connection with name = " + connectionName + " is not present in the list...");

        Thread.sleep(1_000);

        boolean flag = (boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dbConnectionsForm\\\\:dbConnectionsTable_data tr td:contains(\"" + connectionName + "\")').is(\":visible\")");
        System.out.println("flag = " + flag);
        Assert.assertFalse(flag);

        Thread.sleep(4_000);

        System.out.println("--------- END OF AddDbConnection ---------");
    }
}
