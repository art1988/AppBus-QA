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

public class ProvisionConfigCreateCertN2
{
    @Test
    public void ProvisionConfigCreateCertN2() throws InterruptedException
    {
        ProvisionConfigCreateCertN2(true);
    }

    public void ProvisionConfigCreateCertN2(boolean refresh) throws InterruptedException
    {

        String cName = "crtAutoName02";
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

        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigCreateCertN2: noProblems = " + noProblems);

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

        AddNewProvConfig addPop = pc.clickAddConfig();
        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigCreateCertN2: Click Tomorrow Day in calendar", addPop.clickTomorrowDay());
        Thread.sleep(1_000);
        String tomorrow = addPop.getStartTimeValue();
        Thread.sleep(1_000);
        addPop.clickOk();

        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigCreateCertN2: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

        Thread.sleep(1_000);
        pc.clickApply();
        Thread.sleep(3_000);
        Assert.assertTrue("ProvisionConfigCreateCertN2: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());
        Thread.sleep(1_000);

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);
        String tomorrowSaved = pc.getStartTimeValue();

        Assert.assertEquals("ProvisionConfigCreateCertN2: entered StartTime value is equal to saved StartTime value", tomorrow, tomorrowSaved);

        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCreateCertN2: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType);
        cd.setCertificateName(cName);
        Assert.assertTrue("ProvisionConfigCreateCertN2: Password field is no active for \"der\" type Certificate:", !cd.ifCertPassFieldActive());
        cd.clickSave();
        Thread.sleep(1_000);

        String result = pc.getCertTableContent();
        boolean success = result.contains(cName) && result.contains(cType) && result.contains("images/ok-mark");

        Assert.assertTrue("ProvisionConfigCreateCertN2: Verify Certificate fields content :", success);
        Thread.sleep(1_000);
    }
}
