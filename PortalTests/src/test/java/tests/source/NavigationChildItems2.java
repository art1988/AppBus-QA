package tests.source;

import net.portal.constants.Retries;
import net.portal.forms.*;
import net.portal.pages.DeletePolicyConfirmation;
import net.portal.pages.PageObject;
import net.portal.pages.WakeUpPortal;
import net.portal.pages.user_and_role_management.*;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;
import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.pages.HeaderMenu;
import net.portal.pages.portal_administration.Users;
import net.portal.pages.service_management.ServiceCatalog;
import net.portal.pages.service_management.ServiceDashboard;
import net.portal.pages.service_management.UICatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.sql.Timestamp;
import java.io.*;
import java.text.SimpleDateFormat;
import java.util.Set;

import static tests.source.FunctionalTest.driver;

public class NavigationChildItems2
{
    boolean doPortalWakeUp = true;
    WakeUpPortal wkp = new WakeUpPortal(FunctionalTest.getDriver());

    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
    String mdhms = df.format(timeMDHMS);
    String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

    String profileName = "auto2PRFL" + tmpstp; //!
    //z String profileName = "auto2PRFL06122418"; //z
    String profileDSC = profileName + " description.";

    String contextName = "cntxt2AUTO" + tmpstp.substring(4); //!
    //z String contextName = "cntxt2AUTO2418";  //z
    String contextDSC = contextName + " description.";

    String arhetype1Name = "arche1ForChild" + tmpstp.substring(5); //!
    //z String arhetype1Name = "arche1ForChild418"; //z
    String arhetype1DSC = arhetype1Name + " description.";
    String arhetype2Name = "arche2ForChild" + tmpstp.substring(5); //!
    //z String arhetype2Name = "arche2ForChild418"; //z
    String arhetype2DSC = arhetype2Name + " description.";

    String policyName1 = "plcy1AUTOc" + tmpstp.substring(4); //!
    //z String policyName1 = "plcy1AUTOc5132"; //z
    String policyDSC1 = policyName1 + " description.";
    String policyName2 = "plcy2AUTOn" + tmpstp.substring(4); //!
    //z String policyName2 = "plcy2AUTOn5132"; //z
    String policyDSC2 = policyName2 + " description.";
    String policyName3 = "plcy3AUTOn" + tmpstp.substring(4); //!
    //z String policyName3 = "plcy3AUTOn5132"; //z
    String policyDSC3 = policyName3 + " description.";

    String uiGRPname = "uiGRPauto" + tmpstp.substring(3); //!
    //z String uiGRPname = "uiGRPauto22418"; //z
    String uiGRPdsc = uiGRPname + " description.";

    String nvgITM2id = "nvgITM2auto" + tmpstp.substring(3); //!
    //z String nvgITM2id = "nvgITM2name22418"; //z
    String nvgITM2dsc = nvgITM2id + " description.";
    String nvgITM2title = nvgITM2id + " AUTO TITLE";
    String nvgITM2entitle = nvgITM2id + " AUTO ENTITLEMENT";
    String nvgITM2tags = "<span>";

    String nvgITM3id = "nvgITM3auto" + tmpstp.substring(3); //!
    //z String nvgITM3id = "nvgITM3name22418"; //z
    String nvgITM3dsc = nvgITM3id + " description.";
    String nvgITM3title = nvgITM3id + " AUTO TITLE";
    String nvgITM3entitle = nvgITM3id + " AUTO ENTITLEMENT";
    String nvgITM3tags = "<img>";

    String nvgITMparentID = "nvgItmPRNT" + tmpstp.substring(3); //!
    //z String nvgITMparentID = "nvgItmPRNT22418"; //z
    String nvgITMparentDSC = nvgITMparentID + " description.";
    String nvgITMparentTITLE = nvgITMparentID + " AUTO TITLE";
    String nvgITMparentENTITLE = nvgITMparentID + " AUTO ENTITLEMENT";
    String nvgITMparentTAGS = "<frame>";

    //String[] jsSrvcName = {jsSrvcName1,jsSrvcName2,jsSrvcName3};
    //String[] jsSrvcName = {"JSsrv2AUTO04717","EXres3AUTO04717","JSsrv1AUTO04717"};

    @Test
    public void NavigationChildItemsCheck() throws InterruptedException {

        boolean success1 = false; boolean success2 = false; boolean success3 = false; boolean success4 = false; boolean success5 = false;
        System.out.println("profileName = " + profileName);
        System.out.println("contextName = " + contextName);
        System.out.println("arhetype1Name = " + arhetype1Name);
        System.out.println("arhetype2Name = " + arhetype2Name);
        System.out.println("policyName1 = " + policyName1);
        System.out.println("policyName2 = " + policyName2);
        System.out.println("policyName3 = " + policyName3);
        System.out.println("uiGRPname = " + uiGRPname);
        System.out.println("nvgITM3id = " + nvgITM3id);
        System.out.println("nvgITMparentID = " + nvgITMparentID);

        driver.navigate().refresh();
        Thread.sleep(5_000);
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        //Create Profile (start)
        Thread.sleep(1_000);
        Profiles prflPage = headerMenu.clickProfiles(doPortalWakeUp);
        ProfileDetail dtlsPRFL = prflPage.addProfile();
        dtlsPRFL.setName(profileName);
        dtlsPRFL.setDescription(profileDSC);
        dtlsPRFL.clickAdd();
        //Create Profile (finish)

        //Create Context (start)
        Thread.sleep(2_000);
        Contexts contextPage = headerMenu.clickContexts(doPortalWakeUp);
        ContextDetail dtlsCONT = contextPage.addContext();
        dtlsCONT.setName(contextName);
        dtlsCONT.setDescription(contextDSC);
        dtlsCONT.clickAdd();
        //Create Context (finish)

        //Create Archetype1 (start)
        Thread.sleep(2_000);
        Archetypes archetPage = headerMenu.clickArchetypes(doPortalWakeUp);
        ArchetypesDetails archetDTLS = archetPage.addNewArchetype();
        archetDTLS.setName(arhetype1Name);
        archetDTLS.setDescription(arhetype1DSC);
        archetDTLS.clickAdd();
        //Create Archetype1 (finish)

        //Create Archetype2 (start)
        Thread.sleep(2_000);
        archetPage = headerMenu.clickArchetypes(doPortalWakeUp);
        archetDTLS = archetPage.addNewArchetype();
        archetDTLS.setName(arhetype2Name);
        archetDTLS.setDescription(arhetype2DSC);
        archetDTLS.clickAdd();
        //Create Archetype2 (finish)

        //Create CONTROLLER Policy #1 (start)
        Thread.sleep(2_000);
        Policies policyPage = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        PolicyDetail policyDTLS = policyPage.addPolicy();
        Thread.sleep(1_000);
        policyDTLS.setName(policyName1);
        Thread.sleep(1_000);
        //policyDTLS.checkItem();
        //Thread.sleep(5_000);
        policyDTLS.setDescription(policyDSC1);
        Thread.sleep(1_000);
        policyDTLS.setType("TEXT");
        Thread.sleep(1_000);
        policyDTLS.checkGroup();
        Thread.sleep(1_000);
        policyDTLS.checkItem(); //again checkItem due to setType("STRATUM") unchecks Item
        Thread.sleep(1_000);
        policyDTLS.addItemProperty(arhetype1Name, "CONTROLLER", true, false);
        Thread.sleep(1_000);
        policyDTLS.checkGroupRequired();
        Thread.sleep(1_000);
        policyDTLS.checkDevice();
        Thread.sleep(1_000);
        policyDTLS.checkGroupMultiple();
        Thread.sleep(1_000);
        policyDTLS.checkDeviceMultiple();
        Thread.sleep(3_000);
        policyDTLS.clickAdd();
        Thread.sleep(1_000);
        //Create CONTROLLER Policy #1 (finish)

        //Create NAVIGATION Policy #2 (start)
        Thread.sleep(2_000);
        policyPage = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        policyDTLS = policyPage.addPolicy();
        Thread.sleep(1_000);
        policyDTLS.setName(policyName2);
        Thread.sleep(1_000);
        //policyDTLS.checkItem();
        //Thread.sleep(5_000);
        policyDTLS.setDescription(policyDSC2);
        Thread.sleep(1_000);
        policyDTLS.setType("LIST");
        Thread.sleep(1_000);
        policyDTLS.checkItem();
        Thread.sleep(1_000);
        policyDTLS.addItemProperty(arhetype2Name, "NAVIGATION", true, false);
        Thread.sleep(3_000);
        policyDTLS.checkGroupRequired();
        Thread.sleep(1_000);
        policyDTLS.checkDevice();
        Thread.sleep(1_000);
        policyDTLS.checkGroupMultiple();
        Thread.sleep(1_000);
        policyDTLS.checkDeviceMultiple();
        Thread.sleep(3_000);
        policyDTLS.clickAdd();
        Thread.sleep(1_000);
        //Create NAVIGATION Policy #2 (finish)

        //Create NAVIGATION Policy #3 (start)
        Thread.sleep(2_000);
        policyPage = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        policyDTLS = policyPage.addPolicy();
        Thread.sleep(1_000);
        policyDTLS.setName(policyName3);
        Thread.sleep(1_000);
        //policyDTLS.checkItem();
        //Thread.sleep(5_000);
        policyDTLS.setDescription(policyDSC3);
        Thread.sleep(1_000);
        policyDTLS.setType("LIST");
        Thread.sleep(1_000);
        policyDTLS.checkItem();
        Thread.sleep(1_000);
        policyDTLS.addItemProperty(arhetype1Name, "NAVIGATION", true, false);
        Thread.sleep(3_000);
        policyDTLS.checkGroupRequired();
        Thread.sleep(1_000);
        policyDTLS.checkDevice();
        Thread.sleep(1_000);
        policyDTLS.checkGroupMultiple();
        Thread.sleep(1_000);
        policyDTLS.checkDeviceMultiple();
        Thread.sleep(3_000);
        policyDTLS.clickAdd();
        Thread.sleep(1_000);
        //Create NAVIGATION Policy #3 (finish)

        //Create Navigation ItemParent (start)
        Thread.sleep(2_000);
        NavigationItems navigITMPpage = headerMenu.clickNavigationItems(doPortalWakeUp);
        Thread.sleep(1_000);
        ItemAssignmentDetails popItemDetails = navigITMPpage.addNavigationItem();
        Thread.sleep(2_000);
        popItemDetails.setId(nvgITMparentID);
        Thread.sleep(1_000);
        popItemDetails.setDescription(nvgITMparentDSC);
        Thread.sleep(1_000);
        popItemDetails.setDisplayTitle(nvgITMparentTITLE);
        Thread.sleep(1_000);
        popItemDetails.selectArchetype(arhetype1Name);
        Thread.sleep(1_000);
        popItemDetails.setEntitlement(nvgITMparentENTITLE);
        Thread.sleep(1_000);
        popItemDetails.setContext(contextName);
        Thread.sleep(1_000);
        popItemDetails.setTags(nvgITMparentTAGS);
        //popItemDetails.clickSave();
        Thread.sleep(1_000);
        popItemDetails.clickSave();
        //Create Navigation ItemParent (finish)

        //Create UI group (start)
        Thread.sleep(2_000);
        UIGroups uiGRPpage = headerMenu.clickUIGroups(doPortalWakeUp);
        UIGroupDetails uiGRPdetails = uiGRPpage.addUIGroup();
        uiGRPdetails.setTitle(uiGRPname);
        uiGRPdetails.setDescription(uiGRPdsc);
        //uiGRPdetails.clickAddProperty();
        Thread.sleep(2_000);
        uiGRPdetails.clickAdd();
        Boolean noProblems = wkp.fixAllProblems();
        //Create UI group (finish)

        //Create Navigation Item2 as child of the parent Item (start)
        Thread.sleep(2_000);
        navigITMPpage = headerMenu.clickNavigationItems(doPortalWakeUp);
        Thread.sleep(1_000);
        navigITMPpage.searchForId(nvgITMparentID);
        Thread.sleep(2_000);
        popItemDetails = navigITMPpage.clickAddChildNavigationItemIcon();
        Thread.sleep(2_000);
        popItemDetails.setId(nvgITM2id);
        Thread.sleep(1_000);
        popItemDetails.setDescription(nvgITM2dsc);
        Thread.sleep(1_000);
        popItemDetails.setDisplayTitle(nvgITM2title);
        Thread.sleep(1_000);
        //popItemDetails.selectArchetype(arhetype2Name); //Context + Archetype is taken from the Parent Item
        Thread.sleep(1_000);
        popItemDetails.setEntitlement(nvgITM2entitle);
        Thread.sleep(1_000);
        //popItemDetails.setContext(contextName); //Context + Archetype is taken from the Pareте Item
        Thread.sleep(1_000);
        popItemDetails.setTags(nvgITM2tags);
        //popItemDetails.clickSave();
        Thread.sleep(1_000);
        popItemDetails.clickSave();
        //Create Navigation Item2 as child of the parent Item (finish)

        //Select Profile + UIgroup (start)
        Thread.sleep(2_000);
        Navigation nvgtnPage = headerMenu.clickNavigation(doPortalWakeUp);
        nvgtnPage.selectProfile(profileName);
        Thread.sleep(2_000);
        UIGroupDetails uiPopupDetls =  nvgtnPage.addUIGroup();
        Thread.sleep(1_000);
        uiPopupDetls.selectUIgroup(uiGRPname);
        Thread.sleep(1_000);
        uiPopupDetls.clickUIgrpDetailsSave();
        //Select Profile + UIgroup (finish) +

        //Add Navigation Item #2 (start)
        Thread.sleep(1_000);
        boolean noProblem  = wkp.fixLoadBarProblem();
        if (!noProblem) System.out.println("ATTENTION! LoadingBar runs very long time!");
        NavTreeItemAssignmentDetails pop1 = nvgtnPage.addNewNvgItem(); //LoadingBar
        Thread.sleep(1_000);
        pop1.selectChildNvgItem(nvgITMparentID, nvgITM2id,true, true);
        Thread.sleep(1_000);
        pop1.clickAddItemButton();
        //Add Navigation Item #2 (finish)

        //Check just created Navigation Item #2 (start)
        Thread.sleep(1_000);
        //String xDiv = "//div[@style='display: inline-block; font-weight: bold;'][contains(.,'ID:')]/..";
        String xDiv = "//div[@style='display: inline-block;'][contains(.,'" + nvgITM2id + "')]/..";
        Thread.sleep(1_000);
        WebElement idDiv = driver.findElement(By.xpath(xDiv));
        System.out.println(idDiv.getText());
        if (idDiv.getText().contains("ID: " + nvgITM2id)) success1 = true;
        System.out.println("success1 = " + success1);

        Thread.sleep(1_000);
        //xDiv = "//div[@style='display: inline-block; font-weight: bold;'][contains(.,'Display Title:')]/..";
        xDiv = "//div[@style='display: inline-block;'][contains(.,'" + nvgITM2title + "')]/..";
        Thread.sleep(1_000);
        idDiv = driver.findElement(By.xpath(xDiv));
        System.out.println(idDiv.getText());
        if (idDiv.getText().contains("Display Title: " + nvgITM2title)) success2 = true;
        System.out.println("success2 = " + success2);

        Thread.sleep(1_000);
        //xDiv = "//div[@style='display: inline-block; font-weight: bold;'][contains(.,'Archetype:')]/..";
        xDiv = "//div[@style='display: inline-block;'][contains(.,'" + arhetype1Name + "')]/..";
        Thread.sleep(1_000);
        idDiv = driver.findElement(By.xpath(xDiv));
        System.out.println(idDiv.getText());
        if (idDiv.getText().contains("Archetype: " + arhetype1Name)) success3 = true;
        System.out.println("success3 = " + success3);

        Thread.sleep(1_000);
        //xDiv = "//div[@style='display: inline-block; font-weight: bold;'][contains(.,'Contexts:')]/..";
        xDiv = "//div[@style='display: inline-block;'][contains(.,'" + arhetype1Name + "')]/../..";
        Thread.sleep(1_000);
        idDiv = driver.findElement(By.xpath(xDiv));
        System.out.println(idDiv.getText());
        if (idDiv.getText().contains("Contexts: " + contextName)) success4 = true;
        System.out.println("success4 is " + success4);

        Thread.sleep(1_000);
        xDiv = "//td[contains(.,'" + policyName1 + "')]";
        Thread.sleep(1_000);
        idDiv = driver.findElement(By.xpath(xDiv));
        System.out.println(idDiv.getAttribute("outerHTML"));
        if (idDiv.getAttribute("outerHTML").contains(policyName1)) success5 = true;
        System.out.println("success5 = " + success5);

        System.out.println("____________________________________________");
        System.out.println(success1 && success2 && success3 && success4 && success5);
        Assert.assertEquals(true,success1 && success2 && success3 && success4 && success5); //!
        //z Assert.assertEquals(true,success1 && success2 && success3 && success4); //z
        //Check just created Navigation Item #2 (finish)

        //Click Preview and switch to windows #2 (browser sheet #2) start
        String window1 = driver.getWindowHandle(); // driver.switch_to.window(driver.window_handles[1])
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window1);
        Thread.sleep(1_000);
        nvgtnPage.clickPreview();
        Thread.sleep(5_000);
        Set<String> winHandles = driver.getWindowHandles();
        Thread.sleep(1_000);
        String winHandle1 = winHandles.iterator().next();
        Thread.sleep(1_000);
        Object[] winHandleObj = winHandles.toArray();
        Thread.sleep(1_000);
        String winHandle2 = winHandleObj[1].toString();
        Thread.sleep(1_000);
        //driver.switchTo().window(winHandle1);
        Thread.sleep(1_000);
        System.out.println("winHandle1 is " + winHandle1);
        System.out.println("winHandle2 is " + winHandle2);

        driver.switchTo().window(winHandle2);
        //Click Preview and switch to windows #2 (browser sheet #2) finish

        //Check values and parms of just created UI Group (start)
        String xP = "//span[contains(.,'" + uiGRPname + "')]/../..";
        WebElement tD = driver.findElement(By.xpath(xP));
        System.out.println("tD is :" + tD.getText());
        tD.findElement(By.xpath("//span[@class='ui-treetable-toggler ui-icon ui-icon-triangle-1-e ui-c']")).click(); //expand UI Group

        xP = "//span[contains(.,'folder')]/../..";
        tD = driver.findElement(By.xpath(xP));
        System.out.println("tD is :" + tD.getText());
        tD.findElement(By.xpath("//span[@class='ui-treetable-toggler ui-icon ui-icon-triangle-1-e ui-c']")).click(); //expand the "folder" under the UI Group

        //Check Navigation Item #2 parms (start)
        xP = "//span[@class='navigation-item'][contains(.,'" + nvgITM2id + "')]/../..";
        tD = driver.findElement(By.xpath(xP));
        System.out.println("tD is :" + tD.getText());
        String stD = tD.getText();
        System.out.println("|||||||||||||||||||||||||||||||||||||||||");
        System.out.println("stD (Navigation Item #2) is:");
        System.out.println(stD);
        System.out.println("|||||||||||||||||||||||||||||||||||||||||");
        boolean sucecssPreview2 = stD.contains(nvgITM2title) && stD.contains(nvgITM2id) && stD.contains(nvgITM2entitle) && stD.contains(policyName3); // && stD.contains(policyName1) && stD.contains("{ \"glossary\": { \"title\": \"example glossary\" } }");
        System.out.println(stD.contains(nvgITM2title));
        System.out.println(stD.contains(nvgITM2id));
        System.out.println(stD.contains(nvgITM2entitle));
        System.out.println(stD.contains(policyName1));
        System.out.println(stD.contains(policyName3));
        System.out.println(stD.contains("{ \"glossary\": { \"title\": \"example glossary\" } }"));
        Assert.assertEquals(true,sucecssPreview2);
        //Check Navigation Item #2 parms (finish)
        //Check values and parms of just created UI Group (finish)


        //Close windows #2 (browser sheet #2) and switch to windows #1 back (start)
        String window2 = driver.getWindowHandle();
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window2);
        Thread.sleep(1_000);
        driver.switchTo().window(window2).close();
        Thread.sleep(1_000);
        driver.switchTo().window(window1);
        Thread.sleep(1_000);
        //Close windows #2 (browser sheet #2) and switch to windows #1 back (finish)

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
        policyPgForDel.searchForName(policyName1);
        Thread.sleep(2_000);
        policyPgForDel.clickApplyFilter();
        Thread.sleep(2_000);
        DeletePolicyConfirmation popP = policyPgForDel.clickFirstDeleteIcon();
        Thread.sleep(1_000);
        popP.clickYes();
        Thread.sleep(1_000);
        //Delete CONTROLLER Policy #1 (finish)

        //Delete NAVIGATION Policy #2 (start)
        Thread.sleep(2_000);
        policyPgForDel = headerMenu.clickPolicies(doPortalWakeUp);
        Thread.sleep(1_000);
        //PolicyDetail editDTLS = policyPage.clickEdit(policyName2);
        Thread.sleep(1_000);
        //editDTLS.checkItem();
        Thread.sleep(1_000);
        //editDTLS.clickSave();
        Thread.sleep(2_000);
        policyPgForDel.searchForName(policyName2);
        Thread.sleep(2_000);
        policyPgForDel.clickApplyFilter();
        Thread.sleep(2_000);
        popP = policyPgForDel.clickFirstDeleteIcon();
        Thread.sleep(1_000);
        popP.clickYes();
        Thread.sleep(1_000);
        //Delete NAVIGATION Policy #2 (finish)

        //Delete NAVIGATION Policy #3 (start)
        Thread.sleep(2_000);
        policyPage = headerMenu.clickPolicies();
        Thread.sleep(1_000);
        //PolicyDetail editDTLS = policyPage.clickEdit(policyName3);
        Thread.sleep(1_000);
        //editDTLS.checkItem();
        Thread.sleep(1_000);
        //editDTLS.clickSave();
        Thread.sleep(2_000);
        policyPage.searchForName(policyName3);
        Thread.sleep(2_000);
        policyPage.clickApplyFilter();
        Thread.sleep(2_000);
        popP = policyPage.clickFirstDeleteIcon();
        Thread.sleep(1_000);
        popP.clickYes();
        Thread.sleep(1_000);
        //Delete NAVIGATION Policy #3 (finish)

        //Delete UI group (start)
        Thread.sleep(2_000);
        UIGroups uiGRPpgForDel = headerMenu.clickUIGroups(doPortalWakeUp);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted popupConfirm = uiGRPpgForDel.deleteUIGroup(uiGRPname);
        Thread.sleep(1_000);
        popupConfirm.clickDelete();
        Thread.sleep(1_000);
        //Delete UI group (finish)

        //Delete Archetype1 (start)
        Thread.sleep(2_000);
        Archetypes archetPgForDel = headerMenu.clickArchetypes(doPortalWakeUp);
        Thread.sleep(1_000);
        archetPage.selectArchetype(arhetype1Name);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted popupDel = archetPgForDel.deleteArchetype();
        Thread.sleep(1_000);
        popupDel.clickDelete();
        Thread.sleep(1_000);
        //Delete Archetype1 (finish)

        //Delete Archetype2 (start)
        Thread.sleep(2_000);
        archetPgForDel = headerMenu.clickArchetypes(doPortalWakeUp);
        Thread.sleep(1_000);
        archetPgForDel.selectArchetype(arhetype2Name);
        Thread.sleep(1_000);
        popupDel = archetPgForDel.deleteArchetype();
        Thread.sleep(1_000);
        popupDel.clickDelete();
        Thread.sleep(1_000);
        //Delete Archetype2 (finish)

        //Delete Context (start)
        Thread.sleep(2_000);
        Contexts contextPgForDel = headerMenu.clickContexts(doPortalWakeUp);
        Thread.sleep(1_000);
        contextPgForDel.selectContext(contextName);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted delCONT = contextPgForDel.deleteContext();
        Thread.sleep(1_000);
        delCONT.clickDelete();
        //Delete Context (finish)

        //Delete Profile (start)
        Thread.sleep(2_000);
        Profiles prflPgForDel = headerMenu.clickProfiles(doPortalWakeUp);
        Thread.sleep(1_000);
        DeleteWithAssignments page = prflPgForDel.clickDeleteIcon(profileDSC);
        Thread.sleep(1_000);
        page.clickDeleteButton();
        //Delete Profile (finish)

    }
}
