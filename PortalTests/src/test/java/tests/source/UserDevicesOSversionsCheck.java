package tests.source;

import static tests.source.FunctionalTest.driver;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import net.portal.pages.device_management.UserDevices;
import org.openqa.selenium.By;

public class UserDevicesOSversionsCheck
{
    @Test
    public void UserDevicesOSversionsCheck() throws InterruptedException
    {
        UserDevicesOSversionsCheck(false);
    }

    public void UserDevicesOSversionsCheck(boolean refresh) throws InterruptedException
    {
        driver.navigate().refresh();
        Thread.sleep(5_000);

        boolean doPortalWakeUp = true;
        Thread.sleep(1_000);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000);
        else Thread.sleep(2_000);
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        WakeUpPortal wkp = new WakeUpPortal(FunctionalTest.getDriver());
        Thread.sleep(2_000);

        UserDevices ud = headerMenu.clickUserDevices(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("UserDevicesOSversionsCheck: noProblems = " + noProblems);

        ud.clickOSversionsSheet();
        Thread.sleep(2_000);
        ud.setStartDate("01/01/2017");
        Thread.sleep(2_000);

        ud.selectOStype("OSX");
        Thread.sleep(1_000);
        String chartHeader = driver.findElement(By.xpath("//div[@class='jqplot-title']")).getText();
        System.out.println("UserDevicesOSversionsCheck: chartHeader = " + chartHeader);
        Assert.assertEquals("Head of Chart if Chart exists", "Versions Chart" ,chartHeader);

        ud.selectOStype("WINDOWS");
        Thread.sleep(1_000);

        ud.selectOStype("ANDROID");
        Thread.sleep(1_000);

        ud.selectOStype("IOS");
        Thread.sleep(1_000);
        chartHeader = driver.findElement(By.xpath("//div[@class='jqplot-title']")).getText();
        System.out.println("UserDevicesOSversionsCheck: chartHeader = " + chartHeader);
        Assert.assertEquals("Head of Chart if Chart exists", "Versions Chart" ,chartHeader);

    }

}
