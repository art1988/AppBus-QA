package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.*;
import net.portal.pages.DeleteConfirmPopup;
import net.portal.pages.DeleteNavigationItemPopup;
import net.portal.pages.DeletePolicyConfirmation;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.*;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;

public class AddNavigationItem
{
    @Test
    public void addNavigationItem() throws InterruptedException
    {
        System.out.println("--- START OF AddNavigationItem ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        // First, create Authentication Stratums
        AuthenticationStratums authenticationStratumsPage = headerMenu.clickAuthenticationStratums();

        StratumDetail stratumDetail = authenticationStratumsPage.addNewStratum();
        Thread.sleep(3_000);

        String stratumName = "Autotest stratum_detail";
        stratumDetail.setName(stratumName);
        stratumDetail.setExpiration(153);

        stratumDetail.clickAdd();
        Thread.sleep(3_000);

        // Second, lets check that Stratum is visible on Authentication Groups
        AuthenticationGroups authenticationGroupsPage = headerMenu.clickAuthenticationGroups();

        StratumGroupDetail stratumGroupDetail = authenticationGroupsPage.addNewAuthenticationGroup();
        Thread.sleep(3_000);

        String stratumGroupName = "Autotest stratum_group";
        stratumGroupDetail.setGroupName(stratumGroupName);
        stratumGroupDetail.setStratum(stratumName);

        stratumGroupDetail.clickAdd();
        Thread.sleep(3_000);

        // Third, create archetype (Controller type)
        Archetypes archetypesPage = headerMenu.clickArchetypes();

        ArchetypesDetails archetypesDetails = archetypesPage.addNewArchetype();
        Thread.sleep(3_000);

        String archetypeName = "Autotest archetype_3";
        archetypesDetails.setName(archetypeName);
        archetypesDetails.setDescription("Archetype description [AT]");

        archetypesDetails.clickAdd();
        Thread.sleep(3_000);

        // Fourth, create context
        Contexts contextsPage = headerMenu.clickContexts();

        ContextDetail applicationDetail = contextsPage.addContext();

        String contextName = "Autotest context";
        applicationDetail.setName(contextName);
        applicationDetail.setDescription("Context description [AT]");

        applicationDetail.clickAdd();
        Thread.sleep(3_000);

        // Fifth, create new property: one for controller, and another for navigation
        Policies policiesPage = headerMenu.clickPolicies();

        PolicyDetail policyDetail = policiesPage.addPolicy();
        Thread.sleep(3_000);

        String controllerProperty = "property_controller_autotest",
               navigationProperty = "property_navigation_autotest";

        policyDetail.setName(controllerProperty);
        policyDetail.checkItem();
        policyDetail.addItemProperty(archetypeName, "CON", true, false);
        policyDetail.clickAdd();
        Thread.sleep(4_000);

        policyDetail = policiesPage.addPolicy();
        Thread.sleep(3_000);

        policyDetail.setName(navigationProperty);
        policyDetail.checkItem();
        policyDetail.addItemProperty(archetypeName, "NAV", true, false);
        policyDetail.clickAdd();
        Thread.sleep(3_000);

        // Finally, create Navigation Item
        NavigationItems navigationItemsPage = headerMenu.clickNavigationItems();

        ItemAssignmentDetails itemAssignmentDetails = navigationItemsPage.addNavigationItem();

        String navItemId    = "auto_id_new",
               displayTitle = "auto_display_title",
               description  = "auto_description",
               val1         = "val_1",
               val2         = "val_2";

        itemAssignmentDetails.setId(navItemId);
        itemAssignmentDetails.setDisplayTitle(displayTitle);
        itemAssignmentDetails.setDescription(description);
        itemAssignmentDetails.setControllerType(archetypeName);
        itemAssignmentDetails.setContext(contextName);
        itemAssignmentDetails.setPropertyValue(controllerProperty, val1);
        itemAssignmentDetails.setPropertyValue(navigationProperty, val2);

        itemAssignmentDetails.clickSave();
        Thread.sleep(3_000);

        System.out.println("Check that navigation item was added successfully");

        navigationItemsPage.searchForId(navItemId);
        Thread.sleep(3_000);
        navigationItemsPage.clickRefresh();
        Thread.sleep(3_000);

        Assert.assertEquals(navItemId, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(1)').eq(0).text()")));
        Assert.assertEquals(controllerProperty, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(1)').eq(1).text()")));
        Assert.assertEquals(navigationProperty, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(1)').eq(2).text()")));
        Assert.assertEquals(val1, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(2)').eq(1).text()")));
        Assert.assertEquals(val2, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(2)').eq(2).text()")));
        Assert.assertEquals(displayTitle, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(3)').eq(0).text()")));
        Assert.assertEquals(description, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(4)').eq(0).text()")));
        Assert.assertEquals(archetypeName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(5)').eq(0).text()")));
        Assert.assertEquals(contextName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(8)').eq(0).text()")));

        // Copy Navigation Item test
        System.out.println("Let's copy just added navigation item...");

        itemAssignmentDetails = navigationItemsPage.copyNavigationItem(navItemId);
        Thread.sleep(3_000);

        itemAssignmentDetails.setId(navItemId + "_COPY");
        itemAssignmentDetails.clickSave();
        Thread.sleep(3_000);

        navigationItemsPage.clickRefresh();
        Thread.sleep(3_000);

        System.out.println("Assert that copy has the same values as original...");

        Assert.assertEquals(navItemId + "_COPY", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(1)').eq(3).text()")));
        Assert.assertEquals(controllerProperty, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(1)').eq(4).text()")));
        Assert.assertEquals(navigationProperty, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(1)').eq(5).text()")));
        Assert.assertEquals(val1, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(2)').eq(4).text()")));
        Assert.assertEquals(val2, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(2)').eq(5).text()")));
        Assert.assertEquals(displayTitle, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(3)').eq(1).text()")));
        Assert.assertEquals(description, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(4)').eq(1).text()")));
        Assert.assertEquals(archetypeName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(5)').eq(1).text()")));
        Assert.assertEquals(contextName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:nth-child(8)').eq(1).text()")));


        System.out.println("Delete COPY...");
        DeleteNavigationItemPopup deleteNavigationItemPopup = navigationItemsPage.deleteNavigationItem(navItemId + "_COPY");
        Thread.sleep(3_000);

        deleteNavigationItemPopup.clickYes();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        // Download JSON test
        System.out.println("Download JSON of " + navItemId);
        navigationItemsPage.downloadJsonFile(navItemId);
        Thread.sleep(6_000);

        File navItemFile = new File(Const.DOWNLOAD_FOLDER + "\\" + navItemId + ".json");
        Assert.assertTrue(navItemFile.exists());


        System.out.println("*** After-test clean-up ***");
        // 1. Remove Authentication Stratum
        authenticationStratumsPage = headerMenu.clickAuthenticationStratums();
        authenticationStratumsPage.selectStratum(stratumName);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = authenticationStratumsPage.deleteStratum();
        Thread.sleep(1_000);
        Assert.assertEquals("name = " + stratumName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        // 2. Go to Authentication Groups and check that label is "No stratum selected"; then remove group
        authenticationGroupsPage = headerMenu.clickAuthenticationGroups();
        Assert.assertEquals("No stratum selected", authenticationGroupsPage.getListOfStratums(stratumGroupName));
        authenticationGroupsPage.selectGroupName(stratumGroupName);
        followingItemsWillBeDeleted = authenticationGroupsPage.deleteGroup();
        Thread.sleep(1_000);
        Assert.assertEquals("name = " + stratumGroupName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        // 3. Go to Archetypes
        archetypesPage = headerMenu.clickArchetypes();
        archetypesPage.selectArchetype(archetypeName);
        followingItemsWillBeDeleted = archetypesPage.deleteArchetype();
        Thread.sleep(1_000);
        Assert.assertEquals("controllerTypeName = " + archetypeName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        // Check that "Can't remove controller types which are assigned to..." notification was displayed
        Thread.sleep(1_000);
        Assert.assertTrue(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.ui-growl-title').text()")).contains("Can't remove controller types which are assigned to items or item properties:Autotest archetype_3"));

        Thread.sleep(4_000);

        // 4. Go to Contexts
        contextsPage = headerMenu.clickContexts();
        contextsPage.selectContext(contextName);
        followingItemsWillBeDeleted = contextsPage.deleteContext();
        Thread.sleep(6_000);
        Assert.assertEquals("name = " + contextName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        // 5. Go to Policies and remove 2
        policiesPage = headerMenu.clickPolicies();
        policiesPage.searchForName("autotest");
        policiesPage.clickApplyFilter();
        Thread.sleep(3_000);
        policyDetail = policiesPage.clickEdit(controllerProperty);
        Thread.sleep(3_000);
        policyDetail.selectAllItemProperties();
        DeleteConfirmPopup deleteConfirmPopup = policyDetail.deleteItemProperty();
        Thread.sleep(3_000);
        deleteConfirmPopup.clickYes();
        Thread.sleep(3_000);
        policyDetail.clickSave();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_UPDATED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        policyDetail = policiesPage.clickEdit(navigationProperty);
        Thread.sleep(3_000);
        policyDetail.selectAllItemProperties();
        deleteConfirmPopup = policyDetail.deleteItemProperty();
        Thread.sleep(3_000);
        deleteConfirmPopup.clickYes();
        Thread.sleep(3_000);
        policyDetail.clickSave();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_UPDATED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        DeletePolicyConfirmation deletePolicyConfirmation = policiesPage.deletePolicy(controllerProperty);
        Thread.sleep(4_000);

        deletePolicyConfirmation.clickYes();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        // TODO: remove after fixing of ED-3902
        policiesPage.clickApplyFilter(); // apply filter again after removing of policy
        Thread.sleep(2_000);

        deletePolicyConfirmation = policiesPage.deletePolicy(navigationProperty);
        Thread.sleep(2_000);

        deletePolicyConfirmation.clickYes();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        // visit Policies page again
        // TODO: Refresh here doesn't update -> check in the future
        policiesPage = headerMenu.clickPolicies();
        policiesPage.searchForName("autotest");
        policiesPage.clickApplyFilter();
        Thread.sleep(3_000);
        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data').text()")));

        // 6. Go to Nav Items and remove "auto_id_new" nav.item
        navigationItemsPage = headerMenu.clickNavigationItems();
        navigationItemsPage.searchForId(navItemId);
        Thread.sleep(3_000);
        navigationItemsPage.clickRefresh();
        Thread.sleep(3_000);

        DeleteNavigationItemPopup deleteNavigationItemPopup1 = navigationItemsPage.deleteNavigationItem(navItemId);
        Thread.sleep(2_000);

        deleteNavigationItemPopup1.clickYes();
        Thread.sleep(3_000);

        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data').text()")));
        // TODO: See ED-3567 -> there should be nav.item. Currently it removes with archetype which is wrong

        // 7. Go back to Archetypes and remove
        archetypesPage = headerMenu.clickArchetypes();
        archetypesPage.selectArchetype(archetypeName);
        followingItemsWillBeDeleted = archetypesPage.deleteArchetype();
        Thread.sleep(1_000);
        Assert.assertEquals("controllerTypeName = " + archetypeName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        // TODO: See ED-3567 -> there should be warning that archetype is assigned to some nav item ? Not it is SUCCESSFULLY_DELETED
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        // 8. Delete downloaded json file
        if( navItemFile.delete() )
        {
            System.out.println(navItemFile.getAbsolutePath() + " was deleted");
        } else
        {
            System.err.println("Unable to delete " + navItemFile.getAbsolutePath());
        }

        System.out.println("--- END OF AddNavigationItem ---");
    }
}
