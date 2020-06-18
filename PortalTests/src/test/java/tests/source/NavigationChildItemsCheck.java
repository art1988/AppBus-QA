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

public class NavigationChildItemsCheck {
    WakeUpPortal wkp = new WakeUpPortal(FunctionalTest.getDriver());

    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
    String mdhms = df.format(timeMDHMS);
    String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

    String profileName = "autoPRFL" + tmpstp; //!
    //z String profileName = "autoPRFL06122418"; //z
    String profileDSC = profileName + " description.";

    String contextName = "cntxtAUTO" + tmpstp.substring(4); //!
    //z String contextName = "cntxtAUTO2418";  //z
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

    String nvgITM1id = "nvgITM1auto" + tmpstp.substring(3); //!
    //z String nvgITM1id = "nvgITM1name22418"; //z
    String nvgITM1dsc = nvgITM1id + " description.";
    String nvgITM1title = nvgITM1id + " AUTO TITLE";
    String nvgITM1entitle = nvgITM1id + " AUTO ENTITLEMENT";
    String nvgITM1tags = "a, div, body";

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
        System.out.println("nvgITM1id = " + nvgITM1id);
        System.out.println("nvgITM2id = " + nvgITM2id);
        System.out.println("nvgITM3id = " + nvgITM3id);
        System.out.println("nvgITMparentID = " + nvgITMparentID);

        driver.navigate().refresh();
        Thread.sleep(5_000);
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        //Create Profile (start)
        Thread.sleep(1_000);
        Profiles prflPage = headerMenu.clickProfiles();
        ProfileDetail dtlsPRFL = prflPage.addProfile();
        dtlsPRFL.setName(profileName);
        dtlsPRFL.setDescription(profileDSC);
        dtlsPRFL.clickAdd();
        //Create Profile (finish)

        //Create Context (start)
        Thread.sleep(2_000);
        Contexts contextPage = headerMenu.clickContexts();
        ContextDetail dtlsCONT = contextPage.addContext();
        dtlsCONT.setName(contextName);
        dtlsCONT.setDescription(contextDSC);
        dtlsCONT.clickAdd();
        //Create Context (finish)

        //Create Archetype1 (start)
        Thread.sleep(2_000);
        Archetypes archetPage = headerMenu.clickArchetypes();
        ArchetypesDetails archetDTLS = archetPage.addNewArchetype();
        archetDTLS.setName(arhetype1Name);
        archetDTLS.setDescription(arhetype1DSC);
        archetDTLS.clickAdd();
        //Create Archetype1 (finish)

        //Create Archetype2 (start)
        Thread.sleep(2_000);
        archetPage = headerMenu.clickArchetypes();
        archetDTLS = archetPage.addNewArchetype();
        archetDTLS.setName(arhetype2Name);
        archetDTLS.setDescription(arhetype2DSC);
        archetDTLS.clickAdd();
        //Create Archetype2 (finish)

        //Create CONTROLLER Policy #1 (start)
        Thread.sleep(2_000);
        Policies policyPage = headerMenu.clickPolicies();
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
        policyPage = headerMenu.clickPolicies();
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
        policyPage = headerMenu.clickPolicies();
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
        NavigationItems navigITMPpage = headerMenu.clickNavigationItems();
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

        //Create Navigation Item1 (start)
        Thread.sleep(2_000);
        navigITMPpage = headerMenu.clickNavigationItems();
        Thread.sleep(1_000);
        popItemDetails = navigITMPpage.addNavigationItem();
        Thread.sleep(2_000);
        popItemDetails.setId(nvgITM1id);
        Thread.sleep(1_000);
        popItemDetails.setDescription(nvgITM1dsc);
        Thread.sleep(1_000);
        popItemDetails.setDisplayTitle(nvgITM1title);
        Thread.sleep(1_000);
        popItemDetails.selectArchetype(arhetype1Name);
        Thread.sleep(1_000);
        popItemDetails.setEntitlement(nvgITM1entitle);
        Thread.sleep(1_000);
        popItemDetails.setContext(contextName);
        Thread.sleep(1_000);
        popItemDetails.setTags(nvgITM1tags);
        //popItemDetails.clickSave();
        Thread.sleep(1_000);
        popItemDetails.clickSave();
        //Create Navigation Item1 (finish)

        //Create UI group (start)
        Thread.sleep(2_000);
        UIGroups uiGRPpage = headerMenu.clickUIGroups();
        UIGroupDetails uiGRPdetails = uiGRPpage.addUIGroup();
        uiGRPdetails.setTitle(uiGRPname);
        uiGRPdetails.setDescription(uiGRPdsc);
        //uiGRPdetails.clickAddProperty();
        Thread.sleep(2_000);
        uiGRPdetails.clickAdd();
        Boolean noProblems = wkp.fixAllProblems();
        //Create UI group (finish)

        //Set Navigation Item1 is child of Navigation ItemParent (start)
        Thread.sleep(2_000);
        navigITMPpage = headerMenu.clickNavigationItems();
        Thread.sleep(3_000);
        navigITMPpage.searchForId(" nvgITM"); //should be nvgITM1id value name
        Thread.sleep(1_000);
        navigITMPpage.clickRefresh();
        Thread.sleep(1_000);
        SelectParentItem popSelect = navigITMPpage.moveToAnotherItemAsChild(nvgITM1id);
        Thread.sleep(1_000);
        popSelect.selectParentItem(nvgITMparentID);
        Thread.sleep(1_000);
        MoveToItemAsChild popYes = popSelect.clickOkByTab();
        Thread.sleep(1_000);
        //ED-3923 (start)
        try {
            Thread.sleep(1_000);
            popYes.clickYesByTab();
            System.out.println("The popYes.clickYesByTab() method clicked the Yes button");
        } catch (Exception e) {System.out.println("The popYes.clickYesByTab() method DIDN'T click the Yes button");}
        //ED-3923 (finish)

        //Set Navigation Item1 is child of Navigation ItemParent (finish)

        //Create Navigation Item2 as child of the parent Item (start)
        Thread.sleep(2_000);
        navigITMPpage = headerMenu.clickNavigationItems();
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
        Navigation nvgtnPage = headerMenu.clickNavigation();
        nvgtnPage.selectProfile(profileName);
        Thread.sleep(2_000);
        UIGroupDetails uiPopupDetls =  nvgtnPage.addUIGroup();
        Thread.sleep(1_000);
        uiPopupDetls.selectUIgroup(uiGRPname);
        Thread.sleep(1_000);
        uiPopupDetls.clickUIgrpDetailsSave();
        //Select Profile + UIgroup (finish) +

        //Add Navigation Item #1 (start)
        Thread.sleep(1_000);
        NavTreeItemAssignmentDetails pop1 = nvgtnPage.addNewNvgItem();
        Thread.sleep(3_000);

        pop1.selectChildNvgItem(nvgITMparentID, nvgITM1id,true, true);
        Thread.sleep(1_000);
        pop1.clickAddItemButton();
        //Add Navigation Item #1 (finish)

        //Add Navigation Item #2 (start)
        Thread.sleep(1_000);
        pop1 = nvgtnPage.addNewNvgItem();
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
        System.out.println(idDiv.getText());
        if (idDiv.getText().contains(policyName1)) success5 = true;
        System.out.println("success5 = " + success5);

        System.out.println("____________________________________________");
        System.out.println(success1 && success2 && success3 && success4 && success5);
        Assert.assertEquals(true,success1 && success2 && success3 && success4 && success5); //!
        //z Assert.assertEquals(true,success1 && success2 && success3 && success4); //z
        //Check just created Navigation Item #2 (finish)

        //Add (create) Navigation Item #3 (start)
        Thread.sleep(1_000);
        pop1 = nvgtnPage.addNewNvgItem();
        Thread.sleep(1_000);
        ItemDetails pop2 = pop1.clickCreateNewItem();
        pop2.setParentItem(nvgITMparentID);
        Thread.sleep(1_000);
        pop2.setIdField(nvgITM3id);
        Thread.sleep(1_000);
        pop2.setDisplaytitleField(nvgITM3title);
        Thread.sleep(1_000);
        pop2.setDescriptionField(nvgITM3dsc);
        Thread.sleep(1_000);
        pop2.setArchetype(arhetype1Name);
        Thread.sleep(1_000);
        pop2.setEntitlementField(nvgITM3entitle);
        Thread.sleep(1_000);
        pop2.setContext(contextName);
        Thread.sleep(1_000);
        //WebElement save = pop2.getSaveButton();
        Thread.sleep(1_000);
        pop2.setTagsField(nvgITM3tags);
        Thread.sleep(1_000);
        pop2.clickSave();
        //save.click();
        Thread.sleep(1_000);
        //Add (create) Navigation Item #3 (finish)

        //Add Navigation Item #3 (start)
        Thread.sleep(2_000);
        pop1.selectChildNvgItem(nvgITMparentID, nvgITM3id,false, true);
        Thread.sleep(1_000);
        pop1.clickAddItemButton();
        //Add Navigation Item #3 (finish)

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

        //Check Navigation Item #1 parms (start)
        xP = "//span[@class='navigation-item'][contains(.,'" + nvgITM1id + "')]/../..";
        tD = driver.findElement(By.xpath(xP));
        System.out.println("tD is :" + tD.getText());
        String stD = tD.getText();
        //nvgITM1auto50758 nvgITM1auto50758 AUTO TITLE arche1AUTO758 nvgITM1auto50758 AUTO ENTITLEMENT
        //policyAUTOc0758 { "glossary": { "title": "example glossary" } }
        boolean sucecssPreview1 = stD.contains(nvgITM1title) && stD.contains(nvgITM1id) && stD.contains(nvgITM1entitle); // && stD.contains(policyName1) && stD.contains(policyName3) && stD.contains("{ \"glossary\": { \"title\": \"example glossary\" } }");
        System.out.println(stD.contains(nvgITM1title));
        System.out.println(stD.contains(nvgITM1id));
        System.out.println(stD.contains(nvgITM1entitle));
        System.out.println(stD.contains(policyName1));
        System.out.println(stD.contains(policyName3));
        System.out.println(stD.contains("{ \"glossary\": { \"title\": \"example glossary\" } }"));
        Assert.assertEquals(true,sucecssPreview1);
        //Check Navigation Item #1 parms (finish)

        //Check Navigation Item #2 parms (start)
        xP = "//span[@class='navigation-item'][contains(.,'" + nvgITM2id + "')]/../..";
        tD = driver.findElement(By.xpath(xP));
        System.out.println("tD is :" + tD.getText());
        stD = tD.getText();
        boolean sucecssPreview2 = stD.contains(nvgITM2title) && stD.contains(nvgITM2id) && stD.contains(nvgITM2entitle) && stD.contains(policyName3); // && stD.contains(policyName1) && stD.contains("{ \"glossary\": { \"title\": \"example glossary\" } }");
        System.out.println(stD.contains(nvgITM2title));
        System.out.println(stD.contains(nvgITM2id));
        System.out.println(stD.contains(nvgITM2entitle));
        System.out.println(stD.contains(policyName1));
        System.out.println(stD.contains(policyName3));
        System.out.println(stD.contains("{ \"glossary\": { \"title\": \"example glossary\" } }"));
        Assert.assertEquals(true,sucecssPreview2);
        //Check Navigation Item #2 parms (finish)

        //Check Navigation Item #3 parms (start)
        xP = "//span[@class='navigation-item'][contains(.,'" + nvgITM3id + "')]/../..";
        tD = driver.findElement(By.xpath(xP));
        System.out.println("tD is :" + tD.getText());
        stD = tD.getText();
        boolean sucecssPreview3 = stD.contains(nvgITM3title) && stD.contains(nvgITM3id) && stD.contains(nvgITM3entitle) && stD.contains(policyName3); // && stD.contains(policyName1);
        System.out.println(stD.contains(nvgITM3title));
        System.out.println(stD.contains(nvgITM3id));
        System.out.println(stD.contains(nvgITM3entitle));
        System.out.println(stD.contains(policyName1));
        System.out.println(stD.contains(policyName3));
        Assert.assertEquals(true,sucecssPreview3);
        //Check Navigation Item #3 parms (finish)

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
        Policies  policyPgForDel = headerMenu.clickPolicies();
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
        policyPgForDel = headerMenu.clickPolicies();
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
        UIGroups uiGRPpgForDel = headerMenu.clickUIGroups();
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted popupConfirm = uiGRPpgForDel.deleteUIGroup(uiGRPname);
        Thread.sleep(1_000);
        popupConfirm.clickDelete();
        Thread.sleep(1_000);
        //Delete UI group (finish)

        //Delete Archetype1 (start)
        Thread.sleep(2_000);
        Archetypes archetPgForDel = headerMenu.clickArchetypes();
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
        archetPgForDel = headerMenu.clickArchetypes();
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
        Contexts contextPgForDel = headerMenu.clickContexts();
        Thread.sleep(1_000);
        contextPgForDel.selectContext(contextName);
        Thread.sleep(1_000);
        FollowingItemsWillBeDeleted delCONT = contextPgForDel.deleteContext();
        Thread.sleep(1_000);
        delCONT.clickDelete();
        //Delete Context (finish)

        //Delete Profile (start)
        Thread.sleep(2_000);
        Profiles prflPgForDel = headerMenu.clickProfiles();
        Thread.sleep(1_000);
        DeleteWithAssignments page = prflPgForDel.clickDeleteIcon(profileDSC);
        Thread.sleep(1_000);
        page.clickDeleteButton();
        //Delete Profile (finish)

    }
}
