package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.*;
import net.portal.pages.DeleteItemPopup;
import net.portal.pages.DeleteNavigationItemPopup;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Archetypes;
import net.portal.pages.user_and_role_management.Navigation;
import net.portal.pages.user_and_role_management.NavigationItems;
import net.portal.pages.user_and_role_management.Profiles;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddComplexNavItem
{
    @Test
    public void addComplexNavItem() throws InterruptedException
    {
        System.out.println("--- START OF AddComplexNavItem ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        // 1. Create new profile
        Profiles profilesPage = headerMenu.clickProfiles();

        ProfileDetail profileDetail = profilesPage.addProfile();
        Thread.sleep(2_000);

        String profileName = "CplxProf";

        profileDetail.setName(profileName);

        profileDetail.clickAdd();
        Thread.sleep(3_000);

        // 2. Create new Archetype
        Archetypes archetypesPage = headerMenu.clickArchetypes();

        ArchetypesDetails archetypesDetails = archetypesPage.addNewArchetype();
        Thread.sleep(3_000);

        String archetypeName = "AKM_custom_Arch";

        archetypesDetails.setName(archetypeName);

        archetypesDetails.clickAdd();
        Thread.sleep(3_000);

        // 3. Go to Navigation Items and add custom item
        NavigationItems navigationItemsPage = headerMenu.clickNavigationItems();

        ItemAssignmentDetails itemAssignmentDetails = navigationItemsPage.addNavigationItem();
        Thread.sleep(3_000);

        String navItemID = "akm_customNAVItem";

        itemAssignmentDetails.setId(navItemID);
        itemAssignmentDetails.selectArchetype(archetypeName);
        itemAssignmentDetails.clickSave();
        Thread.sleep(5_000);

        // 4. Go to Navigation and select just created profile. Add UI groups
        Navigation navigationPage = headerMenu.clickNavigation();

        navigationPage.selectProfile(profileName);

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.DATA_WERE_RELOADED_FROM_DB.getNotificationText(), notificationPopup.getText());

        UIGroupDetails uiGroupDetails = navigationPage.addUIGroup();
        Thread.sleep(3_000);

        uiGroupDetails.selectGroup("leftMenuGroup");
        uiGroupDetails.clickSave();
        Thread.sleep(3_000);

        itemAssignmentDetails = navigationPage.addNavigationItem();
        Thread.sleep(5_000);

        itemAssignmentDetails.selectItem(navItemID);
        itemAssignmentDetails.clickAdd();
        Thread.sleep(2_000);

        itemAssignmentDetails = navigationPage.addNavigationItem();
        Thread.sleep(5_000);

        itemAssignmentDetails.selectItem("folder");
        itemAssignmentDetails.clickAdd();
        Thread.sleep(2_000);

        System.out.println("Go inside of just added folder...");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even:contains(\"folder\")').parent().next().find(\"button\").eq(0).parent().prev().find(\"a\")[0].click()");
        Thread.sleep(2_000);

        itemAssignmentDetails = navigationPage.addNavigationItem();
        itemAssignmentDetails.selectItem("help");
        itemAssignmentDetails.clickAdd();
        Thread.sleep(2_000);

        itemAssignmentDetails = navigationPage.addNavigationItem();
        itemAssignmentDetails.expandItemFolder("rootPDFItem");
        itemAssignmentDetails.selectItem("pdfSummary");
        itemAssignmentDetails.clickAdd();
        Thread.sleep(2_000);

        System.out.println("Checking that all items are in the list...");
        Assert.assertEquals("ID:helpID:pdfSummary", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even').text().replace(/\\n/g,\"\").replace(/\\s/g, '')")));

        System.out.println("Go outside of folder - to leftMenuGroup...");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#navigation-table-panel-breadcrumb').find(\"a:contains('leftMenuGroup')\").click()");
        Thread.sleep(2_000);

        Assert.assertEquals("ID:akm_customNAVItemID:folder", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even').text().replace(/\\n/g,\"\").replace(/\\s/g, '')")));

        DeleteItemPopup deleteItemPopup = navigationPage.deleteItem(navItemID);
        Thread.sleep(2_000);

        deleteItemPopup.clickYes();
        Thread.sleep(3_000);

        // Delete folder with inner items - check of ED-4183
        deleteItemPopup = navigationPage.deleteItem("folder");
        Thread.sleep(2_000);

        deleteItemPopup.clickYes();
        Thread.sleep(3_000);

        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable_data').text()")));

        System.out.println("*** After-test clean-up ***");

        // 1. delete nav. item
        navigationItemsPage = headerMenu.clickNavigationItems();

        navigationItemsPage.searchForId(navItemID);
        navigationItemsPage.clickRefresh();
        Thread.sleep(3_000);

        DeleteNavigationItemPopup deleteNavigationItemPopup = navigationItemsPage.deleteNavigationItem(navItemID);
        Thread.sleep(3_000);

        deleteNavigationItemPopup.clickYes();
        Thread.sleep(3_000);

        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data').text()")));

        // 2. then delete archetype
        archetypesPage = headerMenu.clickArchetypes();

        archetypesPage.selectArchetype(archetypeName);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = archetypesPage.deleteArchetype();
        Thread.sleep(2_000);

        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(2_000);

        // 3. delete profile
        profilesPage = headerMenu.clickProfiles();

        DeleteWithAssignments deleteWithAssignmentsPopup = profilesPage.clickDelete(profileName);
        Thread.sleep(2_000);

        deleteWithAssignmentsPopup.clickDeleteButton();

        System.out.println("--- END OF AddComplexNavItem ---");
    }
}
