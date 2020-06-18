package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.DeleteJavaLib;
import net.portal.forms.JavaLibrary;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import net.portal.pages.device_management.UserDevices;
import net.portal.pages.service_management.ServiceCatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.io.File;
import static tests.source.FunctionalTest.driver;

public class UserDevicesTabsAvailability

{
    @Test
    public void UserDevicesTabsAvailability() throws InterruptedException
    {
        UserDevicesTabsAvailability(false);
    }

    public void UserDevicesTabsAvailability(boolean refresh) throws InterruptedException {

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
        System.out.println("UserDevicesTabsAvailability: noProblems = " + noProblems);

        boolean success = ud.ifFindDevicesSheetSelected();
        System.out.println("UserDevicesTabsAvailability: ifFindDevicesSheetSelected = " + success);
        Assert.assertTrue("UserDevicesTabsAvailability: ifFindDevicesSheetSelected = ",success);

        ud.selectUser("dsmirnov");
        Thread.sleep(1_000);

        Thread.sleep(1_000);
        ud.clickReviewWipeListSheet();
        Thread.sleep(2_000);
        /*
        noProblems = wkp.fixLoadBarProblem(); //LB //ED-4110 is fixed
        if (!noProblems)
        {
            System.out.println("ATTENTION !!! UserDevicesTabsAvailability: Review Wipe List Sheet doesn't work !");
            ud = headerMenu.clickUserDevices(doPortalWakeUp);
        }
        */
        ud.clickOSversionsSheet();
        Thread.sleep(2_000);
        ud.selectOStype("OSX");
        Thread.sleep(1_000);
    }
}
