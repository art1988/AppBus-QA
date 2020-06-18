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


public class ProvisionConfigCrtCertInCurren1
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    static final SimpleDateFormat pf = new SimpleDateFormat("MM/dd/YY");

    @Test
    public void ProvisionConfigCrtCertInCurren1() throws InterruptedException
    {
        ProvisionConfigCrtCertInCurren1(true);
    }

    public void ProvisionConfigCrtCertInCurren1(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());

        String mmddyy = pf.format(System.currentTimeMillis()-24*60*60*1000); //yesterday
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        //String cPass = "uniq98Pass@##$#";
        String cName = "crtAutoName98" + tmpstp;
        String cType = "der";


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
        System.out.println("ProvisionConfigCrtCertInCurren1: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigCrtCertInCurren1: create please Current config if one doesn't exist", ItemLIst.contains("Current config"));
//stop script if Current config doesn't exist (finish)

        System.out.println("ProvisionConfigCrtCertInCurren1: going to select Current config");
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


        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCrtCertInCurren1: Data uploaded mark hasn't been change to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType);
        cd.setCertificateName(cName);
        Assert.assertTrue("ProvisionConfigCrtCertInCurren1: Cert Pass field should be disabled :", !cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        String result = pc.getCertTableContent();
        boolean success = result.contains(cName) && result.contains(cType);

        Assert.assertTrue("ProvisionConfigCrtCertInCurren1: Verify Certificate fields content :", success);
        Thread.sleep(1_000);
        pc.clickApply();
        Thread.sleep(2_000);

        System.out.println("ProvisionConfigCrtCertInCurren1: going to select Current config");
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

        //Assert.assertTrue("ProvisionConfigCrtCertInCurrent: Certificates table is the same:",table1after.contains(table1sourse));

        Assert.assertTrue("ProvisionConfigCrtCertInCurren2: Gateways table is the same:",table2after.equals(table2sourse));

        Assert.assertTrue("ProvisionConfigCrtCertInCurren2: Services table is the same:",table3after.equals(table3sourse));

    }
}
