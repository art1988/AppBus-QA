package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.DeleteFollowingUsers;
import net.portal.forms.UserDetail;
import net.portal.pages.HeaderMenu;
import net.portal.pages.portal_administration.Users;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Basic_AddUser
{
    @Test
    public void basic_AddUser() throws InterruptedException
    {
        checkPresenceOfHeader();

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Users usersPage = headerMenu.clickUsers();

        UserDetail userDetailForm = usersPage.addNewUser();

        Thread.sleep(6_000);

        userDetailForm.setUserName("BASIC_AKM");
        userDetailForm.setFirstName("BASIC_FN");
        userDetailForm.setLastName("BASIC_LN");

        userDetailForm.clickAdd();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_ADDED.getNotificationText(), notificationPopup.getText());

        usersPage.searchForUserName("BASIC_AKM");
        usersPage.searchForFirstName(" ");
        Thread.sleep(6_000);

        usersPage.clickSelectAllCheckbox();

        DeleteFollowingUsers deleteFollowingUsers = usersPage.deleteUser();
        Thread.sleep(6_000);

        deleteFollowingUsers.clickDelete();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
    }

    private void checkPresenceOfHeader()
    {
        String menuItems = String.valueOf(((JavascriptExecutor)FunctionalTest.getDriver()).executeScript("return $('.menu-toggler-wrapper').toArray().map(function(node){return node.textContent.trim()}).join('')"));

        Assert.assertEquals("ReportingUser & Role ManagementService ManagementPool ManagementDevice ManagementServer ConfigurationAuditPortal Administration", menuItems);
    }
}
