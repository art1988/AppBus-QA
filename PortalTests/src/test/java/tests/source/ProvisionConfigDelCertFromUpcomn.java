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

public class ProvisionConfigDelCertFromUpcomn
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigDelCertFromUpcomn() throws InterruptedException
    {
        ProvisionConfigDelCertFromUpcomn(true);
    }

    public void ProvisionConfigDelCertFromUpcomn(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cName44 = "crt44AutoNm" + tmpstp.substring(4); System.out.println("cName44: " + cName44);
        String cType44 = "der";                               System.out.println("cType44: " + cType44);
        String cPass44 = "44*^^%$^%#$#" +tmpstp.substring(4); System.out.println("cPass44: " + cPass44);

        String cName99 = "crt99AutoNm" + tmpstp.substring(4); System.out.println("cName99: " + cName99);
        String cType99 = "der";                               System.out.println("cType99: " + cType99);
        String cPass99 = "99*^^%$^%#$#" +tmpstp.substring(4); System.out.println("cPass99: " + cPass99);

        String gName99 = "gat99AutoNm" + tmpstp.substring(4); System.out.println("gName99: " + gName99);
        String gPort99 = "99";                                System.out.println("gPort99: " + gPort99);
        String gHost99 = "lingvoexpert.com";                  System.out.println("gHost99: " + gHost99);

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
        System.out.println("ProvisionConfigDelCertFromUpcomn: noProblems = " + noProblems);

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

        Assert.assertTrue("ProvisionConfigDelCertFromUpcomn: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

//add Certificate #44 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigDelCertFromUpcomn: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType44);
        cd.setCertificateName(cName44);
        //cd.setCertPassword(cPass44);
        cd.clickSave();
        Thread.sleep(2_000);
//add Certificate #44 (finish)

//add Certificate #99 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigDelCertFromUpcomn: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType99);
        cd.setCertificateName(cName99);
        //cd.setCertPassword(cPass99);
        cd.clickSave();
        Thread.sleep(2_000);
//add Certificate #44 (finish)

//add Gateway #99 (start)
        GatewayDetails gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName99);
        Thread.sleep(1_000);
        gd.setClientCertificateByName(cName99);
        Thread.sleep(1_000);
        gd.setTrustCertificateByName(cName99);
        Thread.sleep(1_000);
        gd.setPort("0000000" + gPort99);
        Thread.sleep(1_000);
        gd.setHost(gHost99);
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(3_000);
//add Gateway #99 (finish)

//try to delete certificate #99 (start)
        SureToDelete std = pc.deleteCertificateByName(cName99);
        Thread.sleep(1_000);
        std.clickYesCertByParent();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.UNABLE_TO_REMOVE_CERTIFICATE.getNotificationText(), notificationPopup.getText());
        Thread.sleep(5_000);
//try to delete certificate #99 (finish)

//delete certificate #44 (start)
        std = pc.deleteCertificateByName(cName44);
        Thread.sleep(1_000);
        std.clickYesCertByParent();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(5_000);
//delete certificate #44 (finish)

//delete gateway #99 (start)
        std = pc.deleteGatewayByName(gName99);
        Thread.sleep(1_000);
        std.clickYesGateByParent();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(5_000);
//delete gateway #99 (finish)

//delete certificate #99 (start)
        std = pc.deleteCertificateByName(cName99);
        Thread.sleep(1_000);
        std.clickYesCertByParent();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(5_000);
//delete certificate #99 (finish)

        pc.clickApply();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_SAVED.getNotificationText(), notificationPopup.getText());
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
        String table1after = pc.getCertTableText();
        System.out.println("________________________________");
        //System.out.println("table1after : " + table1after);
        System.out.println("________________________________");
        Assert.assertEquals(table1sourse,table1after);

        String table2after = pc.getGatewaysTableText();
        System.out.println("________________________________");
        //System.out.println("table2after : " + table2after);
        System.out.println("________________________________");
        Assert.assertEquals(table2sourse,table2after);

        String table3after = pc.getServiceTableText();
        System.out.println("________________________________");
        //System.out.println("table3after : " + table3after);
        System.out.println("________________________________");
        Assert.assertEquals(table3sourse,table3after);
//Check saved config (finish)

    }
}
