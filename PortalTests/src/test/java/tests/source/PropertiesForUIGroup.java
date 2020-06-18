package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.PolicyDetail;
import net.portal.forms.SelectPolicy;
import net.portal.forms.UIGroupDetails;
import net.portal.pages.DeletePolicyConfirmation;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Policies;
import net.portal.pages.user_and_role_management.UIGroups;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class PropertiesForUIGroup
{
    @Test
    public void propertiesForUIGroup() throws InterruptedException
    {
        System.out.println("--- START OF PropertiesForUIGroup ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Policies policiesPage = headerMenu.clickPolicies();

        // Create two new policies for group: one is required and another is not
        PolicyDetail propertyDetailForm = policiesPage.addPolicy(); // "group_policy_required"
        Thread.sleep(4_000);

        System.out.println("Assert that [Group required:] and [Group multiple:] checkboxes are disabled...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:navigationGroupRequired_input').is(':disabled')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:navigationMultipleGroup_input').is(':disabled')"));

        String policy_req     = "group_policy_required",
               policy_not_req = "group_policy_not_required";

        propertyDetailForm.setName(policy_req);
        propertyDetailForm.checkGroup();

        System.out.println("Assert that [Group required:] and [Group multiple:] checkboxes are enabled...");
        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:navigationGroupRequired_input').is(':disabled')"));
        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:navigationMultipleGroup_input').is(':disabled')"));

        propertyDetailForm.checkGroupRequired();
        propertyDetailForm.clickAdd();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_ADDED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        System.out.println("Search for name : " + policy_req);
        policiesPage.searchForName(policy_req);
        policiesPage.clickApplyFilter();
        Thread.sleep(3_000);

        System.out.println("Assert that added group policy has group mark and required mark and doesn't have item mark...");
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data td:contains(\"" + policy_req + "\")').next().next().next().find('img').attr(\"src\")").equals("/edapt-admin/images/ok-mark-24.png"));
        Assert.assertEquals("R", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data td:contains(\"" + policy_req + "\")').next().next().next().find(\"span\").text()")));
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data td:contains(\"" + policy_req + "\")').next().next().next().next().find('img').attr(\"src\")").equals("/edapt-admin/images/x-mark-24.png"));

        policiesPage = headerMenu.clickPolicies();

        propertyDetailForm = policiesPage.addPolicy(); // add "group_policy_not_required"
        Thread.sleep(4_000);

        propertyDetailForm.setName(policy_not_req);
        propertyDetailForm.checkGroup();
        propertyDetailForm.clickAdd();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_ADDED.getNotificationText(), notificationPopup.getText());

        // Check all properties on UI Groups page...
        UIGroups uiGroupsPage = headerMenu.clickUIGroups();

        UIGroupDetails uiGroupDetails = uiGroupsPage.addUIGroup();
        Thread.sleep(3_000);

        System.out.println("Assert that only required policy: " + policy_req + " is on the list...");
        Assert.assertTrue((boolean) (((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:propertyValuesTable_data td > span:contains(\"" + policy_req + "\")').is(\":visible\")")));

        SelectPolicy selectPolicyForm = uiGroupDetails.clickAddProperty();
        Thread.sleep(2_000);

        System.out.println("Assert that not required policy is in the list...");
        selectPolicyForm.expandPolicyDropdown();
        Thread.sleep(2_000);

        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#addPropertyForm\\\\:addPropertyDropdown_items li:contains(\"" + policy_not_req + "\")').is(\":visible\")"));
        selectPolicyForm.expandPolicyDropdown(); // collapse dropdown
        Thread.sleep(2_000);
        selectPolicyForm.addPolicy(policy_not_req); // add not required policy
        selectPolicyForm.clickOk();
        Thread.sleep(2_000);

        System.out.println("Assert that required and not required policies are on the list...");
        Assert.assertTrue((boolean) (((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:propertyValuesTable_data td > span:contains(\"" + policy_not_req + "\")').is(\":visible\")")));
        Assert.assertTrue((boolean) (((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:propertyValuesTable_data td > span:contains(\"" + policy_req + "\")').is(\":visible\")")));

        uiGroupDetails.clickCancel();
        Thread.sleep(2_000);


        // After test clen-up: go back to policies page and remove created
        System.out.println("*** After-test clean-up ***");
        policiesPage = headerMenu.clickPolicies();
        policiesPage.searchForName("group_policy_");
        policiesPage.clickApplyFilter();
        Thread.sleep(2_000);

        DeletePolicyConfirmation deletePolicyConfirmation = policiesPage.deletePolicy(policy_req);
        Thread.sleep(2_000);

        deletePolicyConfirmation.clickYes();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());


        deletePolicyConfirmation = policiesPage.deletePolicy(policy_not_req);
        Thread.sleep(2_000);

        deletePolicyConfirmation.clickYes();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        System.out.println("--- END OF PropertiesForUIGroup ---");
    }
}