package tests.source;

import static tests.source.FunctionalTest.driver;
import net.portal.forms.*;
import net.portal.pages.device_management.ProvisioningConfig;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;


public class ProvisionConfigEditCertifiUpcom
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigEditCertifiUpcom() throws InterruptedException
    {
        ProvisionConfigEditCertifiUpcom(true);
    }

    public void ProvisionConfigEditCertifiUpcom(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cType55 = "p12";                                      System.out.println("cType55: " + cType55);
        String cName55 = "crtAuto55Name" + tmpstp.substring(4);      System.out.println("cName55: " + cName55);
        String cPass55 = "unique55Pass@##$#" + tmpstp.substring(4);  System.out.println("cPass55: " + cPass55);

        String cType56 = "p12";                                      System.out.println("cType56: " + cType56);
        String cName56 = "crtAuto56Name" + tmpstp.substring(4);      System.out.println("cName56: " + cName56);
        String cPass56 = "unique56Pass@##$#" + tmpstp.substring(4);  System.out.println("cPass56: " + cPass56);

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
        System.out.println("ProvisionConfigEditCertifiUpcom: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigEditCertifiUpcom: create please Upcoming config if one doesn't exist", ItemLIst.contains("Upcoming config"));
//stop script if Upcoming config doesn't exist (finish)

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);

//stop script if number of certs less than 3 (start)
        int certificateNum = pc.getCertificNumber();
        Assert.assertTrue("ProvisionConfigEditCertifiUpcom: create please Certificates more if their number less than 3", certificateNum > 2);
//stop script if number of certs less than 3 (finish)

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


//edit Certificate #55 (start)
        CertificateDetails cd = pc.clickEditTheFirstCertifi();
        Thread.sleep(1_000);

        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(2_000);
        cd.setCertificateType(cType55);
        cd.setCertificateName(cName55);
        Thread.sleep(1_000);
        cd.setCertPassword(cPass55);
        cd.clickSave();
        Thread.sleep(3_000);
//edit Certificate #55 (finish)

//edit Certificate #56 (start)
        cd = pc.clickEditTheSecondCertifi();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(2_000);
        cd.setCertificateType(cType56);
        cd.setCertificateName(cName56);
        Thread.sleep(1_000);
        cd.setCertPassword(cPass56);
        cd.clickSave();
        Thread.sleep(3_000);
//edit Certificate #56 (finish)

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

        int cerNumber = pc.getCertificNumber();

        for (int i = 0; i < cerNumber; i++)
        {
            String rowText = pc.getCertifiRowText(i);
            if (rowText.contains(cName55))
            {
                Assert.assertTrue(rowText.contains(cType55) && rowText.contains(cPass55));
            }

            if (rowText.contains(cName56))
            {
                Assert.assertTrue(rowText.contains(cType56) && rowText.contains(cPass56));
            }
        }
    }
}
