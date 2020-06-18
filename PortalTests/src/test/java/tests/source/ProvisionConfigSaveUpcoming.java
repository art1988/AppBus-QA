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

public class ProvisionConfigSaveUpcoming
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigSaveUpcoming() throws InterruptedException
    {
        ProvisionConfigSaveUpcoming(true);
    }

    public void ProvisionConfigSaveUpcoming(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cName88 = "crt88AutoNm" + tmpstp.substring(4); System.out.println("cName88: " + cName88);
        String cType88 = "p12";                               System.out.println("cType88: " + cType88);
        String cPass88 = "88*^^%$^%#$#" +tmpstp.substring(4); System.out.println("cPass88: " + cPass88);

        String gName88 = "gat88AutoNm" + tmpstp.substring(4); System.out.println("gName88: " + gName88);
        String gPort88 = "88";                                System.out.println("gPort88: " + gPort88);
        String gHost88 = "lingvoexpert.com";                  System.out.println("gHost88: " + gHost88);

        String gName22 = "gat22AutoNm" + tmpstp.substring(4); System.out.println("gName22: " + gName22);
        String gPort22 = "22";                                System.out.println("gPort22: " + gPort22);
        String gHost22 = "lingvoexpert.com";                  System.out.println("gHost22: " + gHost22);

        String sName88 = "ser88AutoNm" + tmpstp.substring(4); System.out.println("sName88: " + sName88);

        String aName88 = "arc88AutoNm" + tmpstp.substring(4); System.out.println("aName88: " + aName88);
        String aDesc88 = "arc88AutoDs" + tmpstp.substring(4); System.out.println("aDesc88: " + aDesc88);

        String pName88 = "pol88AutoNm" + tmpstp.substring(4); System.out.println("pName88: " + pName88);
        String pDesc88 = "pol88AutoDs" + tmpstp.substring(4); System.out.println("pDesc88: " + pDesc88);
        String pValu88 = "pValu88Auto" + tmpstp.substring(4); System.out.println("pValu88: " + pValu88);

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

//Create Archetype (start)
        Thread.sleep(2_000);
        Archetypes archetPage = headerMenu.clickArchetypes(doPortalWakeUp);
        ArchetypesDetails archetDTLS = archetPage.addNewArchetype();
        archetDTLS.setName(aName88);
        archetDTLS.setDescription(aDesc88);
        archetDTLS.clickAdd();
//Create Archetype (finish)

//Create CONTROLLER Policy (start)
        Thread.sleep(2_000);
        Policies policyPage = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        PolicyDetail policyDTLS = policyPage.addPolicy();
        Thread.sleep(1_000);
        policyDTLS.setName(pName88);
        Thread.sleep(1_000);
        policyDTLS.setDescription(pDesc88);
        Thread.sleep(1_000);
        policyDTLS.setType("TEXT");
        Thread.sleep(1_000);
        policyDTLS.checkGroup();
        Thread.sleep(1_000);
        policyDTLS.checkItem(); //again checkItem due to setType("STRATUM") unchecks Item
        Thread.sleep(1_000);
        policyDTLS.addItemProperty(aName88, "CONTROLLER", true, false);
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

//analyze Upcoming config if exists (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigSaveUpcoming: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("Create please Upcoming config if it does not exist, it exists (?):",ItemLIst.contains("Upcoming config"));

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);

        String table1before = pc.getCertTableText();
        //System.out.println("table1before : " + table1before);
        String table2before = pc.getGatewaysTableText();
        //System.out.println("table2before : " + table2before);
        String table3before = pc.getServiceTableText();
        //System.out.println("table3before : " + table3before);
//analyze Upcoming config if exists (finish)


//add Instances with Apply (start)
//add Certificate #88 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigSaveUpcoming: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType88);
        cd.setCertificateName(cName88);
        cd.setCertPassword(cPass88);
        cd.clickSave();
        Thread.sleep(2_000);

        String result1 = pc.getCertTableText();
        System.out.println("result1 : " + result1);
        //boolean success1 = result1.contains(cPass77) && result1.contains(cName77) && result1.contains(cType77);
        //Assert.assertTrue("ProvisionConfigDiscardChanges: Verify Certificate fields content :", success1);
        Thread.sleep(1_000);
//add Certificate #88 (finish)

//add Gateway #88 (start)
        GatewayDetails gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName88);
        Thread.sleep(1_000);
        gd.setClientCertificateByName(cName88);
        Thread.sleep(1_000);
        gd.setTrustCertificateByName(cName88);
        Thread.sleep(1_000);
        gd.setPort("0000000" + gPort88);
        Thread.sleep(1_000);
        gd.setHost(gHost88);
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(3_000);
//add Gateway #88 (finish)

//check saved data (start)
        //String row1 = gName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayClient\">" + cName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayTrust\">" + cName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayPort\">" + gPort00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayHost\">" + gHost00;
        String content = pc.getGatewaysTableText();
        System.out.println("content : " + content);
        //boolean success = content.contains(row1);
        //Assert.assertTrue("ProvisionConfigDiscardChanges: row1 should be in the page",success);
//check saved data (finish)

//add Gateway #22 (start)
        gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName22);
        Thread.sleep(1_000);
        gd.setClientCertificateByName(cName88);
        Thread.sleep(1_000);
        gd.setTrustCertificateByName(cName88);
        Thread.sleep(1_000);
        gd.setPort("0000000" + gPort22);
        Thread.sleep(1_000);
        gd.setHost(gHost22);
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(3_000);
//add Gateway #22 (finish)

//add Service #88 (start)
        Thread.sleep(1_000);
        ServiceDetails sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName88);
        Thread.sleep(1_000);
        AddPolicy ap = sd.clickAddPolicy();
        Thread.sleep(1_000);
        ap.selectPolicy(pName88);
        Thread.sleep(1_000);
        ap.clickOk();
        Thread.sleep(1_000);
        sd.setGatewayByName(gName88);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(pValu88);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #88 (finish)

//delete gateway #22 - C18151 (was C2767) case on testrail (start)
        SureToDelete std = pc.deleteGatewayByName(gName22);
        Thread.sleep(1_000);
        std.clickYesGateByParent();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(5_000);

//delete gateway #22 - C18151 (was C2767) case on testrail (start)

        String content00 = pc.getServiceTableText();
        System.out.println("content00 : " + content00);
        //boolean success00 = content00.contains(sName77) && content00.contains(gName77) && content00.contains(pValu77) && content00.contains(pName77);
        //Assert.assertTrue("ProvisionConfigDiscardChanges: Service #1, Policy and Policy value should be in the page",success00);

        pc.clickApply();
        Thread.sleep(5_000);
//add Instances with Apply (finish)

//check just saved Upcoming config changes (start)
        pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigDiscardChanges: noProblems = " + noProblems);

        pc.clickSelectConfiguration();
        pc.clickCurrentConfig();
        Thread.sleep(2_000);
        pc.clickSelectConfiguration();
        Thread.sleep(2_000);
        pc.clickUpcomingConfig();
        Thread.sleep(1_000);

        String table1after = pc.getCertTableText();
        String table1aft88= cName88 + cType88 + cPass88;
        System.out.println("________________________________");
        System.out.println("table1after : " + table1after);
        System.out.println("________________________________");
        Assert.assertTrue(table1after.contains(table1before.substring(0,130)) && table1after.contains(table1aft88));
        String table2after = pc.getGatewaysTableText();
        String table2aft88 = gName88 + cName88 + cName88 + gPort88 + gHost88;
        System.out.println("________________________________");
        System.out.println("table2after : " + table2after);
        System.out.println("________________________________");
        Assert.assertTrue(table2after.contains(table2before) && table2after.contains(table2aft88));
        String table3after = pc.getServiceTableText();
        String table3aft88 = sName88 + "gate" + gName88 + pName88 + pValu88;
        System.out.println("________________________________");
        System.out.println("table3after : " + table3after);
        System.out.println("________________________________");
        Assert.assertTrue(table3after.contains(table3before) && table3after.contains(table3aft88));

//check just saved Upcoming config changes (finish)

//try to delete gateway #88 - C18151 (was C2767) case on testrail (start)
        std = pc.deleteGatewayByName(gName88);
        Thread.sleep(1_000);
        std.clickYesGateByParent();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.UNABLE_TO_REMOVE_GATEWAY.getNotificationText(), notificationPopup.getText());
        Thread.sleep(5_000);

//try to delete gateway #88 - C18151 (was C2767) case on testrail (start)

//Delete CONTROLLER Policy #1 (start)
        Thread.sleep(1_000);
        Policies  policyPgForDel = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        //PolicyDetail editDTLS = policyPage.clickEdit(policyName1);
        Thread.sleep(1_000);
        //editDTLS.checkItem();
        Thread.sleep(1_000);
        //editDTLS.clickSave();
        Thread.sleep(2_000);
        policyPgForDel.searchForName(pName88);
        Thread.sleep(2_000);
        policyPgForDel.clickApplyFilter();
        Thread.sleep(2_000);
        DeletePolicyConfirmation popP = policyPgForDel.clickFirstDeleteIcon();
        Thread.sleep(1_000);
        popP.clickYes();
        Thread.sleep(1_000);
//Delete CONTROLLER Policy #1 (finish)

//Delete Archetype1 (start)
        Thread.sleep(2_000);
        Archetypes archetPgForDel = headerMenu.clickArchetypes(doPortalWakeUp);
        Thread.sleep(1_000);
        archetPage.selectArchetype(aName88);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted popupDel = archetPgForDel.deleteArchetype();
        Thread.sleep(1_000);
        popupDel.clickDelete();
        Thread.sleep(1_000);
//Delete Archetype1 (finish)

    }
}
