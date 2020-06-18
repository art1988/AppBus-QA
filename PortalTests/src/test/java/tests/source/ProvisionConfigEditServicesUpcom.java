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
import java.util.ArrayList;
import java.util.List;

public class ProvisionConfigEditServicesUpcom
{
    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    @Test
    public void ProvisionConfigEditServicesUpcom() throws InterruptedException
    {
        ProvisionConfigEditServicesUpcom(true);
    }

    public void ProvisionConfigEditServicesUpcom(boolean refresh) throws InterruptedException
    {

        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
        String mdhms = df.format(timeMDHMS);
        String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

        int ServisesNumber = 0;

        String cName33 = "crt33AutoNm" + tmpstp.substring(4); System.out.println("cName33: " + cName33);
        String cType33 = "der";                               System.out.println("cType33: " + cType33);
        String cPass33 = "33*^^%$^%#$#" +tmpstp.substring(4); System.out.println("cPass33: " + cPass33);

        String gName33 = "gat33AutoNm" + tmpstp.substring(4); System.out.println("gName33: " + gName33);
        String gPort33 = "33";                                System.out.println("gPort33: " + gPort33);
        String gHost33 = "lingvoexpert.com";                  System.out.println("gHost33: " + gHost33);

        String sName[] = {
                "ser00AutoNm" + tmpstp.substring(4),
                "ser01AutoNm" + tmpstp.substring(4),
                "ser02AutoNm" + tmpstp.substring(4),
                "ser03AutoNm" + tmpstp.substring(4),
                "ser04AutoNm" + tmpstp.substring(4),
                "ser05AutoNm" + tmpstp.substring(4),
                "ser06AutoNm" + tmpstp.substring(4),
                            };
        System.out.println("sName[0]: " + sName[0]);
        System.out.println("sName[1]: " + sName[1]);
        System.out.println("sName[2]: " + sName[2]);
        System.out.println("sName[3]: " + sName[3]);
        System.out.println("sName[4]: " + sName[4]);
        System.out.println("sName[5]: " + sName[5]);
        System.out.println("sName[6]: " + sName[6]);

        String aName33 = "arc33AutoNm" + tmpstp.substring(4); System.out.println("aName33: " + aName33);
        String aDesc33 = "arc33AutoDs" + tmpstp.substring(4); System.out.println("aDesc33: " + aDesc33);

        String pName33 = "pol33AutoNm" + tmpstp.substring(4); System.out.println("pName33: " + pName33);
        String pDesc33 = "pol33AutoDs" + tmpstp.substring(4); System.out.println("pDesc33: " + pDesc33);
        String pValu33 = "pValu33Auto" + tmpstp.substring(4); System.out.println("pValu33: " + pValu33);

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
        System.out.println("ProvisionConfigEditServicesUpcom: noProblems = " + noProblems);

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

        int ServicesNumber = pc.getServicesNumber();
        if (ServicesNumber < 6) //need to create services more
        {
            //Create Archetype (start)
            Thread.sleep(2_000);
            Archetypes archetPage = headerMenu.clickArchetypes(doPortalWakeUp);
            ArchetypesDetails archetDTLS = archetPage.addNewArchetype();
            archetDTLS.setName(aName33);
            archetDTLS.setDescription(aDesc33);
            archetDTLS.clickAdd();
            //Create Archetype (finish)

            //Create CONTROLLER Policy (start)
            Thread.sleep(2_000);
            Policies policyPage = headerMenu.clickPolicies(doPortalWakeUp);
            Thread.sleep(1_000);
            PolicyDetail policyDTLS = policyPage.addPolicy();
            Thread.sleep(1_000);
            policyDTLS.setName(pName33);
            Thread.sleep(1_000);
            policyDTLS.setDescription(pDesc33);
            Thread.sleep(1_000);
            policyDTLS.setType("TEXT");
            Thread.sleep(1_000);
            policyDTLS.checkGroup();
            Thread.sleep(1_000);
            policyDTLS.checkItem(); //again checkItem due to setType("STRATUM") unchecks Item
            Thread.sleep(1_000);
            policyDTLS.addItemProperty(aName33, "CONTROLLER", true, false);
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
            System.out.println("ProvisionConfigEditServicesUpcom: noProblems = " + noProblems);

            pc.clickSelectConfiguration();
            Thread.sleep(1_000);
            pc.clickCurrentConfig();
            Thread.sleep(3_000);
            pc.clickSelectConfiguration();
            Thread.sleep(2_000);
            pc.clickUpcomingConfig();
            Thread.sleep(3_000);

            //add Certificate #33 (start)
            CertificateDetails cd = pc.clickAddCertificate();
            Thread.sleep(1_000);
            cd.sendFileToInput("C:\\automation\\QA\\PortalTests\\Samples\\files\\in_app_proxy_cert");
            Thread.sleep(1_000);
            cd.clickUpload();
            Thread.sleep(2_000);

            Assert.assertTrue("ProvisionConfigEditServicesUpcom: Data uploaded mark changed to Ok (true/false):", cd.ifUploadedIcon());

            cd.setCertificateType(cType33);
            cd.setCertificateName(cName33);
            //cd.setCertPassword(cPass44);
            cd.clickSave();
            Thread.sleep(2_000);
            //add Certificate #33 (finish)

            //add Gateway #33 (start)
            GatewayDetails gd = pc.clickAddGateway();
            Thread.sleep(1_000);
            gd.setName(gName33);
            Thread.sleep(1_000);
            gd.setClientCertificateByName(cName33);
            Thread.sleep(1_000);
            gd.setTrustCertificateByName(cName33);
            Thread.sleep(1_000);
            gd.setPort("0000000" + gPort33);
            Thread.sleep(1_000);
            gd.setHost(gHost33);
            Thread.sleep(1_000);
            gd.clickSave();
            Thread.sleep(3_000);
            //add Gateway #33 (finish)

            for (int i = ServicesNumber; i < 6; i++)
            {
                //add Service #[i] (start)
                Thread.sleep(1_000);
                ServiceDetails sd = pc.clickAddService();
                Thread.sleep(1_000);
                sd.inputServiceName(sName[i]);
                Thread.sleep(1_000);
                AddPolicy ap = sd.clickAddPolicy();
                Thread.sleep(1_000);
                ap.selectPolicy(pName33);
                Thread.sleep(1_000);
                ap.clickOk();
                Thread.sleep(1_000);
                sd.setGatewayByName(gName33);
                driver.switchTo().activeElement().sendKeys(Keys.TAB);
                Thread.sleep(1_000);
                driver.switchTo().activeElement().sendKeys(pValu33);
                sd.clickSave();
                Thread.sleep(3_000);
                //add Service #[i] (finish)
            }
        }

        List<String> newServicesPolNm = new ArrayList<String>();
        List<String> newServicesRowsA = new ArrayList<String>();
        List<String> newServicesRowsB = new ArrayList<String>();
//Rename 6 of services (start)
        pValu33 = pValu33.replace("Auto", "Edit");
        List<String> OldServiceNames = new ArrayList<String>();
        List<WebElement> ServiceRows = pc.getServicesRows();
        String unitedServiceRows = "";
        //String xP = "//tbody[@id='form:servicesTable_data']/tr[@role='row'][@data-ri='0']";

        for (int j=0; j < ServiceRows.size(); j++)
        {
            String xP = "//tbody[@id='form:servicesTable_data']/tr[@role='row'][@data-ri='" + j + "']/td[@role='gridcell']";
            OldServiceNames.add(driver.findElement(By.xpath(xP)).getText());
            unitedServiceRows =  unitedServiceRows + "#" + OldServiceNames.get(j);
            System.out.println("unitedServiceRows is: " + unitedServiceRows);
            System.out.println("OldServiceNames.get(" + j + ")" + OldServiceNames.get(j));
        }
        int currentRowIndex = 0;
        boolean wasDelSerValOperation = false;

        for (int i = 0; i < 6; i++)
        {
            ServiceRows.clear();
            ServiceRows = pc.getServicesRows();


            for (int m=0; m < ServiceRows.size(); m++)
            {
                String xP = "//tbody[@id='form:servicesTable_data']/tr[@role='row'][@data-ri='" + m + "']/td[@role='gridcell']";
                System.out.println("m is " + m + " ,text() is: " + driver.findElement(By.xpath(xP)).getText());
                if (unitedServiceRows.contains(driver.findElement(By.xpath(xP)).getText()))
                {
                    currentRowIndex = m;
                    System.out.println("currentRowIndex : " + currentRowIndex);
                    break;
                }
            }

            System.out.println("Starting to sleep 3 seconds...");
            Thread.sleep(3_000);
            String iD = "form:servicesTable:" + currentRowIndex + ":editService";
            ServiceRows.get(currentRowIndex).findElement(By.id(iD)).click();
            ServiceDetails sd =  new ServiceDetails(driver);
            Thread.sleep(1_000);
            sName[i] = sName[i].replace("Auto","Edit");
            sd.inputServiceName(sName[i]);
            Thread.sleep(5_000);
            //NewServiceNames.add(sName[i]);

            if(i == 1 || i == 2 || i == 3 || i == 4 || i == 5)
            {
                sd.setLastGatewayItem();
                Thread.sleep(1_000);
            }

            if(i == 0 || i == 2)
            {
                wasDelSerValOperation = sd.deleteTheFirstValue();
                if (wasDelSerValOperation)
                {
                    WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
                    Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
                    Thread.sleep(5_000);
                }
            }

            String selectedPol = "";
            if(i == 0 || i == 2 || i == 3 || i == 5)
            {
                AddPolicy ap = sd.clickAddPolicy();
                Thread.sleep(1_000);
                //ap.selectPolicy(pName33);
                Thread.sleep(1_000);
                selectedPol = ap.clickOk();
            }

            //String selectedPolVal = "";
            if(i == 0 || i == 2 || i == 3 || i == 5)
            {
                Thread.sleep(1_000);
                //sd.setGatewayByName(gName33);
                sd.setFocusOnGatewayField();
                driver.switchTo().activeElement().sendKeys(Keys.TAB);
                Thread.sleep(1_000);

                for (int g=0; g < 10; g++)
                {
                    System.out.println("Value (activeElement().getAttribute(\"value\") is :" + driver.switchTo().activeElement().getAttribute("value"));
                    if (driver.switchTo().activeElement().getAttribute("value").equals(""))
                    {
                        System.out.println("Got empty field, will enter a value");
                        driver.switchTo().activeElement().sendKeys(pValu33);
                        selectedPol = selectedPol + pValu33;
                        break;
                    }
                    else {
                        System.out.println("driver.switchTo().activeElement().getText(): " + driver.switchTo().activeElement().getText());
                        driver.switchTo().activeElement().sendKeys(Keys.TAB);
                        Thread.sleep(1_000);
                        driver.switchTo().activeElement().sendKeys(Keys.TAB);
                        Thread.sleep(1_000);
                    }
                }

            }

            Thread.sleep(3_000);

            String gatewayName = sd.getGatewayName();
            if (gatewayName.contains("Select gateway")) gatewayName = "";
            else gatewayName = "gate" + gatewayName;

            String policyParms = sd.getPolicyParms();
            if(i == 0 || i == 2 || i == 3 || i == 5) policyParms = policyParms + pValu33;
            if (policyParms.contains("No records found.")) policyParms = "";

            String newCurrentRowA = gatewayName; // sName[i] + ..
            newCurrentRowA = newCurrentRowA.replace("ui-button", "");
            newCurrentRowA = newCurrentRowA.replace("\n", "");
            System.out.println("newCurrentRowA : " + newCurrentRowA);
            newServicesRowsA.add(newCurrentRowA);

            policyParms = policyParms.replace("ui-button", "");
            policyParms = policyParms.replace("\n", "");
            newServicesPolNm.add(selectedPol); //add(policyParms);

            sd.clickSave();
            Thread.sleep(3_000);
            //rename Service #[i] (finish)
        }
//Rename 6 of services (finish)

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

//Check saved config - service table (start)
        String table3after = pc.getServiceTableText();
        //table3after = table3after.replace(sName99 + "gate" + gName99 + pName99 + pValu99 + "ui-buttonui-button","");
        System.out.println("________________________________");
        System.out.println("table3after : " + table3after);
        System.out.println("________________________________");

        for (int k = 0; k < newServicesRowsA.size(); k++)
        {
            System.out.println("               sName[k] : " + sName[k]);
            System.out.println("newServicesRowsA.get(k) : " + newServicesRowsA.get(k));
            System.out.println("newServicesPolNm.get(k) : " + newServicesPolNm.get(k));

            Assert.assertTrue(table3after.contains(newServicesPolNm.get(k)) && table3after.contains(sName[k]) && table3after.contains(newServicesRowsA.get(k)));
        }

//Check saved config - service table (finish)

        if (ServicesNumber < 6) //need to delete items were created for creating additional Services
        {
            //Delete CONTROLLER Policy #33 (start)
            Thread.sleep(1_000);
            Policies  policyPgForDel = headerMenu.clickPolicies(doPortalWakeUp);
            Thread.sleep(3_000);
            policyPgForDel.searchForName(pName33);
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
            archetPgForDel.selectArchetype(aName33);
            Thread.sleep(1_000);
            FollowingItemsWillBeDeleted popupDel = archetPgForDel.deleteArchetype();
            Thread.sleep(1_000);
            popupDel.clickDelete();
            Thread.sleep(1_000);
            //Delete Archetype33 (finish)
        }

    }
}
