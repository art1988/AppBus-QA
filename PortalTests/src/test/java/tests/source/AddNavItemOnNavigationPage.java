package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.ItemAssignmentDetails;
import net.portal.forms.UIGroupDetails;
import net.portal.pages.DeleteItemPopup;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Navigation;
import net.portal.pages.user_and_role_management.UIGroups;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddNavItemOnNavigationPage
{
    @Test
    public void addNavItemOnNavigationPage() throws InterruptedException
    {
        System.out.println("--- START OF AddNavItemOnNavigationPage ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        // Add new UI Group first...
        UIGroups uiGroupsPage = headerMenu.clickUIGroups();

        UIGroupDetails uiGroupDetails = uiGroupsPage.addUIGroup();
        Thread.sleep(2_000);

        String groupTitle = "UI_Gr_AT_519";

        uiGroupDetails.setTitle(groupTitle);
        uiGroupDetails.clickAdd();
        Thread.sleep(2_000);

        Navigation navigationPage = headerMenu.clickNavigation();

        navigationPage.selectProfile("AKM"); // todo: change prof. name later
        Thread.sleep(2_000);

        uiGroupDetails = navigationPage.addGroup();
        Thread.sleep(2_000);

        uiGroupDetails.selectGroup(groupTitle);
        Thread.sleep(2_000);

        uiGroupDetails.clickSave();
        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.NAVIGATION_TREE_WAS_REGENERATED.getNotificationText(), notificationPopup.getText());

        System.out.println("Checking that Navigation items has breadcrumb...");
        Assert.assertEquals(groupTitle + "\u2192folder()", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#navigation-table-panel-breadcrumb_content').text().trim().replace(/\\n/g,\"\").replace(/\\s/g, '');")));
        Thread.sleep(2_000);

        ItemAssignmentDetails itemAssignmentDetails = navigationPage.addNavigationItem();

        itemAssignmentDetails.selectItem("barcodeMedical");
        itemAssignmentDetails.clickAdd();

        itemAssignmentDetails = navigationPage.addNavigationItem();
        itemAssignmentDetails.selectItem("documents");
        itemAssignmentDetails.clickAdd();

        itemAssignmentDetails = navigationPage.addNavigationItem();
        itemAssignmentDetails.selectItem("help");
        itemAssignmentDetails.clickAdd();

        itemAssignmentDetails = navigationPage.addNavigationItem();
        itemAssignmentDetails.selectItem("htmlTemplateItem");
        itemAssignmentDetails.clickAdd();

        System.out.println("Checking that all items are in the list...");
        Assert.assertEquals("ID:barcodeMedicalID:documentsID:helpID:htmlTemplateItem", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even').text().replace(/\\n/g,\"\").replace(/\\s/g, '')")));

        System.out.println("Move Help item down and check that order is correct...");
        navigationPage.moveItemDown("help");
        Thread.sleep(2_000);

        Assert.assertEquals("ID:barcodeMedicalID:documentsID:htmlTemplateItemID:help", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even').text().replace(/\\n/g,\"\").replace(/\\s/g, '')")));

        System.out.println("Move documents item up and check that order is correct...");
        navigationPage.moveItemUp("documents");
        Thread.sleep(2_000);

        Assert.assertEquals("ID:documentsID:barcodeMedicalID:htmlTemplateItemID:help", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even').text().replace(/\\n/g,\"\").replace(/\\s/g, '')")));

        System.out.println("Delete barcodeMedical item and assert deletion...");
        DeleteItemPopup deleteItemPopup = navigationPage.deleteItem("barcodeMedical");
        Thread.sleep(1_000);

        deleteItemPopup.clickYes();
        Thread.sleep(2_000);

        Assert.assertEquals("ID:documentsID:htmlTemplateItemID:help", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even').text().replace(/\\n/g,\"\").replace(/\\s/g, '')")));

        // Edit documents item
        itemAssignmentDetails = navigationPage.editItem("documents");
        Thread.sleep(2_000);

        itemAssignmentDetails.clickOverrideCheckbox();
        Thread.sleep(2_000);

        System.out.println("Checking that fields are enabled...");
        // Display title is enabled..
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#itemDetailForm\\\\:itemDisplayTitle input').is(':enabled');"));
        // Entitlement is enabled...
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#itemDetailForm\\\\:itemEntitlement input').is(':enabled');"));

        // Add and Delete buttons of controller policies are enabled...
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#itemDetailForm\\\\:controllerItemPropertiesTable\\\\:controllerPoliciesAddButton').is(':enabled');"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#itemDetailForm\\\\:controllerItemPropertiesTable\\\\:controllerPoliciesDeleteButton').is(':enabled');"));

        // Add and Delete buttons of navigation policies are enabled...
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#itemDetailForm\\\\:navigationItemPropertiesTable\\\\:navigationPoliciesAddButton').is(':enabled');"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#itemDetailForm\\\\:navigationItemPropertiesTable\\\\:navigationPoliciesDeleteButton').is(':enabled');"));

        // Click Cancel
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#itemDetailForm\\\\:itemAssignmentDetailsCancelButton').click()");
        Thread.sleep(2_000);

        System.out.println("*** After test clean-up ***");
        DeleteItemPopup deleteItemPopup1 = navigationPage.deleteNavigationGroups();
        Thread.sleep(1_000);

        deleteItemPopup.clickYes();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.GROUP_WAS_REMOVED.getNotificationText(), notificationPopup.getText());

        // Go back to UI Groups page
        uiGroupsPage = headerMenu.clickUIGroups();

        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = uiGroupsPage.deleteUIGroup(groupTitle);
        Thread.sleep(2_000);

        followingItemsWillBeDeleted.clickDelete();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        System.out.println("--- END OF AddNavItemOnNavigationPage ---");
    }
}
