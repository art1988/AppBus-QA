package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.constants.Notifications;
import net.portal.forms.AddNewProvConfig;
import net.portal.forms.SureToDelete;
import net.portal.pages.device_management.ProvisioningConfig;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import net.portal.pages.device_management.UserDevices;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Set;
import java.util.TimeZone;

public class ProvisionConfigAddRevertCheck
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM/dd/yyyy HH:mm");
    static final SimpleDateFormat pitUTC = new SimpleDateFormat("MM/dd/yyyy HH:mm");
    //String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

    @Test
    public void ProvisionConfigAddRevertCheck() throws InterruptedException
    {
        ProvisionConfigAddRevertCheck(false);
    }

    public void ProvisionConfigAddRevertCheck(boolean refresh) throws InterruptedException
    {

        TimeZone tzDFLT = TimeZone.getDefault();
        df.setTimeZone(tzDFLT);
        pitUTC.setTimeZone(TimeZone.getTimeZone("UTC")); //GMT, UTC
        System.out.println("tz = " + tzDFLT);
        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        System.out.println("timeMDHMS = " + timeMDHMS);
        String currentTimeUTC = pitUTC.format(timeMDHMS);
        String currentTimeDFL = df.format(timeMDHMS);
        System.out.println("currentTimeUTC = " + currentTimeUTC);
        System.out.println("currentTimeDFL = " + currentTimeDFL);

        String timeMMDDYY = currentTimeUTC.substring(0,6) + currentTimeUTC.substring(8,10);
        System.out.println("timeMMDDYY = " + timeMMDDYY);

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

        //delete Upcoming config if exists (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigCreateCertN6: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        if (ItemLIst.contains("Upcoming config"))
        {
            pc.clickSelectConfiguration();
            Thread.sleep(1_000);
            pc.clickUpcomingConfig();
            Thread.sleep(3_000);
            SureToDelete pop = pc.clickDeleteConfig();
            Thread.sleep(1_000);
            pop.clickYes();
            Thread.sleep(2_000);
        }
        //delete Upcoming config if exists (finish)

        AddNewProvConfig addPop = pc.clickAddConfig();
        Thread.sleep(2_000);
        //addPop.setStartTime(timeMMDDYY); //bug: date entered manually is not saved (ED-4069)
        addPop.clickCurrentDate();
        //Thread.sleep(1_000);
        WebElement notificationPopup = (new WebDriverWait(driver, 4)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.DATE_CANT_LESS_THAN_CURRENT.getNotificationText(), notificationPopup.getText());
        Thread.sleep(2_000);
        addPop.clickStartTime();
        Thread.sleep(1_000);
        addPop.clickTomorrowDayPlus1();
        addPop.clickOk();

        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigAddRevertCheck: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

        Thread.sleep(1_000);
        pc.clickRevertChanges();
        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigAddRevertCheck: Add Config button should be enabled this time", pc.ifAddConfigEnabled());
        Thread.sleep(1_000);
    }
}
