package tests.source;

import java.lang.String;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

import net.portal.constants.Notifications;
import net.portal.constants.Retries;
import net.portal.forms.*;
import net.portal.pages.DeletePolicyConfirmation;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import net.portal.pages.user_and_role_management.*;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.pagefactory.ByChained;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import static tests.source.FunctionalTest.driver;

public class NavigationMultipleValueIcon {
    static final SimpleDateFormat sdf = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss");

    @Test
    public void NavigationMultipleValueIcon() throws InterruptedException
    {
        driver.navigate().refresh();
        Thread.sleep(5_000);
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        WakeUpPortal wkp = new WakeUpPortal(FunctionalTest.getDriver());
    /*

    https://appbus.testrail.io/index.php?/cases/view/3368 (C3368)

    */

        Thread.sleep(2_000);

        // create 2 of Profiles

        Profiles profilesPage = headerMenu.clickProfiles();

        ProfileDetail profileDetail = profilesPage.addProfile();
        Thread.sleep(2_000);

        Timestamp timestp = new Timestamp(System.currentTimeMillis());
        String tmstp = sdf.format(timestp);
        tmstp = tmstp.substring(5);

        String nameOfProfile1 = "uiGRPauto01" + tmstp;
        String nameOfProfile2 = "uiGRPauto02" + tmstp;

        //String nameOfProfile1 = "TSTauto_01";
        String dscOfProfile1 = "TSTauto_01 dsc";

        profileDetail.setName(nameOfProfile1);
        profileDetail.setDescription(dscOfProfile1);
        profileDetail.clickAdd();
        Thread.sleep(2_000);

        boolean noProblems = wkp.fixLoadBarProblem(); //LB
        if (!noProblems)
        {
            System.out.println("ATTENTION !!! NavigationMultipleValueIcon: adding Profile doesn't work !");
            profilesPage = headerMenu.clickProfiles();
        }

        //String nameOfProfile2 = "TSTauto_02";
        String dscOfProfile2 = "TSTauto_02 dsc";

        profileDetail = profilesPage.addProfile();
        Thread.sleep(2_000);

        System.out.println(nameOfProfile2);
        profileDetail.setName(nameOfProfile2);
        profileDetail.setDescription(dscOfProfile2);
        profileDetail.clickAdd();
        Thread.sleep(2_000);

        //profileDetail = profilesPage.refreshProfile();
        Thread.sleep(2_000);

        // create 2 of Policies

        //HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Policies policiesPage = headerMenu.clickPolicies();

        String nameOfPolicy1 = "tstPauto1_" + tmstp; //z
        //String nameOfPolicy1 = "tstPauto1_04.10.06.59.27";
        String nameOfPolicy2 = "tstPauto2_" + tmstp; //z
        String policyDescription1 = "tstPauto_011 dsc";
        String policyDescription2 = "tstPauto_012 dsc";

        PolicyDetail propertyDetail = policiesPage.addPolicy();
        Thread.sleep(2_000);

        propertyDetail.setName(nameOfPolicy1);
        propertyDetail.setDescription(policyDescription1);
        propertyDetail.setType("TEXT");

        propertyDetail.checkItem();
        Thread.sleep(1_000);
        propertyDetail.checkGroup();
        Thread.sleep(1_000);
        propertyDetail.checkGroupRequired();
        Thread.sleep(2_000);
        propertyDetail.addItemProperty("SYSTEM-FUNCTION", "NAVIGATION", true, true);
        Thread.sleep(2_000);
        propertyDetail.checkGroupMultiple();
        Thread.sleep(1_000);
        propertyDetail.checkDevice();
        Thread.sleep(1_000);
        propertyDetail.checkDeviceMultiple();
        Thread.sleep(1_000);
        propertyDetail.checkProvision();
        Thread.sleep(1_000);
        propertyDetail.clickAdd();
        Thread.sleep(2_000);

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 2)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_ADDED.getNotificationText(), notificationPopup.getText());

        propertyDetail = policiesPage.addPolicy();
        Thread.sleep(2_000);

        propertyDetail.setName(nameOfPolicy2);
        propertyDetail.setDescription(policyDescription2);
        propertyDetail.setType("LIST");
        Thread.sleep(1_000);
        propertyDetail.checkGroup();
        Thread.sleep(1_000);
        propertyDetail.checkGroupRequired();
        Thread.sleep(1_000);
        propertyDetail.clickAdd();
        Thread.sleep(1_000);

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_ADDED.getNotificationText(), notificationPopup.getText());

        // create Policy assignment

        String [] vals = new String[2];
        vals [0] = "VAL01"; // PolicyValues
        vals [1] = "VAL02"; // PolicyValues

        String application = "edge";

        PolicyAssignment policyAssignment = headerMenu.clickPolicyAssignment();

        PolicyAssignmentDetail policyAssignmentDetail = policyAssignment.addPolicyAssignment();
        Thread.sleep(2_000);

        //String nameOfPolicy1 = "tstPauto_011"; //temp row for debug
        //String nameOfPolicy2 = "tstPauto_012"; //temp row for debug

        policyAssignmentDetail.setPolicyName(nameOfPolicy1);
        //policyAssignmentDetail.setPolicyName("tstPauto_011"); //"tstPauto_011","DraftUrl" could be used for check
        Thread.sleep(1_000);
        policyAssignmentDetail.clickGroupRadio();
        Thread.sleep(1_000);
        policyAssignmentDetail.setAppName(application);
        Thread.sleep(1_000);
        policyAssignmentDetail.setPolicyValuesEditing(vals); //!
        Thread.sleep(2_000);
        policyAssignmentDetail.clickAdd();



        // create 2 of UI groups


        Timestamp timestamp = new Timestamp(System.currentTimeMillis());
        String uiGroup1 = "uiGRPauto01" + sdf.format(timestamp);
        String uiGroup2 = "uiGRPauto02" + sdf.format(timestamp);
        System.out.println("uiGroup1 name is : " + uiGroup1);
        System.out.println("uiGroup2 name is : " + uiGroup2);

        String uiGrupds1 = "tstUIGRPauto01 dsc";
        String uiGrupds2 = "tstUIGRPauto02 dsc";

        Thread.sleep(2_000);
        UIGroups uiGroupsPage = headerMenu.clickUIGroups();

        UIGroupDetails uiGrpDetailsPage1 = uiGroupsPage.addUIGroup();
        uiGrpDetailsPage1.setTitle(uiGroup1);
        uiGrpDetailsPage1.setDescription(uiGrupds1);
        WebElement uiGRPtempFlag1 = uiGrpDetailsPage1.getFlagByPolName(nameOfPolicy1);
        uiGrpDetailsPage1.clickMainFlag();
        Thread.sleep(1_000);
        uiGRPtempFlag1.click();
        Thread.sleep(1_000);
        uiGrpDetailsPage1.clickDelete();
        Thread.sleep(1_000);
        uiGrpDetailsPage1.clickYes();
        Thread.sleep(1_000);
        uiGrpDetailsPage1.clickAdd();
        Thread.sleep(1_000);

        uiGroupsPage = headerMenu.clickUIGroups();
        Thread.sleep(1_000);

        UIGroupDetails uiGrpDetailsPage2 = uiGroupsPage.addUIGroup();
        Thread.sleep(1_000);
        uiGrpDetailsPage2.setTitle(uiGroup2);
        Thread.sleep(1_000);
        uiGrpDetailsPage2.setDescription(uiGrupds2);
        Thread.sleep(1_000);
        WebElement uiGRPtempFlag2 = uiGrpDetailsPage2.getFlagByPolName(nameOfPolicy2);
        Thread.sleep(1_000);
        uiGrpDetailsPage2.clickMainFlag();
        Thread.sleep(1_000);
        uiGRPtempFlag2.click();
        Thread.sleep(1_000);
        uiGrpDetailsPage2.clickDelete();
        Thread.sleep(1_000);
        uiGrpDetailsPage2.clickYes();
        Thread.sleep(1_000);
        uiGrpDetailsPage2.clickAdd();
        Thread.sleep(1_000);

        // create 2 of Navigation Trees

        Navigation navigationPage = headerMenu.clickNavigation();
        Thread.sleep(1_000);
        navigationPage.selectProfile(nameOfProfile1);
        Thread.sleep(2_000);
        UIGroupDetails navTreeUIgrpDtlPop = navigationPage.addUIGroup();
        System.out.println("uiGroup1 name is : " + uiGroup1);
        Thread.sleep(2_000);

        navTreeUIgrpDtlPop.selectUIgroup(uiGroup1);
        Thread.sleep(2_000);
        navTreeUIgrpDtlPop.clickEditUIbutton();
        Thread.sleep(1_000);
        //WebElement tmpOkButton = navTreeUIgrpDtlPop.getOkButtonOfPopup();
        navTreeUIgrpDtlPop.clickMultiValueAdd();
        //System.out.println("<clickMultiValueAdd> has just been performed");
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE); //Click "Add" again
        Thread.sleep(1_000);
        navTreeUIgrpDtlPop.addTwoValues("VAL03","VAL04");
        Thread.sleep(1_000);
        //navTreeUIgrpDtlPop.clickMultiValueOk();
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        navTreeUIgrpDtlPop.clickUIgrpDetailsSave();

        navigationPage.selectProfile(nameOfProfile2);
        Thread.sleep(1_000);

        noProblems = wkp.fixLoadBarProblem();
        if (!noProblems) System.out.println("ATTENTION! LoadingBar (id=\"ajaxLoadingBar_modal\") runs very long time!");

        navTreeUIgrpDtlPop = navigationPage.addUIGroup(); //LoadingBar
        System.out.println("uiGroup2 name is : " + uiGroup2);
        Thread.sleep(1_000);
        navTreeUIgrpDtlPop.selectUIgroup(uiGroup2);
        Thread.sleep(1_000);
        navTreeUIgrpDtlPop.addSingleValue("%VAL05^06&");
        Thread.sleep(1_000);
        navTreeUIgrpDtlPop.clickUIgrpDetailsSave();

        Thread.sleep(1_000);
        String window1 = driver.getWindowHandle(); // driver.switch_to.window(driver.window_handles[1])
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window1);
        Thread.sleep(1_000);
        navigationPage.clickPreview();
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

        Thread.sleep(3_000);
        Assert.assertTrue(((JavascriptExecutor) driver).executeScript("return $('.navigation-group').text()").toString().contains(uiGroup2));
        Thread.sleep(3_000);
        String tmpGRPname = driver.findElement(By.xpath("//span[text()='" + uiGroup2 + "']")).getText().toString();
        System.out.println("Group Name is " + tmpGRPname);
        Thread.sleep(1_000);
        String window2 = driver.getWindowHandle();
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window2);
        Thread.sleep(1_000);
        driver.switchTo().window(window2).close();
        Thread.sleep(1_000);
        driver.switchTo().window(window1);
        Thread.sleep(1_000);


        // delete 2 of UI Groups

        UIGroups uiGroupsPageForDel = headerMenu.clickUIGroups();
        Thread.sleep(1_000);
        uiGroupsPageForDel.deleteUIGroup(uiGroup1);
        Thread.sleep(3_000);
        uiGroupsPageForDel.ConfirmDelete(); //Time
        Thread.sleep(1_000);
        uiGroupsPageForDel.deleteUIGroup(uiGroup2);
        Thread.sleep(1_000);
        uiGroupsPageForDel.ConfirmDelete();
        Thread.sleep(1_000);

        // delete PolicyAssignment (no need to delete this for now, this was deleted at UI group deleting)
/*
        PolicyAssignment policyAssForDel = headerMenu.clickPolicyAssignment();

        policyAssForDel.filterPolicyByName(nameOfPolicy1);
        policyAssForDel.selectPolicyByName(nameOfPolicy1);
        policyAssForDel.clickDeleteButton();
        policyAssForDel.clickDeleteOnPopUp();
*/

        // delete 2 of Policies

        Policies policiesPageForDel = headerMenu.clickPolicies();

        Thread.sleep(2_000);
        System.out.println("Going delete policies");

        Thread.sleep(1_000);
        policiesPageForDel.searchForName(nameOfPolicy2);
        Thread.sleep(1_000);
        policiesPageForDel.clickApplyFilter();
        Thread.sleep(1_000);
        DeletePolicyConfirmation popP = policiesPageForDel.clickFirstDeleteIcon();
        Thread.sleep(1_000);
        popP.clickYes();
        Thread.sleep(3_000);
        policiesPageForDel.refreshPolicy();
        Thread.sleep(3_000);
        policiesPageForDel.searchForName(nameOfPolicy1);
        Thread.sleep(1_000);
        policiesPageForDel.clickApplyFilter();
        Thread.sleep(1_000);
        popP = policiesPageForDel.clickFirstDeleteIcon();
        Thread.sleep(1_000);
        popP.clickYes();
        Thread.sleep(2_000);

        // delete 2 of Profiles

        Profiles profilesPageForDel = headerMenu.clickProfiles(true);
        profilesPageForDel.refreshProfile();
        Thread.sleep(2_000);



        final DeleteWithAssignments profileDel0 = profilesPageForDel.clickDelete(nameOfProfile1);

        Thread.sleep(3_000);
        noProblems = wkp.fixLoadBarProblem(); //LB //ED-4110 is fixed
        if (!noProblems)
        {
            System.out.println("ATTENTION !!! NavigationMultipleValueIcon: delete profile doesn't work !");
        }

        profileDel0.clickDeleteButton(); //Time
        Thread.sleep(2_000);
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        Thread.sleep(2_000);
        profilesPageForDel.refreshProfile();
        Thread.sleep(2_000);

        final DeleteWithAssignments profileDel1 = profilesPageForDel.clickDelete(nameOfProfile2);
        Thread.sleep(4_000);
        Retries.RETRY_10_TIMES.run(     () -> profileDel1.clickDeleteButton());
        Thread.sleep(2_000);
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

    }

}
