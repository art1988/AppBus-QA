package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.forms.AddNewProvConfig;
import net.portal.forms.CertificateDetails;
import net.portal.forms.SureToDelete;
import net.portal.pages.device_management.ProvisioningConfig;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;

public class ProvisionConfigCreateCertN6
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigCreateCertN6() throws InterruptedException
    {
        ProvisionConfigCreateCertN6(true);
    }

    public void ProvisionConfigCreateCertN6(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cName01 = "crt01AutoName" + tmpstp.substring(4); System.out.println("cName01: " + cName01);
        String cType01 = "p12";                                 System.out.println("cType01: " + cType01);
        String cPass01 = "01*^^%$^%#$#" +  tmpstp.substring(4); System.out.println("cPass01: " + cPass01);

        String cName02 = "crt02AutoName" + tmpstp.substring(4); System.out.println("cName02: " + cName02);
        String cType02 = "p12";                                 System.out.println("cType02: " + cType02);
        String cPass02 = "02*^^%$^%#$#" +  tmpstp.substring(4); System.out.println("cPass02: " + cPass02);

        String cName03 = "crt03AutoName" + tmpstp.substring(4); System.out.println("cName03: " + cName03);
        String cType03 = "der";                                 System.out.println("cType03: " + cType03);

        String cName04 = "crt04AutoName" + tmpstp.substring(4); System.out.println("cName04: " + cName04);
        String cType04 = "der";                                 System.out.println("cType04: " + cType04);

        String cName05 = "crt05AutoName" + tmpstp.substring(4); System.out.println("cName04: " + cName05);
        String cType05 = "der";

        String cName06 = "crt06AutoName" + tmpstp.substring(4); System.out.println("cName04: " + cName06);
        String cType06 = "der";

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


        //add Config without saving of Certs (start)
        AddNewProvConfig addPop = pc.clickAddConfig();
        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigCreateCertN6: Click Tomorrow Day in calendar", addPop.clickTomorrowDay());
        Thread.sleep(1_000);
        String tomorrow = addPop.getStartTimeValue();
        Thread.sleep(1_000);
        addPop.clickOk();

        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigCreateCertN6: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

        Thread.sleep(1_000);
        pc.clickApply();
        Thread.sleep(3_000);
        Assert.assertTrue("ProvisionConfigCreateCertN6: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());
        Thread.sleep(1_000);

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);
        String tomorrowSaved = pc.getStartTimeValue();

        Assert.assertEquals("ProvisionConfigCreateCertN6: entered StartTime value is equal to saved StartTime value", tomorrow, tomorrowSaved);

        //add Certificate #01 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCreateCertN6: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType01);
        cd.setCertificateName(cName01);
        cd.setCertPassword(cPass01);
        cd.clickSave();
        Thread.sleep(1_000);

        String result1 = pc.getCertTableContent();
        boolean success1 = result1.contains(cPass01) && result1.contains(cName01) && result1.contains(cType01);

        Assert.assertTrue("ProvisionConfigCreateCertN6: Verify Certificate fields content :", success1);
        Thread.sleep(1_000);
        //add Certificate #01 (finish)

        //add Certificate #02 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCreateCertN6: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType02);
        cd.setCertificateName(cName02);
        cd.setCertPassword(cPass02);
        cd.clickSave();
        Thread.sleep(1_000);

        String result2 = pc.getCertTableContent();
        boolean success2 = result2.contains(cPass02) && result2.contains(cName02) && result2.contains(cType02);

        Assert.assertTrue("ProvisionConfigCreateCertN6: Verify Certificate fields content :", success2);
        Thread.sleep(1_000);
        //add Certificate #02 (finish)

        //add Certificate #03 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCreateCertN6: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType03);
        cd.setCertificateName(cName03);
        Assert.assertTrue("ProvisionConfigCreateCertN6: Password field is no active for \"der\" type Certificate:", !cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        String result3 = pc.getCertTableContent();
        boolean success3 = result3.contains(cName03) && result3.contains(cType03) && result3.contains("images/ok-mark");

        Assert.assertTrue("ProvisionConfigCreateCertN6: Verify Certificate fields content :", success3);
        Thread.sleep(1_000);
        //add Certificate #03 (finish)

        //add Certificate #04 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCreateCertN6: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType04);
        cd.setCertificateName(cName04);
        Assert.assertTrue("ProvisionConfigCreateCertN6: Password field is no active for \"der\" type Certificate:", !cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        String result4 = pc.getCertTableContent();
        boolean success4 = result4.contains(cName04) && result4.contains(cType04) && result4.contains("images/ok-mark");

        Assert.assertTrue("ProvisionConfigCreateCertN6: Verify Certificate fields content :", success4);
        Thread.sleep(1_000);
        //add Certificate #04 (finish)

        //add Certificate #05 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCreateCertN6: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType05);
        cd.setCertificateName(cName05);
        Assert.assertTrue("ProvisionConfigCreateCertN6: Password field is no active for \"der\" type Certificate:", !cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        String result5 = pc.getCertTableContent();
        boolean success5 = result5.contains(cName05) && result5.contains(cType05) && result5.contains("images/ok-mark");

        Assert.assertTrue("ProvisionConfigCreateCertN6: Verify Certificate fields content :", success5);
        Thread.sleep(1_000);
        //add Certificate #05 (finish)

        //add Certificate #06 (start)
        cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCreateCertN6: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType06);
        cd.setCertificateName(cName06);
        Assert.assertTrue("ProvisionConfigCreateCertN6: Password field is no active for \"der\" type Certificate:", !cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        String result6 = pc.getCertTableContent();
        boolean success6 = result6.contains(cName06) && result6.contains(cType06) && result6.contains("images/ok-mark");

        Assert.assertTrue("ProvisionConfigCreateCertN6: Verify Certificate fields content :", success6);
        Thread.sleep(1_000);
        //add Certificate #06 (finish)


        //add Config without saving of Certs (finish)
    }
}
