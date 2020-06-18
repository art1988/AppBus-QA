package tests.source;

import net.portal.pages.HeaderMenu;
import net.portal.pages.device_management.UserDevices;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class VisitUserDevices
{
    @Test
    public void visitUserDevices() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        UserDevices userDevicesPage = headerMenu.clickUserDevices();

        userDevicesPage.clickFindDevicesTab();
        Thread.sleep(3_000);

        System.out.println("Make sure that Lookup button is visible...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:tabs\\\\:lookupButton').is(':visible')"));

        userDevicesPage.clickReviewWipeListTab();
        Thread.sleep(3_000);

        userDevicesPage.clickOSVersionsTab();
        Thread.sleep(3_000);

        System.out.println("Make sure that Filter and Apply button are visible...");
        Assert.assertEquals("Filter", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.ui-tabs-panels .ui-panel-title').text()")));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:tabs\\\\:applyButton').is(':visible')"));
    }
}
