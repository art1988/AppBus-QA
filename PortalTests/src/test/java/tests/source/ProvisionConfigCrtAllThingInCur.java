package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.constants.Const;
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

import java.io.File;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.List;


public class ProvisionConfigCrtAllThingInCur
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    static final SimpleDateFormat pf = new SimpleDateFormat("MM/dd/YY");

    @Test
    public void ProvisionConfigCrtAllThingInCur() throws InterruptedException
    {
        ProvisionConfigCrtAllThingInCur(true);
    }

    public void ProvisionConfigCrtAllThingInCur(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());

        String mmddyy = pf.format(System.currentTimeMillis()-24*60*60*1000); //yesterday
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cPass = "10uniqPass@##$#";                       System.out.println("cPass: " + cPass);
        String cName = "10crtAutoName" + tmpstp;                System.out.println("cName: " + cName);
        String cType = "p12";                                   System.out.println("cType: " + cType);

        String gName01 = "10gatAutoName" + tmpstp.substring(4); System.out.println("gName01: " + gName01);
        String gPort01 = "10";                                  System.out.println("gPort01: " + gPort01);
        String gHost01 = "https://restcountries.eu/";           System.out.println("gHost01: " + gHost01);

        String aName01 = "01arcAutoNm" + tmpstp.substring(4);   System.out.println("aName01: " + aName01);
        String aDesc01 = "01arcAutoDs" + tmpstp.substring(4);   System.out.println("aDesc01: " + aDesc01);

        String pName01 = "01polAutoNm" + tmpstp.substring(4);   System.out.println("pName01: " + pName01);
        String pDesc01 = "01polAutoDs" + tmpstp.substring(4);   System.out.println("pDesc01: " + pDesc01);
        String pValu01 = "01pValuAuto" + tmpstp.substring(4);   System.out.println("pValu01: " + pValu01);

        String sName01 = "01serAutoNm" + tmpstp.substring(4);   System.out.println("sName01: " + sName01);

        String sName03 = "03serAutoNm" + tmpstp.substring(4);   System.out.println("sName03: " + sName03);
        String pVl0003 = "0003pVlAuto" + tmpstp.substring(4);   System.out.println("pVl0003: " + pVl0003);

        String sName04 = "04serAutoNm" + tmpstp.substring(4);   System.out.println("sName04: " + sName04);
        String pVl0004 = "0004pVlAuto" + tmpstp.substring(4);   System.out.println("pVl0004: " + pVl0004);

        String sName05 = "05serAutoNm" + tmpstp.substring(4);   System.out.println("sName05: " + sName05);
        String pVl0005 = "0005pVlAuto" + tmpstp.substring(4);   System.out.println("pVl0005: " + pVl0005);


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
        archetDTLS.setName(aName01);
        archetDTLS.setDescription(aDesc01);
        archetDTLS.clickAdd();
//Create Archetype (finish)

//Create CONTROLLER Policy (start)
        Thread.sleep(2_000);
        Policies policyPage = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        PolicyDetail policyDTLS = policyPage.addPolicy();
        Thread.sleep(1_000);
        policyDTLS.setName(pName01);
        Thread.sleep(1_000);
        policyDTLS.setDescription(pDesc01);
        Thread.sleep(1_000);
        policyDTLS.setType("TEXT");
        Thread.sleep(1_000);
        policyDTLS.checkGroup();
        Thread.sleep(1_000);
        policyDTLS.checkItem(); //again checkItem due to setType("STRATUM") unchecks Item
        Thread.sleep(1_000);
        policyDTLS.addItemProperty(aName01, "CONTROLLER", true, false);
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

        boolean noProblem  = wkp.fixLoadBarProblem();
        if (!noProblem) System.out.println("ATTENTION! LoadingBar runs very long time!");

//stop script if Current config doesn't exist (start)
        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigCrtAllThingInCur: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: create please Current config if one doesn't exist", ItemLIst.contains("Current config"));
//stop script if Current config doesn't exist (finish)

        System.out.println("ProvisionConfigCrtAllThingInCur: going to select Current config");
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

//Add Certificate #1 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType);
        cd.setCertificateName(cName);
        cd.setCertPassword(cPass);
        cd.clickSave();
        //System.out.println("going to sleep for 100 secs");
        Thread.sleep(2_000);

        String result = pc.getCertTableContent();
        boolean success = result.contains(cPass) && result.contains(cName) && result.contains(cType);

        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: Verify Certificate fields content :", success);
        Thread.sleep(1_000);
//Add Certificate #1 (finish)

//add Gateway #01 (start)
        GatewayDetails gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName01);
        Thread.sleep(1_000);
        gd.setClientCertificateByName(cName);
        Thread.sleep(1_000);
        gd.setTrustCertificateByName(cName);
        Thread.sleep(1_000);
        gd.setPort("Z" + gPort01);
        Thread.sleep(1_000);
        gd.clickSaveForNoteCheck();

        WebElement notificationPopup = (new WebDriverWait(driver, 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.INVALID_FORMAT_OR_VALUE.getNotificationText(), notificationPopup.getText());

        gd.setPort("00" + gPort01);
        Thread.sleep(1_000);
        gd.setHost(gHost01);
        Thread.sleep(2_000);
        gd.clickSave();
        Thread.sleep(2_000);
//add Gateway #01 (finish)

//add Service #01 (start)
        ServiceDetails sd = pc.clickAddService();
        Thread.sleep(2_000);
        sd.clickSave();

        notificationPopup = (new WebDriverWait(driver, 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.FIELD_NAME_CANNONT_BE_EMPTY.getNotificationText(), notificationPopup.getText());

        sd.inputServiceName(sName01);
        Thread.sleep(1_000);
        sd.clickSave();
        Thread.sleep(2_000);
//add Service #01 (finish)

//trying to add Service #02 (start)
        sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName01);
        Thread.sleep(1_000);
        sd.clickSave();

        notificationPopup = (new WebDriverWait(driver, 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SERVICE_WITH_THIS_NAME_ALREADY_EXISTS.getNotificationText(), notificationPopup.getText());

        Thread.sleep(1_000);
        sd.clickCancel();
//trying to add Service #02 (finish)

//add Service #03 (start)
        sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName03);
        Thread.sleep(1_000);
        sd.setGatewayByName(gName01);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(pVl0003);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #03 (finish)

//add Service #04 (start)
        sd = pc.clickAddService();
        Thread.sleep(1_000);
        AddPolicy ap = sd.clickAddPolicy();
        Thread.sleep(1_000);
        ap.selectPolicy(pName01);
        Thread.sleep(1_000);
        ap.clickOk();
        Thread.sleep(2_000);
        sd.inputServiceName(sName04);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(pVl0004);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #04 (finish)

//add Service #05 (start)
        sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName05);
        Thread.sleep(1_000);
        ap = sd.clickAddPolicy();
        Thread.sleep(1_000);
        ap.selectPolicy(pName01);
        Thread.sleep(1_000);
        ap.clickOk();
        Thread.sleep(2_000);
        sd.setGatewayByName(gName01);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(pVl0005);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #05 (finish)

//Apply (start)
        pc.clickApply();
        Thread.sleep(2_000);

        System.out.println("ProvisionConfigCrtAllThingInCur: going to select Current config");
        pc.clickSelectConfiguration(); //f
        Thread.sleep(1_000);
        pc.clickCurrentConfig();
        Thread.sleep(3_000);
//Apply (finish)

//Check Current config after (start)
        String table1afterRow = pc.getCertTableRowText(cName);
        System.out.println("________________________________");
        System.out.println("table1afterRow : " + table1afterRow);
        System.out.println("________________________________");

        String table2afterRow1 = pc.getGatewayTableRowText(gName01);
        System.out.println("________________________________");
        System.out.println("table2afterRow1 : " + table2afterRow1);
        System.out.println("________________________________");

        String table3after1 = pc.getServiceTableRowText(sName01);
        System.out.println("________________________________");
        System.out.println("table3after1 : " + table3after1);
        System.out.println("________________________________");

        String table3after3 = pc.getServiceTableRowText(sName03);
        System.out.println("________________________________");
        System.out.println("table3after3 : " + table3after3);
        System.out.println("________________________________");

        String table3after4 = pc.getServiceTableRowText(sName04);
        System.out.println("________________________________");
        System.out.println("table3after4 : " + table3after4);
        System.out.println("________________________________");

        String table3after5 = pc.getServiceTableRowText(sName05);
        System.out.println("________________________________");
        System.out.println("table3after5 : " + table3after5);
        System.out.println("________________________________");
//Check Current config after (finish)

        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: Certificates table is updated:",table1afterRow.contains(cPass) && table1afterRow.contains(cType));

        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: Gateways table is updated by Gateway #1:",table2afterRow1.contains(cName) && table2afterRow1.contains(gHost01) && table2afterRow1.contains(gPort01));

        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: Services table is updated by Service #1:",table3after1.contains(sName01));
        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: Services table is updated by Service #3:",table3after3.contains(gName01) && table3after3.contains("gate"));
        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: Services table is updated by Service #4:",table3after4.contains(pName01) && table3after4.contains(pVl0004));
        Assert.assertTrue("ProvisionConfigCrtAllThingInCur: Services table is updated by Service #5:",table3after5.contains(pName01) && table3after5.contains(gName01) && table3after5.contains(pVl0005));

//Delete Service #4 + #5 (start)
        int indexS = pc.getServiceIndex(sName04);
        if (indexS!=999) {

            String iD = "form:servicesTable:" + indexS + ":removeService";
            driver.findElement(By.id(iD)).click();
            Thread.sleep(2_000);
            driver.findElement(By.id("serviceRemoveDlgForm:yesButtonservice")).click();

            notificationPopup = (new WebDriverWait(driver, 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
            Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

            Thread.sleep(2_000);
        }

        indexS = pc.getServiceIndex(sName05);
        if (indexS!=999) {

            String iD = "form:servicesTable:" + indexS + ":removeService";
            driver.findElement(By.id(iD)).click();
            Thread.sleep(2_000);
            driver.findElement(By.id("serviceRemoveDlgForm:yesButtonservice")).click();

            notificationPopup = (new WebDriverWait(driver, 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
            Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

            Thread.sleep(2_000);
        }
//Delete Service #4 + #5 (finish)

//Apply (start)
        pc.clickApply();
        Thread.sleep(2_000);
//Apply (finish)

//Delete CONTROLLER Policy #33 (start)
        Thread.sleep(1_000);
        Policies  policyPgForDel = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(3_000);
        policyPgForDel.searchForName(pName01);
        Thread.sleep(2_000);
        policyPgForDel.clickApplyFilter();
        Thread.sleep(2_000);
        DeletePolicyConfirmation popP = policyPgForDel.clickFirstDeleteIcon();
        Thread.sleep(1_000);
        popP.clickYes();
        Thread.sleep(1_000);
//Delete CONTROLLER Policy #33 (finish)

//Delete Archetype33 (start)
        Thread.sleep(2_000);
        Archetypes archetPgForDel = headerMenu.clickArchetypes(doPortalWakeUp);
        Thread.sleep(1_000);
        archetPgForDel.selectArchetype(aName01);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted popupDel = archetPgForDel.deleteArchetype();
        Thread.sleep(1_000);
        popupDel.clickDelete();
        Thread.sleep(1_000);
//Delete Archetype33 (finish)

    }
}
