package tests.source;

import net.portal.forms.*;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Navigation;
import net.portal.pages.user_and_role_management.Profiles;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.Set;

public class NavigationTreePreview
{
    @Test
    public void navigationTreePreview() throws InterruptedException
    {
        System.out.println("--- START OF NavigationTreePreview ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Profiles profilesPage = headerMenu.clickProfiles();

        ProfileDetail profileDetailForm = profilesPage.addProfile();
        Thread.sleep(2_000);

        String profileName = "AA_Test_NavTree";

        profileDetailForm.setName(profileName);
        profileDetailForm.clickAdd();
        Thread.sleep(3_000);

        Navigation navigationPage = headerMenu.clickNavigation();

        navigationPage.selectProfile(profileName);
        Thread.sleep(3_000);

        UIGroupDetails uiGroupDetails = navigationPage.addGroup();
        Thread.sleep(2_000);

        // Add UI group - bottomFixedGroup
        uiGroupDetails.selectGroup("bottom");
        uiGroupDetails.clickSave();
        Thread.sleep(2_000);

        NavTreeItemAssignmentDetails itemAssignmentDetails = navigationPage.addNewNvgItem();
        Thread.sleep(2_000);

        itemAssignmentDetails.selectItem("barcodeMedical");
        itemAssignmentDetails.clickAddItemButton();
        Thread.sleep(2_000);

        itemAssignmentDetails = navigationPage.addNewNvgItem();
        Thread.sleep(2_000);

        itemAssignmentDetails.selectItem("help");
        itemAssignmentDetails.clickAddItemButton();
        Thread.sleep(2_000);

        itemAssignmentDetails = navigationPage.addNewNvgItem();
        Thread.sleep(2_000);

        itemAssignmentDetails.selectItem("folder-lock");
        itemAssignmentDetails.clickAddItemButton();
        Thread.sleep(2_000);

        // Add new UI group - floatingGroup
        uiGroupDetails = navigationPage.addGroup();
        Thread.sleep(2_000);

        uiGroupDetails.selectGroup("floatingGroup");
        uiGroupDetails.clickSave();
        Thread.sleep(2_000);

        itemAssignmentDetails = navigationPage.addNewNvgItem();
        Thread.sleep(2_000);

        itemAssignmentDetails.selectItem("documents");
        itemAssignmentDetails.clickAddItemButton();
        Thread.sleep(2_000);

        itemAssignmentDetails = navigationPage.addNewNvgItem();
        Thread.sleep(2_000);

        itemAssignmentDetails.selectItem("logOut");
        itemAssignmentDetails.clickAddItemButton();
        Thread.sleep(2_000);

        String originalTab = FunctionalTest.getDriver().getWindowHandle();
        Set<String> oldWindowsSet = FunctionalTest.getDriver().getWindowHandles();

        navigationPage.clickPreview();

        String newTab = (new WebDriverWait(FunctionalTest.getDriver(), 5))
                .until(new ExpectedCondition<String>() {
                           public String apply(WebDriver driver) {
                               Set<String> newWindowsSet = driver.getWindowHandles();
                               newWindowsSet.removeAll(oldWindowsSet);
                               return newWindowsSet.size() > 0 ?
                                       newWindowsSet.iterator().next() : null;
                           }
                       }
                );

        // Switch to Preview tab
        FunctionalTest.getDriver().switchTo().window(newTab);

        System.out.println("Making sure that preview page was opened...");
        Assert.assertEquals("Navigation Tree", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#navigationTree_header').text()")));

        System.out.println("Expanding [bottomFixedGroup]");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#tree_data td span:contains(\"bottom\")').prev().click()");
        Thread.sleep(3_000);

        System.out.println("Expanding [folder] under [bottomFixedGroup]");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#tree_data td span:contains(\"bottom\")').parent().parent().next().find(\"span\").click()");
        Thread.sleep(3_000);

        System.out.println("Asserting that barcodeMedical/help/folder-lock are under [folder] node...");
        Assert.assertEquals("barcodeMedicalBarcodeBARCODEconfigURLhttps://demo.e-dapt.net/abc654321/config/medical1.jscontextNameurl", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tree_data td span:contains(\"bottom\")').parent().parent().next().find(\"span\").parent().parent().next().text()")));
        Assert.assertEquals("helpHelpWEBicon_help.pngurl", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tree_data td span:contains(\"bottom\")').parent().parent().next().find(\"span\").parent().parent().next().next().text()")));
        Assert.assertEquals("folder-lockLockSYSTEM-FUNCTIONlock", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tree_data td span:contains(\"bottom\")').parent().parent().next().find(\"span\").parent().parent().next().next().next().text()")));

        System.out.println("Expanding [floatingGroup]");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#tree_data td span:contains(\"floating\")').prev().click()");
        Thread.sleep(3_000);

        System.out.println("Expanding [folder] under [floatingGroup]");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#tree_data td span:contains(\"floating\")').parent().parent().next().find(\"span\").click()");
        Thread.sleep(3_000);

        System.out.println("Asserting that documents/folder-logOut are under [folder] node...");
        Assert.assertEquals("documentsDocumentsDOCUMENTSicon_documents.pngtypedocumentsurlmaps51doc:///webGroupdocallowedOfflinetrue", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tree_data td span:contains(\"floating\")').parent().parent().next().find(\"span\").parent().parent().next().text()")));
        Assert.assertEquals("folder-logOutLog outSYSTEM-FUNCTIONlogout", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#tree_data td span:contains(\"floating\")').parent().parent().next().find(\"span\").parent().parent().next().next().text()")));

        System.out.println("Closing Preview tab...");
        FunctionalTest.getDriver().close();

        // Switch back to original tab
        FunctionalTest.getDriver().switchTo().window(originalTab);
        Thread.sleep(2_000);

        profilesPage = headerMenu.clickProfiles();

        DeleteWithAssignments deleteWithAssignments = profilesPage.clickDelete(profileName);
        Thread.sleep(2_000);

        deleteWithAssignments.clickDeleteButton();


        System.out.println("--- END OF NavigationTreePreview ---");
    }
}
