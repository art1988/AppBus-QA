package tests.source;

import net.portal.constants.Const;
import net.portal.pages.HeaderMenu;
import net.portal.pages.reporting.TotalLogins;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.io.File;

public class VisitTotalLogins
{
    @Test
    public void visitTotalLogins() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        TotalLogins totalLoginsPage = headerMenu.clickTotalLogins();

        System.out.println("Make sure that Apply button is visible");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#statisticUser\\\\:filterApplyButton').is(':visible')"));

        System.out.println("Make sure that CSV icon is visible...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#printForm\\\\:csvPrintButton').is(':visible')"));

        totalLoginsPage.clickCSVIcon();
        Thread.sleep(3_000);

        System.out.println("Make sure that file was downloaded...");

        File totalLoginsFile = new File(Const.DOWNLOAD_FOLDER + "\\" + "total-logins.csv");

        Assert.assertTrue(totalLoginsFile.exists());

        // After-test routine: delete downloaded file...
        if( totalLoginsFile.delete() )
        {
            System.out.println(totalLoginsFile.getAbsolutePath() + " was deleted...");
        }
    }
}
