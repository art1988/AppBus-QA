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


public class ProvisionConfigCrtCertAndGatInC
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    static final SimpleDateFormat pf = new SimpleDateFormat("MM/dd/YY");

    @Test
    public void ProvisionConfigCrtCertAndGatInC() throws InterruptedException
    {
        ProvisionConfigCrtCertAndGatInC(true);
    }

    public void ProvisionConfigCrtCertAndGatInC(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());

        String mmddyy = pf.format(System.currentTimeMillis()-24*60*60*1000); //yesterday
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cPass = "00uniqPass@##$#";                       System.out.println("cPass: " + cPass);
        String cName = "00crtAutoName" + tmpstp;                System.out.println("cName: " + cName);
        String cType = "p12";                                   System.out.println("cType: " + cType);

        String gName01 = "gat00AutoName" + tmpstp.substring(4); System.out.println("gName01: " + gName01);
        String gPort01 = "1";                                   System.out.println("gPort01: " + gPort01);
        String gHost01 = "https://time.is/";                    System.out.println("gHost01: " + gHost01);

        String gName02 = "gat01AutoName" + tmpstp.substring(4); System.out.println("gName02: " + gName02);
        String gPort02 = "2";                                   System.out.println("gPort02: " + gPort02);
        String gHost02 = "https://restcountries.eu/";           System.out.println("gHost02: " + gHost02);

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
        System.out.println("ProvisionConfigCrtCertAndGatInC: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigCrtCertAndGatInC: create please Current config if one doesn't exist", ItemLIst.contains("Current config"));
//stop script if Current config doesn't exist (finish)

        System.out.println("ProvisionConfigCrtCertAndGatInC: going to select Current config");
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

//Add Certificate #1 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCrtCertAndGatInC: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType);
        cd.setCertificateName(cName);
        cd.setCertPassword(cPass);
        cd.clickSave();
        //System.out.println("going to sleep for 100 secs");
        Thread.sleep(2_000);

        String result = pc.getCertTableContent();
        boolean success = result.contains(cPass) && result.contains(cName) && result.contains(cType);

        Assert.assertTrue("ProvisionConfigCrtCertAndGatInC: Verify Certificate fields content :", success);
        Thread.sleep(1_000);
//Add Certificate #1 (finish)

//add Gateway #01 (start)
        GatewayDetails gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName01);
        Thread.sleep(1_000);
        gd.setClientCertificateByName(cName);
        Thread.sleep(1_000);
        gd.setTrustCertificateByName(cName);
        Thread.sleep(1_000);
        gd.setPort("Z" + gPort01);
        Thread.sleep(1_000);
        gd.clickSaveForNoteCheck();

        WebElement notificationPopup = (new WebDriverWait(driver, 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.INVALID_FORMAT_OR_VALUE.getNotificationText(), notificationPopup.getText());

        gd.setPort("00" + gPort01);
        Thread.sleep(1_000);
        gd.setHost(gHost01);
        Thread.sleep(2_000);
        gd.clickSave();
        Thread.sleep(2_000);
//add Gateway #01 (finish)

//add Gateway #02 (start)
        gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName02);
        Thread.sleep(1_000);
        gd.setClientCertificateByName(cName);
        Thread.sleep(1_000);
        gd.setTrustCertificateByName(cName);
        Thread.sleep(1_000);
        gd.setPort("0000" + gPort02);
        Thread.sleep(1_000);
        gd.setHost(gHost02);
        Thread.sleep(2_000);
        gd.clickSave();
        Thread.sleep(2_000);
//add Gateway #02 (finish)

//Apply (start)
        pc.clickApply();
        Thread.sleep(2_000);

        System.out.println("ProvisionConfigCrtCertAndGatInC: going to select Current config");
        pc.clickSelectConfiguration(); //f
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);
//Apply (finish)

//Check Current config after (start)
        String table1afterRow = pc.getCertTableRowText(cName);
        System.out.println("________________________________");
        System.out.println("table1afterRow : " + table1afterRow);
        System.out.println("________________________________");

        String table2afterRow1 = pc.getGatewayTableRowText(gName01);
        System.out.println("________________________________");
        System.out.println("table2afterRow1 : " + table2afterRow1);
        System.out.println("________________________________");

        String table2afterRow2 = pc.getGatewayTableRowText(gName02);
        System.out.println("________________________________");
        System.out.println("table2afterRow2 : " + table2afterRow2);
        System.out.println("________________________________");

        String table3after = pc.getServiceTableText();
        System.out.println("________________________________");
        System.out.println("table3after : " + table3after);
        System.out.println("________________________________");
//Check Current config after (finish)

        Assert.assertTrue("ProvisionConfigCrtCertInCurrent: Certificates table is updated:",table1afterRow.contains(cPass) && table1afterRow.contains(cType));

        Assert.assertTrue("ProvisionConfigCrtCertInCurrent: Gateways table is updated by Gateway #1:",table2afterRow1.contains(cName) && table2afterRow1.contains(gHost01) && table2afterRow1.contains(gPort01));
        Assert.assertTrue("ProvisionConfigCrtCertInCurrent: Gateways table is updated by Gateway #2:",table2afterRow2.contains(cName) && table2afterRow2.contains(gHost02) && table2afterRow2.contains(gPort02));

        Assert.assertTrue("ProvisionConfigCrtCertAndGatInC: Services table is the same:",table3after.equals(table3sourse));

    }
}
