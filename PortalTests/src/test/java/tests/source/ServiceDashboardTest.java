package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.DeleteService;
import net.portal.forms.DownloadServiceClientLibrary;
import net.portal.pages.HeaderMenu;
import net.portal.pages.service_management.ServiceCatalog;
import net.portal.pages.service_management.ServiceDashboard;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.text.SimpleDateFormat;
import java.util.Date;

public class ServiceDashboardTest
{
    @Test
    public void serviceDashboardTest() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        ServiceDashboard serviceDashboardPage = headerMenu.clickServiceDashboard();

        serviceDashboardPage.setProjectName("AT Proj 5");
        Thread.sleep(4_000);

        Assert.assertEquals("JSService_AT[edited]1",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceDashboard\\\\:serviceDashboardTable_data td').text().replace(/\\n/g,\"\").replace(/\\s/g, '')")));

        System.out.println("Click by JSService link...");

        serviceDashboardPage.clickByService("JSServ");
        Thread.sleep(2_000);

        System.out.println("Assert creation date...");
        String createdText = String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceDashboard\\\\:serviceDashboardInstancesTable_data td:nth(3)').text()"));

        Assert.assertTrue(createdText.startsWith(new SimpleDateFormat("MM/dd/Y").format(new Date())));

        serviceDashboardPage.openAPISpecification();
        Thread.sleep(8_000);

        //Assert.assertEquals("AT Proj 5 latest [ Base URL: DEV-MSA-QA.botf03.net:9613 ]",
//                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.info').text()")));

        serviceDashboardPage.clickCloseOpenAPISpecification();
        Thread.sleep(2_000);

        DownloadServiceClientLibrary downloadServiceClientLibrary = serviceDashboardPage.clickDownloadServiceClientLibrary();
        Thread.sleep(2_000);

        System.out.println("Expand prog.lang dropdown...");

        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#serviceDashboard\\\\:downloadClientLibDlgForm\\\\:clientLibLanguage label').click()");
        Thread.sleep(500);

        Assert.assertEquals("jsonjavagocpprestjavascriptphppythonrubyscalaspring",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceDashboard\\\\:downloadClientLibDlgForm\\\\:clientLibLanguage_items').text()")));

        // Collapse dropdown
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#serviceDashboard\\\\:downloadClientLibDlgForm\\\\:clientLibLanguage label').click()");
        Thread.sleep(500);

        // Close popup
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#serviceDashboard\\\\:downloadClientLibDlg .ui-icon.ui-icon-closethick').click()");
        Thread.sleep(1_000);

        serviceDashboardPage.clickAllServices();
        Thread.sleep(5_000);

        // Making sure that button 'AllServices' is not on the page
        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceDashboard\\\\:showServicesTableButton').is(':visible')"));

        ServiceCatalog serviceCatalogPage = headerMenu.clickServiceCatalog();
        Thread.sleep(6_000);

        serviceCatalogPage.selectProject("AT Proj 5");
        Thread.sleep(1_000);

        DeleteService deleteService = serviceCatalogPage.deleteJSService("JSService_AT");
        Thread.sleep(1_000);

        deleteService.clickYes();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SERVICE_WAS_REMOVED.getNotificationText(), notificationPopup.getText());

        Assert.assertEquals("",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceCatalogForm\\\\:serviceTable_data tr td:contains(\"JSService_AT\")').text()")));

        Thread.sleep(4_000);
    }
}
