package tests.source;

import net.portal.pages.HeaderMenu;
import net.portal.pages.reporting.CrashLog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class VisitCrashLog
{
    @Test
    public void visitCrashLog() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        CrashLog crashLogPage = headerMenu.clickCrashLog();

        System.out.println("Make sure that Apply button is visible...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#crashLogStatistic\\\\:searchApplyButton').is(':visible')"));

        System.out.println("Make sure that chart is visible...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.jqplot-base-canvas').is(':visible')"));
    }
}
