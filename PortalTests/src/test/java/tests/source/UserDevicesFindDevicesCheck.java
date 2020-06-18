package tests.source;

import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import net.portal.pages.device_management.UserDevices;
import org.junit.Assert;
import org.junit.Test;

import static tests.source.FunctionalTest.driver;

public class UserDevicesFindDevicesCheck
{
    @Test
    public void UserDevicesFindDevicesCheck() throws InterruptedException
    {
        UserDevicesFindDevicesCheck(false);
    }

    public void UserDevicesFindDevicesCheck(boolean refresh) throws InterruptedException
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
        System.out.println("UserDevicesFindDevicesCheck: noProblems = " + noProblems);

        boolean success = ud.ifFindDevicesSheetSelected();
        System.out.println("UserDevicesFindDevicesCheck: ifFindDevicesSheetSelected = " + success);
        Assert.assertTrue("UserDevicesFindDevicesCheck: ifFindDevicesSheetSelected = ",success);

        ud.selectUser("dsmirnov");
        Thread.sleep(1_000);
        ud.selectMainCheckBox();
        Thread.sleep(1_000);
        Assert.assertTrue("UserDevicesFindDevicesCheck: if selected all table rows", ud.countSelectedRows());

        Thread.sleep(1_000);
        ud.selectMainCheckBox();
        Thread.sleep(1_000);

        Assert.assertEquals("13445af7-99b6-46c7-b855-bb2f7a4d8eda 2019-04-25T13:04:32.857 NOT_ACTIVE", ud.getContentOfRow1());

        Assert.assertTrue("UserDevicesFindDevicesCheck: if row is selected after click", ud.selectLastRow());
        Thread.sleep(1_000);

        ud.deselectSelectedRow();
        Thread.sleep(1_000);
        Assert.assertTrue("UserDevicesFindDevicesCheck: if all rows is deselected after click", ud.countDeselectedRows());
    }

}
