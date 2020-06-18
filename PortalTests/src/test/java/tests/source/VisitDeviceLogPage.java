package tests.source;

import net.portal.pages.HeaderMenu;
import net.portal.pages.audit.DeviceLog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class VisitDeviceLogPage
{
    @Test
    public void visitDeviceLogPage() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        DeviceLog deviceLogPage = headerMenu.clickDeviceLog();

        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tabs\\\\:deviceLog\\\\:selectedFolder').is(':visible')"));

        deviceLogPage.clickCrashTab();
        Thread.sleep(1_000);

        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tabs\\\\:deviceLog\\\\:uploadDeviceLogButton').is(':visible')"));

        deviceLogPage.clickFullLogTab();
        Thread.sleep(1_000);

    }
}
