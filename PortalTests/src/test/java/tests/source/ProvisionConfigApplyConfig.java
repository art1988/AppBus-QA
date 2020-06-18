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

public class ProvisionConfigApplyConfig
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigApplyConfig() throws InterruptedException
    {
        ProvisionConfigApplyConfig(true);
    }

    public void ProvisionConfigApplyConfig(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cName00 = "crt00AutoNm" + tmpstp.substring(4); System.out.println("cName00: " + cName00);
        String cType00 = "p12";                               System.out.println("cType00: " + cType00);
        String cPass00 = "00*^^%$^%#$#" +tmpstp.substring(4); System.out.println("cPass00: " + cPass00);

        String gName00 = "gat00AutoNm" + tmpstp.substring(4); System.out.println("gName00: " + gName00);
        String gPort00 = "1";                                 System.out.println("gPort00: " + gPort00);
        String gHost00 = "lingvoexpert.com";                  System.out.println("gHost00: " + gHost00);

        String sName00 = "ser00AutoNm" + tmpstp.substring(4); System.out.println("sName00: " + sName00);

        String aName00 = "arc00AutoNm" + tmpstp.substring(4); System.out.println("aName00: " + aName00);
        String aDesc00 = "arc00AutoDs" + tmpstp.substring(4); System.out.println("aDesc00: " + aDesc00);

        String pName00 = "pol00AutoNm" + tmpstp.substring(4); System.out.println("pName00: " + pName00);
        String pDesc00 = "pol00AutoDs" + tmpstp.substring(4); System.out.println("pDesc00: " + pDesc00);
        String pValu00 = "pValu00Auto" + tmpstp.substring(4); System.out.println("pValu00: " + pValu00);

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
        archetDTLS.setName(aName00);
        archetDTLS.setDescription(aDesc00);
        archetDTLS.clickAdd();
//Create Archetype (finish)

//Create CONTROLLER Policy (start)
        Thread.sleep(2_000);
        Policies policyPage = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        PolicyDetail policyDTLS = policyPage.addPolicy();
        Thread.sleep(1_000);
        policyDTLS.setName(pName00);
        Thread.sleep(1_000);
        policyDTLS.setDescription(pDesc00);
        Thread.sleep(1_000);
        policyDTLS.setType("TEXT");
        Thread.sleep(1_000);
        policyDTLS.checkGroup();
        Thread.sleep(1_000);
        policyDTLS.checkItem(); //again checkItem due to setType("STRATUM") unchecks Item
        Thread.sleep(1_000);
        policyDTLS.addItemProperty(aName00, "CONTROLLER", true, false);
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
        Boolean noProblems = wkp.fixLoadBarProblem(); //LB
        Thread.sleep(1_000);
        if (!noProblems) {System.out.println("ProvisionConfigApplyConfig: Policy page is not operable!");}
//Create CONTROLLER Policy (finish)

//delete Upcoming config if exists (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigApplyConfig: noProblems = " + noProblems);

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


//add Config with Apply (start)
        AddNewProvConfig addPop = pc.clickAddConfig();
        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigApplyConfig: Click Tomorrow Day in calendar", addPop.clickTomorrowDay());
        Thread.sleep(1_000);
        String tomorrow = addPop.getStartTimeValue();
        Thread.sleep(1_000);
        addPop.clickOk();

        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigApplyConfig: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

        Thread.sleep(1_000);
        pc.clickApply();
        Thread.sleep(5_000);
        Assert.assertTrue("ProvisionConfigApplyConfig: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());
        Thread.sleep(1_000);

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);
        String tomorrowSaved = pc.getStartTimeValue();

        Assert.assertEquals("ProvisionConfigApplyConfig: entered StartTime value is equal to saved StartTime value", tomorrow, tomorrowSaved);

//add Certificate #01 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigApplyConfig: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType00);
        cd.setCertificateName(cName00);
        cd.setCertPassword(cPass00);
        cd.clickSave();
        Thread.sleep(2_000);

        String result1 = pc.getCertTableContent();
        boolean success1 = result1.contains(cPass00) && result1.contains(cName00) && result1.contains(cType00);

        Assert.assertTrue("ProvisionConfigApplyConfig: Verify Certificate fields content :", success1);
        Thread.sleep(1_000);
//add Certificate #01 (finish)

//add Gateway #00 (start)
        GatewayDetails gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName00);
        Thread.sleep(1_000);
        gd.setClientCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setTrustCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setPort("0000000" + gPort00);
        Thread.sleep(1_000);
        gd.setHost(gHost00);
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(2_000);
//add Gateway #00 (finish)

//check saved data (start)
        String row1 = gName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayClient\">" + cName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayTrust\">" + cName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayPort\">" + gPort00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayHost\">" + gHost00;
        String content = pc.getGatewaysTableContent();
        boolean success = content.contains(row1);
        Assert.assertTrue("ProvisionConfigApplyConfig: row1 should be in the page",success);
//check saved data (finish)

//add Service #00 (start)
        ServiceDetails sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName00);
        Thread.sleep(1_000);
        AddPolicy ap = sd.clickAddPolicy();
        Thread.sleep(1_000);
        ap.selectPolicy(pName00);
        Thread.sleep(1_000);
        ap.clickOk();
        Thread.sleep(1_000);
        sd.setGatewayTheFirstItem();
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(pValu00);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #00 (finish)
        String content00 = pc.getServiceTableContent();
        boolean success00 = content00.contains(sName00) && content00.contains(gName00) && content00.contains(pValu00) && content00.contains(pName00);
        Assert.assertTrue("ProvisionConfigApplyConfig: Service #1, Policy and Policy value should be in the page",success00);

        pc.clickApply();
        Thread.sleep(5_000);
//add Config with Apply (finish)

//check just created Upcoming config (start)
        pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigApplyConfig: noProblems = " + noProblems);

        pc.clickSelectConfiguration();
        pc.clickCurrentConfig();
        Thread.sleep(2_000);
        pc.clickSelectConfiguration();
        Thread.sleep(2_000);
        pc.clickUpcomingConfig();
        Thread.sleep(2_000);

        String tb1exp = cName00 + cType00 + cPass00;
        String table1 = pc.getCertTableText();
        System.out.println("table1 : " + table1);
        Boolean tb1isGood = table1.contains(tb1exp);
        Assert.assertTrue("Certificates table contains right data", tb1isGood);

        String tb2exp = gName00 + cName00 + cName00 + gPort00 + gHost00;
        String table2 = pc.getGatewaysTableText();
        System.out.println("table2 : " + table2);
        //System.out.println("tb2exp : " + tb2exp);
        Boolean tb2isGood = table2.contains(tb2exp);
        Assert.assertTrue("Gateways table contains right data", tb2isGood);

        String tb3exA = sName00 + pName00 + pValu00 + "gate" + gName00;
        String tb3exB = sName00 + "gate" + gName00 + pName00 + pValu00;
        String table3 = pc.getServiceTableText();
        System.out.println("table3 : " + table3);
        //System.out.println("tb3exA : " + tb3exA);
        //System.out.println("tb3exB : " + tb3exB);
        Boolean tb3isGood = table3.contains(tb3exA) || table3.contains(tb3exB);
        Assert.assertTrue("Services table contains right data", tb3isGood);

//check just created Upcoming config (finish)

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
        policyPgForDel.searchForName(pName00);
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
        archetPage.selectArchetype(aName00);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted popupDel = archetPgForDel.deleteArchetype();
        Thread.sleep(1_000);
        popupDel.clickDelete();
        Thread.sleep(1_000);
//Delete Archetype1 (finish)

    }
}
