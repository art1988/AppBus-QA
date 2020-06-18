package tests.source;

import net.portal.constants.Const;
import net.portal.pages.HeaderMenu;
import net.portal.pages.reporting.ActiveUsers;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.io.File;

public class VisitActiveUsersPage
{
    @Test
    public void visitActiveUsersPage() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        ActiveUsers activeUsersPage = headerMenu.clickActiveUsers();

        System.out.println("Make sure that Apply button is visible...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#activeUser\\\\:filterApplyButton').is(':visible')"));

        System.out.println("Make sure that CSV icon is visible...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#activeUser\\\\:csvIcon').is(':visible')"));

        activeUsersPage.clickCSVIcon();
        Thread.sleep(3_000);

        System.out.println("Make sure that file was downloaded...");

        File activeUsersFile = new File(Const.DOWNLOAD_FOLDER + "\\" + "active-users.csv");

        Assert.assertTrue(activeUsersFile.exists());

        // After-test routine: delete downloaded file...
        if( activeUsersFile.delete() )
        {
            System.out.println(activeUsersFile.getAbsolutePath() + " was deleted...");
        }
    }
}
