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


public class ProvisionConfigDownloadCertOfCr
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigDownloadCertOfCr() throws InterruptedException
    {
        ProvisionConfigDownloadCertOfCr(true);
    }

    public void ProvisionConfigDownloadCertOfCr(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
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

//stop script if Current config doesn't exist (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigDownloadCertOfCr: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigDownloadCertOfCr: create please Current config if one doesn't exist", ItemLIst.contains("Current config"));
//stop script if Upcoming config doesn't exist (finish)

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);

        String fileName = pc.downloadTheFirstCert();
        Thread.sleep(5_000);
        File certificateFile = new File(Const.DOWNLOAD_FOLDER + "\\" + fileName);
        Assert.assertTrue(certificateFile.exists());
        Thread.sleep(1_000);
        certificateFile.delete();
        Thread.sleep(1_000);

        System.out.println("ProvisionConfigDownloadCertOfCr: Certificate file has just been downloaded and then deleted.");
    }
}
