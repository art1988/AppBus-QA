package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.ApplicationDetail;
import net.portal.forms.AssignmentDetail;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Application;
import net.portal.pages.user_and_role_management.ProfileAssignment;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddApplication
{
    @Test
    public void addApplication() throws InterruptedException
    {
        System.out.println("--- START OF AddApplication ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Application applicationPage = headerMenu.clickApplication();

        ApplicationDetail applicationDetailPopup = applicationPage.addNewApplication();
        Thread.sleep(2_000);

        String appName = "AT App_name";

        applicationDetailPopup.setName(appName);
        applicationDetailPopup.clickAdd();
        Thread.sleep(2_000);

        System.out.println("Making sure that Application with name = " + appName + " is in the list...");
        Assert.assertTrue(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2)').text()")).contains(appName));

        applicationPage.editApplication(appName, appName += " [edited]");
        Thread.sleep(2_000);

        applicationDetailPopup = applicationPage.addNewApplication();
        Thread.sleep(2_000);

        applicationDetailPopup.setName(appName);
        applicationDetailPopup.clickAdd();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.APPLICATION_NAME_SHOULD_BE_UNIQUE.getNotificationText(), notificationPopup.getText());

        applicationDetailPopup.clickCancel();
        Thread.sleep(2_000);

        System.out.println("Making sure that Application with name = " + appName + " is in the list...");
        Assert.assertTrue(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2)').text()")).contains(appName));

        System.out.println("Go to User & Role Management > Profile Assignment and make sure that Application is in the list...");

        ProfileAssignment profileAssignmentPage = headerMenu.clickProfileAssignment();

        AssignmentDetail assignmentDetail = profileAssignmentPage.addProfileAssignment();
        Thread.sleep(2_000);

        assignmentDetail.setApplication(appName);

        Assert.assertEquals(appName, assignmentDetail.getApplication());

        assignmentDetail.clickCancel();
        Thread.sleep(2_000);

        // Go back to Application adn delete just created...
        applicationPage = headerMenu.clickApplication();

        FollowingItemsWillBeDeleted followingItemsWillBeDeletedPopup = applicationPage.deleteApplication(appName);
        Thread.sleep(2_000);

        Assert.assertEquals("applicationName = AT App_name [edited]", followingItemsWillBeDeletedPopup.getListOfItemsToDelete());
        followingItemsWillBeDeletedPopup.clickDelete();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        Assert.assertFalse(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2)').text()")).contains(appName));

        System.out.println("--- END OF AddApplication ---");
    }
}
