package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.EnvironmentDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.HeaderMenu;
import net.portal.pages.portal_administration.Users;
import net.portal.pages.server_configuration.Environments;
import net.portal.pages.user_and_role_management.AuthenticationGroups;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddEnvironment
{
    @Test
    public void addEnvironment() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Environments environmentsPage = headerMenu.clickEnvironments();

        EnvironmentDetails environmentDetails = environmentsPage.addEnvironment();
        Thread.sleep(2_000);

        String envName        = "AT-env-04",
               envDescription = "Test environment: AT";

        environmentDetails.setEnvironmentName("env name with spaces"); // set incorrect name first
        environmentDetails.setEnvironmentDescription(envDescription);
        environmentDetails.clickAdd();
        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.ENVIRONMENT_SHOULDNT_CONTAIN_WHITESPACES.getNotificationText(), notificationPopup.getText());
        Thread.sleep(2_000);

        environmentDetails.setEnvironmentName(envName); // set correct name
        environmentDetails.clickAdd();
        Thread.sleep(2_000);

        environmentsPage.searchForEnvironment(envName);
        environmentsPage.clickRefresh();
        Thread.sleep(2_000);

        Assert.assertEquals(envName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data td:nth-child(2)').text()")));
        Assert.assertEquals(envDescription, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data td:nth-child(3)').text()")));

        // TODO: add test to download and upload Json file ( not implemented yet )

        // Go to different page and check that user can change environment
        AuthenticationGroups authenticationGroupsPage = headerMenu.clickAuthenticationGroups();

        headerMenu.expandEnvironmentDropdown();
        headerMenu.selectEnvironment(envName);
        Thread.sleep(2_000);

        // Go back to Environments page
        environmentsPage = headerMenu.clickEnvironments();
        // Check that envName is selected
        Assert.assertEquals(envName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#environmentForm\\\\:environmentSelect label').text()")));

        // Remove envName
        environmentsPage.selectEnvironment(envName);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = environmentsPage.deleteEnvironment();
        Thread.sleep(2_000);
        Assert.assertEquals("environmentName = " + envName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(2_000);

        // Visit different page
        Users usersPage = headerMenu.clickUsers();

        // Expand environment dropdown and make sure that there is no envName in the list
        headerMenu.expandEnvironmentDropdown();
        Assert.assertFalse(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#environmentForm\\\\:environmentSelect_items').text()")).contains(envName));
    }
}
