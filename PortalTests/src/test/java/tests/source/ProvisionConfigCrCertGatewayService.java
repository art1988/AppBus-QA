package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.constants.Notifications;
import net.portal.forms.*;
import net.portal.pages.device_management.ProvisioningConfig;
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

public class ProvisionConfigCrCertGatewayService
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigCrCertGatewayService() throws InterruptedException
    {
        ProvisionConfigCrCertGatewayService(true);
    }

    public void ProvisionConfigCrCertGatewayService(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cName01 = "crt01AutoNm" + tmpstp.substring(4); System.out.println("cName01: " + cName01);
        String cType01 = "p12";                               System.out.println("cType01: " + cType01);
        String cPass01 = "01*^^%$^%#$#" +tmpstp.substring(4); System.out.println("cPass01: " + cPass01);

        String gName01 = "gat01AutoNm" + tmpstp.substring(4); System.out.println("gName01: " + gName01);
        String gPort01 = "1";                                 System.out.println("gPort01: " + gPort01);
        String gHost01 = "lingvoexpert.com";                  System.out.println("gHost01: " + gHost01);

        String sName01 = "ser01AutoNm" + tmpstp.substring(4); System.out.println("sName01: " + sName01);
        String sName03 = "ser03AutoNm" + tmpstp.substring(4); System.out.println("sName03: " + sName03);

        //String pName01 = "Policy1Auto"+tmpstp.substring(4); System.out.println("pName01: " + pName01);
        String pName01 = "_property_edit";                    System.out.println("pName01: " + pName01);

        String sName04 = "ser04AutoNm" + tmpstp.substring(4); System.out.println("sName04: " + sName04);
        String pValu04 = "pValu04Auto" + tmpstp.substring(4); System.out.println("pValu04: " + pValu04);

        String sName05 = "ser05AutoNm" + tmpstp.substring(4); System.out.println("sName05: " + sName05);
        String pValu05 = "pValu05Auto" + tmpstp.substring(4); System.out.println("pValu05: " + pValu05);

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
        System.out.println("ProvisionConfigCrCertGatewayService: noProblems = " + noProblems);

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


//add Config without saving of Certs (start)
        AddNewProvConfig addPop = pc.clickAddConfig();
        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Click Tomorrow Day in calendar", addPop.clickTomorrowDay());
        Thread.sleep(1_000);
        String tomorrow = addPop.getStartTimeValue();
        Thread.sleep(1_000);
        addPop.clickOk();

        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

        Thread.sleep(1_000);
        pc.clickApply();
        Thread.sleep(5_000);
        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());
        Thread.sleep(1_000);

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);
        String tomorrowSaved = pc.getStartTimeValue();

        Assert.assertEquals("ProvisionConfigCrCertGatewayService: entered StartTime value is equal to saved StartTime value", tomorrow, tomorrowSaved);

        //add Certificate #01 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType01);
        cd.setCertificateName(cName01);
        cd.setCertPassword(cPass01);
        cd.clickSave();
        Thread.sleep(2_000);

        String result1 = pc.getCertTableContent();
        boolean success1 = result1.contains(cPass01) && result1.contains(cName01) && result1.contains(cType01);

        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Verify Certificate fields content :", success1);
        Thread.sleep(1_000);
//add Certificate #01 (finish)

//add Gateway #01 (start)
        GatewayDetails gd = pc.clickAddGateway();
        Thread.sleep(1_000);
        gd.setName(gName01);
        Thread.sleep(1_000);
        gd.setClientCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setTrustCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setPort("0000000" + gPort01);
        Thread.sleep(1_000);
        gd.setHost(gHost01);
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(2_000);
//add Gateway #01 (finish)

//check saved data (start)
        String row1 = gName01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayClient\">" + cName01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayTrust\">" + cName01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayPort\">" + gPort01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayHost\">" + gHost01;

        String content = pc.getGatewaysTableContent();
        boolean success = content.contains(row1);
        Assert.assertTrue("ProvisionConfigCrCertGatewayService: row1 should be in the page",success);
//check saved data (finish)

//add Service #01 (start)
        ServiceDetails sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName01);
        Thread.sleep(1_000);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #01 (finish)

        String content01 = pc.getServiceTableContent();
        boolean success01 = content01.contains(sName01);
        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Service #1 should be in the page",success01);

//try to add Service #02 (start)
        sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName01);
        Thread.sleep(1_000);
        sd.clickSave();
        Thread.sleep(1_000);

        WebElement notificationPopup = (new WebDriverWait(driver, 2)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SERVICE_WITH_THIS_NAME_ALREADY_EXISTS.getNotificationText(), notificationPopup.getText());

        sd.clickCancel();
        Thread.sleep(1_000);
//try to add Service #02 (finish)

//add Service #03 (start)
        sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName03);
        Thread.sleep(1_000);
        sd.setGatewayTheFirstItem();
        Thread.sleep(1_000);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #03 (finish)

        String content03 = pc.getServiceTableContent();
        boolean success03 = content03.contains(sName03) && content03.contains(gName01);
        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Service #1 should be in the page",success03);





//add Service #04 (start)
        sd = pc.clickAddService();
        Thread.sleep(1_000);
        sd.inputServiceName(sName04);
        Thread.sleep(1_000);
        AddPolicy ap = sd.clickAddPolicy();
        Thread.sleep(1_000);
        ap.selectPolicy(pName01);
        Thread.sleep(1_000);
        ap.clickOk();
        Thread.sleep(2_000);
        sd.setGatewayTheFirstItem();
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(pValu04);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #04 (finish)

        String content04 = pc.getServiceTableContent();
        boolean success04 = content04.contains(sName04) && content04.contains(gName01) && content04.contains(pValu04) && content04.contains(pName01);
        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Service #1, Policy and Policy value should be in the page",success04);

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
        Thread.sleep(1_000);
        sd.setGatewayTheFirstItem();
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(pValu05);
        sd.clickSave();
        Thread.sleep(1_000);
//add Service #05 (finish)

        String content05 = pc.getServiceTableContent();
        boolean success05 = content05.contains(sName05) && content05.contains(gName01) && content05.contains(pValu05) && content05.contains(pName01);
        Assert.assertTrue("ProvisionConfigCrCertGatewayService: Service #1, Policy and Policy value should be in the page",success05);

//add Config without saving of Certs (finish)
    }
}
