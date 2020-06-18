package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.*;
import net.portal.pages.device_management.ProvisioningConfig;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;


public class ProvisionConfigCrtCertInCurren5
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    static final SimpleDateFormat pf = new SimpleDateFormat("MM/dd/YY");

    @Test
    public void ProvisionConfigCrtCertInCurren5() throws InterruptedException
    {
        ProvisionConfigCrtCertInCurren5(true);
    }

    public void ProvisionConfigCrtCertInCurren5(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());

        String mmddyy = pf.format(System.currentTimeMillis()-24*60*60*1000); //yesterday
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String c1Name = "crt1Name" + tmpstp;
        String c1Type = "der";
        System.out.println("c1Name + c1Type : " + c1Name + c1Type);

        String c2Name = "crt2Name" + tmpstp;
        String c2Type = "der";
        System.out.println("c2Name + c2Type : " + c2Name + c2Type);

        String c3Name = "crt3Name" + tmpstp;
        String c3Type = "p12";
        String c3Pass = "3Pass@##$#";
        System.out.println("c3Name + c3Type + c3Pass : " + c3Name + c3Type + c3Pass);

        String c4Name = "crt4Name" + tmpstp;
        String c4Type = "p12";
        String c4Pass = "4Pass@##$#";
        System.out.println("c4Name + c4Type + c4Pass : " + c4Name + c4Type + c4Pass);

        String c5Name = "crt5Name" + tmpstp;
        System.out.println("c5Name : " + c5Name);

        String c6Name = "crt6Name" + tmpstp;
        System.out.println("c6Name : " + c6Name);

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
        System.out.println("ProvisionConfigCrtCertInCurren5: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: create please Current config if one doesn't exist", ItemLIst.contains("Current config"));
//stop script if Current config doesn't exist (finish)

        System.out.println("ProvisionConfigCrtCertInCurren5: going to select Current config");
        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);

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

//Create Certificate #1 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(c1Type);
        cd.setCertificateName(c1Name);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Cert Pass field should be disabled :", !cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        String result = pc.getCertTableContent();
        boolean success = result.contains(c1Name) && result.contains(c1Type);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Verify Certificate #1 fields content :", success);
//Create Certificate #1 (finish)

//Create Certificate #2 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(c2Type);
        cd.setCertificateName(c2Name);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Cert Pass field should be disabled :", !cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        result = pc.getCertTableContent();
        success = result.contains(c2Name) && result.contains(c2Type);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Verify Certificate #2 fields content :", success);
//Create Certificate #2 (finish)

//Create Certificate #3 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(c3Type);
        cd.setCertificateName(c3Name);
        cd.setCertPassword(c3Pass);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Cert Pass field should be enaabled :", cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        result = pc.getCertTableContent();
        success = result.contains(c3Name) && result.contains(c3Type) && result.contains(c3Pass);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Verify Certificate #3 fields content :", success);
//Create Certificate #3 (finish)

//Create Certificate #4 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(c4Type);
        cd.setCertificateName(c4Name);
        cd.setCertPassword(c4Pass);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Cert Pass field should be enaabled :", cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        result = pc.getCertTableContent();
        success = result.contains(c4Name) && result.contains(c4Type) && result.contains(c4Pass);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Verify Certificate #4 fields content :", success);
//Create Certificate #4 (finish)

//Create Certificate #5 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);

        cd.setCertificateName(c5Name);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Cert Pass field should be enaabled :", !cd.ifCertPassFieldActive());
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Data uploaded mark didn't change to Ok (true/false):", cd.ifNoUploadedIcon());
        cd.clickSave();

        WebElement notificationPopup = (new WebDriverWait(driver, 4)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.CERTIFICATE_IS_EMPTY.getNotificationText(), notificationPopup.getText());

        Thread.sleep(1_000);
        cd.clickCancel();
        Thread.sleep(1_000);

        result = pc.getCertTableContent();
        success = !result.contains(c5Name);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Verify Certificate #5 fields content :", success);
//Create Certificate #5 (finish)

//Create Certificate #6 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);

        cd.setCertificateName(c6Name);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Cert Pass field should be enaabled :", !cd.ifCertPassFieldActive());
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Data uploaded mark didn't change to Ok (true/false):", cd.ifNoUploadedIcon());
        cd.clickSave();

        notificationPopup = (new WebDriverWait(driver, 4)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.CERTIFICATE_IS_EMPTY.getNotificationText(), notificationPopup.getText());

        Thread.sleep(1_000);
        cd.clickCancel();
        Thread.sleep(1_000);

        result = pc.getCertTableContent();
        success = !result.contains(c6Name);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Verify Certificate #6 fields content :", success);
//Create Certificate #6 (finish)


        Thread.sleep(1_000);
        pc.clickApply();
        Thread.sleep(2_000);

        System.out.println("ProvisionConfigCrtCertInCurren5: going to select Current config");
        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);

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

        boolean sertTab = table1after.contains(c1Name) && table1after.contains(c2Name) && table1after.contains(c3Name) && table1after.contains(c4Name)
                && !table1after.contains(c5Name) && !table1after.contains(c6Name) && table1after.contains(c3Pass) && table1after.contains(c4Pass);

        Assert.assertTrue("ProvisionConfigCrtCertInCurrent: Certificates table has new parms:",sertTab);

        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Gateways table is the same:",table2after.equals(table2sourse));

        Assert.assertTrue("ProvisionConfigCrtCertInCurren5: Services table is the same:",table3after.equals(table3sourse));

    }
}
