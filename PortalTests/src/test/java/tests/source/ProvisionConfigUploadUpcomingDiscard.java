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

public class ProvisionConfigUploadUpcomingDiscard
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigUploadUpcomingDiscard() throws InterruptedException
    {
        ProvisionConfigUploadUpcomingDiscard(true);
    }

    public void ProvisionConfigUploadUpcomingDiscard(boolean refresh) throws InterruptedException
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
        System.out.println("ProvisionConfigUploadUpcomingDiscard: noProblems = " + noProblems);

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

        pc.uploadConfig("C:\\automation\\QA\\PortalTests\\Samples\\files\\main_test_env.json");
        //check notification
        Thread.sleep(5_000);

//Check uploaded config (start)
        String table1after = pc.getCertTableText();
        String table1expec = "1_this_is_the_current_configui-buttonDownloadui-buttonin_app_proxy_certp12ipad_1ui-buttonDownloadui-buttonproxy_client_certp12ipad_2ui-buttonDownloadui-buttontrust_certder";
        System.out.println("________________________________");
        //System.out.println("table1after : " + table1after);
        System.out.println("________________________________");
        Assert.assertTrue(table1after.contains(table1expec));

        String table2after = pc.getGatewaysTableText();
        String table2expec = "1_no_service_gatewayin_app_proxy_certin_app_proxy_cert0host_123ui-buttonui-buttonin_app_proxyin_app_proxy_certin_app_proxy_cert4440dev0.e-dapt.net";
        System.out.println("________________________________");
        //System.out.println("table2after : " + table2after);
        System.out.println("________________________________");
        Assert.assertTrue(table2after.contains(table2expec));

        String table3after = pc.getServiceTableText();
        String table3expec = "AddAttachmentgateproxypath/proxy/exchange/email/addAttachmentui-buttonui-buttonConfigurationgateloginpath/proxy/config/getBinaryConfigui-buttonui-buttonContextLoggatein_app_proxypath/proxy/log/changeContext/addui-buttonui-buttonno_contentui-buttonui-buttonno_gategetget_valueui-buttonui-buttonno_propertygatein_app_proxy";
        System.out.println("________________________________");
        System.out.println("table3after : " + table3after);
        System.out.println("________________________________");
        Assert.assertTrue(table3after.contains(table3expec));

//Check uploaded config (finish)

        pc.clickRevertChanges();
        Thread.sleep(2_000);

//Check reverted config (start)
        table1after = pc.getCertTableText();
        table1expec = "No records found.";
        System.out.println("________________________________");
        //System.out.println("table1after : " + table1after);
        System.out.println("________________________________");
        Assert.assertTrue(table1after.contains(table1expec));

        table2after = pc.getGatewaysTableText();
        table2expec = "No records found.";
        System.out.println("________________________________");
        //System.out.println("table2after : " + table2after);
        System.out.println("________________________________");
        Assert.assertTrue(table2after.contains(table2expec));

        table3after = pc.getServiceTableText();
        table3expec = "No records found.";
        System.out.println("________________________________");
        System.out.println("table3after : " + table3after);
        System.out.println("________________________________");
        Assert.assertTrue(table3after.contains(table3expec));
//Check reverted config (finish)
//Check config list (start)
        ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");
        Assert.assertTrue(!ItemLIst.contains("Upcoming config"));
//Check config list (finish)
        Assert.assertTrue("ProvisionConfigUploadUpcomingDiscard: Add Config button should be enabled this time", pc.ifAddConfigEnabled());
    }
}
