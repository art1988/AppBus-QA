package tests.source;

import net.portal.forms.LogLast200Lines;
import net.portal.pages.DeleteItemLogPopup;
import net.portal.pages.DeleteItemPopup;
import net.portal.pages.HeaderMenu;
import net.portal.pages.audit.DeviceLog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class DecodeTest
{
    @Test
    public void decodeTest() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        DeviceLog deviceLogPage = headerMenu.clickDeviceLog();

        deviceLogPage.selectFolder("Failed");
        Thread.sleep(2_000);

        String fileToDecode = "encrypted-test.log";

        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tabs\\\\:logForm\\\\:deviceLogTable_data tr td:contains(\"" + fileToDecode + "\")').is(':visible')"));

        deviceLogPage.decode(fileToDecode);
        Thread.sleep(2_000);

        System.out.println("Making sure that file " + fileToDecode + " is no longer in Failed folder...");
        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tabs\\\\:logForm\\\\:deviceLogTable_data tr td:contains(\"" + fileToDecode + "\")').is(':visible')"));

        deviceLogPage.selectFolder("Decoded");
        Thread.sleep(2_000);

        System.out.println("Making sure that file " + fileToDecode + " is in Decoded folder...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tabs\\\\:logForm\\\\:deviceLogTable_data tr td:contains(\"" + fileToDecode + "\")').is(':visible')"));

        LogLast200Lines logLast200LinesForm = deviceLogPage.viewLast200Lines(fileToDecode);
        Thread.sleep(2_000);

        System.out.println("Making sure that file was decoded...");
        Assert.assertTrue(logLast200LinesForm.getContent().startsWith("2019-06-05 01:05:18.1745|TRACE|e_dapt.Core.Services.Com"));

        logLast200LinesForm.clickOk();
        Thread.sleep(2_000);

        DeleteItemLogPopup deleteItemLogPopup = deviceLogPage.deleteLog(fileToDecode);
        Thread.sleep(2_000);

        deleteItemLogPopup.clickYes();
        Thread.sleep(2_000);

        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tabs\\\\:logForm\\\\:deviceLogTable_data').text()")));
    }
}
