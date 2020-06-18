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
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

public class ProvisionConfigEditGatewayUpcom
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigEditGatewayUpcom() throws InterruptedException
    {
        ProvisionConfigEditGatewayUpcom(true);
    }

    public void ProvisionConfigEditGatewayUpcom(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String gName44 = "gat44AutoNm" + tmpstp.substring(4); System.out.println("gName44: " + gName44);
        String gPort44 = "44";                                System.out.println("gPort44: " + gPort44);
        String gHost44 = "https://www.ru.is/";                System.out.println("gHost44: " + gHost44);

        String gName45 = "gat45AutoNm" + tmpstp.substring(4); System.out.println("gName45: " + gName45);
        String gPort45 = "45";                                System.out.println("gPort45: " + gPort45);
        String gHost45 = "http://us.net/";                    System.out.println("gHost45: " + gHost45);

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

//stop script if Upcoming config doesn't exist (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigEditGatewayUpcom: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigEditGatewayUpcom: create please Upcoming config if one doesn't exist", ItemLIst.contains("Upcoming config"));
//stop script if Upcoming config doesn't exist (finish)

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);

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


//edit Gateway #44 (start)
        GatewayDetails gd = pc.clickEditTheFirstGateway();
        Thread.sleep(1_000);
        gd.setName(gName44);
        Thread.sleep(1_000);
        String c1Name44 = gd.setClientCertificateTheFirstItem();
        Thread.sleep(1_000);
        String c2Name44 = gd.setTrustCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setPort("0000000" + gPort44);
        Thread.sleep(1_000);
        gd.setHost(gHost44);
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(3_000);
//edit Gateway #44 (finish)


//edit Gateway #45 (start)
        gd = pc.clickEditTheSecondGateway();
        Thread.sleep(1_000);
        gd.setName(gName45);
        Thread.sleep(1_000);
        String c1Name45 = gd.setClientCertificateTheFirstItem();
        Thread.sleep(1_000);
        String c2Name45 = gd.setTrustCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setPort("0000000" + gPort45);
        Thread.sleep(1_000);
        gd.setHost(gHost45);
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(3_000);
//edit Gateway #45 (finish)

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

//Check Upcoming config after (start)
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
//Check Upcoming config before (finish)

        int gatewaysNumber = pc.getGatewaysNumber();

        for (int i = 0; i < gatewaysNumber; i++)
        {
            String rowText = pc.getGatewayRowText(i);
            if (rowText.contains(gName44))
            {
                Assert.assertTrue(rowText.contains(gPort44) && rowText.contains(gHost44) && rowText.contains(c1Name44) && rowText.contains(c2Name44));
            }

            if (rowText.contains(gName45))
            {
                Assert.assertTrue(rowText.contains(gPort45) && rowText.contains(gHost45) && rowText.contains(c1Name45) && rowText.contains(c2Name45));
            }
        }
    }
}
