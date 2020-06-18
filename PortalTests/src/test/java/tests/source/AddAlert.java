package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.AlertDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.HeaderMenu;
import net.portal.pages.audit.Alerts;
import net.portal.pages.audit.EmailGroups;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddAlert
{
    @Test
    public void addAlert() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Alerts alertsPage = headerMenu.clickAlerts();

        AlertDetails alertDetailsForm = alertsPage.addAlert();
        Thread.sleep(3_000);

        String action = "Send email",
               emailGroup = "AT EmGr [edited]", // from test VisitEmailGroupsPage
               subject = "Hello : read details",
               body = "I have not got any reply, a positive or negative one, from Seibido yet.\n" +
                       "Let's wait and hope that it will make a BOOK.",
               description = "description AT";

        alertDetailsForm.setAction(action);
        alertDetailsForm.setEmailGroup(emailGroup);
        alertDetailsForm.setSubject(subject);
        alertDetailsForm.setBody(body);
        alertDetailsForm.setDescription(description);

        alertDetailsForm.clickAdd();
        Thread.sleep(3_000);

        System.out.println("Make sure that item was added...");

        Assert.assertEquals(action, ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:contains(\"" + action + "\")').text()"));
        Assert.assertEquals(emailGroup, ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:contains(\"" + action + "\")').next().text()"));
        Assert.assertEquals(subject, ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:contains(\"" + action + "\")').next().next().text()"));
        Assert.assertEquals(body, ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:contains(\"" + action + "\")').next().next().next().text()"));
        Assert.assertEquals(description, ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:contains(\"" + action + "\")').next().next().next().next().text()"));

        Thread.sleep(5_000);
        // After-test routine: delete created email group - should get notification
        // go back to Email Groups page
        EmailGroups emailGroupsPage = headerMenu.clickEmailGroups();

        emailGroupsPage.selectEmailGroup(emailGroup);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = emailGroupsPage.deleteEmailGroup();
        Thread.sleep(3_000);

        Assert.assertEquals("name = " + emailGroup, followingItemsWillBeDeleted.getListOfItemsToDelete());

        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(3_000);

        Assert.assertEquals("ErrorsEmail group: AT EmGr [edited] is in use. Please reassign it on Alerts page ", ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#errorForm\\\\:errorDialog tbody span').text()"));

        // Click Close
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#errorForm\\\\:errorDialog button').click()");
        Thread.sleep(3_000);

        // go back to Alerts page and delete Alert
        alertsPage = headerMenu.clickAlerts();

        alertsPage.selectAlert(action);
        followingItemsWillBeDeleted = alertsPage.deleteAlert();
        Thread.sleep(2_000);

        Assert.assertEquals("action = " + action, followingItemsWillBeDeleted.getListOfItemsToDelete());

        followingItemsWillBeDeleted.clickDelete();
        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        // Go back to Email groups and delete Email Group that was created from test AddEmailGroup with name = "AT EmGr [edited]"
        emailGroupsPage = headerMenu.clickEmailGroups();

        emailGroupsPage.selectEmailGroup(emailGroup);
        followingItemsWillBeDeleted = emailGroupsPage.deleteEmailGroup();
        Thread.sleep(1_000);

        Assert.assertEquals("name = " + emailGroup, followingItemsWillBeDeleted.getListOfItemsToDelete());

        followingItemsWillBeDeleted.clickDelete();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        Thread.sleep(3_000);
    }
}
