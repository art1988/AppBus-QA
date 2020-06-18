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
import org.openqa.selenium.Keys;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;

public class ProvisionConfigDiscardChanges
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigDiscardChanges() throws InterruptedException
    {
        ProvisionConfigDiscardChanges(true);
    }

    public void ProvisionConfigDiscardChanges(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cName77 = "crt77AutoNm" + tmpstp.substring(4); System.out.println("cName77: " + cName77);
        String cType77 = "p12";                               System.out.println("cType77: " + cType77);
        String cPass77 = "77*^^%$^%#$#" +tmpstp.substring(4); System.out.println("cPass77: " + cPass77);

        String gName77 = "gat77AutoNm" + tmpstp.substring(4); System.out.println("gName77: " + gName77);
        String gPort77 = "77";                                System.out.println("gPort77: " + gPort77);
        String gHost77 = "lingvoexpert.com";                  System.out.println("gHost77: " + gHost77);

        String sName77 = "ser77AutoNm" + tmpstp.substring(4); System.out.println("sName77: " + sName77);

        String aName77 = "arc77AutoNm" + tmpstp.substring(4); System.out.println("aName77: " + aName77);
        String aDesc77 = "arc77AutoDs" + tmpstp.substring(4); System.out.println("aDesc77: " + aDesc77);

        String pName77 = "pol77AutoNm" + tmpstp.substring(4); System.out.println("pName77: " + pName77);
        String pDesc77 = "pol77AutoDs" + tmpstp.substring(4); System.out.println("pDesc77: " + pDesc77);
        String pValu77 = "pValu77Auto" + tmpstp.substring(4); System.out.println("pValu77: " + pValu77);

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
        archetDTLS.setName(aName77);
        archetDTLS.setDescription(aDesc77);
        archetDTLS.clickAdd();
//Create Archetype (finish)

//Create CONTROLLER Policy (start)
        Thread.sleep(2_000);
        Policies policyPage = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        PolicyDetail policyDTLS = policyPage.addPolicy();
        Thread.sleep(1_000);
        policyDTLS.setName(pName77);
        Thread.sleep(1_000);
        policyDTLS.setDescription(pDesc77);
        Thread.sleep(1_000);
        policyDTLS.setType("TEXT");
        Thread.sleep(1_000);
        policyDTLS.checkGroup();
        Thread.sleep(1_000);
        policyDTLS.checkItem(); //again checkItem due to setType("STRATUM") unchecks Item
        Thread.sleep(1_000);
        policyDTLS.addItemProperty(aName77, "CONTROLLER", true, false);
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
        System.out.println("ProvisionConfigDiscardChanges: noProblems = " + noProblems);

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


//add Instances with Discard (start)
//add Certificate #77 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigDiscardChanges: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType77);
        cd.setCertificateName(cName77);
        cd.setCertPassword(cPass77);
        cd.clickSave();
        Thread.sleep(2_000);

        String result1 = pc.getCertTableText();
        System.out.println("result1 : " + result1);
        //boolean success1 = result1.contains(cPass77) && result1.contains(cName77) && result1.contains(cType77);
        //Assert.assertTrue("ProvisionConfigDiscardChanges: Verify Certificate fields content :", success1);
        Thread.sleep(1_000);
//add Certificate #77 (finish)

//add Gateway #77 (start)
        GatewayDetails gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName77);
        Thread.sleep(1_000);
        gd.setClientCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setTrustCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setPort("0000000" + gPort77);
        Thread.sleep(1_000);
        gd.setHost(gHost77);
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(2_000);
//add Gateway #77 (finish)

//check saved data (start)
        //String row1 = gName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayClient\">" + cName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayTrust\">" + cName00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayPort\">" + gPort00 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayHost\">" + gHost00;
        String content = pc.getGatewaysTableText();
        System.out.println("content : " + content);
        //boolean success = content.contains(row1);
        //Assert.assertTrue("ProvisionConfigDiscardChanges: row1 should be in the page",success);
//check saved data (finish)

//add Service #77 (start)
        ServiceDetails sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName77);
        Thread.sleep(1_000);
        AddPolicy ap = sd.clickAddPolicy();
        Thread.sleep(1_000);
        ap.selectPolicy(pName77);
        Thread.sleep(1_000);
        ap.clickOk();
        Thread.sleep(1_000);
        sd.setGatewayTheFirstItem();
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(pValu77);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #77 (finish)
        String content00 = pc.getServiceTableText();
        System.out.println("content00 : " + content00);
        //boolean success00 = content00.contains(sName77) && content00.contains(gName77) && content00.contains(pValu77) && content00.contains(pName77);
        //Assert.assertTrue("ProvisionConfigDiscardChanges: Service #1, Policy and Policy value should be in the page",success00);

        pc.clickRevertChanges();
        Thread.sleep(1_000);
//add Instances with Discard (finish)

//check just discarted Upcoming config changes (start)
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
        //System.out.println("table1after : " + table1after);
        Assert.assertTrue(table1after.equals(table1before));
        String table2after = pc.getGatewaysTableText();
        //System.out.println("table2after : " + table2after);
        Assert.assertTrue(table2after.equals(table2before));
        String table3after = pc.getServiceTableText();
        //System.out.println("table3after : " + table3after);
        Assert.assertTrue(table3after.equals(table3before));

//check just discarted Upcoming config changes (finish)

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
        policyPgForDel.searchForName(pName77);
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
        archetPage.selectArchetype(aName77);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted popupDel = archetPgForDel.deleteArchetype();
        Thread.sleep(1_000);
        popupDel.clickDelete();
        Thread.sleep(1_000);
//Delete Archetype1 (finish)

    }
}
