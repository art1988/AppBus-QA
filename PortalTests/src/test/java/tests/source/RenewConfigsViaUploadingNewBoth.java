package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.forms.*;
import net.portal.pages.device_management.ProvisioningConfig;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;


public class RenewConfigsViaUploadingNewBoth
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void RenewConfigsViaUploadingNewBoth() throws InterruptedException
    {
        RenewConfigsViaUploadingNewBoth(true);
    }

    public void RenewConfigsViaUploadingNewBoth(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

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

//get configs list (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("RenewConfigsViaUploadingNewBoth: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");
//get configs list (finish)

//delete both of configs (start)
        if (ItemLIst.contains("Upcoming config"))
        {
            System.out.println("RenewConfigsViaUploadingNewBoth: going to delete Upcoming config");

            pc.clickSelectConfiguration();
            Thread.sleep(1_000);
            pc.clickUpcomingConfig();
            Thread.sleep(3_000);
            SureToDelete pop = pc.clickDeleteConfig();
            Thread.sleep(2_000);
            pop.clickYes();
            Thread.sleep(2_000);
        }

        if (ItemLIst.contains("Current config"))
        {
            System.out.println("RenewConfigsViaUploadingNewBoth: going to delete Current config");

            pc.clickSelectConfiguration();
            Thread.sleep(1_000);
            pc.clickCurrentConfig();
            Thread.sleep(3_000);
            SureToDelete pop = pc.clickDeleteConfig();
            Thread.sleep(2_000);
            pop.clickYes();
            Thread.sleep(2_000);
        }
//delete both of configs (finish)

//stop script if any config exists (start)
        ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("RenewConfigsViaUploadingNewBoth: delete please all configs if anyone exists", !ItemLIst.contains("Current config") && !ItemLIst.contains("Upcoming config"));
//stop script if any config exists (finish)

        pc.uploadConfig("C:\\automation\\QA\\PortalTests\\Samples\\files\\upcomingProvisioningConfig.json");
        //check notification
        Thread.sleep(5_000);
        pc.clickApply();
        Thread.sleep(5_000);

        //check notification "...you don't have current config..."

        pc.uploadConfig("C:\\automation\\QA\\PortalTests\\Samples\\files\\currentProvisioningConfig.json");
        //check notification
        Thread.sleep(5_000);
        pc.clickApply();
        Thread.sleep(5_000);

    }
}
