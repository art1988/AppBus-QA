package tests.source;

import net.portal.constants.Const;
import net.portal.pages.HeaderMenu;
import net.portal.pages.audit.LoginLogout;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.io.File;

public class VisitLoginLogoutPage
{
    @Test
    public void visitLoginLogoutPage() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        LoginLogout loginLogoutPage = headerMenu.clickLoginLogout();

        System.out.println("Make sure that we see Filter and Apply button...");

        Assert.assertEquals("Filter", ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#filter_header').text()"));

        loginLogoutPage.setStartDate("05/01/2019 00:00");
        loginLogoutPage.setEndDate("05/27/2019 23:59");

        loginLogoutPage.clickApply();
        Thread.sleep(2_000);

        Assert.assertEquals("2", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:dataTable_data tr').length")));

        loginLogoutPage.clickCSVIcon();
        Thread.sleep(3_000);

        System.out.println("Make sure that file was downloaded...");

        File loginLogoutFile = new File(Const.DOWNLOAD_FOLDER + "\\" + "login-logout.csv");

        Assert.assertTrue(loginLogoutFile.exists());

        System.out.println("Checking fancy menu features...");

        System.out.println("Click '-'");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#filter_toggler').click()");
        Thread.sleep(1_000);
        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#loginglogoutStatistic\\\\:filterApplyButton').is(':visible')"));

        System.out.println("Click '+'");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#filter_toggler').click()");
        Thread.sleep(1_000);
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#loginglogoutStatistic\\\\:filterApplyButton').is(':visible')"));

        System.out.println("Hide left-side menu...");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#close-menu').click()");
        Thread.sleep(1_000);
        Assert.assertEquals("0", ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.main-menu').css('opacity')"));

        System.out.println("Show left-side menu...");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#close-menu').click()");
        Thread.sleep(1_000);
        Assert.assertEquals("1", ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.main-menu').css('opacity')"));

        // After-test routine: delete downloaded file...
        if( loginLogoutFile.delete() )
        {
            System.out.println(loginLogoutFile.getAbsolutePath() + " was deleted...");
        }
    }
}
