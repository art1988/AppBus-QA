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

public class ProvisionConfigDelServFromUpcomn
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigDelServFromUpcomn() throws InterruptedException
    {
        ProvisionConfigDelServFromUpcomn(true);
    }

    public void ProvisionConfigDelServFromUpcomn(boolean refresh) throws InterruptedException
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

        String sName44 = "ser44AutoNm" + tmpstp.substring(4); System.out.println("sName44: " + sName44);
        String sName99 = "ser99AutoNm" + tmpstp.substring(4); System.out.println("sName99: " + sName99);

        String aName99 = "arc99AutoNm" + tmpstp.substring(4); System.out.println("aName99: " + aName99);
        String aDesc99 = "arc99AutoDs" + tmpstp.substring(4); System.out.println("aDesc99: " + aDesc99);

        String pName99 = "pol99AutoNm" + tmpstp.substring(4); System.out.println("pName99: " + pName99);
        String pDesc99 = "pol99AutoDs" + tmpstp.substring(4); System.out.println("pDesc99: " + pDesc99);
        String pValu99 = "pValu99Auto" + tmpstp.substring(4); System.out.println("pValu99: " + pValu99);

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
        System.out.println("ProvisionConfigDelServFromUpcomn: noProblems = " + noProblems);

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

        Assert.assertTrue("ProvisionConfigDelServFromUpcomn: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

//Create Archetype (start)
        Thread.sleep(2_000);
        Archetypes archetPage = headerMenu.clickArchetypes(doPortalWakeUp);
        ArchetypesDetails archetDTLS = archetPage.addNewArchetype();
        archetDTLS.setName(aName99);
        archetDTLS.setDescription(aDesc99);
        archetDTLS.clickAdd();
//Create Archetype (finish)

//Create CONTROLLER Policy (start)
        Thread.sleep(2_000);
        Policies policyPage = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        PolicyDetail policyDTLS = policyPage.addPolicy();
        Thread.sleep(1_000);
        policyDTLS.setName(pName99);
        Thread.sleep(1_000);
        policyDTLS.setDescription(pDesc99);
        Thread.sleep(1_000);
        policyDTLS.setType("TEXT");
        Thread.sleep(1_000);
        policyDTLS.checkGroup();
        Thread.sleep(1_000);
        policyDTLS.checkItem(); //again checkItem due to setType("STRATUM") unchecks Item
        Thread.sleep(1_000);
        policyDTLS.addItemProperty(aName99, "CONTROLLER", true, false);
        Thread.sleep(1_000);
        policyDTLS.checkGroupRequired();
        Thread.sleep(1_000);
        policyDTLS.checkDevice();
        Thread.sleep(1_000);
        policyDTLS.checkGroupMultiple();
        Thread.sleep(1_000);
        policyDTLS.checkDeviceMultiple();
        Thread.sleep(1_000);
        policyDTLS.checkProvision();
        Thread.sleep(3_000);
        policyDTLS.clickAdd();
        Thread.sleep(1_000);
//Create CONTROLLER Policy (finish)

        pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigDelServFromUpcomn: noProblems = " + noProblems);

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);
        pc.clickSelectConfiguration();
        Thread.sleep(2_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);

//add Certificate #44 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(10_000);

        Assert.assertTrue("ProvisionConfigDelServFromUpcomn: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

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

        Assert.assertTrue("ProvisionConfigDelServFromUpcomn: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

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

//add Service #44 (start)
        ServiceDetails sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName44);
        Thread.sleep(1_000);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #44 (finish)

//add Service #99 (start)
        Thread.sleep(1_000);
        sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName99);
        Thread.sleep(1_000);
        AddPolicy ap = sd.clickAddPolicy();
        Thread.sleep(1_000);
        ap.selectPolicy(pName99);
        Thread.sleep(1_000);
        ap.clickOk();
        Thread.sleep(1_000);
        sd.setGatewayByName(gName99);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(pValu99);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #99 (finish)

//delete Service #44 (start)
        std = pc.deleteServiceByName(sName44);
        Thread.sleep(1_000);
        std.clickYesServByParent();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(5_000);
//delete Service #44 (finish)

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
        String table1after = pc.getCertTableText();
        table1after = table1after.replace(cName99 + cType99 + "ui-buttonDownloadui-button","");
        //crt99AutoNm4832derui-buttonDownloadui-button
        System.out.println("________________________________");
        //System.out.println("table1after : " + table1after);
        System.out.println("________________________________");
        Assert.assertTrue(table1after.equals(table1sourse));

        String table2after = pc.getGatewaysTableText();
        table2after = table2after.replace(gName99 + cName99 + cName99 + gPort99 + gHost99 + "ui-buttonui-button","");
        System.out.println("________________________________");
        //System.out.println("table2after : " + table2after);
        System.out.println("________________________________");
        Assert.assertTrue(table2after.equals(table2sourse));

        String table3after = pc.getServiceTableText();
        table3after = table3after.replace(sName99 + "gate" + gName99 + pName99 + pValu99 + "ui-buttonui-button","");
        System.out.println("________________________________");
        System.out.println("table3after : " + table3after);
        System.out.println("________________________________");
        Assert.assertTrue(table3after.equals(table3sourse));
//Check saved config (finish)

//Delete CONTROLLER Policy #99 (start)
        Thread.sleep(1_000);
        Policies  policyPgForDel = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        //PolicyDetail editDTLS = policyPage.clickEdit(policyName1);
        Thread.sleep(1_000);
        //editDTLS.checkItem();
        Thread.sleep(1_000);
        //editDTLS.clickSave();
        Thread.sleep(2_000);
        policyPgForDel.searchForName(pName99);
        Thread.sleep(2_000);
        policyPgForDel.clickApplyFilter();
        Thread.sleep(2_000);
        DeletePolicyConfirmation popP = policyPgForDel.clickFirstDeleteIcon();
        Thread.sleep(1_000);
        popP.clickYes();
        Thread.sleep(1_000);
//Delete CONTROLLER Policy #99 (finish)

//Delete Archetype99 (start)
        Thread.sleep(2_000);
        Archetypes archetPgForDel = headerMenu.clickArchetypes(doPortalWakeUp);
        Thread.sleep(1_000);
        archetPgForDel.selectArchetype(aName99);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted popupDel = archetPgForDel.deleteArchetype();
        Thread.sleep(1_000);
        popupDel.clickDelete();
        Thread.sleep(1_000);
//Delete Archetype99 (finish)

    }
}
