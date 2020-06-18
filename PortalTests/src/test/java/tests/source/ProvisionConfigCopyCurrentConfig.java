package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.constants.Notifications;
import net.portal.forms.*;
import net.portal.pages.DeletePolicyConfirmation;
import net.portal.pages.device_management.ProvisioningConfig;
import net.portal.pages.user_and_role_management.Archetypes;
import net.portal.pages.user_and_role_management.Policies;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import org.openqa.selenium.Keys;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;

public class ProvisionConfigCopyCurrentConfig
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigCopyCurrentConfig() throws InterruptedException
    {
        ProvisionConfigCopyCurrentConfig(true);
    }

    public void ProvisionConfigCopyCurrentConfig(boolean refresh) throws InterruptedException
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

//delete Upcoming config if exists (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigCopyCurrentConfig: noProblems = " + noProblems);

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

            SureToDelete std = pc.clickDeleteConfig();
            Thread.sleep(1_000);
            std.clickYes();
            Thread.sleep(1_000);
        }
//delete Upcoming config if exists (finish)

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);

//Check Current config (start)
        String table1sourse = pc.getCertTableText();
        System.out.println("________________________________");
        //System.out.println("table1sourse : " + table1sourse);
        System.out.println("________________________________");

        String table2sourse = pc.getGatewaysTableText();
        System.out.println("________________________________");
        //System.out.println("table2sourse : " + table2sourse);
        System.out.println("________________________________");

        String table3sourse = pc.getServiceTableText();
        System.out.println("________________________________");
        //System.out.println("table3sourse : " + table3sourse);
        System.out.println("________________________________");
//Check Current config (finish)

        AddNewProvConfig anc = pc.clickCopyConfig();
        Thread.sleep(2_000);
        anc.clickNextMonthFirstDay();
        Thread.sleep(1_000);
        anc.clickOk();
        Thread.sleep(2_000);
        pc.clickApply();
        Thread.sleep(5_000);

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);
        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);

//Check saved config (start)
        String table1target = pc.getCertTableText();
        System.out.println("________________________________");
        //System.out.println("table1target : " + table1target);
        System.out.println("________________________________");
        Assert.assertEquals(table1sourse,table1target);

        String table2target = pc.getGatewaysTableText();
        System.out.println("________________________________");
        //System.out.println("table2target : " + table2target);
        System.out.println("________________________________");
        Assert.assertEquals(table2sourse,table2target);

        String table3target = pc.getServiceTableText();
        System.out.println("________________________________");
        //System.out.println("table3target : " + table3target);
        System.out.println("________________________________");
        Assert.assertEquals(table3sourse,table3target);
//Check saved config (finish)

//Check config list (start)
        ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");
        Assert.assertTrue(ItemLIst.contains("Upcoming config"));
//Check config list (finish)

        Assert.assertTrue("ProvisionConfigUploadUpcomingSave: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());
    }
}
