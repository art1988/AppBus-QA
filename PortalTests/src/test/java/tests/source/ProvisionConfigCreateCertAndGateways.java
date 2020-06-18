package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.constants.Notifications;
import net.portal.forms.AddNewProvConfig;
import net.portal.forms.CertificateDetails;
import net.portal.forms.GatewayDetails;
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

import java.sql.Timestamp;
import java.text.SimpleDateFormat;

public class ProvisionConfigCreateCertAndGateways
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigCreateCertAndGateways() throws InterruptedException
    {
        ProvisionConfigCreateCertAndGateways(true);
    }

    public void ProvisionConfigCreateCertAndGateways(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        String cName01 = "crt01AutoName" + tmpstp.substring(4); System.out.println("cName01: " + cName01);
        String cType01 = "p12";                                 System.out.println("cType01: " + cType01);
        String cPass01 = "01*^^%$^%#$#" +  tmpstp.substring(4); System.out.println("cPass01: " + cPass01);

        String gName01 = "gat01AutoName" + tmpstp.substring(4); System.out.println("gName01: " + gName01);
        String gPort01 = "1";                                  System.out.println("gPort01: " + gPort01);
        String gHost01 = "lingvoexpert.com";                    System.out.println("gHost01: " + gHost01);

        String gName02 = "gat02AutoName" + tmpstp.substring(4); System.out.println("gName02: " + gName02);
        String gPort02 = "2";                                  System.out.println("gPort02: " + gPort02);
        String gHost02 = "lingvoexpert.com";                    System.out.println("gHost02: " + gHost02);

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
        System.out.println("ProvisionConfigCreateCertAndGateways: noProblems = " + noProblems);

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
        Assert.assertTrue("ProvisionConfigCreateCertAndGateways: Click Tomorrow Day in calendar", addPop.clickTomorrowDay());
        Thread.sleep(1_000);
        String tomorrow = addPop.getStartTimeValue();
        Thread.sleep(1_000);
        addPop.clickOk();

        Thread.sleep(1_000);
        Assert.assertTrue("ProvisionConfigCreateCertAndGateways: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());

        Thread.sleep(1_000);
        pc.clickApply();
        Thread.sleep(3_000);
        Assert.assertTrue("ProvisionConfigCreateCertAndGateways: Add Config button should be disabled this time", !pc.ifAddConfigEnabled());
        Thread.sleep(1_000);

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);
        String tomorrowSaved = pc.getStartTimeValue();

        Assert.assertEquals("ProvisionConfigCreateCertAndGateways: entered StartTime value is equal to saved StartTime value", tomorrow, tomorrowSaved);

        //add Certificate #01 (start)
        CertificateDetails cd = pc.clickAddCertificate();
        Thread.sleep(1_000);
        cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
        Thread.sleep(1_000);
        cd.clickUpload();
        Thread.sleep(1_000);

        Assert.assertTrue("ProvisionConfigCreateCertAndGateways: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

        cd.setCertificateType(cType01);
        cd.setCertificateName(cName01);
        cd.setCertPassword(cPass01);
        cd.clickSave();
        Thread.sleep(2_000);

        String result1 = pc.getCertTableContent();
        boolean success1 = result1.contains(cPass01) && result1.contains(cName01) && result1.contains(cType01);

        Assert.assertTrue("ProvisionConfigCreateCertAndGateways: Verify Certificate fields content :", success1);
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

//add Gateway #02 (start)
        gd = pc.clickAddGateway(); //time
        Thread.sleep(1_000);
        gd.setName(gName02);
        Thread.sleep(1_000);
        gd.setTrustCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.setPort("00" + gPort02);
        Thread.sleep(1_000);
        gd.setHost(gHost02);
        Thread.sleep(1_000);
        gd.clickSaveForNoteCheck();

        notificationPopup = (new WebDriverWait(driver, 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.FIELD_CLIENT_DROPDOWN_CANNOT_BE_EMPTY.getNotificationText(), notificationPopup.getText());

        gd.setClientCertificateTheFirstItem();
        Thread.sleep(1_000);
        gd.clickSave();
        Thread.sleep(2_000);
//add Gateway #02 (finish)

//check saved data (start)
        String row1 = gName01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayClient\">" + cName01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayTrust\">" + cName01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayPort\">" + gPort01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:0:gatewayHost\">" + gHost01;
        String row2 = gName02 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:1:gatewayClient\">" + cName01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:1:gatewayTrust\">" + cName01 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:1:gatewayPort\">" + gPort02 + "</span></td><td role=\"gridcell\"><span id=\"form:gatewaysTable:1:gatewayHost\">" + gHost01;

        String content = pc.getGatewaysTableContent();
        boolean success = content.contains(row1) && content.contains(row2);
        Assert.assertTrue("ProvisionConfigCreateCertAndGateways: row1 and row2 should be in the page",success);

//check saved data (finish)

//add Config without saving of Certs (finish)
    }
}
