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


public class ProvisionConfigMakeUpComToCurre
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    static final SimpleDateFormat pf = new SimpleDateFormat("MM/dd/YY");

    @Test
    public void ProvisionConfigMakeUpComToCurre() throws InterruptedException
    {
        ProvisionConfigMakeUpComToCurre(true);
    }

    public void ProvisionConfigMakeUpComToCurre(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());

        //String mmddyy = pf.format(System.currentTimeMillis()-24*60*60*1000); //yesterday
        String mmddyy = pf.format(System.currentTimeMillis()); //today
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

//stop script if any config doesn't exist (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigMakeUpComToCurre: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigMakeUpComToCurre: create please Current config if one doesn't exist", ItemLIst.contains("Current config"));
        Assert.assertTrue("ProvisionConfigMakeUpComToCurre: create please Upcoming config if one doesn't exist", ItemLIst.contains("Upcoming config"));
//stop script if any config doesn't exist (finish)

        if (ItemLIst.contains("Current config"))
        {
            System.out.println("ProvisionConfigMakeUpComToCurre: going to delete Current config");

            pc.clickSelectConfiguration();
            Thread.sleep(1_000);
            pc.clickCurrentConfig();
            Thread.sleep(3_000);
            SureToDelete pop = pc.clickDeleteConfig();
            Thread.sleep(2_000);
            pop.clickYes();
            Thread.sleep(2_000);
        }

//Check red message (start)
        String redMessage = pc.getErrorMessage();
        //Assert.assertSame("You don't have current config. To work correct move one of the upcoming configs to current by changing start date.",redMessage);
        Assert.assertTrue(redMessage.contains("You don't have current config. To work correct move one of the upcoming configs to current by changing start date."));
//Check red message (finish)

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);

//Check red message (start)
        String redMessage1 = pc.getErrorMessage();
        //Assert.assertSame(redMessage,redMessage1);
        Assert.assertTrue(redMessage1.contains("You don't have current config. To work correct move one of the upcoming configs to current by changing start date."));
//Check red message (finish)

//Check Upcoming config before (start)
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
//Check Upcoming config before (finish)

//create Current config (start)
        System.out.println("Going to set the following config date : " + mmddyy + " ,it should be today");
        pc.setStartTime(mmddyy); //pc.setStartTime("7/11/19");
        Thread.sleep(2_000);
        pc.clickApply();
        Thread.sleep(3_000);
        System.out.println("ProvisionConfigMakeUpComToCurre: Current config was set");
//create Current config (finish)

//Current config should be presented (start)
        ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigMakeUpComToCurre: Current config only exists:", ItemLIst.contains("Current config") && !ItemLIst.contains("Upcoming config"));

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);
//Current config should be presented (finish)

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

        Assert.assertTrue("ProvisionConfigDeleteExpiredCon: Certificates table is the same:",table1after.equals(table1sourse));

        Assert.assertTrue("ProvisionConfigDeleteExpiredCon: Gateways table is the same:",table2after.equals(table2sourse));

        Assert.assertTrue("ProvisionConfigDeleteExpiredCon: Services table is the same:",table3after.equals(table3sourse));

    }
}
