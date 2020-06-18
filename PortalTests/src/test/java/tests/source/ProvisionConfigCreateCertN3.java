package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.constants.Notifications;
import net.portal.forms.AddNewProvConfig;
import net.portal.forms.CertificateDetails;
import net.portal.forms.SureToDelete;
import net.portal.pages.device_management.ProvisioningConfig;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class ProvisionConfigCreateCertN3
{
    @Test
    public void ProvisionConfigCreateCertN3() throws InterruptedException
    {
        ProvisionConfigCreateCertN3(true);
    }

    public void ProvisionConfigCreateCertN3(boolean refresh) throws InterruptedException
    {

        String cName = "crtAutoName03";

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
        System.out.println("ProvisionConfigCreateCertN3: noProblems = " + noProblems);

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
        Assert.assertTrue("ProvisionConfigCreateCertN3: Click Tomorrow Day in calendar", addPop.clickTomorrowDay());
        Thread.sleep(1_000);
        String tomorrow = addPop.getStartTimeValue();
        Thread.sleep(1_000);
        addPop.clickOk();

        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigCreateCertN3: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

        Thread.sleep(1_000);
        pc.clickApply();
        Thread.sleep(3_000);
        Assert.assertTrue("ProvisionConfigCreateCertN3: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());
        Thread.sleep(1_000);

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);
        String tomorrowSaved = pc.getStartTimeValue();

        Assert.assertEquals("ProvisionConfigCreateCertN3: entered StartTime value is equal to saved StartTime value", tomorrow, tomorrowSaved);

        String before = pc.getCertTableContent();

        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);

        cd.setCertificateName(cName);
        Assert.assertTrue("ProvisionConfigCreateCertN3: Password field is no active for \"der\" type Certificate:", !cd.ifCertPassFieldActive());
        cd.clickSave();
        WebElement notificationPopup = (new WebDriverWait(driver, 4)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.CERTIFICATE_IS_EMPTY.getNotificationText(), notificationPopup.getText());
        Thread.sleep(2_000);
        cd.clickCancel();
        Thread.sleep(1_000);

        String result = pc.getCertTableContent();
        boolean success = result.equals(before);

        Assert.assertTrue("ProvisionConfigCreateCertN3: Verify Certificate fields content :", success);
        Thread.sleep(1_000);
    }
}
