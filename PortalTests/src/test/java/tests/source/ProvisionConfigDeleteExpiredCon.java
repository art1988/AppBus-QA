package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.constants.Const;
import net.portal.forms.*;
import net.portal.pages.device_management.ProvisioningConfig;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;

import java.io.File;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;


public class ProvisionConfigDeleteExpiredCon
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigDeleteExpiredCon() throws InterruptedException
    {
        ProvisionConfigDeleteExpiredCon(true);
    }

    public void ProvisionConfigDeleteExpiredCon(boolean refresh) throws InterruptedException
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

//stop script if Current config doesn't exist (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigDeleteExpiredCon: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigDeleteExpiredCon: create please Current config if one doesn't exist", ItemLIst.contains("Current config"));
//stop script if Current config doesn't exist (finish)

        if (ItemLIst.contains("Upcoming config"))
        {
            System.out.println("ProvisionConfigDeleteExpiredCon: going to delete Upcoming config");

            pc.clickSelectConfiguration();
            Thread.sleep(1_000);
            pc.clickUpcomingConfig();
            Thread.sleep(3_000);
            SureToDelete pop = pc.clickDeleteConfig();
            Thread.sleep(2_000);
            pop.clickYes();
            Thread.sleep(2_000);
        }

//stop script if Current config doesn't exist (finish)
        ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigDeleteExpiredCon: create please Current config if one does not exist", ItemLIst.contains("Current config"));

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);
//stop script if Current config doesn't exist (finish)

//Check Current config before (start)
        String table1sourse = pc.getCertTableText();
        System.out.println("________________________________");
        System.out.println("table1sourse : " + table1sourse);
        System.out.println("________________________________");

        String table2sourse = pc.getGatewaysTableText();
        System.out.println("________________________________");
        System.out.println("table2sourse : " + table2sourse);
        System.out.println("________________________________");

        String table3sourse = pc.getServiceTableText();
        System.out.println("________________________________");
        System.out.println("table3sourse : " + table3sourse);
        System.out.println("________________________________");
//Check Current config before (finish)

//create Expired config (start)
        AddNewProvConfig adcon = pc.clickAddConfig();
        Thread.sleep(1_000);
        adcon.clickYesterday();
        Thread.sleep(1_000);
        adcon.clickOk();
        Thread.sleep(2_000);
        pc.clickApply();
        Thread.sleep(3_000);
        System.out.println("ProvisionConfigDeleteExpiredCon: Expired config is ready");
//create Expired config (finish)

        pc.deleteExpiredConfig(); //ED-4196
/*      AddNewProvConfig pop = pc.makeUpcomingConfig();
        Thread.sleep(1_000);
        pop.clickTomorrowDay();
        Thread.sleep(1_000);
        pop.clickOkTurning();  */
        Thread.sleep(1_000);

//both of configs should be presented (start)
        ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        //! Assert.assertTrue("ProvisionConfigDeleteExpiredCon: Current config and Upcoming config exist:", ItemLIst.contains("Current config") && ItemLIst.contains("Upcoming config"));

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);
//both of configs should be presented (finish)

//Check Current config after (start)
        String table1after = pc.getCertTableText();
        System.out.println("________________________________");
        System.out.println("table1after : " + table1after);
        System.out.println("________________________________");

        String table2after = pc.getGatewaysTableText();
        System.out.println("________________________________");
        System.out.println("table2after : " + table2after);
        System.out.println("________________________________");

        String table3after = pc.getServiceTableText();
        System.out.println("________________________________");
        System.out.println("table3after : " + table3after);
        System.out.println("________________________________");
//Check Current config after (finish)

        //Assert.assertTrue("ProvisionConfigDeleteExpiredCon: Certificates table is the same:",table1after.equals(table1sourse));

        //Assert.assertTrue("ProvisionConfigDeleteExpiredCon: Gateways table is the same:",table2after.equals(table2sourse));

        //Assert.assertTrue("ProvisionConfigDeleteExpiredCon: Services table is the same:",table3after.equals(table3sourse));

    }
}
